## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3405.23.2.0.0
-  __TEXT.__text: 0x96fb1c
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0xcd864
-  __TEXT.__const: 0x11830
-  __TEXT.__cstring: 0x76eb7
-  __TEXT.__constg_swiftt: 0x6220
-  __TEXT.__swift5_typeref: 0x1864
-  __TEXT.__swift5_builtin: 0x38cc
+3500.90.2.0.0
+  __TEXT.__text: 0x9ebc5c
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0xcf78c
+  __TEXT.__const: 0x11988
+  __TEXT.__cstring: 0x7823f
+  __TEXT.__constg_swiftt: 0x62c0
+  __TEXT.__swift5_typeref: 0x1882
+  __TEXT.__swift5_builtin: 0x3930
   __TEXT.__swift5_reflstr: 0x214
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xe98
-  __TEXT.__swift5_types: 0xbac
+  __TEXT.__swift5_proto: 0xeb4
+  __TEXT.__swift5_types: 0xbc0
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x29930
-  __TEXT.__eh_frame: 0x1f98
-  __TEXT.__objc_classname: 0x1525e
-  __TEXT.__objc_methname: 0x11b3fb
-  __TEXT.__objc_methtype: 0x27232
-  __TEXT.__objc_stubs: 0x672a0
-  __DATA_CONST.__got: 0x4b80
-  __DATA_CONST.__const: 0x33738
-  __DATA_CONST.__objc_classlist: 0x4a48
+  __TEXT.__unwind_info: 0x29df0
+  __TEXT.__eh_frame: 0x22b0
+  __TEXT.__objc_classname: 0x15599
+  __TEXT.__objc_methname: 0x11e1c0
+  __TEXT.__objc_methtype: 0x27a27
+  __TEXT.__objc_stubs: 0x68080
+  __DATA_CONST.__got: 0x4c10
+  __DATA_CONST.__const: 0x346f8
+  __DATA_CONST.__objc_classlist: 0x4af0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35538
+  __DATA_CONST.__objc_selrefs: 0x35cc8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7330
-  __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__const: 0x20b00
-  __AUTH_CONST.__cfstring: 0x673a0
-  __AUTH_CONST.__objc_const: 0x1167e0
+  __DATA_CONST.__objc_superrefs: 0x7448
+  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__const: 0x20f80
+  __AUTH_CONST.__cfstring: 0x68420
+  __AUTH_CONST.__objc_const: 0x119180
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0xe448
-  __DATA.__objc_ivar: 0xdd8c
-  __DATA.__data: 0x1fb0
-  __DATA.__bss: 0x18300
-  __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x204d8
-  __DATA_DIRTY.__data: 0x598
-  __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x100
+  __AUTH.__objc_data: 0x11058
+  __DATA.__objc_ivar: 0xdfa4
+  __DATA.__data: 0x1fd0
+  __DATA.__bss: 0x18680
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x1df58
+  __DATA_DIRTY.__data: 0x590
+  __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E8C4B922-2EAD-38D5-A3E1-7FD668F07187
-  Functions: 74418
-  Symbols:   185198
-  CStrings:  76222
+  UUID: 0CF55D6F-5259-36C7-A52B-AC9D0E7FA2BC
+  Functions: 75126
+  Symbols:   186924
+  CStrings:  76910
 
Symbols:
+ +[EXPSiriSchemaEXPSiriClientEvent(Component) joinability]
+ -[DIMSchemaDIMDeviceFixedContext deleteIsLongLivedIDUploadDisabled]
+ -[DIMSchemaDIMDeviceFixedContext hasIsLongLivedIDUploadDisabled]
+ -[DIMSchemaDIMDeviceFixedContext isLongLivedIDUploadDisabled]
+ -[DIMSchemaDIMDeviceFixedContext setHasIsLongLivedIDUploadDisabled:]
+ -[DIMSchemaDIMDeviceFixedContext setIsLongLivedIDUploadDisabled:]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorRequestContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorRequestContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorRequestContext]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorRequestContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorRequestContext:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled deleteExists]
+ -[ExecutorSiriSchemaExecutorRequestCanceled dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorRequestCanceled exists]
+ -[ExecutorSiriSchemaExecutorRequestCanceled hasExists]
+ -[ExecutorSiriSchemaExecutorRequestCanceled hash]
+ -[ExecutorSiriSchemaExecutorRequestCanceled initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled initWithJSON:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled isEqual:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled jsonData]
+ -[ExecutorSiriSchemaExecutorRequestCanceled readFrom:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled setExists:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled setHasExists:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled writeTo:]
+ -[ExecutorSiriSchemaExecutorRequestCanceled(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorRequestContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorRequestContext canceled]
+ -[ExecutorSiriSchemaExecutorRequestContext deleteCanceled]
+ -[ExecutorSiriSchemaExecutorRequestContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorRequestContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorRequestContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorRequestContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorRequestContext ended]
+ -[ExecutorSiriSchemaExecutorRequestContext failed]
+ -[ExecutorSiriSchemaExecutorRequestContext hasCanceled]
+ -[ExecutorSiriSchemaExecutorRequestContext hasEnded]
+ -[ExecutorSiriSchemaExecutorRequestContext hasFailed]
+ -[ExecutorSiriSchemaExecutorRequestContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorRequestContext hash]
+ -[ExecutorSiriSchemaExecutorRequestContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorRequestContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorRequestContext isEqual:]
+ -[ExecutorSiriSchemaExecutorRequestContext jsonData]
+ -[ExecutorSiriSchemaExecutorRequestContext readFrom:]
+ -[ExecutorSiriSchemaExecutorRequestContext setCanceled:]
+ -[ExecutorSiriSchemaExecutorRequestContext setEnded:]
+ -[ExecutorSiriSchemaExecutorRequestContext setFailed:]
+ -[ExecutorSiriSchemaExecutorRequestContext setHasCanceled:]
+ -[ExecutorSiriSchemaExecutorRequestContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorRequestContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorRequestContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorRequestContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorRequestContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorRequestContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorRequestContext writeTo:]
+ -[ExecutorSiriSchemaExecutorRequestContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorRequestContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorRequestEnded .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorRequestEnded deleteOutcome]
+ -[ExecutorSiriSchemaExecutorRequestEnded deleteSuccess]
+ -[ExecutorSiriSchemaExecutorRequestEnded deleteToolDisambiguation]
+ -[ExecutorSiriSchemaExecutorRequestEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorRequestEnded hasOutcome]
+ -[ExecutorSiriSchemaExecutorRequestEnded hasSuccess]
+ -[ExecutorSiriSchemaExecutorRequestEnded hasToolDisambiguation]
+ -[ExecutorSiriSchemaExecutorRequestEnded hash]
+ -[ExecutorSiriSchemaExecutorRequestEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorRequestEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorRequestEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorRequestEnded jsonData]
+ -[ExecutorSiriSchemaExecutorRequestEnded outcome]
+ -[ExecutorSiriSchemaExecutorRequestEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setHasOutcome:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setHasSuccess:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setHasToolDisambiguation:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setOutcome:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setSuccess:]
+ -[ExecutorSiriSchemaExecutorRequestEnded setToolDisambiguation:]
+ -[ExecutorSiriSchemaExecutorRequestEnded success]
+ -[ExecutorSiriSchemaExecutorRequestEnded toolDisambiguation]
+ -[ExecutorSiriSchemaExecutorRequestEnded whichOutcomedetails]
+ -[ExecutorSiriSchemaExecutorRequestEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorRequestEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorRequestEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorRequestFailed .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorRequestFailed deleteError]
+ -[ExecutorSiriSchemaExecutorRequestFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorRequestFailed error]
+ -[ExecutorSiriSchemaExecutorRequestFailed hasError]
+ -[ExecutorSiriSchemaExecutorRequestFailed hash]
+ -[ExecutorSiriSchemaExecutorRequestFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorRequestFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorRequestFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorRequestFailed jsonData]
+ -[ExecutorSiriSchemaExecutorRequestFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorRequestFailed setError:]
+ -[ExecutorSiriSchemaExecutorRequestFailed setHasError:]
+ -[ExecutorSiriSchemaExecutorRequestFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorRequestFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorRequestStarted deleteInputPayload]
+ -[ExecutorSiriSchemaExecutorRequestStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorRequestStarted hasInputPayload]
+ -[ExecutorSiriSchemaExecutorRequestStarted hash]
+ -[ExecutorSiriSchemaExecutorRequestStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorRequestStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorRequestStarted inputPayload]
+ -[ExecutorSiriSchemaExecutorRequestStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorRequestStarted jsonData]
+ -[ExecutorSiriSchemaExecutorRequestStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorRequestStarted setHasInputPayload:]
+ -[ExecutorSiriSchemaExecutorRequestStarted setInputPayload:]
+ -[ExecutorSiriSchemaExecutorRequestStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorRequestStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATClientEvent deleteModelAgentCaptured]
+ -[GATSchemaGATClientEvent deleteNotForMeResponseReturned]
+ -[GATSchemaGATClientEvent hasModelAgentCaptured]
+ -[GATSchemaGATClientEvent hasNotForMeResponseReturned]
+ -[GATSchemaGATClientEvent modelAgentCaptured]
+ -[GATSchemaGATClientEvent notForMeResponseReturned]
+ -[GATSchemaGATClientEvent setHasModelAgentCaptured:]
+ -[GATSchemaGATClientEvent setHasNotForMeResponseReturned:]
+ -[GATSchemaGATClientEvent setModelAgentCaptured:]
+ -[GATSchemaGATClientEvent setNotForMeResponseReturned:]
+ -[GATSchemaGATModelAgentCaptured deleteRequestedAgent]
+ -[GATSchemaGATModelAgentCaptured deleteSettingsAgent]
+ -[GATSchemaGATModelAgentCaptured dictionaryRepresentation]
+ -[GATSchemaGATModelAgentCaptured hasRequestedAgent]
+ -[GATSchemaGATModelAgentCaptured hasSettingsAgent]
+ -[GATSchemaGATModelAgentCaptured hash]
+ -[GATSchemaGATModelAgentCaptured initWithDictionary:]
+ -[GATSchemaGATModelAgentCaptured initWithJSON:]
+ -[GATSchemaGATModelAgentCaptured isEqual:]
+ -[GATSchemaGATModelAgentCaptured jsonData]
+ -[GATSchemaGATModelAgentCaptured readFrom:]
+ -[GATSchemaGATModelAgentCaptured requestedAgent]
+ -[GATSchemaGATModelAgentCaptured setHasRequestedAgent:]
+ -[GATSchemaGATModelAgentCaptured setHasSettingsAgent:]
+ -[GATSchemaGATModelAgentCaptured setRequestedAgent:]
+ -[GATSchemaGATModelAgentCaptured setSettingsAgent:]
+ -[GATSchemaGATModelAgentCaptured settingsAgent]
+ -[GATSchemaGATModelAgentCaptured writeTo:]
+ -[GATSchemaGATModelAgentCaptured(SensitiveConditions) suppressMessageUnderConditions]
+ -[GATSchemaGATNotForMeResponseReturned deleteIsUtteranceRewritten]
+ -[GATSchemaGATNotForMeResponseReturned dictionaryRepresentation]
+ -[GATSchemaGATNotForMeResponseReturned hasIsUtteranceRewritten]
+ -[GATSchemaGATNotForMeResponseReturned hash]
+ -[GATSchemaGATNotForMeResponseReturned initWithDictionary:]
+ -[GATSchemaGATNotForMeResponseReturned initWithJSON:]
+ -[GATSchemaGATNotForMeResponseReturned isEqual:]
+ -[GATSchemaGATNotForMeResponseReturned isUtteranceRewritten]
+ -[GATSchemaGATNotForMeResponseReturned jsonData]
+ -[GATSchemaGATNotForMeResponseReturned readFrom:]
+ -[GATSchemaGATNotForMeResponseReturned setHasIsUtteranceRewritten:]
+ -[GATSchemaGATNotForMeResponseReturned setIsUtteranceRewritten:]
+ -[GATSchemaGATNotForMeResponseReturned writeTo:]
+ -[GATSchemaGATNotForMeResponseReturned(SensitiveConditions) suppressMessageUnderConditions]
+ -[GMSSchemaGMSModelRequestStarted clientTraceId]
+ -[GMSSchemaGMSModelRequestStarted deleteClientTraceId]
+ -[GMSSchemaGMSModelRequestStarted hasClientTraceId]
+ -[GMSSchemaGMSModelRequestStarted setClientTraceId:]
+ -[GMSSchemaGMSModelRequestStarted setHasClientTraceId:]
+ -[IFTSchemaIFTActionFailureFailure deleteUnableToHandleRequest]
+ -[IFTSchemaIFTActionFailureFailure hasUnableToHandleRequest]
+ -[IFTSchemaIFTActionFailureFailure setHasUnableToHandleRequest:]
+ -[IFTSchemaIFTActionFailureFailure setUnableToHandleRequest:]
+ -[IFTSchemaIFTActionFailureFailure unableToHandleRequest]
+ -[NLRouterSchemaHeuristicsHandleEndedData deleteTriggeredHeuristic]
+ -[NLRouterSchemaHeuristicsHandleEndedData hasTriggeredHeuristic]
+ -[NLRouterSchemaHeuristicsHandleEndedData setHasTriggeredHeuristic:]
+ -[NLRouterSchemaHeuristicsHandleEndedData setTriggeredHeuristic:]
+ -[NLRouterSchemaHeuristicsHandleEndedData triggeredHeuristic]
+ -[NLRouterSchemaNLRouterClientEvent deleteNLRouterInvalidDecisionEmitted]
+ -[NLRouterSchemaNLRouterClientEvent hasNLRouterInvalidDecisionEmitted]
+ -[NLRouterSchemaNLRouterClientEvent nLRouterInvalidDecisionEmitted]
+ -[NLRouterSchemaNLRouterClientEvent setHasNLRouterInvalidDecisionEmitted:]
+ -[NLRouterSchemaNLRouterClientEvent setNLRouterInvalidDecisionEmitted:]
+ -[NLRouterSchemaNLRouterDecisionGenAIMetadata deleteRequestedGenAIAgent]
+ -[NLRouterSchemaNLRouterDecisionGenAIMetadata hasRequestedGenAIAgent]
+ -[NLRouterSchemaNLRouterDecisionGenAIMetadata requestedGenAIAgent]
+ -[NLRouterSchemaNLRouterDecisionGenAIMetadata setHasRequestedGenAIAgent:]
+ -[NLRouterSchemaNLRouterDecisionGenAIMetadata setRequestedGenAIAgent:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted .cxx_destruct]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted deleteIsSuppressed]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted deleteNlRouterInvalidDecisionReason]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted deleteTraceId]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted hasIsSuppressed]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted hasNlRouterInvalidDecisionReason]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted hasTraceId]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted hash]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted initWithDictionary:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted initWithJSON:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted isEqual:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted isSuppressed]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted jsonData]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted nlRouterInvalidDecisionReason]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted readFrom:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setHasIsSuppressed:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setHasNlRouterInvalidDecisionReason:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setHasTraceId:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setIsSuppressed:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setNlRouterInvalidDecisionReason:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted setTraceId:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted traceId]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted writeTo:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterInvalidDecisionEmitted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties deleteGenAIAccountType]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties deleteIsGenAIConfirmationAlwaysRequired]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties deleteIsGenAISetUpPrompts]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties genAIAccountType]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties hasGenAIAccountType]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties hasIsGenAIConfirmationAlwaysRequired]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties hasIsGenAISetUpPrompts]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties isGenAIConfirmationAlwaysRequired]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties isGenAISetUpPrompts]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setGenAIAccountType:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setHasGenAIAccountType:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setHasIsGenAIConfirmationAlwaysRequired:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setHasIsGenAISetUpPrompts:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setIsGenAIConfirmationAlwaysRequired:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setIsGenAISetUpPrompts:]
+ -[ODDSiriSchemaODDAssistantCarPlayCounts carPlayConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDAssistantCarPlayCounts deleteCarPlayConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDAssistantCarPlayCounts hasCarPlayConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDAssistantCarPlayCounts setCarPlayConnectionsInTheLast24Hours:]
+ -[ODDSiriSchemaODDAssistantCarPlayCounts setHasCarPlayConnectionsInTheLast24Hours:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts checkerNearMissBeforeAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts checkerRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteCheckerNearMissBeforeAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteCheckerRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithNoTriggerPhraseCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithSpeechNoMatchCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithTTMMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNcAcceptPostNcMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deletePhsRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteSpkidAcceptPostSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteTtmAcceptPostTtmMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithNoTriggerPhraseCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithSpeechNoMatchCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithTTMMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasCheckerNearMissBeforeAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasCheckerRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithNoTriggerPhraseCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithSpeechNoMatchCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithTTMMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasNcAcceptPostNcMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasPhsRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasSpkidAcceptPostSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasTtmAcceptPostTtmMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hash]
+ -[ODDSiriSchemaODDAttentionInvocationCounts initWithDictionary:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts initWithJSON:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts isEqual:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts jsonData]
+ -[ODDSiriSchemaODDAttentionInvocationCounts ncAcceptPostNcMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts phsRejectBeforeActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts readFrom:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setCheckerNearMissBeforeAcceptCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setCheckerRejectBeforeActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithNoTriggerPhraseCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithSpeechNoMatchCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithTTMMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasCheckerNearMissBeforeAcceptCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasCheckerRejectBeforeActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithNoTriggerPhraseCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithSpeechNoMatchCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithTTMMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasNcAcceptPostNcMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasPhsRejectBeforeActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasSpkidAcceptPostSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasTtmAcceptPostTtmMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNcAcceptPostNcMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setPhsRejectBeforeActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setSpkidAcceptPostSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setTtmAcceptPostTtmMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts spkidAcceptPostSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts ttmAcceptPostTtmMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts writeTo:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported digests]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported hash]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported jsonData]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAttentionInvocationDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAttentionInvocationDigest counts]
+ -[ODDSiriSchemaODDAttentionInvocationDigest deleteCounts]
+ -[ODDSiriSchemaODDAttentionInvocationDigest deleteDimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAttentionInvocationDigest dimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDigest hasCounts]
+ -[ODDSiriSchemaODDAttentionInvocationDigest hasDimensions]
+ -[ODDSiriSchemaODDAttentionInvocationDigest hash]
+ -[ODDSiriSchemaODDAttentionInvocationDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest initWithJSON:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest isEqual:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest jsonData]
+ -[ODDSiriSchemaODDAttentionInvocationDigest readFrom:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest setCounts:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest setDimensions:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest setHasCounts:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest writeTo:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAttentionInvocationDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions ageOfProfileInMonths]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions dataSharingOptInStatus]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteAgeOfProfileInMonths]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteDataSharingOptInStatus]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteEnrollmentPitchEstimation]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteInvocationSource]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteMitigationAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteSiriInputLocale]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteSystemBuild]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteTriggerPhrase]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions deleteVoiceTriggerAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions enrollmentPitchEstimation]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasAgeOfProfileInMonths]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasDataSharingOptInStatus]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasEnrollmentPitchEstimation]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasInvocationSource]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasMitigationAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasSiriInputLocale]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasSystemBuild]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasTriggerPhrase]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hasVoiceTriggerAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions hash]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions initWithJSON:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions invocationSource]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions isEqual:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions jsonData]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions mitigationAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions readFrom:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setAgeOfProfileInMonths:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setEnrollmentPitchEstimation:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasAgeOfProfileInMonths:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasEnrollmentPitchEstimation:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasInvocationSource:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasMitigationAssetVersion:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasSiriInputLocale:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasSystemBuild:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasTriggerPhrase:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setHasVoiceTriggerAssetVersion:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setInvocationSource:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setMitigationAssetVersion:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setSiriInputLocale:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setSystemBuild:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setTriggerPhrase:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions setVoiceTriggerAssetVersion:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions siriInputLocale]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions systemBuild]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions triggerPhrase]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions voiceTriggerAssetVersion]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions writeTo:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAttentionInvocationDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDBluetoothCarCounts .cxx_destruct]
+ -[ODDSiriSchemaODDBluetoothCarCounts bluetoothCarConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDBluetoothCarCounts deleteBluetoothCarConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDBluetoothCarCounts deleteSiriInBTCarTurnCounts]
+ -[ODDSiriSchemaODDBluetoothCarCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDBluetoothCarCounts hasBluetoothCarConnectionsInTheLast24Hours]
+ -[ODDSiriSchemaODDBluetoothCarCounts hasSiriInBTCarTurnCounts]
+ -[ODDSiriSchemaODDBluetoothCarCounts hash]
+ -[ODDSiriSchemaODDBluetoothCarCounts initWithDictionary:]
+ -[ODDSiriSchemaODDBluetoothCarCounts initWithJSON:]
+ -[ODDSiriSchemaODDBluetoothCarCounts isEqual:]
+ -[ODDSiriSchemaODDBluetoothCarCounts jsonData]
+ -[ODDSiriSchemaODDBluetoothCarCounts readFrom:]
+ -[ODDSiriSchemaODDBluetoothCarCounts setBluetoothCarConnectionsInTheLast24Hours:]
+ -[ODDSiriSchemaODDBluetoothCarCounts setHasBluetoothCarConnectionsInTheLast24Hours:]
+ -[ODDSiriSchemaODDBluetoothCarCounts setHasSiriInBTCarTurnCounts:]
+ -[ODDSiriSchemaODDBluetoothCarCounts setSiriInBTCarTurnCounts:]
+ -[ODDSiriSchemaODDBluetoothCarCounts siriInBTCarTurnCounts]
+ -[ODDSiriSchemaODDBluetoothCarCounts writeTo:]
+ -[ODDSiriSchemaODDBluetoothCarCounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDBluetoothCarCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDBluetoothCarDigest .cxx_destruct]
+ -[ODDSiriSchemaODDBluetoothCarDigest counts]
+ -[ODDSiriSchemaODDBluetoothCarDigest deleteCounts]
+ -[ODDSiriSchemaODDBluetoothCarDigest deleteDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDBluetoothCarDigest dimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigest hasCounts]
+ -[ODDSiriSchemaODDBluetoothCarDigest hasDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigest hash]
+ -[ODDSiriSchemaODDBluetoothCarDigest initWithDictionary:]
+ -[ODDSiriSchemaODDBluetoothCarDigest initWithJSON:]
+ -[ODDSiriSchemaODDBluetoothCarDigest isEqual:]
+ -[ODDSiriSchemaODDBluetoothCarDigest jsonData]
+ -[ODDSiriSchemaODDBluetoothCarDigest readFrom:]
+ -[ODDSiriSchemaODDBluetoothCarDigest setCounts:]
+ -[ODDSiriSchemaODDBluetoothCarDigest setDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDigest setHasCounts:]
+ -[ODDSiriSchemaODDBluetoothCarDigest setHasDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDigest writeTo:]
+ -[ODDSiriSchemaODDBluetoothCarDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDBluetoothCarDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported .cxx_destruct]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported addDigests:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported clearDigests]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported deleteDigests]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported digestsAtIndex:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported digestsCount]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported digests]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported fixedDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported hasFixedDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported hash]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported initWithDictionary:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported initWithJSON:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported isEqual:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported jsonData]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported readFrom:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported setDigests:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported setFixedDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported writeTo:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDBluetoothCarDigestReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDBluetoothCarDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDBluetoothCarDimensions assistantDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDimensions deleteAssistantDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDimensions deleteVehicleManufacturer]
+ -[ODDSiriSchemaODDBluetoothCarDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDBluetoothCarDimensions hasAssistantDimensions]
+ -[ODDSiriSchemaODDBluetoothCarDimensions hasVehicleManufacturer]
+ -[ODDSiriSchemaODDBluetoothCarDimensions hash]
+ -[ODDSiriSchemaODDBluetoothCarDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions initWithJSON:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions isEqual:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions jsonData]
+ -[ODDSiriSchemaODDBluetoothCarDimensions readFrom:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions setAssistantDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions setHasAssistantDimensions:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions setHasVehicleManufacturer:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions setVehicleManufacturer:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions vehicleManufacturer]
+ -[ODDSiriSchemaODDBluetoothCarDimensions writeTo:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDBluetoothCarDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationDimensions deleteInvocationSource]
+ -[ODDSiriSchemaODDDictationDimensions hasInvocationSource]
+ -[ODDSiriSchemaODDDictationDimensions invocationSource]
+ -[ODDSiriSchemaODDDictationDimensions setHasInvocationSource:]
+ -[ODDSiriSchemaODDDictationDimensions setInvocationSource:]
+ -[ODDSiriSchemaODDSiriClientEvent attentionInvocationDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent bluetoothCarDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAttentionInvocationDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteBluetoothCarDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAttentionInvocationDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasBluetoothCarDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent setAttentionInvocationDigestsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setBluetoothCarDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAttentionInvocationDigestsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasBluetoothCarDigestReported:]
+ -[ORCHSchemaORCHDeviceDynamicContext deleteIsSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext hasIsSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext isSoundAnalysisEnabled]
+ -[ORCHSchemaORCHDeviceDynamicContext setHasIsSoundAnalysisEnabled:]
+ -[ORCHSchemaORCHDeviceDynamicContext setIsSoundAnalysisEnabled:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo addPersonalizedItemInfo:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo clearPersonalizedItemInfo]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo deleteIsPersonalizationEligible]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo deleteIsPersonalizedSessionAffected]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo deleteIsPersonalizedSession]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo deletePersonalizedItemInfo]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo hasIsPersonalizationEligible]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo hasIsPersonalizedSessionAffected]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo hasIsPersonalizedSession]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo hash]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo isEqual:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo isPersonalizationEligible]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo isPersonalizedSessionAffected]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo isPersonalizedSession]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo jsonData]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo personalizedItemInfoAtIndex:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo personalizedItemInfoCount]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo personalizedItemInfos]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo readFrom:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setHasIsPersonalizationEligible:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setHasIsPersonalizedSession:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setHasIsPersonalizedSessionAffected:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setIsPersonalizationEligible:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setIsPersonalizedSession:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setIsPersonalizedSessionAffected:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo setPersonalizedItemInfos:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo writeTo:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deleteIsPersonalized]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deletePersonalizationArtistAffinity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deletePersonalizationCosineSimilarity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deletePersonalizationPafFrequency]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deletePersonalizationRankingScore]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deletePositionWithoutPersonalization]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo deleteScore]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasIsPersonalized]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasPersonalizationArtistAffinity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasPersonalizationCosineSimilarity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasPersonalizationPafFrequency]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasPersonalizationRankingScore]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasPositionWithoutPersonalization]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hasScore]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo hash]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo initWithJSON:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo isEqual:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo isPersonalized]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo jsonData]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo personalizationArtistAffinity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo personalizationCosineSimilarity]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo personalizationPafFrequency]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo personalizationRankingScore]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo positionWithoutPersonalization]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo readFrom:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo score]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasIsPersonalized:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasPersonalizationArtistAffinity:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasPersonalizationCosineSimilarity:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasPersonalizationPafFrequency:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasPersonalizationRankingScore:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasPositionWithoutPersonalization:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setHasScore:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setIsPersonalized:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setPersonalizationArtistAffinity:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setPersonalizationCosineSimilarity:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setPersonalizationPafFrequency:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setPersonalizationRankingScore:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setPositionWithoutPersonalization:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo setScore:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo writeTo:]
+ -[PEGASUSSchemaPEGASUSPersonalizedItemInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSServerEvent deletePegasusAmpPersonalizationLoggingInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent hasPegasusAmpPersonalizationLoggingInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent pegasusAmpPersonalizationLoggingInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent setHasPegasusAmpPersonalizationLoggingInfo:]
+ -[PEGASUSSchemaPEGASUSServerEvent setPegasusAmpPersonalizationLoggingInfo:]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered deleteOfferedAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered hasOfferedAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered offeredAgent]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered setHasOfferedAgent:]
+ -[POMMESSchemaPOMMESKnowledgeFallbackOffered setOfferedAgent:]
+ -[POMMESSchemaPOMMESRequestResult deleteIsQueryDirectQuestion]
+ -[POMMESSchemaPOMMESRequestResult hasIsQueryDirectQuestion]
+ -[POMMESSchemaPOMMESRequestResult isQueryDirectQuestion]
+ -[POMMESSchemaPOMMESRequestResult setHasIsQueryDirectQuestion:]
+ -[POMMESSchemaPOMMESRequestResult setIsQueryDirectQuestion:]
+ -[SISchemaIFError .cxx_destruct]
+ -[SISchemaIFError code]
+ -[SISchemaIFError deleteCode]
+ -[SISchemaIFError deleteDomain]
+ -[SISchemaIFError dictionaryRepresentation]
+ -[SISchemaIFError domain]
+ -[SISchemaIFError hasCode]
+ -[SISchemaIFError hasDomain]
+ -[SISchemaIFError hash]
+ -[SISchemaIFError initWithDictionary:]
+ -[SISchemaIFError initWithJSON:]
+ -[SISchemaIFError isEqual:]
+ -[SISchemaIFError jsonData]
+ -[SISchemaIFError readFrom:]
+ -[SISchemaIFError setCode:]
+ -[SISchemaIFError setDomain:]
+ -[SISchemaIFError setHasCode:]
+ -[SISchemaIFError setHasDomain:]
+ -[SISchemaIFError writeTo:]
+ -[SISchemaIFError(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaIFOutcomeSuccess .cxx_destruct]
+ -[SISchemaIFOutcomeSuccess deleteDidShowInAppResult]
+ -[SISchemaIFOutcomeSuccess deleteFollowUpActionBundleId]
+ -[SISchemaIFOutcomeSuccess deleteShouldOpen]
+ -[SISchemaIFOutcomeSuccess dictionaryRepresentation]
+ -[SISchemaIFOutcomeSuccess didShowInAppResult]
+ -[SISchemaIFOutcomeSuccess followUpActionBundleId]
+ -[SISchemaIFOutcomeSuccess hasDidShowInAppResult]
+ -[SISchemaIFOutcomeSuccess hasFollowUpActionBundleId]
+ -[SISchemaIFOutcomeSuccess hasShouldOpen]
+ -[SISchemaIFOutcomeSuccess hash]
+ -[SISchemaIFOutcomeSuccess initWithDictionary:]
+ -[SISchemaIFOutcomeSuccess initWithJSON:]
+ -[SISchemaIFOutcomeSuccess isEqual:]
+ -[SISchemaIFOutcomeSuccess jsonData]
+ -[SISchemaIFOutcomeSuccess readFrom:]
+ -[SISchemaIFOutcomeSuccess setDidShowInAppResult:]
+ -[SISchemaIFOutcomeSuccess setFollowUpActionBundleId:]
+ -[SISchemaIFOutcomeSuccess setHasDidShowInAppResult:]
+ -[SISchemaIFOutcomeSuccess setHasFollowUpActionBundleId:]
+ -[SISchemaIFOutcomeSuccess setHasShouldOpen:]
+ -[SISchemaIFOutcomeSuccess setShouldOpen:]
+ -[SISchemaIFOutcomeSuccess shouldOpen]
+ -[SISchemaIFOutcomeSuccess writeTo:]
+ -[SISchemaIFOutcomeSuccess(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SISchemaIFOutcomeSuccess(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaIFOutcomeToolDisambiguation .cxx_destruct]
+ -[SISchemaIFOutcomeToolDisambiguation assistantSchemaKind]
+ -[SISchemaIFOutcomeToolDisambiguation deleteAssistantSchemaKind]
+ -[SISchemaIFOutcomeToolDisambiguation dictionaryRepresentation]
+ -[SISchemaIFOutcomeToolDisambiguation hasAssistantSchemaKind]
+ -[SISchemaIFOutcomeToolDisambiguation hash]
+ -[SISchemaIFOutcomeToolDisambiguation initWithDictionary:]
+ -[SISchemaIFOutcomeToolDisambiguation initWithJSON:]
+ -[SISchemaIFOutcomeToolDisambiguation isEqual:]
+ -[SISchemaIFOutcomeToolDisambiguation jsonData]
+ -[SISchemaIFOutcomeToolDisambiguation readFrom:]
+ -[SISchemaIFOutcomeToolDisambiguation setAssistantSchemaKind:]
+ -[SISchemaIFOutcomeToolDisambiguation setHasAssistantSchemaKind:]
+ -[SISchemaIFOutcomeToolDisambiguation writeTo:]
+ -[SISchemaIFOutcomeToolDisambiguation(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SISchemaIFOutcomeToolDisambiguation(SensitiveConditions) suppressMessageUnderConditions]
+ -[TTSSchemaTTSSpeechStarted deleteLlmStylePrompt]
+ -[TTSSchemaTTSSpeechStarted hasLlmStylePrompt]
+ -[TTSSchemaTTSSpeechStarted llmStylePrompt]
+ -[TTSSchemaTTSSpeechStarted setHasLlmStylePrompt:]
+ -[TTSSchemaTTSSpeechStarted setLlmStylePrompt:]
+ OBJC_IVAR_$_DIMSchemaDIMDeviceFixedContext._isLongLivedIDUploadDisabled
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorRequestContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestCanceled._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestCanceled._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._canceled
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._outcome
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._success
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._toolDisambiguation
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestFailed._error
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestStarted._inputPayload
+ OBJC_IVAR_$_GATSchemaGATClientEvent._modelAgentCaptured
+ OBJC_IVAR_$_GATSchemaGATClientEvent._notForMeResponseReturned
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._has
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._requestedAgent
+ OBJC_IVAR_$_GATSchemaGATModelAgentCaptured._settingsAgent
+ OBJC_IVAR_$_GATSchemaGATNotForMeResponseReturned._has
+ OBJC_IVAR_$_GATSchemaGATNotForMeResponseReturned._isUtteranceRewritten
+ OBJC_IVAR_$_GMSSchemaGMSModelRequestStarted._clientTraceId
+ OBJC_IVAR_$_IFTSchemaIFTActionFailureFailure._unableToHandleRequest
+ OBJC_IVAR_$_NLRouterSchemaHeuristicsHandleEndedData._has
+ OBJC_IVAR_$_NLRouterSchemaHeuristicsHandleEndedData._triggeredHeuristic
+ OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._nLRouterInvalidDecisionEmitted
+ OBJC_IVAR_$_NLRouterSchemaNLRouterDecisionGenAIMetadata._requestedGenAIAgent
+ OBJC_IVAR_$_NLRouterSchemaNLRouterInvalidDecisionEmitted._has
+ OBJC_IVAR_$_NLRouterSchemaNLRouterInvalidDecisionEmitted._isSuppressed
+ OBJC_IVAR_$_NLRouterSchemaNLRouterInvalidDecisionEmitted._nlRouterInvalidDecisionReason
+ OBJC_IVAR_$_NLRouterSchemaNLRouterInvalidDecisionEmitted._traceId
+ OBJC_IVAR_$_ODDSiriSchemaODDAppleIntelligenceProperties._genAIAccountType
+ OBJC_IVAR_$_ODDSiriSchemaODDAppleIntelligenceProperties._isGenAIConfirmationAlwaysRequired
+ OBJC_IVAR_$_ODDSiriSchemaODDAppleIntelligenceProperties._isGenAISetUpPrompts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantCarPlayCounts._carPlayConnectionsInTheLast24Hours
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantCarPlayCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._checkerNearMissBeforeAcceptCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._checkerRejectBeforeActivationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithNoTriggerPhraseCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithSpeechNoMatchCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithTTMMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._ncAcceptPostNcMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._phsRejectBeforeActivationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._spkidAcceptPostSpkidMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._ttmAcceptPostTtmMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._ageOfProfileInMonths
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._dataSharingOptInStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._enrollmentPitchEstimation
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._invocationSource
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._mitigationAssetVersion
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._siriInputLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._systemBuild
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._triggerPhrase
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._voiceTriggerAssetVersion
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarCounts._bluetoothCarConnectionsInTheLast24Hours
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarCounts._siriInBTCarTurnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigestReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigestReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDimensions._assistantDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDimensions._vehicleManufacturer
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._invocationSource
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._attentionInvocationDigestsReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._bluetoothCarDigestReported
+ OBJC_IVAR_$_ORCHSchemaORCHDeviceDynamicContext._isSoundAnalysisEnabled
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo._isPersonalizationEligible
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo._isPersonalizedSession
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo._isPersonalizedSessionAffected
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo._personalizedItemInfos
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._isPersonalized
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._personalizationArtistAffinity
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._personalizationCosineSimilarity
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._personalizationPafFrequency
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._personalizationRankingScore
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._positionWithoutPersonalization
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo._score
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSServerEvent._pegasusAmpPersonalizationLoggingInfo
+ OBJC_IVAR_$_POMMESSchemaPOMMESKnowledgeFallbackOffered._offeredAgent
+ OBJC_IVAR_$_POMMESSchemaPOMMESRequestResult._isQueryDirectQuestion
+ OBJC_IVAR_$_SISchemaIFError._code
+ OBJC_IVAR_$_SISchemaIFError._domain
+ OBJC_IVAR_$_SISchemaIFError._has
+ OBJC_IVAR_$_SISchemaIFOutcomeSuccess._didShowInAppResult
+ OBJC_IVAR_$_SISchemaIFOutcomeSuccess._followUpActionBundleId
+ OBJC_IVAR_$_SISchemaIFOutcomeSuccess._has
+ OBJC_IVAR_$_SISchemaIFOutcomeSuccess._shouldOpen
+ OBJC_IVAR_$_SISchemaIFOutcomeToolDisambiguation._assistantSchemaKind
+ OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._llmStylePrompt
+ _ExecutorSiriSchemaExecutorRequestCanceledReadFrom
+ _ExecutorSiriSchemaExecutorRequestContextReadFrom
+ _ExecutorSiriSchemaExecutorRequestEndedReadFrom
+ _ExecutorSiriSchemaExecutorRequestFailedReadFrom
+ _ExecutorSiriSchemaExecutorRequestStartedReadFrom
+ _GATSchemaGATModelAgentCapturedReadFrom
+ _GATSchemaGATNotForMeResponseReturnedReadFrom
+ _NLRouterSchemaNLRouterInvalidDecisionEmittedReadFrom
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorRequestCanceled
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorRequestContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorRequestEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorRequestFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorRequestStarted
+ _OBJC_CLASS_$_GATSchemaGATModelAgentCaptured
+ _OBJC_CLASS_$_GATSchemaGATNotForMeResponseReturned
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ _OBJC_CLASS_$_ODDSiriSchemaODDAttentionInvocationCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAttentionInvocationDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAttentionInvocationDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDBluetoothCarCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDBluetoothCarDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDBluetoothCarDigestReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDBluetoothCarDimensions
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ _OBJC_CLASS_$_SISchemaIFError
+ _OBJC_CLASS_$_SISchemaIFOutcomeSuccess
+ _OBJC_CLASS_$_SISchemaIFOutcomeToolDisambiguation
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorRequestContext
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._hasCanceled
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._hasEnded
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._hasFailed
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._hasStartedOrChanged
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestContext._whichContextevent
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._hasSuccess
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._hasToolDisambiguation
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestEnded._whichOutcomedetails
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorRequestFailed._hasError
+ _OBJC_IVAR_$_GATSchemaGATClientEvent._hasModelAgentCaptured
+ _OBJC_IVAR_$_GATSchemaGATClientEvent._hasNotForMeResponseReturned
+ _OBJC_IVAR_$_GMSSchemaGMSModelRequestStarted._hasClientTraceId
+ _OBJC_IVAR_$_IFTSchemaIFTActionFailureFailure._hasUnableToHandleRequest
+ _OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._hasNLRouterInvalidDecisionEmitted
+ _OBJC_IVAR_$_NLRouterSchemaNLRouterInvalidDecisionEmitted._hasTraceId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._hasMitigationAssetVersion
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._hasSiriInputLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._hasSystemBuild
+ _OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationDimensions._hasVoiceTriggerAssetVersion
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarCounts._hasSiriInBTCarTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDigestReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDimensions._hasAssistantDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDBluetoothCarDimensions._hasVehicleManufacturer
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAttentionInvocationDigestsReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasBluetoothCarDigestReported
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSServerEvent._hasPegasusAmpPersonalizationLoggingInfo
+ _OBJC_IVAR_$_SISchemaIFError._hasDomain
+ _OBJC_IVAR_$_SISchemaIFOutcomeSuccess._hasFollowUpActionBundleId
+ _OBJC_IVAR_$_SISchemaIFOutcomeToolDisambiguation._hasAssistantSchemaKind
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorRequestCanceled
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorRequestContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorRequestEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorRequestFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorRequestStarted
+ _OBJC_METACLASS_$_GATSchemaGATModelAgentCaptured
+ _OBJC_METACLASS_$_GATSchemaGATNotForMeResponseReturned
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAttentionInvocationCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAttentionInvocationDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAttentionInvocationDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDBluetoothCarCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDBluetoothCarDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDBluetoothCarDigestReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDBluetoothCarDimensions
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ _OBJC_METACLASS_$_SISchemaIFError
+ _OBJC_METACLASS_$_SISchemaIFOutcomeSuccess
+ _OBJC_METACLASS_$_SISchemaIFOutcomeToolDisambiguation
+ _ODDSiriSchemaODDAttentionInvocationCountsReadFrom
+ _ODDSiriSchemaODDAttentionInvocationDeviceDigestsReportedReadFrom
+ _ODDSiriSchemaODDAttentionInvocationDigestReadFrom
+ _ODDSiriSchemaODDAttentionInvocationDimensionsReadFrom
+ _ODDSiriSchemaODDBluetoothCarCountsReadFrom
+ _ODDSiriSchemaODDBluetoothCarDigestReadFrom
+ _ODDSiriSchemaODDBluetoothCarDigestReportedReadFrom
+ _ODDSiriSchemaODDBluetoothCarDimensionsReadFrom
+ _OUTLINED_FUNCTION_141
+ _OUTLINED_FUNCTION_142
+ _OUTLINED_FUNCTION_143
+ _OUTLINED_FUNCTION_144
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_146
+ _OUTLINED_FUNCTION_147
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_149
+ _OUTLINED_FUNCTION_150
+ _OUTLINED_FUNCTION_151
+ _OUTLINED_FUNCTION_152
+ _OUTLINED_FUNCTION_153
+ _PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfoReadFrom
+ _PEGASUSSchemaPEGASUSPersonalizedItemInfoReadFrom
+ _SISchemaIFErrorReadFrom
+ _SISchemaIFOutcomeSuccessReadFrom
+ _SISchemaIFOutcomeToolDisambiguationReadFrom
+ __OBJC_$_CLASS_METHODS_EXPSiriSchemaEXPSiriClientEvent(Component|SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_EXPSiriSchemaEXPSiriClientEvent(Component|SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorRequestCanceled(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorRequestContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorRequestEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorRequestFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorRequestStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATModelAgentCaptured(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_GATSchemaGATNotForMeResponseReturned(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterInvalidDecisionEmitted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAttentionInvocationCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAttentionInvocationDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAttentionInvocationDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDBluetoothCarCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDBluetoothCarDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDBluetoothCarDigestReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDBluetoothCarDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSPersonalizedItemInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaIFError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaIFOutcomeSuccess(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaIFOutcomeToolDisambiguation(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorRequestCanceled
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorRequestContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorRequestEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorRequestFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorRequestStarted
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATModelAgentCaptured
+ __OBJC_$_INSTANCE_VARIABLES_GATSchemaGATNotForMeResponseReturned
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAttentionInvocationCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAttentionInvocationDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAttentionInvocationDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDBluetoothCarCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDBluetoothCarDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDBluetoothCarDigestReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDBluetoothCarDimensions
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaIFError
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaIFOutcomeSuccess
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaIFOutcomeToolDisambiguation
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorRequestCanceled
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorRequestContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorRequestEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorRequestFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorRequestStarted
+ __OBJC_$_PROP_LIST_GATSchemaGATModelAgentCaptured
+ __OBJC_$_PROP_LIST_GATSchemaGATNotForMeResponseReturned
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAttentionInvocationCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAttentionInvocationDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAttentionInvocationDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDBluetoothCarCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDBluetoothCarDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDBluetoothCarDigestReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDBluetoothCarDimensions
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ __OBJC_$_PROP_LIST_SISchemaIFError
+ __OBJC_$_PROP_LIST_SISchemaIFOutcomeSuccess
+ __OBJC_$_PROP_LIST_SISchemaIFOutcomeToolDisambiguation
+ __OBJC_CLASS_PROTOCOLS_$_EXPSiriSchemaEXPSiriClientEvent(Component|SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorRequestCanceled
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorRequestContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorRequestEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorRequestFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorRequestStarted
+ __OBJC_CLASS_RO_$_GATSchemaGATModelAgentCaptured
+ __OBJC_CLASS_RO_$_GATSchemaGATNotForMeResponseReturned
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAttentionInvocationCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDBluetoothCarCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDBluetoothCarDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDBluetoothCarDigestReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDBluetoothCarDimensions
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ __OBJC_CLASS_RO_$_SISchemaIFError
+ __OBJC_CLASS_RO_$_SISchemaIFOutcomeSuccess
+ __OBJC_CLASS_RO_$_SISchemaIFOutcomeToolDisambiguation
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorRequestCanceled
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorRequestContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorRequestEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorRequestFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorRequestStarted
+ __OBJC_METACLASS_RO_$_GATSchemaGATModelAgentCaptured
+ __OBJC_METACLASS_RO_$_GATSchemaGATNotForMeResponseReturned
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterInvalidDecisionEmitted
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAttentionInvocationCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAttentionInvocationDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDBluetoothCarCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDBluetoothCarDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDBluetoothCarDigestReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDBluetoothCarDimensions
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSPersonalizedItemInfo
+ __OBJC_METACLASS_RO_$_SISchemaIFError
+ __OBJC_METACLASS_RO_$_SISchemaIFOutcomeSuccess
+ __OBJC_METACLASS_RO_$_SISchemaIFOutcomeToolDisambiguation
+ ___swift_coroFrameAllocStub
+ ___unnamed_11
+ ___unnamed_2
+ ___unnamed_7
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriInstrumentation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriInstrumentation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriInstrumentation
+ _objc_msgSend$_setError
+ _objc_msgSend$addPersonalizedItemInfo:
+ _objc_msgSend$ageOfProfileInMonths
+ _objc_msgSend$attentionInvocationDigestsReported
+ _objc_msgSend$bluetoothCarConnectionsInTheLast24Hours
+ _objc_msgSend$bluetoothCarDigestReported
+ _objc_msgSend$carPlayConnectionsInTheLast24Hours
+ _objc_msgSend$checkerNearMissBeforeAcceptCount
+ _objc_msgSend$checkerRejectBeforeActivationCount
+ _objc_msgSend$clearPersonalizedItemInfo
+ _objc_msgSend$deleteAttentionInvocationDigestsReported
+ _objc_msgSend$deleteBluetoothCarDigestReported
+ _objc_msgSend$deleteExecutorRequestContext
+ _objc_msgSend$deleteFollowUpActionBundleId
+ _objc_msgSend$deleteModelAgentCaptured
+ _objc_msgSend$deleteNLRouterInvalidDecisionEmitted
+ _objc_msgSend$deleteNotForMeResponseReturned
+ _objc_msgSend$deletePegasusAmpPersonalizationLoggingInfo
+ _objc_msgSend$deleteSiriInBTCarTurnCounts
+ _objc_msgSend$enrollmentPitchEstimation
+ _objc_msgSend$executorRequestContext
+ _objc_msgSend$falseWakeWithNoTriggerPhraseCount
+ _objc_msgSend$falseWakeWithSpeechNoMatchCount
+ _objc_msgSend$falseWakeWithTTMMitigationCount
+ _objc_msgSend$followUpActionBundleId
+ _objc_msgSend$genAIAccountType
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$inputPayload
+ _objc_msgSend$isGenAIConfirmationAlwaysRequired
+ _objc_msgSend$isGenAISetUpPrompts
+ _objc_msgSend$isPersonalizationEligible
+ _objc_msgSend$isPersonalized
+ _objc_msgSend$isPersonalizedSession
+ _objc_msgSend$isPersonalizedSessionAffected
+ _objc_msgSend$isQueryDirectQuestion
+ _objc_msgSend$isSoundAnalysisEnabled
+ _objc_msgSend$isSuppressed
+ _objc_msgSend$isUtteranceRewritten
+ _objc_msgSend$llmStylePrompt
+ _objc_msgSend$modelAgentCaptured
+ _objc_msgSend$nLRouterInvalidDecisionEmitted
+ _objc_msgSend$ncAcceptPostNcMitigationCount
+ _objc_msgSend$nlRouterInvalidDecisionReason
+ _objc_msgSend$notForMeResponseReturned
+ _objc_msgSend$offeredAgent
+ _objc_msgSend$pegasusAmpPersonalizationLoggingInfo
+ _objc_msgSend$personalizationArtistAffinity
+ _objc_msgSend$personalizationCosineSimilarity
+ _objc_msgSend$personalizationPafFrequency
+ _objc_msgSend$personalizationRankingScore
+ _objc_msgSend$personalizedItemInfos
+ _objc_msgSend$position
+ _objc_msgSend$positionWithoutPersonalization
+ _objc_msgSend$requestedGenAIAgent
+ _objc_msgSend$setAgeOfProfileInMonths:
+ _objc_msgSend$setAttentionInvocationDigestsReported:
+ _objc_msgSend$setBluetoothCarConnectionsInTheLast24Hours:
+ _objc_msgSend$setBluetoothCarDigestReported:
+ _objc_msgSend$setCarPlayConnectionsInTheLast24Hours:
+ _objc_msgSend$setCheckerNearMissBeforeAcceptCount:
+ _objc_msgSend$setCheckerRejectBeforeActivationCount:
+ _objc_msgSend$setEnrollmentPitchEstimation:
+ _objc_msgSend$setExecutorRequestContext:
+ _objc_msgSend$setFalseWakeWithNoTriggerPhraseCount:
+ _objc_msgSend$setFalseWakeWithSpeechNoMatchCount:
+ _objc_msgSend$setFalseWakeWithTTMMitigationCount:
+ _objc_msgSend$setFollowUpActionBundleId:
+ _objc_msgSend$setGenAIAccountType:
+ _objc_msgSend$setInputPayload:
+ _objc_msgSend$setIsGenAIConfirmationAlwaysRequired:
+ _objc_msgSend$setIsGenAISetUpPrompts:
+ _objc_msgSend$setIsPersonalizationEligible:
+ _objc_msgSend$setIsPersonalized:
+ _objc_msgSend$setIsPersonalizedSession:
+ _objc_msgSend$setIsPersonalizedSessionAffected:
+ _objc_msgSend$setIsQueryDirectQuestion:
+ _objc_msgSend$setIsSoundAnalysisEnabled:
+ _objc_msgSend$setIsSuppressed:
+ _objc_msgSend$setIsUtteranceRewritten:
+ _objc_msgSend$setLlmStylePrompt:
+ _objc_msgSend$setModelAgentCaptured:
+ _objc_msgSend$setNLRouterInvalidDecisionEmitted:
+ _objc_msgSend$setNcAcceptPostNcMitigationCount:
+ _objc_msgSend$setNlRouterInvalidDecisionReason:
+ _objc_msgSend$setNotForMeResponseReturned:
+ _objc_msgSend$setOfferedAgent:
+ _objc_msgSend$setPegasusAmpPersonalizationLoggingInfo:
+ _objc_msgSend$setPersonalizationArtistAffinity:
+ _objc_msgSend$setPersonalizationCosineSimilarity:
+ _objc_msgSend$setPersonalizationPafFrequency:
+ _objc_msgSend$setPersonalizationRankingScore:
+ _objc_msgSend$setPersonalizedItemInfos:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setPositionWithoutPersonalization:
+ _objc_msgSend$setRequestedGenAIAgent:
+ _objc_msgSend$setSettingsAgent:
+ _objc_msgSend$setSiriInBTCarTurnCounts:
+ _objc_msgSend$setSpkidAcceptPostSpkidMitigationCount:
+ _objc_msgSend$setTriggeredHeuristic:
+ _objc_msgSend$setTtmAcceptPostTtmMitigationCount:
+ _objc_msgSend$setUnableToHandleRequest:
+ _objc_msgSend$setVoiceTriggerAssetVersion:
+ _objc_msgSend$settingsAgent
+ _objc_msgSend$siriInBTCarTurnCounts
+ _objc_msgSend$spkidAcceptPostSpkidMitigationCount
+ _objc_msgSend$triggeredHeuristic
+ _objc_msgSend$ttmAcceptPostTtmMitigationCount
+ _objc_msgSend$unableToHandleRequest
+ _objc_msgSend$voiceTriggerAssetVersion
+ _objc_msgSend$whichOutcomedetails
+ _objc_retain_x9
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorRequestContext
+ _qname_GATSchemaGATClientEvent_WhichEvent_Type_modelAgentCaptured
+ _qname_GATSchemaGATClientEvent_WhichEvent_Type_notForMeResponseReturned
+ _qname_NLRouterSchemaNLRouterClientEvent_WhichEvent_Type_nLRouterInvalidDecisionEmitted
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_attentionInvocationDigestsReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_bluetoothCarDigestReported
+ _qname_PEGASUSSchemaPEGASUSServerEvent_WhichEvent_Type_pegasusAmpPersonalizationLoggingInfo
+ _swift_coroFrameAlloc
+ _symbolic _____ So014NLRouterSchemaA21InvalidDecisionReasonV
+ _symbolic _____ So014NLRouterSchemaA22TriggeredHeuristicRuleV
+ _symbolic _____ So17SISchemaIFOutcomeV
+ _symbolic _____ So17SISchemaIFPayloadV
+ _symbolic _____ So26TTSSchemaTTSLLMStylePromptV
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- __OBJC_$_CLASS_METHODS_EXPSiriSchemaEXPSiriClientEvent(SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
- __OBJC_$_INSTANCE_METHODS_EXPSiriSchemaEXPSiriClientEvent(SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
- __OBJC_CLASS_PROTOCOLS_$_EXPSiriSchemaEXPSiriClientEvent(SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
- ___unnamed_1
- ___unnamed_10
- ___unnamed_6
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SiriInstrumentation
- _swift_bridgeObjectRelease_n
- _swift_release_n
- _swift_setDeallocating
CStrings:
+ "@\"ExecutorSiriSchemaExecutorRequestCanceled\""
+ "@\"ExecutorSiriSchemaExecutorRequestContext\""
+ "@\"ExecutorSiriSchemaExecutorRequestEnded\""
+ "@\"ExecutorSiriSchemaExecutorRequestFailed\""
+ "@\"ExecutorSiriSchemaExecutorRequestStarted\""
+ "@\"GATSchemaGATModelAgentCaptured\""
+ "@\"GATSchemaGATNotForMeResponseReturned\""
+ "@\"NLRouterSchemaNLRouterInvalidDecisionEmitted\""
+ "@\"ODDSiriSchemaODDAttentionInvocationCounts\""
+ "@\"ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported\""
+ "@\"ODDSiriSchemaODDAttentionInvocationDimensions\""
+ "@\"ODDSiriSchemaODDBluetoothCarCounts\""
+ "@\"ODDSiriSchemaODDBluetoothCarDigestReported\""
+ "@\"ODDSiriSchemaODDBluetoothCarDimensions\""
+ "@\"PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo\""
+ "@\"SISchemaIFError\""
+ "@\"SISchemaIFOutcomeSuccess\""
+ "@\"SISchemaIFOutcomeToolDisambiguation\""
+ "DISMISSALREASON_ASSETS_NOT_READY"
+ "ExecutorSiriSchemaExecutorRequestCanceled"
+ "ExecutorSiriSchemaExecutorRequestContext"
+ "ExecutorSiriSchemaExecutorRequestEnded"
+ "ExecutorSiriSchemaExecutorRequestFailed"
+ "ExecutorSiriSchemaExecutorRequestStarted"
+ "FLOWAPPRESOLUTIONTYPE_NOT_SUPPORTED_INTENT"
+ "GATSchemaGATModelAgentCaptured"
+ "GATSchemaGATNotForMeResponseReturned"
+ "GENAIAGENT_AGENT_PLACEHOLDER_2"
+ "GENAIAGENT_AGENT_PLACEHOLDER_3"
+ "IFOUTCOME_ACTION_CONFIRMATION"
+ "IFOUTCOME_ACTION_REQUIREMENT"
+ "IFOUTCOME_FAILURE"
+ "IFOUTCOME_PARAMETER_CANDIDATES_NOT_FOUND"
+ "IFOUTCOME_PARAMETER_CONFIRMATION"
+ "IFOUTCOME_PARAMETER_DISAMBIGUATION"
+ "IFOUTCOME_PARAMETER_NEEDS_VALUE"
+ "IFOUTCOME_PARAMETER_NOT_ALLOWED"
+ "IFOUTCOME_SNIPPET_STREAM"
+ "IFOUTCOME_SUCCESS"
+ "IFOUTCOME_TOOL_DISAMBIGUATION"
+ "IFOUTCOME_UNKNOWN"
+ "IFOUTCOME_VALUE_DISAMBIGUATION"
+ "IFPAYLOAD_ACTION_CANCELED"
+ "IFPAYLOAD_ACTION_CREATED"
+ "IFPAYLOAD_QUERIES_CREATED"
+ "IFPAYLOAD_TYPE_CONVERSION_REQUEST"
+ "IFPAYLOAD_UNDO_REDO_REQUEST"
+ "IFPAYLOAD_UNKNOWN"
+ "MTINVOCATIONTYPE_FACETIME_TRANSLATION"
+ "MTINVOCATIONTYPE_MESSAGES_TRANSLATION"
+ "MTINVOCATIONTYPE_PHONECALL_TRANSLATION"
+ "NLROUTERINVALIDDECISIONREASON_GENAI"
+ "NLROUTERINVALIDDECISIONREASON_MULTIPLE_ROUTINGLABEL"
+ "NLROUTERINVALIDDECISIONREASON_SIRIX"
+ "NLROUTERINVALIDDECISIONREASON_UNEXPECTED_OUTPUT"
+ "NLROUTERINVALIDDECISIONREASON_UNEXPECTED_ROUTINGLABEL"
+ "NLROUTERINVALIDDECISIONREASON_UNKNOWN"
+ "NLROUTERTRIGGEREDHEURISTICRULE_ALARMRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_ANNOUNCEMENTRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_APPLAUNCHRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_CALENDARRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_CRISISRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_DISMISSALRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_EMAILRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_FINDMYRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_GENAIRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_HALLUCINATIONRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_MATHRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_MDMRREWRITERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_MESSAGERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_MULTITURNHEURISTICRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_NLXOVERRIDESEXCEPTIONSRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_NOTERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_OVERRIDESSHORTCUTRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_PHONECALLRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_PLANNERDELETERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_PLANNERPHOTORULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_PLANNERUPDATERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_PLANNERWRITINGTOOLSRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_REMINDERRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_SETTINGRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_STOPRECORDINGRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_SUPERSUBSCRIPTINUTTERANCERULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_TIMERRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_TRANSLATIONRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_TWOSTEPCORRECTIONSRULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_UNDORULE"
+ "NLROUTERTRIGGEREDHEURISTICRULE_UNKNOWN"
+ "NLRouterSchemaNLRouterInvalidDecisionEmitted"
+ "ODDEVENTORIGIN_SIRI_ATTENTION_AND_INVOCATION"
+ "ODDEXTENSIONNAME_SIRI_ATTENTION_AND_INVOCATION_EXTENSION"
+ "ODDSiriSchemaODDAttentionInvocationCounts"
+ "ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported"
+ "ODDSiriSchemaODDAttentionInvocationDigest"
+ "ODDSiriSchemaODDAttentionInvocationDimensions"
+ "ODDSiriSchemaODDBluetoothCarCounts"
+ "ODDSiriSchemaODDBluetoothCarDigest"
+ "ODDSiriSchemaODDBluetoothCarDigestReported"
+ "ODDSiriSchemaODDBluetoothCarDimensions"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_SEARCH_SUCCEEDED_NO_MATCHING_TOOL"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_UNABLE_TO_HANDLE_REQUEST"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_VALUE_SELECTION_REQUIRED"
+ "PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo"
+ "PEGASUSSchemaPEGASUSPersonalizedItemInfo"
+ "SISchemaIFError"
+ "SISchemaIFOutcomeSuccess"
+ "SISchemaIFOutcomeToolDisambiguation"
+ "SUBREQUESTTYPE_THIRD_PARTY_LLM_NOT_FOR_ME"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_APP_SHORTCUTS"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_BASE_SET_APP_INTENTS"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_VOICE_SHORTCUTS"
+ "SUGUIACTIVITY_RENDERED"
+ "T@\"ExecutorSiriSchemaExecutorRequestCanceled\",&,N,V_canceled"
+ "T@\"ExecutorSiriSchemaExecutorRequestContext\",&,N,V_executorRequestContext"
+ "T@\"ExecutorSiriSchemaExecutorRequestEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorRequestFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorRequestStarted\",&,N,V_startedOrChanged"
+ "T@\"GATSchemaGATModelAgentCaptured\",&,N,V_modelAgentCaptured"
+ "T@\"GATSchemaGATNotForMeResponseReturned\",&,N,V_notForMeResponseReturned"
+ "T@\"NLRouterSchemaNLRouterInvalidDecisionEmitted\",&,N,V_nLRouterInvalidDecisionEmitted"
+ "T@\"NSArray\",C,N,V_personalizedItemInfos"
+ "T@\"NSString\",C,N,V_followUpActionBundleId"
+ "T@\"NSString\",C,N,V_voiceTriggerAssetVersion"
+ "T@\"ODDSiriSchemaODDAttentionInvocationCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDAttentionInvocationDeviceDigestsReported\",&,N,V_attentionInvocationDigestsReported"
+ "T@\"ODDSiriSchemaODDAttentionInvocationDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDBluetoothCarCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDBluetoothCarDigestReported\",&,N,V_bluetoothCarDigestReported"
+ "T@\"ODDSiriSchemaODDBluetoothCarDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDTurnCounts\",&,N,V_siriInBTCarTurnCounts"
+ "T@\"PEGASUSSchemaPEGASUSAMPPersonalizationLoggingInfo\",&,N,V_pegasusAmpPersonalizationLoggingInfo"
+ "T@\"SISchemaIFError\",&,N,V_error"
+ "T@\"SISchemaIFOutcomeSuccess\",&,N,V_success"
+ "T@\"SISchemaIFOutcomeToolDisambiguation\",&,N,V_toolDisambiguation"
+ "TB,N,V_hasAttentionInvocationDigestsReported"
+ "TB,N,V_hasBluetoothCarDigestReported"
+ "TB,N,V_hasExecutorRequestContext"
+ "TB,N,V_hasFollowUpActionBundleId"
+ "TB,N,V_hasModelAgentCaptured"
+ "TB,N,V_hasNLRouterInvalidDecisionEmitted"
+ "TB,N,V_hasNotForMeResponseReturned"
+ "TB,N,V_hasPegasusAmpPersonalizationLoggingInfo"
+ "TB,N,V_hasSiriInBTCarTurnCounts"
+ "TB,N,V_hasUnableToHandleRequest"
+ "TB,N,V_hasVoiceTriggerAssetVersion"
+ "TB,N,V_isGenAIConfirmationAlwaysRequired"
+ "TB,N,V_isGenAISetUpPrompts"
+ "TB,N,V_isPersonalizationEligible"
+ "TB,N,V_isPersonalized"
+ "TB,N,V_isPersonalizedSession"
+ "TB,N,V_isPersonalizedSessionAffected"
+ "TB,N,V_isQueryDirectQuestion"
+ "TB,N,V_isSoundAnalysisEnabled"
+ "TB,N,V_isSuppressed"
+ "TB,N,V_isUtteranceRewritten"
+ "TB,N,V_unableToHandleRequest"
+ "TI,N,V_ageOfProfileInMonths"
+ "TI,N,V_bluetoothCarConnectionsInTheLast24Hours"
+ "TI,N,V_carPlayConnectionsInTheLast24Hours"
+ "TI,N,V_checkerNearMissBeforeAcceptCount"
+ "TI,N,V_checkerRejectBeforeActivationCount"
+ "TI,N,V_falseWakeWithNoTriggerPhraseCount"
+ "TI,N,V_falseWakeWithSpeechNoMatchCount"
+ "TI,N,V_falseWakeWithTTMMitigationCount"
+ "TI,N,V_ncAcceptPostNcMitigationCount"
+ "TI,N,V_positionWithoutPersonalization"
+ "TI,N,V_spkidAcceptPostSpkidMitigationCount"
+ "TI,N,V_ttmAcceptPostTtmMitigationCount"
+ "TQ,R,N,V_whichOutcomedetails"
+ "TTSLLMSTYLEPROMPT_DEFAULT"
+ "TTSLLMSTYLEPROMPT_HIGH_INTENSITY"
+ "TTSLLMSTYLEPROMPT_MILD_INTENSITY"
+ "TTSLLMSTYLEPROMPT_NARRATION"
+ "TTSLLMSTYLEPROMPT_UNKNOWN"
+ "Tf,N,V_enrollmentPitchEstimation"
+ "Tf,N,V_personalizationArtistAffinity"
+ "Tf,N,V_personalizationCosineSimilarity"
+ "Tf,N,V_personalizationPafFrequency"
+ "Tf,N,V_personalizationRankingScore"
+ "Ti,N,V_genAIAccountType"
+ "Ti,N,V_inputPayload"
+ "Ti,N,V_llmStylePrompt"
+ "Ti,N,V_nlRouterInvalidDecisionReason"
+ "Ti,N,V_offeredAgent"
+ "Ti,N,V_requestedGenAIAgent"
+ "Ti,N,V_settingsAgent"
+ "Ti,N,V_triggeredHeuristic"
+ "_ageOfProfileInMonths"
+ "_attentionInvocationDigestsReported"
+ "_bluetoothCarConnectionsInTheLast24Hours"
+ "_bluetoothCarDigestReported"
+ "_carPlayConnectionsInTheLast24Hours"
+ "_checkerNearMissBeforeAcceptCount"
+ "_checkerRejectBeforeActivationCount"
+ "_enrollmentPitchEstimation"
+ "_executorRequestContext"
+ "_falseWakeWithNoTriggerPhraseCount"
+ "_falseWakeWithSpeechNoMatchCount"
+ "_falseWakeWithTTMMitigationCount"
+ "_followUpActionBundleId"
+ "_genAIAccountType"
+ "_hasAttentionInvocationDigestsReported"
+ "_hasBluetoothCarDigestReported"
+ "_hasExecutorRequestContext"
+ "_hasFollowUpActionBundleId"
+ "_hasModelAgentCaptured"
+ "_hasNLRouterInvalidDecisionEmitted"
+ "_hasNotForMeResponseReturned"
+ "_hasPegasusAmpPersonalizationLoggingInfo"
+ "_hasSiriInBTCarTurnCounts"
+ "_hasUnableToHandleRequest"
+ "_hasVoiceTriggerAssetVersion"
+ "_inputPayload"
+ "_isGenAIConfirmationAlwaysRequired"
+ "_isGenAISetUpPrompts"
+ "_isPersonalizationEligible"
+ "_isPersonalized"
+ "_isPersonalizedSession"
+ "_isPersonalizedSessionAffected"
+ "_isQueryDirectQuestion"
+ "_isSoundAnalysisEnabled"
+ "_isSuppressed"
+ "_isUtteranceRewritten"
+ "_llmStylePrompt"
+ "_modelAgentCaptured"
+ "_nLRouterInvalidDecisionEmitted"
+ "_ncAcceptPostNcMitigationCount"
+ "_nlRouterInvalidDecisionReason"
+ "_notForMeResponseReturned"
+ "_offeredAgent"
+ "_pegasusAmpPersonalizationLoggingInfo"
+ "_personalizationArtistAffinity"
+ "_personalizationCosineSimilarity"
+ "_personalizationPafFrequency"
+ "_personalizationRankingScore"
+ "_personalizedItemInfos"
+ "_positionWithoutPersonalization"
+ "_requestedGenAIAgent"
+ "_setError"
+ "_settingsAgent"
+ "_siriInBTCarTurnCounts"
+ "_spkidAcceptPostSpkidMitigationCount"
+ "_triggeredHeuristic"
+ "_ttmAcceptPostTtmMitigationCount"
+ "_unableToHandleRequest"
+ "_voiceTriggerAssetVersion"
+ "_whichOutcomedetails"
+ "addPersonalizedItemInfo:"
+ "ageOfProfileInMonths"
+ "attentionInvocationDigestsReported"
+ "bluetoothCarConnectionsInTheLast24Hours"
+ "bluetoothCarDigestReported"
+ "carPlayConnectionsInTheLast24Hours"
+ "checkerNearMissBeforeAcceptCount"
+ "checkerRejectBeforeActivationCount"
+ "clearPersonalizedItemInfo"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorRequestContext"
+ "com.apple.aiml.siri.gat.GATClientEvent.GATModelAgentCaptured"
+ "com.apple.aiml.siri.gat.GATClientEvent.GATNotForMeResponseReturned"
+ "com.apple.aiml.siri.nlrouter.NLRouterClientEvent.NLRouterInvalidDecisionEmitted"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAttentionInvocationDeviceDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDBluetoothCarDigestReported"
+ "com.apple.aiml.siri.pegasus.PEGASUSServerEvent.PEGASUSAMPPersonalizationLoggingInfo"
+ "deleteAgeOfProfileInMonths"
+ "deleteAttentionInvocationDigestsReported"
+ "deleteBluetoothCarConnectionsInTheLast24Hours"
+ "deleteBluetoothCarDigestReported"
+ "deleteCarPlayConnectionsInTheLast24Hours"
+ "deleteCheckerNearMissBeforeAcceptCount"
+ "deleteCheckerRejectBeforeActivationCount"
+ "deleteEnrollmentPitchEstimation"
+ "deleteExecutorRequestContext"
+ "deleteFalseWakeWithNoTriggerPhraseCount"
+ "deleteFalseWakeWithSpeechNoMatchCount"
+ "deleteFalseWakeWithTTMMitigationCount"
+ "deleteFollowUpActionBundleId"
+ "deleteGenAIAccountType"
+ "deleteInputPayload"
+ "deleteIsGenAIConfirmationAlwaysRequired"
+ "deleteIsGenAISetUpPrompts"
+ "deleteIsPersonalizationEligible"
+ "deleteIsPersonalized"
+ "deleteIsPersonalizedSession"
+ "deleteIsPersonalizedSessionAffected"
+ "deleteIsQueryDirectQuestion"
+ "deleteIsSoundAnalysisEnabled"
+ "deleteIsSuppressed"
+ "deleteIsUtteranceRewritten"
+ "deleteLlmStylePrompt"
+ "deleteModelAgentCaptured"
+ "deleteNLRouterInvalidDecisionEmitted"
+ "deleteNcAcceptPostNcMitigationCount"
+ "deleteNlRouterInvalidDecisionReason"
+ "deleteNotForMeResponseReturned"
+ "deleteOfferedAgent"
+ "deletePegasusAmpPersonalizationLoggingInfo"
+ "deletePersonalizationArtistAffinity"
+ "deletePersonalizationCosineSimilarity"
+ "deletePersonalizationPafFrequency"
+ "deletePersonalizationRankingScore"
+ "deletePersonalizedItemInfo"
+ "deletePositionWithoutPersonalization"
+ "deleteRequestedGenAIAgent"
+ "deleteSettingsAgent"
+ "deleteSiriInBTCarTurnCounts"
+ "deleteSpkidAcceptPostSpkidMitigationCount"
+ "deleteTriggeredHeuristic"
+ "deleteTtmAcceptPostTtmMitigationCount"
+ "deleteUnableToHandleRequest"
+ "deleteVoiceTriggerAssetVersion"
+ "enrollmentPitchEstimation"
+ "executorRequestContext"
+ "executorRequestContext.ended.success.followUpActionBundleId"
+ "executorRequestContext.ended.toolDisambiguation.assistantSchemaKind"
+ "falseWakeWithNoTriggerPhraseCount"
+ "falseWakeWithSpeechNoMatchCount"
+ "falseWakeWithTTMMitigationCount"
+ "followUpActionBundleId"
+ "genAIAccountType"
+ "getBytes:range:"
+ "hasAgeOfProfileInMonths"
+ "hasAttentionInvocationDigestsReported"
+ "hasBluetoothCarConnectionsInTheLast24Hours"
+ "hasBluetoothCarDigestReported"
+ "hasCarPlayConnectionsInTheLast24Hours"
+ "hasCheckerNearMissBeforeAcceptCount"
+ "hasCheckerRejectBeforeActivationCount"
+ "hasEnrollmentPitchEstimation"
+ "hasExecutorRequestContext"
+ "hasFalseWakeWithNoTriggerPhraseCount"
+ "hasFalseWakeWithSpeechNoMatchCount"
+ "hasFalseWakeWithTTMMitigationCount"
+ "hasFollowUpActionBundleId"
+ "hasGenAIAccountType"
+ "hasInputPayload"
+ "hasIsGenAIConfirmationAlwaysRequired"
+ "hasIsGenAISetUpPrompts"
+ "hasIsPersonalizationEligible"
+ "hasIsPersonalized"
+ "hasIsPersonalizedSession"
+ "hasIsPersonalizedSessionAffected"
+ "hasIsQueryDirectQuestion"
+ "hasIsSoundAnalysisEnabled"
+ "hasIsSuppressed"
+ "hasIsUtteranceRewritten"
+ "hasLlmStylePrompt"
+ "hasModelAgentCaptured"
+ "hasNLRouterInvalidDecisionEmitted"
+ "hasNcAcceptPostNcMitigationCount"
+ "hasNlRouterInvalidDecisionReason"
+ "hasNotForMeResponseReturned"
+ "hasOfferedAgent"
+ "hasPegasusAmpPersonalizationLoggingInfo"
+ "hasPersonalizationArtistAffinity"
+ "hasPersonalizationCosineSimilarity"
+ "hasPersonalizationPafFrequency"
+ "hasPersonalizationRankingScore"
+ "hasPositionWithoutPersonalization"
+ "hasRequestedGenAIAgent"
+ "hasSettingsAgent"
+ "hasSiriInBTCarTurnCounts"
+ "hasSpkidAcceptPostSpkidMitigationCount"
+ "hasTriggeredHeuristic"
+ "hasTtmAcceptPostTtmMitigationCount"
+ "hasUnableToHandleRequest"
+ "hasVoiceTriggerAssetVersion"
+ "inputPayload"
+ "isGenAIConfirmationAlwaysRequired"
+ "isGenAISetUpPrompts"
+ "isPersonalizationEligible"
+ "isPersonalized"
+ "isPersonalizedSession"
+ "isPersonalizedSessionAffected"
+ "isQueryDirectQuestion"
+ "isSoundAnalysisEnabled"
+ "isSuppressed"
+ "isUtteranceRewritten"
+ "llmStylePrompt"
+ "modelAgentCaptured"
+ "nLRouterInvalidDecisionEmitted"
+ "ncAcceptPostNcMitigationCount"
+ "nlRouterInvalidDecisionReason"
+ "notForMeResponseReturned"
+ "offeredAgent"
+ "pegasusAmpPersonalizationLoggingInfo"
+ "personalizationArtistAffinity"
+ "personalizationCosineSimilarity"
+ "personalizationPafFrequency"
+ "personalizationRankingScore"
+ "personalizedItemInfo"
+ "personalizedItemInfoAtIndex:"
+ "personalizedItemInfoCount"
+ "personalizedItemInfos"
+ "position"
+ "positionWithoutPersonalization"
+ "requestedGenAIAgent"
+ "setAgeOfProfileInMonths:"
+ "setAttentionInvocationDigestsReported:"
+ "setBluetoothCarConnectionsInTheLast24Hours:"
+ "setBluetoothCarDigestReported:"
+ "setCarPlayConnectionsInTheLast24Hours:"
+ "setCheckerNearMissBeforeAcceptCount:"
+ "setCheckerRejectBeforeActivationCount:"
+ "setEnrollmentPitchEstimation:"
+ "setExecutorRequestContext:"
+ "setFalseWakeWithNoTriggerPhraseCount:"
+ "setFalseWakeWithSpeechNoMatchCount:"
+ "setFalseWakeWithTTMMitigationCount:"
+ "setFollowUpActionBundleId:"
+ "setGenAIAccountType:"
+ "setHasAgeOfProfileInMonths:"
+ "setHasAttentionInvocationDigestsReported:"
+ "setHasBluetoothCarConnectionsInTheLast24Hours:"
+ "setHasBluetoothCarDigestReported:"
+ "setHasCarPlayConnectionsInTheLast24Hours:"
+ "setHasCheckerNearMissBeforeAcceptCount:"
+ "setHasCheckerRejectBeforeActivationCount:"
+ "setHasEnrollmentPitchEstimation:"
+ "setHasExecutorRequestContext:"
+ "setHasFalseWakeWithNoTriggerPhraseCount:"
+ "setHasFalseWakeWithSpeechNoMatchCount:"
+ "setHasFalseWakeWithTTMMitigationCount:"
+ "setHasFollowUpActionBundleId:"
+ "setHasGenAIAccountType:"
+ "setHasInputPayload:"
+ "setHasIsGenAIConfirmationAlwaysRequired:"
+ "setHasIsGenAISetUpPrompts:"
+ "setHasIsPersonalizationEligible:"
+ "setHasIsPersonalized:"
+ "setHasIsPersonalizedSession:"
+ "setHasIsPersonalizedSessionAffected:"
+ "setHasIsQueryDirectQuestion:"
+ "setHasIsSoundAnalysisEnabled:"
+ "setHasIsSuppressed:"
+ "setHasIsUtteranceRewritten:"
+ "setHasLlmStylePrompt:"
+ "setHasModelAgentCaptured:"
+ "setHasNLRouterInvalidDecisionEmitted:"
+ "setHasNcAcceptPostNcMitigationCount:"
+ "setHasNlRouterInvalidDecisionReason:"
+ "setHasNotForMeResponseReturned:"
+ "setHasOfferedAgent:"
+ "setHasPegasusAmpPersonalizationLoggingInfo:"
+ "setHasPersonalizationArtistAffinity:"
+ "setHasPersonalizationCosineSimilarity:"
+ "setHasPersonalizationPafFrequency:"
+ "setHasPersonalizationRankingScore:"
+ "setHasPositionWithoutPersonalization:"
+ "setHasRequestedGenAIAgent:"
+ "setHasSettingsAgent:"
+ "setHasSiriInBTCarTurnCounts:"
+ "setHasSpkidAcceptPostSpkidMitigationCount:"
+ "setHasTriggeredHeuristic:"
+ "setHasTtmAcceptPostTtmMitigationCount:"
+ "setHasUnableToHandleRequest:"
+ "setHasVoiceTriggerAssetVersion:"
+ "setInputPayload:"
+ "setIsGenAIConfirmationAlwaysRequired:"
+ "setIsGenAISetUpPrompts:"
+ "setIsPersonalizationEligible:"
+ "setIsPersonalized:"
+ "setIsPersonalizedSession:"
+ "setIsPersonalizedSessionAffected:"
+ "setIsQueryDirectQuestion:"
+ "setIsSoundAnalysisEnabled:"
+ "setIsSuppressed:"
+ "setIsUtteranceRewritten:"
+ "setLlmStylePrompt:"
+ "setModelAgentCaptured:"
+ "setNLRouterInvalidDecisionEmitted:"
+ "setNcAcceptPostNcMitigationCount:"
+ "setNlRouterInvalidDecisionReason:"
+ "setNotForMeResponseReturned:"
+ "setOfferedAgent:"
+ "setPegasusAmpPersonalizationLoggingInfo:"
+ "setPersonalizationArtistAffinity:"
+ "setPersonalizationCosineSimilarity:"
+ "setPersonalizationPafFrequency:"
+ "setPersonalizationRankingScore:"
+ "setPersonalizedItemInfos:"
+ "setPosition:"
+ "setPositionWithoutPersonalization:"
+ "setRequestedGenAIAgent:"
+ "setSettingsAgent:"
+ "setSiriInBTCarTurnCounts:"
+ "setSpkidAcceptPostSpkidMitigationCount:"
+ "setTriggeredHeuristic:"
+ "setTtmAcceptPostTtmMitigationCount:"
+ "setUnableToHandleRequest:"
+ "setVoiceTriggerAssetVersion:"
+ "settingsAgent"
+ "siriInBTCarTurnCounts"
+ "spkidAcceptPostSpkidMitigationCount"
+ "triggeredHeuristic"
+ "ttmAcceptPostTtmMitigationCount"
+ "unableToHandleRequest"
+ "voiceTriggerAssetVersion"
+ "whichOutcomedetails"
+ "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1\"audioQueueLatencyInSecond\"b1\"isWarmStart\"b1\"llmStylePrompt\"b1}"
+ "{?=\"bluetoothCarConnectionsInTheLast24Hours\"b1}"
+ "{?=\"carPlayConnectionsInTheLast24Hours\"b1}"
+ "{?=\"dataSharingOptInStatus\"b1\"invocationSource\"b1\"triggerPhrase\"b1\"ageOfProfileInMonths\"b1\"enrollmentPitchEstimation\"b1}"
+ "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1\"invocationSource\"b1}"
+ "{?=\"didShowInAppResult\"b1\"shouldOpen\"b1}"
+ "{?=\"inputPayload\"b1}"
+ "{?=\"isAppleIntelligenceEnabled\"b1\"isRecordAppleIntelligenceActivity\"b1\"isAppleIntelligenceHardwareCapable\"b1\"isAppleIntelligenceAvailable\"b1\"isChatGPTEnabled\"b1\"isChatGPTConfirmationAlwaysRequired\"b1\"chatGPTAccountType\"b1\"isChatGPTSetUpPrompts\"b1\"isGenAIConfirmationAlwaysRequired\"b1\"genAIAccountType\"b1\"isGenAISetUpPrompts\"b1}"
+ "{?=\"isExplicit\"b1\"genAIAppIntent\"b1\"correctionOutcome\"b1\"requestedGenAIAgent\"b1}"
+ "{?=\"isKnowledgeFallbackConfirmationShown\"b1\"offeredAgent\"b1}"
+ "{?=\"isPersonalizationEligible\"b1\"isPersonalizedSession\"b1\"isPersonalizedSessionAffected\"b1}"
+ "{?=\"isPersonalized\"b1\"score\"b1\"personalizationRankingScore\"b1\"positionWithoutPersonalization\"b1\"personalizationCosineSimilarity\"b1\"personalizationArtistAffinity\"b1\"personalizationPafFrequency\"b1}"
+ "{?=\"isSuppressed\"b1\"nlRouterInvalidDecisionReason\"b1}"
+ "{?=\"isUtteranceRewritten\"b1}"
+ "{?=\"phsRejectBeforeActivationCount\"b1\"checkerRejectBeforeActivationCount\"b1\"checkerNearMissBeforeAcceptCount\"b1\"falseWakeWithNoTriggerPhraseCount\"b1\"falseWakeWithSpeechNoMatchCount\"b1\"falseWakeWithTTMMitigationCount\"b1\"ncAcceptPostNcMitigationCount\"b1\"spkidAcceptPostSpkidMitigationCount\"b1\"ttmAcceptPostTtmMitigationCount\"b1}"
+ "{?=\"pommesConfidenceScore\"b1\"isFromResponseCache\"b1\"pegasusPromptType\"b1\"isLowConfidenceKnowledgeResult\"b1\"isQueryDirectQuestion\"b1}"
+ "{?=\"requestedAgent\"b1\"settingsAgent\"b1}"
+ "{?=\"systemLocale\"b1\"siriInputLocale\"b1\"dataSharingOptInState\"b1\"countryCode\"b1\"isStoreDemoMode\"b1\"timeIntervalSince1970\"b1\"isLowPowerModeEnabled\"b1\"programCode\"b1\"homeKitConfiguration\"b1\"availableDictationKeyboards\"b1\"searchDataOptOutState\"b1\"isLongLivedIDUploadDisabled\"b1}"
+ "{?=\"thermalState\"b1\"motionActivity\"b1\"timeSinceAssistantDaemonStartedInMs\"b1\"headGesturesSupported\"b1\"headGesturesEnabled\"b1\"acceptProceedGesture\"b1\"declineDismissGesture\"b1\"isWifiEnabled\"b1\"bluetoothState\"b1\"flashlightLevel\"b1\"isChatGPTEnabled\"b1\"isSoundAnalysisEnabled\"b1}"
+ "{?=\"triggeredHeuristic\"b1}"
- "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1\"audioQueueLatencyInSecond\"b1\"isWarmStart\"b1}"
- "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1}"
- "{?=\"isAppleIntelligenceEnabled\"b1\"isRecordAppleIntelligenceActivity\"b1\"isAppleIntelligenceHardwareCapable\"b1\"isAppleIntelligenceAvailable\"b1\"isChatGPTEnabled\"b1\"isChatGPTConfirmationAlwaysRequired\"b1\"chatGPTAccountType\"b1\"isChatGPTSetUpPrompts\"b1}"
- "{?=\"isExplicit\"b1\"genAIAppIntent\"b1\"correctionOutcome\"b1}"
- "{?=\"isKnowledgeFallbackConfirmationShown\"b1}"
- "{?=\"pommesConfidenceScore\"b1\"isFromResponseCache\"b1\"pegasusPromptType\"b1\"isLowConfidenceKnowledgeResult\"b1}"
- "{?=\"systemLocale\"b1\"siriInputLocale\"b1\"dataSharingOptInState\"b1\"countryCode\"b1\"isStoreDemoMode\"b1\"timeIntervalSince1970\"b1\"isLowPowerModeEnabled\"b1\"programCode\"b1\"homeKitConfiguration\"b1\"availableDictationKeyboards\"b1\"searchDataOptOutState\"b1}"
- "{?=\"thermalState\"b1\"motionActivity\"b1\"timeSinceAssistantDaemonStartedInMs\"b1\"headGesturesSupported\"b1\"headGesturesEnabled\"b1\"acceptProceedGesture\"b1\"declineDismissGesture\"b1\"isWifiEnabled\"b1\"bluetoothState\"b1\"flashlightLevel\"b1\"isChatGPTEnabled\"b1}"

```
