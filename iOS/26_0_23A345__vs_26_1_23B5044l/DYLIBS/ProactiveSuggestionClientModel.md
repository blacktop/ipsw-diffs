## ProactiveSuggestionClientModel

> `/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/ProactiveSuggestionClientModel`

```diff

-619.1.0.2.0
-  __TEXT.__text: 0x6f1f4
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x776c
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x4908
-  __TEXT.__oslogstring: 0x5895
-  __TEXT.__gcc_except_tab: 0x5f8
-  __TEXT.__unwind_info: 0x1b28
-  __TEXT.__objc_classname: 0x1443
-  __TEXT.__objc_methname: 0xfc52
-  __TEXT.__objc_methtype: 0x224a
-  __TEXT.__objc_stubs: 0x84c0
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x13c8
-  __DATA_CONST.__objc_classlist: 0x3f0
+619.5.1.0.0
+  __TEXT.__text: 0x6d8fc
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x76c4
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x491c
+  __TEXT.__oslogstring: 0x54e5
+  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__unwind_info: 0x1ae0
+  __TEXT.__objc_classname: 0x140c
+  __TEXT.__objc_methname: 0xfa50
+  __TEXT.__objc_methtype: 0x222c
+  __TEXT.__objc_stubs: 0x81a0
+  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__const: 0x1320
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bf0
+  __DATA_CONST.__objc_selrefs: 0x2b88
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xbc0
   __AUTH_CONST.__cfstring: 0x4b20
-  __AUTH_CONST.__objc_const: 0x13a50
+  __AUTH_CONST.__objc_const: 0x13950
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x91c
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x914
   __DATA.__data: 0xa28
   __DATA.__bss: 0x2c0
   __DATA_DIRTY.__objc_data: 0x1360

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99238FE7-225F-32A9-A275-EB85BEF48C7A
-  Functions: 3197
-  Symbols:   10277
-  CStrings:  4190
+  UUID: 255046FB-5A32-3CFD-8365-BDACDFF8ED44
+  Functions: 3174
+  Symbols:   10191
+  CStrings:  4165
 
Symbols:
+ -[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:connection:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:]
+ -[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:connection:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:].cold.1
+ ___165-[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:connection:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:]_block_invoke
+ ___97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.40.cold.1
+ ___97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.41
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e86_v24?0"<ATXProactiveSuggestionRealTimeProviderDelegateProtocol>"8"NSXPCConnection"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e38_v16?0"ATXSuggestionRequestResponse"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$updateSuggestionsFromDelegate:connection:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:
- -[ATXProactiveSuggestionFeedbackMetricsLogger .cxx_destruct]
- -[ATXProactiveSuggestionFeedbackMetricsLogger hyperParameters]
- -[ATXProactiveSuggestionFeedbackMetricsLogger initWithHyperParameters:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger initWithPETEventTracker:hyperParameters:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger init]
- -[ATXProactiveSuggestionFeedbackMetricsLogger petEventTracker]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) handleNewFeedbackResult:previousSessionId:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelClientCacheAgeMetricForFeedbackResult:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelEngagementMetricForFeedbackResult:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelEngagementMetricForFeedbackResult:].cold.1
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelEngagementMetricForFeedbackResult:].cold.2
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelEngagementMetricForFeedbackResult:].cold.3
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logClientModelUICacheAgeMetricForFeedbackResult:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithTestResults:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithUIFeedbackQuery:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logSessionEngagementMetricForFeedbackResult:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logSessionEngagementMetricForFeedbackResult:].cold.1
- -[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:]
- -[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:].cold.1
- GCC_except_table0
- GCC_except_table23
- _ATXBucketUInt32BetweenValuesWithRounding
- _OBJC_CLASS_$_ATXPETEventTracker2Logger
- _OBJC_CLASS_$_ATXProactiveSuggestionFeedbackMetricsLogger
- _OBJC_IVAR_$_ATXProactiveSuggestionFeedbackMetricsLogger._hyperParameters
- _OBJC_IVAR_$_ATXProactiveSuggestionFeedbackMetricsLogger._petEventTracker
- _OBJC_METACLASS_$_ATXProactiveSuggestionFeedbackMetricsLogger
- __OBJC_$_INSTANCE_METHODS_ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback)
- __OBJC_$_INSTANCE_VARIABLES_ATXProactiveSuggestionFeedbackMetricsLogger
- __OBJC_$_PROP_LIST_ATXProactiveSuggestionFeedbackMetricsLogger
- __OBJC_CLASS_RO_$_ATXProactiveSuggestionFeedbackMetricsLogger
- __OBJC_METACLASS_RO_$_ATXProactiveSuggestionFeedbackMetricsLogger
- ___154-[ATXUniversalRealTimeSuggestionRequestCoordinator updateSuggestionsFromDelegate:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:]_block_invoke
- ___89-[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithUIFeedbackQuery:]_block_invoke
- ___89-[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithUIFeedbackQuery:]_block_invoke_2
- ___97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke_2
- ___97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke_3
- ___97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke_4
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32s40r_e48_v16?0"ATXProactiveSuggestionUIFeedbackResult"8ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e8_v12?0B8ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e66_v16?0"<ATXProactiveSuggestionRealTimeProviderDelegateProtocol>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s_e38_v16?0"ATXSuggestionRequestResponse"8ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$abGroup
- _objc_msgSend$cachedAppPredictionPanelLayouts
- _objc_msgSend$cachedSuggestionWidgetLayouts
- _objc_msgSend$clientModelABGroup
- _objc_msgSend$enumerateUIFeedbackResultsWithBlock:completionBlock:
- _objc_msgSend$handleNewFeedbackResult:previousSessionId:
- _objc_msgSend$hyperParameters
- _objc_msgSend$indexOfObject:
- _objc_msgSend$initWithPETEventTracker:hyperParameters:
- _objc_msgSend$logClientModelClientCacheAgeMetricForFeedbackResult:
- _objc_msgSend$logClientModelEngagementMetricForFeedbackResult:
- _objc_msgSend$logClientModelUICacheAgeMetricForFeedbackResult:
- _objc_msgSend$logSessionEngagementMetricForFeedbackResult:
- _objc_msgSend$numSuggestionsForClientModelInLayout
- _objc_msgSend$outcomeType
- _objc_msgSend$petEventTracker
- _objc_msgSend$positionInClientModelCacheOfEngagedSuggestion
- _objc_msgSend$sessionUUID
- _objc_msgSend$setEngagementType:
- _objc_msgSend$setNumSuggestionsForClientModelInLayout:
- _objc_msgSend$setOutcomeType:
- _objc_msgSend$setPositionInClientModelCacheOfEngagedSuggestion:
- _objc_msgSend$trackDistributionForMessage:value:
- _objc_msgSend$trackScalarForMessage:
- _objc_msgSend$uiCache
- _objc_msgSend$updateSuggestionsFromDelegate:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:
CStrings:
+ "Blending: Got xpc error for %@: %@"
+ "updateSuggestionsFromDelegate:connection:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:"
+ "v24@?0@\"<ATXProactiveSuggestionRealTimeProviderDelegateProtocol>\"8@\"NSXPCConnection\"16"
+ "v64@0:8@16@24@32@40@48@56"
- "%@ - logMetricsWithUIFeedbackQuery finished processing new events with error: %@"
- "%@ Metrics - attempting to log metrics for invalid uicache class of %@"
- "%@ Metrics - could not find ATXSuggestionLayout for widget id: %@"
- "@\"<ATXPETEventTracker2Protocol>\""
- "ATXProactiveSuggestionFeedbackMetricsLogger"
- "Blending: Didn't find a cached delegate for client model %{public}@. Trying the XPC route."
- "LOGGED: %@ - ATXMPBBlendingClientModelEngagementClientCacheAgeTracker with consumerSubType: %@ and outcomeType: %@ clientModelId: %@ clientModelABGroup: %@ cacheAge: %f"
- "LOGGED: %@ - ATXMPBBlendingClientModelEngagementTracker with layoutType: %@ consumerSubType: %@, clientModelId: %@, and engagementType: %@ numSuggestionsForClientModelInLayout: %u positionInClientModelCacheOfEngagedSuggestion: %u abGroup: %@ clientModelABGroup: %@"
- "LOGGED: %@ - ATXMPBBlendingClientModelEngagementUICacheAgeTracker with consumerSubType: %@ and outcomeType: %@ abGroup: %@ cacheAge: %f"
- "LOGGED: %@ - ATXMPBBlendingSessionEngagementTracker with consumerSubType: %@ and engagementType: %@"
- "T@\"<ATXPETEventTracker2Protocol>\",R,N,V_petEventTracker"
- "UIFeedback"
- "_petEventTracker"
- "handleNewFeedbackResult:previousSessionId:"
- "indexOfObject:"
- "initWithHyperParameters:"
- "initWithPETEventTracker:hyperParameters:"
- "logClientModelClientCacheAgeMetricForFeedbackResult:"
- "logClientModelEngagementMetricForFeedbackResult:"
- "logClientModelUICacheAgeMetricForFeedbackResult:"
- "logMetricsWithTestResults:"
- "logMetricsWithUIFeedbackQuery:"
- "logSessionEngagementMetricForFeedbackResult:"
- "petEventTracker"
- "trackDistributionForMessage:value:"
- "trackScalarForMessage:"
- "updateSuggestionsFromDelegate:clientModelId:clientModelsPendingUpdate:dispatchGroup:suggestionRequest:"
- "v16@?0@\"<ATXProactiveSuggestionRealTimeProviderDelegateProtocol>\"8"
- "v56@0:8@16@24@32@40@48"

```
