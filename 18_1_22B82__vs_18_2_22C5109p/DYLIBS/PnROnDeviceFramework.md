## PnROnDeviceFramework

> `/System/Library/PrivateFrameworks/PnROnDeviceFramework.framework/PnROnDeviceFramework`

```diff

-3400.20.1.0.0
-  __TEXT.__text: 0x10858
-  __TEXT.__auth_stubs: 0xa70
+3402.20.1.0.0
+  __TEXT.__text: 0x33eb0
+  __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0xcb8
-  __TEXT.__cstring: 0xc65
-  __TEXT.__constg_swiftt: 0x51c
-  __TEXT.__swift5_typeref: 0x9b4
-  __TEXT.__swift5_fieldmd: 0x31c
-  __TEXT.__oslogstring: 0x8bf
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_reflstr: 0x20b
-  __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__eh_frame: 0x2d8
+  __TEXT.__const: 0x2158
+  __TEXT.__cstring: 0x1e83
+  __TEXT.__constg_swiftt: 0x1214
+  __TEXT.__swift5_typeref: 0xe3a
+  __TEXT.__swift5_fieldmd: 0x10ac
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0x1fa0
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_capture: 0x28
+  __TEXT.__swift5_proto: 0xe8
+  __TEXT.__swift5_types: 0xe4
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__oslogstring: 0xb2f
+  __TEXT.__swift5_protos: 0x34
+  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__eh_frame: 0x350
   __TEXT.__objc_classname: 0xe9
-  __TEXT.__objc_methname: 0x1243
+  __TEXT.__objc_methname: 0x1143
   __TEXT.__objc_methtype: 0x164
   __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__objc_selrefs: 0x530
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH_CONST.__auth_ptr: 0x190
-  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_ptr: 0x328
+  __AUTH_CONST.__const: 0x1338
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0xbe8
+  __AUTH_CONST.__objc_const: 0x1d18
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x3e8
+  __AUTH.__objc_data: 0x280
+  __AUTH.__data: 0x15c8
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x260
-  __DATA.__bss: 0x408
-  __DATA.__common: 0x20
+  __DATA.__data: 0x5c0
+  __DATA.__bss: 0x10f0
+  __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
+  - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/LighthouseDataProcessor.framework/LighthouseDataProcessor
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 459
-  Symbols:   332
-  CStrings:  366
+  Functions: 911
+  Symbols:   348
+  CStrings:  519
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_PNRODSchemaPNRODFailureInfo
+ _OBJC_CLASS_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary
+ _OBJC_CLASS_$_SISchemaInvocation
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swiftEmptySetSingleton
+ _bzero
+ _objc_retain_x21
+ _objc_retain_x26
+ _objc_retain_x28
+ _swift_arrayInitWithCopy
+ _swift_getForeignTypeMetadata
+ _swift_getSingletonMetadata
+ _swift_updateClassMetadata2
+ _swift_willThrow
- _OBJC_CLASS_$_PNRODSchemaPNRODIntelligenceFlowPlannerComponentSummary
- __swift_stdlib_bridgeErrorToNSError
- _swift_errorRetain
CStrings:
+ "\n    requestType: "
+ "\nfailureSubSubType: "
+ "\nfailureSubtype: "
+ " metrics dictionary to json string"
+ "%!s(MISSING)"
+ "@\"NSDictionary\"8@?0"
+ "AIMLInstrumentationStreamsIssues"
+ "BiomeStreamIssues"
+ "ContentCollectionToTypedValueResolutionError"
+ "Converting %!s(MISSING) metrics dictionary to json string"
+ "Creating %!s(MISSING)\n%!s(MISSING)"
+ "Creating %!s(MISSING)\n%!s(MISSING)\n%!s(MISSING)"
+ "Encountered Error to extractLatencies for turn "
+ "ExecutionSessionError"
+ "FBSOpenApplicationErrorDomain"
+ "FBSOpenApplicationServiceErrorDomain"
+ "Failed to convert "
+ "Failed to read and parse Siri turns, no Siri metrics: "
+ "IEActionGrainUploadFailed"
+ "IEExecutionGrainCalculator"
+ "IELatencyIntervalSpec"
+ "IEPlannerGrainCalculator"
+ "IEPlannerGrainUploadFailed"
+ "IEReliabilityCalculator"
+ "IERequestGrainCalculator"
+ "IERequestGrainUploadFailed"
+ "INCExtensionErrorDomain"
+ "In updatePlannerFailureSubtype - Found multiple spans with failures, which is unexpected.\n    %!s(MISSING)"
+ "IntelligenceFlow"
+ "IntelligenceFlowPlannerSupport.UnwrappedNilError"
+ "IntelligenceFlowRuntime.RuntimeError"
+ "JSONSerializationError"
+ "LNConnectionErrorDomain"
+ "LNContextErrorDomain"
+ "LNPerformIntentPrebuiltErrorDomain"
+ "LNPerformQueryErrorDomain"
+ "MetricsComputeIssues"
+ "NSCocoaErrorDomain"
+ "NSOSStatusErrorDomain"
+ "NSPOSIXErrorDomain"
+ "PNRODSchemaPNRODIntelligenceFlowActionGrainSummary init failed!"
+ "PnROnDeviceWoker"
+ "PnROnDeviceWorkerIssues"
+ "Processing PlannerFailure %!s(MISSING)"
+ "Processing TranscriptProtoExecutorError.other %!s(MISSING)"
+ "Processing TranscriptProtoSessionCoordinatorError.other %!s(MISSING)"
+ "Processing criticalError from transcript: %!s(MISSING)"
+ "SELFUploadIssues"
+ "ToolExecutorError"
+ "ToolExecutorFatalError"
+ "TypedValueToContentGraphResolutionError"
+ "UEI_INVOCATION"
+ "Unable to extract ExecutionGrain description"
+ "Unable to extract PlannerGrain description"
+ "Unable to extract RequestGrain description"
+ "Unrecognized error from criticalError: %!s(MISSING)"
+ "UnsafeMutablePointer.initialize with negative count"
+ "WFActionErrorDomain"
+ "WFContentItemErrorDomain"
+ "WFFBSOpenApplicationErrorDomain"
+ "WFFBSOpenApplicationServiceErrorDomain"
+ "WFParameterStateToolKitConversionError"
+ "WFWorkflowErrorDomain"
+ "_TtC20PnROnDeviceFramework13IEFailureInfo"
+ "_TtC20PnROnDeviceFramework18IEPlannerGrainSpec"
+ "_TtC20PnROnDeviceFramework18IERequestGrainSpec"
+ "_TtC20PnROnDeviceFramework20IEExecutionGrainSpec"
+ "_TtC20PnROnDeviceFramework21IETranscriptLastEvent"
+ "_TtC20PnROnDeviceFramework21IETranscriptNextEvent"
+ "_TtC20PnROnDeviceFramework23IETranscriptEventFilter"
+ "_TtC20PnROnDeviceFramework24IEPlannerGrainCalculator"
+ "_TtC20PnROnDeviceFramework24IERequestGrainCalculator"
+ "_TtC20PnROnDeviceFramework26IEExecutionGrainCalculator"
+ "_TtC20PnROnDeviceFramework26PlannerGrainDimensionsSpec"
+ "_TtC20PnROnDeviceFramework26RequestGrainDimensionsSpec"
+ "_TtC20PnROnDeviceFramework30IEExecutionGrainDimensionsSpec"
+ "_TtC20PnROnDeviceFramework31IETranscriptLatencyIntervalSpec"
+ "_TtC20PnROnDeviceFramework8PNRError"
+ "actionEventId"
+ "actionResolverRequestToLastResolverEventTime"
+ "actionResponse"
+ "actionResponseTime"
+ "actionWithoutResponse"
+ "appEntityQueryEventId"
+ "appEntityQueryResponseTime"
+ "bPSReadFailed"
+ "bPSReadUnknown"
+ "beginEventFilter"
+ "bundleIds"
+ "calculateInterval - begin: %!s(MISSING), end: %!s(MISSING), duration: %!s(MISSING)"
+ "calculateInterval - failed for begin: %!s(MISSING), end: %!s(MISSING)"
+ "calculator end"
+ "calculator start"
+ "clientApplicationId"
+ "code"
+ "com.apple.aiml.lighthouse.PnROnDeviceFramework.Reliability"
+ "com.apple.assistant.assistantd"
+ "com.apple.extensionKit.errorDomain"
+ "com.apple.shortcuts.toolinvocation"
+ "computed for sessionId: %!s(MISSING) clientRequestId: %!s(MISSING) %!s(MISSING)\n%!s(MISSING)"
+ "computed metrics for %!l(MISSING)d requests"
+ "converting failureInfo to SELFMessage: %!s(MISSING) %!s(MISSING)"
+ "debugInfo"
+ "description"
+ "doWorkIEMetricsFailed"
+ "doWorkSiriMetricsFailed"
+ "domain"
+ "end for sessionId: %!s(MISSING) clientRequestId: %!s(MISSING)"
+ "endEventFilter"
+ "executionGrainDimensions"
+ "failureInfo"
+ "failureSubSubType"
+ "failureSubType"
+ "failureType"
+ "foundEvent"
+ "genericError"
+ "handleStatementEvaluated - found event from executor"
+ "handleStatementEvaluated - found event from planner"
+ "handleStatementEvaluated, sender: %!s(MISSING)"
+ "handling event %!s(MISSING)"
+ "initWithLongLong:"
+ "intermediate"
+ "lastResolverEventToResponseGeneratedTime"
+ "numCriticalError"
+ "numPlanCreated"
+ "numRequest"
+ "numResponseGenerationRequest"
+ "numStatementEvaluated"
+ "numStatementEvaluatedFromPlanner"
+ "numStatementEvaulated"
+ "numSystemResponseGenerated"
+ "permutation - begin: %!s(MISSING), end: %!s(MISSING), result: %!s(MISSING)"
+ "planCreatedToActionResolverRequestTime"
+ "planCreatedToLastResolverEventTime"
+ "planEventId"
+ "plannerGrainDimensions"
+ "plannerGrainStage"
+ "provisionalSiriTurnGrainLatencyUploadFailed"
+ "queryTime"
+ "rawQueryEventId"
+ "reliabilityCategory"
+ "requestAction"
+ "requestDisambiguation"
+ "requestGrainDimensions"
+ "requestType"
+ "resolverTotalQueryTime"
+ "setActionId:"
+ "setBundleId:"
+ "setBundleIds:"
+ "setFailureInfo:"
+ "setFailureSubType:"
+ "setFailureType:"
+ "setPnrodIntelligenceFlowActionGrainSummary:"
+ "setToolId:"
+ "setToolIds:"
+ "siriTurnFailedToGenerate"
+ "siriTurnGrainLatencyUploadFailed"
+ "spanIds"
+ "start for sessionId: %!s(MISSING) clientRequestId: %!s(MISSING)"
+ "startToActionResolverRequestTime"
+ "startToLastResolverEventTime"
+ "systemPromptResolvedAction"
+ "targetEventTypes"
+ "targetWithFailure: "
+ "testError"
+ "toolBundleId"
+ "toolId"
+ "toolIds"
+ "transcriptIFError"
+ "unknown"
+ "uploadIESELFRequest skipped due to empty IESELFEvent."
- "Creating PnROD pnrodIntelligenceFlowPlannerGrainSummary at planner grain %!s(MISSING): %!s(MISSING)"
- "Creating PnROD pnrodPNRODIntelligenceFlowPlannerComponentSummary at planner grain %!s(MISSING): %!s(MISSING)"
- "Creating PnROD transcript events at request grain %!s(MISSING): %!s(MISSING)"
- "Creating createIESELFEvents for PlannerGrainLatency"
- "Encountered Error to extractLatencies for turn %!s(MISSING)"
- "Failed to read and parse Siri turns, no Siri metrics: %!@(MISSING)"
- "IEPlannerComponentEventDictionary PNRODSchemaPNRODMetricDuration init failed!"
- "PnROnDeviceFramework"
- "_TtC20PnROnDeviceFramework23SiriTurnGrainCalculator"
- "fullPlannerServiceHandleTime"
- "ifSumFullPlannerServiceHandleTime"
- "ifSumPlanOverridesServiceHandleTime"
- "ifSumPlanResolverServiceHandleTime"
- "ifSumQueryDecorationServiceHandleTime"
- "ifSumResponseGenerationServiceHandleTime"
- "ifSumStandardPlannerMakePlanTime"
- "planOverridesServiceHandleTime"
- "planResolverServiceHandleTime"
- "responseGenerationServiceHandleTime"
- "setFullPlannerServiceHandleTime:"
- "setPlanOverridesServiceHandleTime:"
- "setPlanResolverServiceHandleTime:"
- "setPnrodPNRODIntelligenceFlowPlannerComponentSummary:"
- "setResponseGenerationServiceHandleTime:"
- "setStandardPlannerMakePlanTime:"
- "setStandardPlannerQueryDecorationTime:"
- "standardPlannerMakePlanTime"
- "standardPlannerQueryDecorationTime"
- "uploadIESELFRequest failed due to createIESELFEvent returned empty array."

```
