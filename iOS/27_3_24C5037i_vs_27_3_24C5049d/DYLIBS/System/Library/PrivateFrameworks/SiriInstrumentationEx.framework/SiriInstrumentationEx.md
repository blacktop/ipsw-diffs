## SiriInstrumentationEx

> `/System/Library/PrivateFrameworks/SiriInstrumentationEx.framework/SiriInstrumentationEx`

```diff

-3610.11.2.0.0
-  __TEXT.__text: 0x29bbbc
-  __TEXT.__objc_methlist: 0x2355c
-  __TEXT.__const: 0x5ba14
+3610.17.1.0.0
+  __TEXT.__text: 0x2b41b0
+  __TEXT.__objc_methlist: 0x25394
+  __TEXT.__const: 0x5c494
   __TEXT.__constg_swiftt: 0xc
-  __TEXT.__swift5_proto: 0x35cc
+  __TEXT.__swift5_proto: 0x362c
   __TEXT.__swift5_typeref: 0xa
-  __TEXT.__cstring: 0xb031
-  __TEXT.__unwind_info: 0xead0
+  __TEXT.__cstring: 0xbd8b
+  __TEXT.__unwind_info: 0xf158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1620
-  __DATA_CONST.__objc_classlist: 0x1168
+  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__objc_classlist: 0x1228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1eda8
-  __DATA_CONST.__objc_superrefs: 0x1168
-  __DATA_CONST.__got: 0x1710
-  __AUTH_CONST.__cfstring: 0xba00
-  __AUTH_CONST.__objc_const: 0x33df0
+  __DATA_CONST.__objc_selrefs: 0x1f650
+  __DATA_CONST.__objc_superrefs: 0x1228
+  __DATA_CONST.__got: 0x17a0
+  __AUTH_CONST.__cfstring: 0xc820
+  __AUTH_CONST.__objc_const: 0x36780
   __AUTH_CONST.__auth_got: 0x260
-  __AUTH.__objc_data: 0xae10
-  __DATA.__objc_ivar: 0x23c0
-  __DATA.__data: 0xb40
+  __AUTH.__objc_data: 0xb590
+  __DATA.__objc_ivar: 0x25ac
+  __DATA.__data: 0xb68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19015
-  Symbols:   18198
-  CStrings:  1495
+  Functions: 19690
+  Symbols:   19114
+  CStrings:  1608
 
Symbols:
+ -[CHSchemaCHGraderResult deleteResponseRelevancyJudgeInferenceMetadata]
+ -[CHSchemaCHGraderResult hasResponseRelevancyJudgeInferenceMetadata]
+ -[CHSchemaCHGraderResult responseRelevancyJudgeInferenceMetadata]
+ -[CHSchemaCHGraderResult setHasResponseRelevancyJudgeInferenceMetadata:]
+ -[CHSchemaCHGraderResult setResponseRelevancyJudgeInferenceMetadata:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata deleteEssentialConstraints]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata deleteGrade]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata deleteOutcomeCoverage]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata deleteQualifyingContent]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata deleteSupportedTask]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata dictionaryRepresentation]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata essentialConstraints]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata grade]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hasEssentialConstraints]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hasGrade]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hasOutcomeCoverage]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hasQualifyingContent]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hasSupportedTask]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata hash]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata initWithDictionary:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata initWithJSON:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata isEqual:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata jsonData]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata outcomeCoverage]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata qualifyingContent]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata readFrom:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setEssentialConstraints:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setGrade:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setHasEssentialConstraints:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setHasGrade:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setHasOutcomeCoverage:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setHasQualifyingContent:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setHasSupportedTask:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setOutcomeCoverage:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setQualifyingContent:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata setSupportedTask:]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata supportedTask]
+ -[CHSchemaCHResponseRelevancyJudgeInferenceMetadata writeTo:]
+ -[MHSchemaMHMutexRequested currentOwner]
+ -[MHSchemaMHMutexRequested deleteCurrentOwner]
+ -[MHSchemaMHMutexRequested deleteHoldTimeOfASRResourceInMs]
+ -[MHSchemaMHMutexRequested deleteHoldTimeOfAudioResourceInMs]
+ -[MHSchemaMHMutexRequested deleteHoldTimeOfUnspecifiedResourceInMs]
+ -[MHSchemaMHMutexRequested deleteRequestedResourceType]
+ -[MHSchemaMHMutexRequested deleteRequester]
+ -[MHSchemaMHMutexRequested deleteSuccessfullyAcquired]
+ -[MHSchemaMHMutexRequested dictionaryRepresentation]
+ -[MHSchemaMHMutexRequested hasCurrentOwner]
+ -[MHSchemaMHMutexRequested hasHoldTimeOfASRResourceInMs]
+ -[MHSchemaMHMutexRequested hasHoldTimeOfAudioResourceInMs]
+ -[MHSchemaMHMutexRequested hasHoldTimeOfUnspecifiedResourceInMs]
+ -[MHSchemaMHMutexRequested hasRequestedResourceType]
+ -[MHSchemaMHMutexRequested hasRequester]
+ -[MHSchemaMHMutexRequested hasSuccessfullyAcquired]
+ -[MHSchemaMHMutexRequested hash]
+ -[MHSchemaMHMutexRequested holdTimeOfASRResourceInMs]
+ -[MHSchemaMHMutexRequested holdTimeOfAudioResourceInMs]
+ -[MHSchemaMHMutexRequested holdTimeOfUnspecifiedResourceInMs]
+ -[MHSchemaMHMutexRequested initWithDictionary:]
+ -[MHSchemaMHMutexRequested initWithJSON:]
+ -[MHSchemaMHMutexRequested isEqual:]
+ -[MHSchemaMHMutexRequested jsonData]
+ -[MHSchemaMHMutexRequested readFrom:]
+ -[MHSchemaMHMutexRequested requestedResourceType]
+ -[MHSchemaMHMutexRequested requester]
+ -[MHSchemaMHMutexRequested setCurrentOwner:]
+ -[MHSchemaMHMutexRequested setHasCurrentOwner:]
+ -[MHSchemaMHMutexRequested setHasHoldTimeOfASRResourceInMs:]
+ -[MHSchemaMHMutexRequested setHasHoldTimeOfAudioResourceInMs:]
+ -[MHSchemaMHMutexRequested setHasHoldTimeOfUnspecifiedResourceInMs:]
+ -[MHSchemaMHMutexRequested setHasRequestedResourceType:]
+ -[MHSchemaMHMutexRequested setHasRequester:]
+ -[MHSchemaMHMutexRequested setHasSuccessfullyAcquired:]
+ -[MHSchemaMHMutexRequested setHoldTimeOfASRResourceInMs:]
+ -[MHSchemaMHMutexRequested setHoldTimeOfAudioResourceInMs:]
+ -[MHSchemaMHMutexRequested setHoldTimeOfUnspecifiedResourceInMs:]
+ -[MHSchemaMHMutexRequested setRequestedResourceType:]
+ -[MHSchemaMHMutexRequested setRequester:]
+ -[MHSchemaMHMutexRequested setSuccessfullyAcquired:]
+ -[MHSchemaMHMutexRequested successfullyAcquired]
+ -[MHSchemaMHMutexRequested writeTo:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteIsEligibleForHighConfidenceUserSession]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteIsFinal]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteIsScoreOverridden]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived hasIsEligibleForHighConfidenceUserSession]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived hasIsFinal]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived hasIsScoreOverridden]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived isEligibleForHighConfidenceUserSession]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived isFinal]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived isScoreOverridden]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setHasIsEligibleForHighConfidenceUserSession:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setHasIsFinal:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setHasIsScoreOverridden:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setIsEligibleForHighConfidenceUserSession:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setIsFinal:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setIsScoreOverridden:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled deleteExists]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled exists]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled hasExists]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled hash]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled setExists:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled setHasExists:]
+ -[PLANNERSchemaPLANNERPCCRoutingCanceled writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingContext canceled]
+ -[PLANNERSchemaPLANNERPCCRoutingContext deleteCanceled]
+ -[PLANNERSchemaPLANNERPCCRoutingContext deleteEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingContext deleteFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingContext deleteStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingContext dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingContext ended]
+ -[PLANNERSchemaPLANNERPCCRoutingContext failed]
+ -[PLANNERSchemaPLANNERPCCRoutingContext hasCanceled]
+ -[PLANNERSchemaPLANNERPCCRoutingContext hasEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingContext hasFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingContext hasStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingContext hash]
+ -[PLANNERSchemaPLANNERPCCRoutingContext initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingContext readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setCanceled:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setHasCanceled:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setHasEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setHasFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setHasStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext setStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingContext startedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingContext whichContextevent]
+ -[PLANNERSchemaPLANNERPCCRoutingContext writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteScoreLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteScoreMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteScoreSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteThresholdLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteThresholdMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteThresholdSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision deleteTier]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasScoreLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasScoreMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasScoreSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasThresholdLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasThresholdMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasThresholdSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hasTier]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision hash]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision scoreLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision scoreMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision scoreSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasScoreLarge:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasScoreMedium:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasScoreSmall:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasThresholdLarge:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasThresholdMedium:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasThresholdSmall:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setHasTier:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setScoreLarge:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setScoreMedium:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setScoreSmall:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setThresholdLarge:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setThresholdMedium:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setThresholdSmall:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision setTier:]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision thresholdLarge]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision thresholdMedium]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision thresholdSmall]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision tier]
+ -[PLANNERSchemaPLANNERPCCRoutingDecision writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded deleteInputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded deleteIsWaitBudgetExceeded]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded deleteOutputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded deleteQualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded hasInputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded hasIsWaitBudgetExceeded]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded hasOutputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded hasQualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded hash]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded inputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded isWaitBudgetExceeded]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded outputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded qualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setHasInputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setHasIsWaitBudgetExceeded:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setHasOutputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setHasQualityDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setInputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setIsWaitBudgetExceeded:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setOutputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded setQualityDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingEnded writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed addErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed clearErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed deleteErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed errorsAtIndex:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed errorsCount]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed errors]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed hash]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed setErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingFailed writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext deleteEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext deleteFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext deleteStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext ended]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext failed]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext hasEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext hasFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext hasStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext hash]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setHasEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setHasFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setHasStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext setStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext startedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext whichContextevent]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadContext writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded deleteModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded hasModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded hash]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded modelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded setHasModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded setModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadEnded writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed addErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed clearErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed deleteErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed errorsAtIndex:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed errorsCount]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed errors]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed hash]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed setErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadFailed writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted deleteProducer]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted hasProducer]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted hash]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted producer]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted setHasProducer:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted setProducer:]
+ -[PLANNERSchemaPLANNERPCCRoutingModelLoadStarted writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext deleteEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext deleteFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext deleteStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext ended]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext failed]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext hasEnded]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext hasFailed]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext hasStartedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext hash]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setHasEnded:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setHasFailed:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setHasStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext setStartedOrChanged:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext startedOrChanged]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext whichContextevent]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineContext writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded deleteInputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded deleteOutputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded deleteQualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded hasInputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded hasOutputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded hasQualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded hash]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded inputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded outputEffortDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded qualityDecision]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setHasInputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setHasOutputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setHasQualityDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setInputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setOutputEffortDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded setQualityDecision:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineEnded writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed addErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed clearErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed deleteErrors]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed errorsAtIndex:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed errorsCount]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed errors]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed hash]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed setErrors:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineFailed writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted deleteModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted deleteOriginalIfRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted deleteOriginalIfSessionId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted deleteOriginalRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted hasModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted hasOriginalIfRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted hasOriginalIfSessionId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted hasOriginalRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted hash]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted modelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted originalIfRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted originalIfSessionId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted originalRequestId]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setHasModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setHasOriginalIfRequestId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setHasOriginalIfSessionId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setHasOriginalRequestId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setOriginalIfRequestId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setOriginalIfSessionId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted setOriginalRequestId:]
+ -[PLANNERSchemaPLANNERPCCRoutingOfflineStarted writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped deleteIsShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped deleteSkipReason]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped hasIsShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped hasSkipReason]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped hash]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped isShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped setHasIsShadowMode:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped setHasSkipReason:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped setIsShadowMode:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped setSkipReason:]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped skipReason]
+ -[PLANNERSchemaPLANNERPCCRoutingSkipped writeTo:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted .cxx_destruct]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted deleteIsShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted deleteModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted hasIsShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted hasModelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted hash]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted initWithDictionary:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted initWithJSON:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted isEqual:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted isShadowMode]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted jsonData]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted modelVersion]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted readFrom:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted setHasIsShadowMode:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted setHasModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted setIsShadowMode:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted setModelVersion:]
+ -[PLANNERSchemaPLANNERPCCRoutingStarted writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo addDrops:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo clearDrops]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo deleteDrops]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo dropsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo dropsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo drops]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo setDrops:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop deleteDroppedCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop deleteReason]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop droppedCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop hasDroppedCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop hasReason]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop reason]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop setDroppedCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop setHasDroppedCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop setHasReason:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop setReason:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool deleteDescriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool deleteNameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool deleteParameterCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool descriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool hasDescriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool hasNameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool hasParameterCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool nameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool parameterCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setDescriptionCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setHasDescriptionCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setHasNameCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setHasParameterCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setNameCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool setParameterCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill bodyCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill deleteBodyCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill deleteDescriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill deleteNameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill descriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill hasBodyCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill hasDescriptionCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill hasNameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill nameCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setBodyCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setDescriptionCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setHasBodyCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setHasDescriptionCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setHasNameCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill setNameCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppSkill writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef deleteRenderedCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef deleteSchemaKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef hasRenderedCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef hasSchemaKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef renderedCharLength]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef schemaKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setHasRenderedCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setHasSchemaKind:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setRenderedCharLength:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setSchemaKind:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult addErrors:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult clearErrors]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult deleteErrors]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult errorsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult errorsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult errors]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult setErrors:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted addAppIntegrationGates:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted addInputEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted appIntegrationGatesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted appIntegrationGatesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted appIntegrationGates]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted appIntegrationSchemaSource]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted clearAppIntegrationGates]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted clearInputEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted deleteAppIntegrationGates]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted deleteAppIntegrationSchemaSource]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted deleteGenerableEntityArgumentCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted deleteInputEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted generableEntityArgumentCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted hasAppIntegrationSchemaSource]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted hasGenerableEntityArgumentCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted inputEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted inputEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted inputEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setAppIntegrationGates:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setAppIntegrationSchemaSource:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setGenerableEntityArgumentCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setHasAppIntegrationSchemaSource:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setHasGenerableEntityArgumentCount:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted setInputEntities:]
+ -[SISchemaUEIDisplayedWeblink .cxx_destruct]
+ -[SISchemaUEIDisplayedWeblink deletePosition]
+ -[SISchemaUEIDisplayedWeblink deleteTopic]
+ -[SISchemaUEIDisplayedWeblink deleteUrl]
+ -[SISchemaUEIDisplayedWeblink dictionaryRepresentation]
+ -[SISchemaUEIDisplayedWeblink hasPosition]
+ -[SISchemaUEIDisplayedWeblink hasTopic]
+ -[SISchemaUEIDisplayedWeblink hasUrl]
+ -[SISchemaUEIDisplayedWeblink hash]
+ -[SISchemaUEIDisplayedWeblink initWithDictionary:]
+ -[SISchemaUEIDisplayedWeblink initWithJSON:]
+ -[SISchemaUEIDisplayedWeblink isEqual:]
+ -[SISchemaUEIDisplayedWeblink jsonData]
+ -[SISchemaUEIDisplayedWeblink position]
+ -[SISchemaUEIDisplayedWeblink readFrom:]
+ -[SISchemaUEIDisplayedWeblink setHasPosition:]
+ -[SISchemaUEIDisplayedWeblink setHasTopic:]
+ -[SISchemaUEIDisplayedWeblink setHasUrl:]
+ -[SISchemaUEIDisplayedWeblink setPosition:]
+ -[SISchemaUEIDisplayedWeblink setTopic:]
+ -[SISchemaUEIDisplayedWeblink setUrl:]
+ -[SISchemaUEIDisplayedWeblink topic]
+ -[SISchemaUEIDisplayedWeblink url]
+ -[SISchemaUEIDisplayedWeblink writeTo:]
+ -[SISchemaUEILinkTapped deleteWeblinkMetadata]
+ -[SISchemaUEILinkTapped hasWeblinkMetadata]
+ -[SISchemaUEILinkTapped setHasWeblinkMetadata:]
+ -[SISchemaUEILinkTapped setWeblinkMetadata:]
+ -[SISchemaUEILinkTapped weblinkMetadata]
+ -[SISchemaUEIWeblinkMetadata deleteOpenSource]
+ -[SISchemaUEIWeblinkMetadata deletePosition]
+ -[SISchemaUEIWeblinkMetadata dictionaryRepresentation]
+ -[SISchemaUEIWeblinkMetadata hasOpenSource]
+ -[SISchemaUEIWeblinkMetadata hasPosition]
+ -[SISchemaUEIWeblinkMetadata hash]
+ -[SISchemaUEIWeblinkMetadata initWithDictionary:]
+ -[SISchemaUEIWeblinkMetadata initWithJSON:]
+ -[SISchemaUEIWeblinkMetadata isEqual:]
+ -[SISchemaUEIWeblinkMetadata jsonData]
+ -[SISchemaUEIWeblinkMetadata openSource]
+ -[SISchemaUEIWeblinkMetadata position]
+ -[SISchemaUEIWeblinkMetadata readFrom:]
+ -[SISchemaUEIWeblinkMetadata setHasOpenSource:]
+ -[SISchemaUEIWeblinkMetadata setHasPosition:]
+ -[SISchemaUEIWeblinkMetadata setOpenSource:]
+ -[SISchemaUEIWeblinkMetadata setPosition:]
+ -[SISchemaUEIWeblinkMetadata writeTo:]
+ -[SISchemaUEIWeblinksDisplayed .cxx_destruct]
+ -[SISchemaUEIWeblinksDisplayed addWeblinks:]
+ -[SISchemaUEIWeblinksDisplayed clearWeblinks]
+ -[SISchemaUEIWeblinksDisplayed deleteIsSearchAllOffered]
+ -[SISchemaUEIWeblinksDisplayed deleteWeblinkCategory]
+ -[SISchemaUEIWeblinksDisplayed deleteWeblinks]
+ -[SISchemaUEIWeblinksDisplayed dictionaryRepresentation]
+ -[SISchemaUEIWeblinksDisplayed hasIsSearchAllOffered]
+ -[SISchemaUEIWeblinksDisplayed hasWeblinkCategory]
+ -[SISchemaUEIWeblinksDisplayed hash]
+ -[SISchemaUEIWeblinksDisplayed initWithDictionary:]
+ -[SISchemaUEIWeblinksDisplayed initWithJSON:]
+ -[SISchemaUEIWeblinksDisplayed isEqual:]
+ -[SISchemaUEIWeblinksDisplayed isSearchAllOffered]
+ -[SISchemaUEIWeblinksDisplayed jsonData]
+ -[SISchemaUEIWeblinksDisplayed readFrom:]
+ -[SISchemaUEIWeblinksDisplayed setHasIsSearchAllOffered:]
+ -[SISchemaUEIWeblinksDisplayed setHasWeblinkCategory:]
+ -[SISchemaUEIWeblinksDisplayed setIsSearchAllOffered:]
+ -[SISchemaUEIWeblinksDisplayed setWeblinkCategory:]
+ -[SISchemaUEIWeblinksDisplayed setWeblinks:]
+ -[SISchemaUEIWeblinksDisplayed weblinkCategory]
+ -[SISchemaUEIWeblinksDisplayed weblinksAtIndex:]
+ -[SISchemaUEIWeblinksDisplayed weblinksCount]
+ -[SISchemaUEIWeblinksDisplayed weblinks]
+ -[SISchemaUEIWeblinksDisplayed writeTo:]
+ -[TCSchemaTCUserGroundingEnded deleteWithheldReason]
+ -[TCSchemaTCUserGroundingEnded hasWithheldReason]
+ -[TCSchemaTCUserGroundingEnded setHasWithheldReason:]
+ -[TCSchemaTCUserGroundingEnded setWithheldReason:]
+ -[TCSchemaTCUserGroundingEnded withheldReason]
+ _OBJC_CLASS_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ _OBJC_CLASS_$_MHSchemaMHMutexRequested
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingCanceled
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingContext
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingDecision
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingEnded
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingFailed
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingSkipped
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERPCCRoutingStarted
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ _OBJC_CLASS_$_SISchemaUEIDisplayedWeblink
+ _OBJC_CLASS_$_SISchemaUEIWeblinkMetadata
+ _OBJC_CLASS_$_SISchemaUEIWeblinksDisplayed
+ _OBJC_IVAR_$_CHSchemaCHGraderResult._hasResponseRelevancyJudgeInferenceMetadata
+ _OBJC_IVAR_$_CHSchemaCHGraderResult._responseRelevancyJudgeInferenceMetadata
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._essentialConstraints
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._grade
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._has
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._outcomeCoverage
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._qualifyingContent
+ _OBJC_IVAR_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata._supportedTask
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._currentOwner
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._has
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._holdTimeOfASRResourceInMs
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._holdTimeOfAudioResourceInMs
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._holdTimeOfUnspecifiedResourceInMs
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._requestedResourceType
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._requester
+ _OBJC_IVAR_$_MHSchemaMHMutexRequested._successfullyAcquired
+ _OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._isEligibleForHighConfidenceUserSession
+ _OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._isFinal
+ _OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._isScoreOverridden
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingCanceled._exists
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingCanceled._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._canceled
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._ended
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._failed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._hasCanceled
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._hasEnded
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._hasFailed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._hasStartedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._startedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingContext._whichContextevent
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._scoreLarge
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._scoreMedium
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._scoreSmall
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._thresholdLarge
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._thresholdMedium
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._thresholdSmall
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingDecision._tier
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._hasInputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._hasOutputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._hasQualityDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._inputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._isWaitBudgetExceeded
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._outputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingEnded._qualityDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingFailed._errors
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._ended
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._failed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._hasEnded
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._hasFailed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._hasStartedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._startedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext._whichContextevent
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded._hasModelVersion
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded._modelVersion
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed._errors
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted._producer
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._ended
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._failed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._hasEnded
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._hasFailed
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._hasStartedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._startedOrChanged
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext._whichContextevent
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._hasInputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._hasOutputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._hasQualityDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._inputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._outputEffortDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded._qualityDecision
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineFailed._errors
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._hasModelVersion
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._hasOriginalIfRequestId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._hasOriginalIfSessionId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._hasOriginalRequestId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._modelVersion
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._originalIfRequestId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._originalIfSessionId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted._originalRequestId
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingSkipped._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingSkipped._isShadowMode
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingSkipped._skipReason
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingStarted._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingStarted._hasModelVersion
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingStarted._isShadowMode
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPCCRoutingStarted._modelVersion
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo._drops
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop._droppedCount
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop._has
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop._reason
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool._descriptionCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool._has
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool._nameCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool._parameterCount
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill._bodyCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill._descriptionCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill._has
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill._nameCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._renderedCharLength
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._schemaKind
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionErrorResult._errors
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted._appIntegrationGates
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted._appIntegrationSchemaSource
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted._generableEntityArgumentCount
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionStarted._inputEntities
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._has
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._hasTopic
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._hasUrl
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._position
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._topic
+ _OBJC_IVAR_$_SISchemaUEIDisplayedWeblink._url
+ _OBJC_IVAR_$_SISchemaUEILinkTapped._hasWeblinkMetadata
+ _OBJC_IVAR_$_SISchemaUEILinkTapped._weblinkMetadata
+ _OBJC_IVAR_$_SISchemaUEIWeblinkMetadata._has
+ _OBJC_IVAR_$_SISchemaUEIWeblinkMetadata._openSource
+ _OBJC_IVAR_$_SISchemaUEIWeblinkMetadata._position
+ _OBJC_IVAR_$_SISchemaUEIWeblinksDisplayed._has
+ _OBJC_IVAR_$_SISchemaUEIWeblinksDisplayed._isSearchAllOffered
+ _OBJC_IVAR_$_SISchemaUEIWeblinksDisplayed._weblinkCategory
+ _OBJC_IVAR_$_SISchemaUEIWeblinksDisplayed._weblinks
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._withheldReason
+ _OBJC_METACLASS_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ _OBJC_METACLASS_$_MHSchemaMHMutexRequested
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingCanceled
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingContext
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingDecision
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingEnded
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingFailed
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingSkipped
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERPCCRoutingStarted
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ _OBJC_METACLASS_$_SISchemaUEIDisplayedWeblink
+ _OBJC_METACLASS_$_SISchemaUEIWeblinkMetadata
+ _OBJC_METACLASS_$_SISchemaUEIWeblinksDisplayed
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ __OBJC_$_INSTANCE_METHODS_MHSchemaMHMutexRequested
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingCanceled
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingContext
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingDecision
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingEnded
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingFailed
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingSkipped
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERPCCRoutingStarted
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIDisplayedWeblink
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIWeblinkMetadata
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIWeblinksDisplayed
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ __OBJC_$_INSTANCE_VARIABLES_MHSchemaMHMutexRequested
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingCanceled
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingContext
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingDecision
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingEnded
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingFailed
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingSkipped
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERPCCRoutingStarted
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIDisplayedWeblink
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIWeblinkMetadata
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIWeblinksDisplayed
+ __OBJC_$_PROP_LIST_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ __OBJC_$_PROP_LIST_MHSchemaMHMutexRequested
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingCanceled
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingContext
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingDecision
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingEnded
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingFailed
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingSkipped
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERPCCRoutingStarted
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ __OBJC_$_PROP_LIST_SISchemaUEIDisplayedWeblink
+ __OBJC_$_PROP_LIST_SISchemaUEIWeblinkMetadata
+ __OBJC_$_PROP_LIST_SISchemaUEIWeblinksDisplayed
+ __OBJC_CLASS_RO_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ __OBJC_CLASS_RO_$_MHSchemaMHMutexRequested
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingCanceled
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingContext
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingDecision
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingEnded
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingFailed
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingSkipped
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingStarted
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ __OBJC_CLASS_RO_$_SISchemaUEIDisplayedWeblink
+ __OBJC_CLASS_RO_$_SISchemaUEIWeblinkMetadata
+ __OBJC_CLASS_RO_$_SISchemaUEIWeblinksDisplayed
+ __OBJC_METACLASS_RO_$_CHSchemaCHResponseRelevancyJudgeInferenceMetadata
+ __OBJC_METACLASS_RO_$_MHSchemaMHMutexRequested
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingCanceled
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingContext
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingDecision
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingEnded
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingFailed
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadContext
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadEnded
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadFailed
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingModelLoadStarted
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineContext
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineEnded
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineFailed
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingOfflineStarted
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingSkipped
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERPCCRoutingStarted
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationAppInfo
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationDrop
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppIntegrationTool
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppSkill
+ __OBJC_METACLASS_RO_$_SISchemaUEIDisplayedWeblink
+ __OBJC_METACLASS_RO_$_SISchemaUEIWeblinkMetadata
+ __OBJC_METACLASS_RO_$_SISchemaUEIWeblinksDisplayed
CStrings:
+ "CHAGENTICGRADERTYPE_RESPONSE_RELEVANCY"
+ "CHRESPONSERELEVANCYCHECKVERDICT_FAIL"
+ "CHRESPONSERELEVANCYCHECKVERDICT_MISSING_EVIDENCE"
+ "CHRESPONSERELEVANCYCHECKVERDICT_PASS"
+ "CHRESPONSERELEVANCYCHECKVERDICT_UNKNOWN"
+ "CHRESPONSERELEVANCYGRADE_BAD"
+ "CHRESPONSERELEVANCYGRADE_GOOD"
+ "CHRESPONSERELEVANCYGRADE_REVIEW"
+ "CHRESPONSERELEVANCYGRADE_UNKNOWN"
+ "EXECUTORACTIONPOISONINGCLASSIFIERSKIPREASON_AGENT_NOT_ELIGIBLE"
+ "MHREQUESTMUTEXOWNER_COMPANION_REQUEST"
+ "MHREQUESTMUTEXOWNER_LOCAL_REQUEST"
+ "MHREQUESTMUTEXOWNER_NO_ONE"
+ "MHREQUESTMUTEXOWNER_UNKNOWN"
+ "MHREQUESTMUTEXRESOURCETYPE_ASR"
+ "MHREQUESTMUTEXRESOURCETYPE_AUDIO"
+ "MHREQUESTMUTEXRESOURCETYPE_UNKNOWN"
+ "MHREQUESTMUTEXRESOURCETYPE_UNSPECIFIED"
+ "PLANNERPCCROUTINGMODELTIER_LARGE"
+ "PLANNERPCCROUTINGMODELTIER_MEDIUM"
+ "PLANNERPCCROUTINGMODELTIER_SMALL"
+ "PLANNERPCCROUTINGMODELTIER_UNKNOWN"
+ "PLANNERPCCROUTINGPRODUCER_OFFLINE_EVALUATION"
+ "PLANNERPCCROUTINGPRODUCER_PLANNER"
+ "PLANNERPCCROUTINGPRODUCER_UNKNOWN"
+ "PLANNERPCCROUTINGSKIPREASON_ATTACHMENT_PRESENT"
+ "PLANNERPCCROUTINGSKIPREASON_MODEL_UNAVAILABLE"
+ "PLANNERPCCROUTINGSKIPREASON_ROUTE_FINALIZED"
+ "PLANNERPCCROUTINGSKIPREASON_UNKNOWN"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_HAS_AUTHORED_PLANNER_TOOL"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_SKILL_OVER_APP_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_SKILL_OVER_BODY_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_SKILL_OVER_DESCRIPTION_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_TOOL_OVER_APP_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_TOOL_OVER_DESCRIPTION_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_TOOL_OVER_PARAMETER_DESCRIPTION_LIMIT"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_UNKNOWN"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_UNSUPPORTED_REQUIRED_PARAMETER"
+ "PLANNERTOOLSAPPINTEGRATIONDROPREASON_UNUSABLE_NAME"
+ "PLANNERTOOLSAPPINTEGRATIONSCHEMASOURCE_APP_SCOPED_PRELOAD"
+ "PLANNERTOOLSAPPINTEGRATIONSCHEMASOURCE_AUTO_LOADED"
+ "PLANNERTOOLSAPPINTEGRATIONSCHEMASOURCE_GET_TOOLS"
+ "PLANNERTOOLSAPPINTEGRATIONSCHEMASOURCE_UNKNOWN"
+ "PLANNERTOOLSENTITYSCHEMAKIND_APP_ENTITY"
+ "PLANNERTOOLSENTITYSCHEMAKIND_ASSISTANT_SCHEMA"
+ "PLANNERTOOLSENTITYSCHEMAKIND_CANNOT_RESOLVE"
+ "PLANNERTOOLSENTITYSCHEMAKIND_NOT_APP_ENTITY"
+ "PLANNERTOOLSENTITYSCHEMAKIND_UNKNOWN"
+ "TCUSERGROUNDINGWITHHELDREASON_DEVICE_LOCKED"
+ "TCUSERGROUNDINGWITHHELDREASON_EMPTY_INPUT"
+ "TCUSERGROUNDINGWITHHELDREASON_NONE"
+ "TCUSERGROUNDINGWITHHELDREASON_NO_VOCAB"
+ "TCUSERGROUNDINGWITHHELDREASON_UNKNOWN"
+ "UEILINKTYPE_WEBLINK"
+ "UEIWEBLINKCATEGORY_OTHER"
+ "UEIWEBLINKCATEGORY_PRODUCT"
+ "UEIWEBLINKCATEGORY_RESTAURANT"
+ "UEIWEBLINKCATEGORY_SERVICE"
+ "UEIWEBLINKCATEGORY_UNKNOWN"
+ "UEIWEBLINKOPENSOURCE_SEARCH_ALL"
+ "UEIWEBLINKOPENSOURCE_SINGLE_LINK"
+ "UEIWEBLINKOPENSOURCE_UNKNOWN"
+ "appIntegrationGates"
+ "appIntegrationSchemaSource"
+ "bodyCharLength"
+ "currentOwner"
+ "descriptionCharLength"
+ "droppedCount"
+ "drops"
+ "essentialConstraints"
+ "generableEntityArgumentCount"
+ "grade"
+ "holdTimeOfASRResourceInMs"
+ "holdTimeOfAudioResourceInMs"
+ "holdTimeOfUnspecifiedResourceInMs"
+ "inputEffortDecision"
+ "inputEntities"
+ "isEligibleForHighConfidenceUserSession"
+ "isFinal"
+ "isScoreOverridden"
+ "isSearchAllOffered"
+ "isWaitBudgetExceeded"
+ "nameCharLength"
+ "openSource"
+ "originalIfRequestId"
+ "originalIfSessionId"
+ "originalRequestId"
+ "outcomeCoverage"
+ "outputEffortDecision"
+ "parameterCount"
+ "position"
+ "producer"
+ "qualifyingContent"
+ "qualityDecision"
+ "renderedCharLength"
+ "requestedResourceType"
+ "requester"
+ "responseRelevancyJudgeInferenceMetadata"
+ "schemaKind"
+ "scoreLarge"
+ "scoreMedium"
+ "scoreSmall"
+ "successfullyAcquired"
+ "supportedTask"
+ "thresholdLarge"
+ "thresholdMedium"
+ "thresholdSmall"
+ "tier"
+ "topic"
+ "weblinkCategory"
+ "weblinkMetadata"
+ "weblinks"
+ "withheldReason"
```
