## GenerativeFunctionsInstrumentation

> `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation`

```diff

-222.43.2.0.0
-  __TEXT.__text: 0x55614
-  __TEXT.__auth_stubs: 0x2640
+279.0.15.0.0
+  __TEXT.__text: 0x59e1c
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x1a30
-  __TEXT.__swift5_typeref: 0xdc6
-  __TEXT.__cstring: 0x18dd
-  __TEXT.__oslogstring: 0x20c6
-  __TEXT.__constg_swiftt: 0xbe4
-  __TEXT.__swift5_reflstr: 0xe68
-  __TEXT.__swift5_fieldmd: 0xbe0
+  __TEXT.__const: 0x1b10
+  __TEXT.__swift5_typeref: 0xe32
+  __TEXT.__cstring: 0x1bed
+  __TEXT.__oslogstring: 0x22d6
+  __TEXT.__constg_swiftt: 0xc30
+  __TEXT.__swift5_reflstr: 0xfc8
+  __TEXT.__swift5_fieldmd: 0xcfc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0xc4
+  __TEXT.__swift5_types: 0xcc
+  __TEXT.__swift5_capture: 0x780
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_assocty: 0xb0
-  __TEXT.__swift5_capture: 0x240
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x1c
+  __TEXT.__swift_as_cont: 0x24
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0xf58
-  __TEXT.__eh_frame: 0x13a0
-  __TEXT.__objc_classname: 0x67a
-  __TEXT.__objc_methname: 0xb3b
-  __TEXT.__objc_methtype: 0x52
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0xe8
+  __TEXT.__unwind_info: 0x1130
+  __TEXT.__eh_frame: 0x1340
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1328
-  __AUTH_CONST.__const: 0x11e8
+  __DATA_CONST.__got: 0x648
+  __AUTH_CONST.__const: 0x1fb0
   __AUTH_CONST.__objc_const: 0x18d0
+  __AUTH_CONST.__auth_got: 0x1410
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x1d8
+  __AUTH.__data: 0x1f0
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x6d0
-  __DATA.__bss: 0x690
-  __DATA.__common: 0x58
+  __DATA.__data: 0x628
+  __DATA.__bss: 0x510
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x1698
-  __DATA_DIRTY.__common: 0x140
-  __DATA_DIRTY.__bss: 0x980
+  __DATA_DIRTY.__data: 0x17e8
+  __DATA_DIRTY.__common: 0x148
+  __DATA_DIRTY.__bss: 0xb00
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 51E0A776-D97B-30D5-BB8D-F7ED4F1FEC22
-  Functions: 1928
-  Symbols:   178
-  CStrings:  406
+  UUID: 2799B569-FF6B-316D-8B62-2687499C9C3E
+  Functions: 2177
+  Symbols:   210
+  CStrings:  259
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _objc_release_x13
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x27
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_n
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_setDeallocating
- _objc_release_x9
CStrings:
+ "Automated.Autograding"
+ "InferencePrefillInstrumenter initialized with mismatched EventReporter and userIdentifier"
+ "InferencePrefillInstrumenter: ignoring event with non-UUID requestIdentifier: %s"
+ "To understand how well our products are performing, this query asks Apple Intelligence to evaluate feature quality. This query is run because this device has opted in to share analytics. The evaluation is processed on Private Cloud Compute, where your data is not accessible to Apple. Results are securely aggregated and protected with differential privacy—so Apple only learns aggregate trends in feature quality and usage."
+ "allocationFailureCount"
+ "assetLoadedFromCacheKB"
+ "com.apple.modelmanager.ifp_cache_expert_stats"
+ "com.apple.tgi.executeRequest.prefill"
+ "completePrompt.prefill"
+ "lastInferenceEvictSkips"
+ "outputTokensCount=%{public, signpost.description=attribute,public}ld requestIdentifier=%{public, signpost.description=attribute,public}s requestType=%{public, signpost.description=attribute,public}s error=%{public, signpost.description=attribute,public}ld prefixKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s providerName=%{public, signpost.description=attribute,public}s modelName=%{public, signpost.description=attribute,public}s"
+ "outputTokensCount=%{public, signpost.description=attribute,public}ld requestIdentifier=%{public, signpost.description=attribute,public}s requestType=%{public, signpost.description=attribute,public}s error=%{public, signpost.description=attribute,public}ld tinyModelInferenceCallCount=%{public, signpost.description=attribute,public}ld draftModelInferenceCallCount=%{public, signpost.description=attribute,public}ld targetModelInferenceCallCount=%{public, signpost.description=attribute,public}ld draftSteps=%{public, signpost.description=attribute,public}ld draftTokenAcceptanceRateInPercent=%{public, signpost.description=attribute,public}f tinyTokenAcceptanceRateInPercent=%{public, signpost.description=attribute,public}f speculationSuccessRateInPercent=%{public, signpost.description=attribute,public}f numberOfDraftOutputTokens=%{public, signpost.description=attribute,public}ld totalNumberOutputTokens=%{public, signpost.description=attribute,public}ld tinyModelTotalLatency=%{public, signpost.description=attribute,public}f draftModelTotalLatency=%{public, signpost.description=attribute,public}f targetModelTotalLatency=%{public, signpost.description=attribute,public}f prefixKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s draftModelPrefixKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s draftEmptyResponse=%{public, signpost.description=attribute,public}s draftEarlyReturn=%{public, signpost.description=attribute,public}s providerName=%{public, signpost.description=attribute,public}s modelName=%{public, signpost.description=attribute,public}s"
+ "totalExpertSwappedCount"
+ "totalExpertsLoadedFromCacheCount"
- "$defaultActor"
- "@\"NSDictionary\"8@?0"
- "@16@0:8"
- "@48@0:8Q16Q24Q32Q40"
- "GFIRusageInfo"
- "GFIRusageUtility"
- "Q"
- "Q16@0:8"
- "TQ,R,N,V_intervalMaxNeuralFootprint"
- "TQ,R,N,V_intervalMaxPhysFootprint"
- "TQ,R,N,V_neuralFootprint"
- "TQ,R,N,V_physFootprint"
- "_TtC34GenerativeFunctionsInstrumentation13EventReporter"
- "_TtC34GenerativeFunctionsInstrumentation14AsyncFIFOQueue"
- "_TtC34GenerativeFunctionsInstrumentation16StringCompressor"
- "_TtC34GenerativeFunctionsInstrumentation17EventReporterImpl"
- "_TtC34GenerativeFunctionsInstrumentation18AssetLoadProcessor"
- "_TtC34GenerativeFunctionsInstrumentation18TransparencyReport"
- "_TtC34GenerativeFunctionsInstrumentation20ManagedConfiguration"
- "_TtC34GenerativeFunctionsInstrumentation21CoreAnalyticsReporter"
- "_TtC34GenerativeFunctionsInstrumentation21PrewarmEventProcessor"
- "_TtC34GenerativeFunctionsInstrumentation25SummarizationKitProcessor"
- "_TtC34GenerativeFunctionsInstrumentation28PartnerCloudRequestProcessor"
- "_TtC34GenerativeFunctionsInstrumentation29InferencePerformanceProcessor"
- "_TtC34GenerativeFunctionsInstrumentation33GenerativeExperiencesAPIProcessor"
- "_TtC34GenerativeFunctionsInstrumentation37GenerativeModelsAvailabilityProcessor"
- "_TtC34GenerativeFunctionsInstrumentation38GenerativeFunctionPerformanceProcessor"
- "_TtCC34GenerativeFunctionsInstrumentation28PartnerCloudRequestProcessorP33_CF6B5976E14BD2252DD8ADBB3890BE4325PartnerCloudRequestEvents"
- "_TtCC34GenerativeFunctionsInstrumentation29InferencePerformanceProcessor15InferenceEvents"
- "_TtCC34GenerativeFunctionsInstrumentation38GenerativeFunctionPerformanceProcessor24FunctionInvocationEvents"
- "_TtCCV34GenerativeFunctionsInstrumentation16PowerLogReporter28PowerLogInferenceEventBuffer15InferenceEvents"
- "_TtCV34GenerativeFunctionsInstrumentation16PowerLogReporter28PowerLogInferenceEventBuffer"
- "_intervalMaxNeuralFootprint"
- "_intervalMaxPhysFootprint"
- "_neuralFootprint"
- "_physFootprint"
- "_streamContinuation"
- "_task"
- "buffer"
- "buffers"
- "bundle"
- "cache"
- "catalogVersions"
- "close"
- "code"
- "comparison"
- "coreAnalyticsReporter"
- "count"
- "daemonJobLabel"
- "data"
- "demand"
- "domain"
- "downstream"
- "downstreamDemand"
- "downstreamLock"
- "errorMapper"
- "executionBegin"
- "executionEnd"
- "extendInferenceBegin"
- "extendInferenceBeginTime"
- "extendInferenceEnd"
- "extendInferenceEndTime"
- "finished"
- "firstTokenEvent"
- "firstTokenInferenceBegin"
- "firstTokenInferenceBeginTime"
- "firstTokenInferenceEnd"
- "firstTokenInferenceEndTime"
- "gfInvocationIdToSessionIdMap"
- "handleForIdentifier:error:"
- "identifier"
- "identifierWithPid:"
- "impl"
- "inferenceBegin"
- "inferenceEnd"
- "inferenceProviderRequestBegin"
- "inferenceProviderRequestEnd"
- "inferenceRequestType"
- "inferenceStartEvent"
- "init"
- "initWithDouble:"
- "initWithInteger:"
- "initWithLongLong:"
- "initWithPhysFootprint:intervalMaxPhysFootprint:neuralFootprint:intervalMaxNeuralFootprint:"
- "initWithString:"
- "initWithSuiteName:"
- "initWithURL:append:"
- "initWithUnsignedInt:"
- "initWithUnsignedLongLong:"
- "intervalMaxNeuralFootprint"
- "intervalMaxPhysFootprint"
- "isAppleIntelligenceReportAllowed"
- "isAppleIntelligenceRestricted"
- "isDaemon"
- "isExternalIntelligenceAllowed"
- "isGenmojiAllowed"
- "isImagePlaygroundAllowed"
- "isImageWandAllowed"
- "isLessThan"
- "isWritingToolsAllowed"
- "isXPCService"
- "lastSent"
- "lock"
- "maxEventBuffereSize"
- "mmRequestIdToSessionIdMap"
- "modelInfoEvent"
- "modelManagerRequestBegin"
- "modelManagerRequestEnd"
- "neuralFootprint"
- "open"
- "outputStreamToMemory"
- "outputTokensCount=%{public, signpost.description=attribute,public}ld requestIdentifier=%{public, signpost.description=attribute,public}s requestType=%{public, signpost.description=attribute,public}s error=%{public, signpost.description=attribute,public}ld prefixKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s"
- "outputTokensCount=%{public, signpost.description=attribute,public}ld requestIdentifier=%{public, signpost.description=attribute,public}s requestType=%{public, signpost.description=attribute,public}s error=%{public, signpost.description=attribute,public}ld tinyModelInferenceCallCount=%{public, signpost.description=attribute,public}ld draftModelInferenceCallCount=%{public, signpost.description=attribute,public}ld targetModelInferenceCallCount=%{public, signpost.description=attribute,public}ld draftSteps=%{public, signpost.description=attribute,public}ld draftTokenAcceptanceRateInPercent=%{public, signpost.description=attribute,public}f tinyTokenAcceptanceRateInPercent=%{public, signpost.description=attribute,public}f speculationSuccessRateInPercent=%{public, signpost.description=attribute,public}f numberOfDraftOutputTokens=%{public, signpost.description=attribute,public}ld totalNumberOutputTokens=%{public, signpost.description=attribute,public}ld tinyModelTotalLatency=%{public, signpost.description=attribute,public}f draftModelTotalLatency=%{public, signpost.description=attribute,public}f targetModelTotalLatency=%{public, signpost.description=attribute,public}f prefixKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%{public, signpost.description=attribute,public}s draftEmptyResponse=%{public, signpost.description=attribute,public}s draftEarlyReturn=%{public, signpost.description=attribute,public}s"
- "pending"
- "physFootprint"
- "prewarmEventIdentifiers"
- "prewarmEvents"
- "privateCloudEnvInfoEvents"
- "privateCloudMetricsEvent"
- "promptConstructionBegin"
- "promptConstructionEnd"
- "propertyForKey:"
- "randomNumberProvider"
- "recursion"
- "recursive"
- "reportToBiome"
- "reportToOSLog"
- "resetFootprintInterval"
- "responseProcessingBegin"
- "responseProcessingEnd"
- "reversed"
- "routeAllEventsToSystemStream"
- "rusageInfo"
- "samplingConfigs"
- "sessionBuffer"
- "setStartDate:"
- "sharedConnection"
- "signedInStatusEvent"
- "size"
- "sourceLock"
- "state"
- "stateStorageProvider"
- "streamError"
- "stringCompressor"
- "subscriptions"
- "systemSourceLock"
- "terminal"
- "terminated"
- "transitionAssetBeginEvents"
- "unlock"
- "upstreamFailed"
- "upstreamFinishes"
- "userIdentifier"
- "v16@0:8"
- "values"
- "webSearchStatusEvent"
- "write:maxLength:"
- "xpcServiceIdentifier"

```
