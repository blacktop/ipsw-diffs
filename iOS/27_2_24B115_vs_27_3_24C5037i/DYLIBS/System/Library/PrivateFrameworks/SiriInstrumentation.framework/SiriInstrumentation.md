## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3605.33.1.0.0
-  __TEXT.__text: 0xdbe6b4
-  __TEXT.__objc_methlist: 0x111c94
-  __TEXT.__const: 0x18fc4
-  __TEXT.__swift5_typeref: 0x2012
-  __TEXT.__cstring: 0x99424
-  __TEXT.__constg_swiftt: 0x84b8
+3610.11.2.0.0
+  __TEXT.__text: 0xde5598
+  __TEXT.__objc_methlist: 0x114c54
+  __TEXT.__const: 0x19894
+  __TEXT.__swift5_typeref: 0x20a8
+  __TEXT.__cstring: 0x9c8b7
+  __TEXT.__constg_swiftt: 0x87d8
   __TEXT.__swift5_reflstr: 0x22d
   __TEXT.__swift5_fieldmd: 0x488
-  __TEXT.__swift5_builtin: 0x4d6c
+  __TEXT.__swift5_builtin: 0x4f60
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0x15b8
-  __TEXT.__swift5_types: 0xfd4
+  __TEXT.__swift5_proto: 0x1624
+  __TEXT.__swift5_types: 0x1038
   __TEXT.__oslogstring: 0x111
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__unwind_info: 0x384f8
-  __TEXT.__eh_frame: 0x4cf0
+  __TEXT.__unwind_info: 0x38eb8
+  __TEXT.__eh_frame: 0x4d60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x400f8
-  __DATA_CONST.__objc_classlist: 0x6b28
+  __DATA_CONST.__const: 0x41550
+  __DATA_CONST.__objc_classlist: 0x6c30
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44650
+  __DATA_CONST.__objc_selrefs: 0x45240
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x6ad8
-  __DATA_CONST.__got: 0x6c80
-  __AUTH_CONST.__const: 0x271f0
-  __AUTH_CONST.__cfstring: 0x83aa0
-  __AUTH_CONST.__objc_const: 0x1877b0
-  __AUTH_CONST.__objc_intobj: 0xd38
+  __DATA_CONST.__objc_superrefs: 0x6be0
+  __DATA_CONST.__got: 0x6d88
+  __AUTH_CONST.__const: 0x27a80
+  __AUTH_CONST.__cfstring: 0x85de0
+  __AUTH_CONST.__objc_const: 0x18b8a0
+  __AUTH_CONST.__objc_intobj: 0xd50
   __AUTH_CONST.__auth_got: 0x9c8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1337c
-  __DATA.__data: 0x3570
+  __AUTH.__objc_data: 0xb90
+  __DATA.__objc_ivar: 0x136b0
+  __DATA.__data: 0x3670
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x430c0
   __DATA_DIRTY.__data: 0x518

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 96883
-  Symbols:   135706
-  CStrings:  18007
+  Functions: 97972
+  Symbols:   137158
+  CStrings:  18314
 
Symbols:
+ -[APCTSchemaAPCTClientEvent deleteOdmDevicePressureGateEvaluated]
+ -[APCTSchemaAPCTClientEvent hasOdmDevicePressureGateEvaluated]
+ -[APCTSchemaAPCTClientEvent odmDevicePressureGateEvaluated]
+ -[APCTSchemaAPCTClientEvent setHasOdmDevicePressureGateEvaluated:]
+ -[APCTSchemaAPCTClientEvent setOdmDevicePressureGateEvaluated:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated deleteOutcome]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated deleteThermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated dictionaryRepresentation]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated hasOutcome]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated hasThermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated hash]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated initWithDictionary:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated initWithJSON:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated isEqual:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated jsonData]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated outcome]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated readFrom:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated setHasOutcome:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated setHasThermalLevel:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated setOutcome:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated setThermalLevel:]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated thermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureGateEvaluated writeTo:]
+ -[APCTSchemaAPCTODMDevicePressureSignals deleteThermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureSignals dictionaryRepresentation]
+ -[APCTSchemaAPCTODMDevicePressureSignals hasThermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureSignals hash]
+ -[APCTSchemaAPCTODMDevicePressureSignals initWithDictionary:]
+ -[APCTSchemaAPCTODMDevicePressureSignals initWithJSON:]
+ -[APCTSchemaAPCTODMDevicePressureSignals isEqual:]
+ -[APCTSchemaAPCTODMDevicePressureSignals jsonData]
+ -[APCTSchemaAPCTODMDevicePressureSignals readFrom:]
+ -[APCTSchemaAPCTODMDevicePressureSignals setHasThermalLevel:]
+ -[APCTSchemaAPCTODMDevicePressureSignals setThermalLevel:]
+ -[APCTSchemaAPCTODMDevicePressureSignals thermalLevel]
+ -[APCTSchemaAPCTODMDevicePressureSignals writeTo:]
+ -[APCTSchemaAPCTRuntimeEnded agentPassReason]
+ -[APCTSchemaAPCTRuntimeEnded deleteAgentPassReason]
+ -[APCTSchemaAPCTRuntimeEnded hasAgentPassReason]
+ -[APCTSchemaAPCTRuntimeEnded setAgentPassReason:]
+ -[APCTSchemaAPCTRuntimeEnded setHasAgentPassReason:]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged agentMode]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged deleteAgentMode]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged deleteOdmDevicePressureSignals]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged hasAgentMode]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged hasOdmDevicePressureSignals]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged odmDevicePressureSignals]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged setAgentMode:]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged setHasAgentMode:]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged setHasOdmDevicePressureSignals:]
+ -[APCTSchemaAPCTRuntimeStartedOrChanged setOdmDevicePressureSignals:]
+ -[CDASchemaCDAClientEvent deleteDeviceSelectionDecisionMade]
+ -[CDASchemaCDAClientEvent deviceSelectionDecisionMade]
+ -[CDASchemaCDAClientEvent hasDeviceSelectionDecisionMade]
+ -[CDASchemaCDAClientEvent setDeviceSelectionDecisionMade:]
+ -[CDASchemaCDAClientEvent setHasDeviceSelectionDecisionMade:]
+ -[CDASchemaCDADeviceSelectionDecisionMade .cxx_destruct]
+ -[CDASchemaCDADeviceSelectionDecisionMade audioOrderDeviceCount]
+ -[CDASchemaCDADeviceSelectionDecisionMade audioOrderPosition]
+ -[CDASchemaCDADeviceSelectionDecisionMade confidence]
+ -[CDASchemaCDADeviceSelectionDecisionMade decisionLatencyInMs]
+ -[CDASchemaCDADeviceSelectionDecisionMade decision]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteAudioOrderDeviceCount]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteAudioOrderPosition]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteConfidence]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteDecisionLatencyInMs]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteDecision]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteDeviceClass]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteDeviceGroup]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteError]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteGoodnessScoreBoosts]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteGoodness]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteOutcome]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteProductType]
+ -[CDASchemaCDADeviceSelectionDecisionMade deleteRawLoudness]
+ -[CDASchemaCDADeviceSelectionDecisionMade deviceClass]
+ -[CDASchemaCDADeviceSelectionDecisionMade deviceGroup]
+ -[CDASchemaCDADeviceSelectionDecisionMade dictionaryRepresentation]
+ -[CDASchemaCDADeviceSelectionDecisionMade error]
+ -[CDASchemaCDADeviceSelectionDecisionMade goodnessScoreBoosts]
+ -[CDASchemaCDADeviceSelectionDecisionMade goodness]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasAudioOrderDeviceCount]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasAudioOrderPosition]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasConfidence]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasDecisionLatencyInMs]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasDecision]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasDeviceClass]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasDeviceGroup]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasError]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasGoodnessScoreBoosts]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasGoodness]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasOutcome]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasProductType]
+ -[CDASchemaCDADeviceSelectionDecisionMade hasRawLoudness]
+ -[CDASchemaCDADeviceSelectionDecisionMade hash]
+ -[CDASchemaCDADeviceSelectionDecisionMade initWithDictionary:]
+ -[CDASchemaCDADeviceSelectionDecisionMade initWithJSON:]
+ -[CDASchemaCDADeviceSelectionDecisionMade isEqual:]
+ -[CDASchemaCDADeviceSelectionDecisionMade jsonData]
+ -[CDASchemaCDADeviceSelectionDecisionMade outcome]
+ -[CDASchemaCDADeviceSelectionDecisionMade productType]
+ -[CDASchemaCDADeviceSelectionDecisionMade rawLoudness]
+ -[CDASchemaCDADeviceSelectionDecisionMade readFrom:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setAudioOrderDeviceCount:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setAudioOrderPosition:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setConfidence:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setDecision:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setDecisionLatencyInMs:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setDeviceClass:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setDeviceGroup:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setError:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setGoodness:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setGoodnessScoreBoosts:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasAudioOrderDeviceCount:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasAudioOrderPosition:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasConfidence:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasDecision:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasDecisionLatencyInMs:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasDeviceClass:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasDeviceGroup:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasError:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasGoodness:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasGoodnessScoreBoosts:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasOutcome:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasProductType:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setHasRawLoudness:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setOutcome:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setProductType:]
+ -[CDASchemaCDADeviceSelectionDecisionMade setRawLoudness:]
+ -[CDASchemaCDADeviceSelectionDecisionMade writeTo:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts alarmOrTimerFiringBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts attentionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteAlarmOrTimerFiringBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteAttentionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteDeviceAdjustmentBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteInEarOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteLiftTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteMediaPlaybackActiveBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteMediaPlaybackRecentPlaybackBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deletePerceptionBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deletePerceptionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deletePlatformBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteRaiseToWakeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteRecencyBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteUnlockTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteWatchGestureBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deleteWatchLoudnessThresholdOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts deviceAdjustmentBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts dictionaryRepresentation]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasAlarmOrTimerFiringBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasAttentionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasDeviceAdjustmentBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasInEarOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasLiftTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasMediaPlaybackActiveBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasMediaPlaybackRecentPlaybackBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasPerceptionBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasPerceptionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasPlatformBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasRaiseToWakeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasRecencyBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasUnlockTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasWatchGestureBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hasWatchLoudnessThresholdOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts hash]
+ -[CDASchemaCDADeviceSelectionScoreBoosts inEarOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts initWithDictionary:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts initWithJSON:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts isEqual:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts jsonData]
+ -[CDASchemaCDADeviceSelectionScoreBoosts liftTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts mediaPlaybackActiveBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts mediaPlaybackRecentPlaybackBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts perceptionBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts perceptionOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts platformBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts raiseToWakeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts readFrom:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts recencyBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setAlarmOrTimerFiringBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setAttentionOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setDeviceAdjustmentBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasAlarmOrTimerFiringBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasAttentionOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasDeviceAdjustmentBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasInEarOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasLiftTimeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasMediaPlaybackActiveBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasMediaPlaybackRecentPlaybackBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasPerceptionBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasPerceptionOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasPlatformBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasRaiseToWakeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasRecencyBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasUnlockTimeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasWatchGestureBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setHasWatchLoudnessThresholdOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setInEarOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setLiftTimeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setMediaPlaybackActiveBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setMediaPlaybackRecentPlaybackBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setPerceptionBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setPerceptionOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setPlatformBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setRaiseToWakeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setRecencyBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setUnlockTimeBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setWatchGestureBoost:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts setWatchLoudnessThresholdOverride:]
+ -[CDASchemaCDADeviceSelectionScoreBoosts unlockTimeBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts watchGestureBoost]
+ -[CDASchemaCDADeviceSelectionScoreBoosts watchLoudnessThresholdOverride]
+ -[CDASchemaCDADeviceSelectionScoreBoosts writeTo:]
+ -[CDASchemaCDAElectionDecisionMade confidence]
+ -[CDASchemaCDAElectionDecisionMade deleteConfidence]
+ -[CDASchemaCDAElectionDecisionMade hasConfidence]
+ -[CDASchemaCDAElectionDecisionMade setConfidence:]
+ -[CDASchemaCDAElectionDecisionMade setHasConfidence:]
+ -[CHSchemaCHSpeechCriterionResult deleteEvidence]
+ -[CHSchemaCHSpeechCriterionResult evidence]
+ -[CHSchemaCHSpeechCriterionResult hasEvidence]
+ -[CHSchemaCHSpeechCriterionResult setEvidence:]
+ -[CHSchemaCHSpeechCriterionResult setHasEvidence:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata alternativesPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata backingSource]
+ -[CHSchemaCHSpeechGradingInferenceMetadata deleteAlternativesPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata deleteBackingSource]
+ -[CHSchemaCHSpeechGradingInferenceMetadata deleteOnscreenOrLiveContextPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata deleteOnscreenOrLiveContextUsed]
+ -[CHSchemaCHSpeechGradingInferenceMetadata deletePlannerResolution]
+ -[CHSchemaCHSpeechGradingInferenceMetadata hasAlternativesPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata hasBackingSource]
+ -[CHSchemaCHSpeechGradingInferenceMetadata hasOnscreenOrLiveContextPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata hasOnscreenOrLiveContextUsed]
+ -[CHSchemaCHSpeechGradingInferenceMetadata hasPlannerResolution]
+ -[CHSchemaCHSpeechGradingInferenceMetadata onscreenOrLiveContextPresent]
+ -[CHSchemaCHSpeechGradingInferenceMetadata onscreenOrLiveContextUsed]
+ -[CHSchemaCHSpeechGradingInferenceMetadata plannerResolution]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setAlternativesPresent:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setBackingSource:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setHasAlternativesPresent:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setHasBackingSource:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setHasOnscreenOrLiveContextPresent:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setHasOnscreenOrLiveContextUsed:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setHasPlannerResolution:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setOnscreenOrLiveContextPresent:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setOnscreenOrLiveContextUsed:]
+ -[CHSchemaCHSpeechGradingInferenceMetadata setPlannerResolution:]
+ -[FTDAudioSchemaFTDAudioToolInvoked contentSource]
+ -[FTDAudioSchemaFTDAudioToolInvoked deleteContentSource]
+ -[FTDAudioSchemaFTDAudioToolInvoked hasContentSource]
+ -[FTDAudioSchemaFTDAudioToolInvoked setContentSource:]
+ -[FTDAudioSchemaFTDAudioToolInvoked setHasContentSource:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest addTurnIds:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest clearTurnIds]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest deleteTurnIds]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest setTurnIds:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest turnIdsAtIndex:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest turnIdsCount]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest turnIds]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest addTurnIds:]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest clearTurnIds]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest deleteTurnIds]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest setTurnIds:]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest turnIdsAtIndex:]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest turnIdsCount]
+ -[ODDSiriSchemaODDAssistantSiriExtensionsDigest turnIds]
+ -[ODDSiriSchemaODDGeneralProperties deleteSearchDataOptOutState]
+ -[ODDSiriSchemaODDGeneralProperties hasSearchDataOptOutState]
+ -[ODDSiriSchemaODDGeneralProperties searchDataOptOutState]
+ -[ODDSiriSchemaODDGeneralProperties setHasSearchDataOptOutState:]
+ -[ODDSiriSchemaODDGeneralProperties setSearchDataOptOutState:]
+ -[ORCHSchemaORCHEmergencyModeCause .cxx_destruct]
+ -[ORCHSchemaORCHEmergencyModeCause addMissingAssets:]
+ -[ORCHSchemaORCHEmergencyModeCause clearMissingAssets]
+ -[ORCHSchemaORCHEmergencyModeCause deleteDesiredOrchestrationMode]
+ -[ORCHSchemaORCHEmergencyModeCause deleteMissingAssets]
+ -[ORCHSchemaORCHEmergencyModeCause desiredOrchestrationMode]
+ -[ORCHSchemaORCHEmergencyModeCause dictionaryRepresentation]
+ -[ORCHSchemaORCHEmergencyModeCause hasDesiredOrchestrationMode]
+ -[ORCHSchemaORCHEmergencyModeCause hash]
+ -[ORCHSchemaORCHEmergencyModeCause initWithDictionary:]
+ -[ORCHSchemaORCHEmergencyModeCause initWithJSON:]
+ -[ORCHSchemaORCHEmergencyModeCause isEqual:]
+ -[ORCHSchemaORCHEmergencyModeCause jsonData]
+ -[ORCHSchemaORCHEmergencyModeCause missingAssetsAtIndex:]
+ -[ORCHSchemaORCHEmergencyModeCause missingAssetsCount]
+ -[ORCHSchemaORCHEmergencyModeCause missingAssets]
+ -[ORCHSchemaORCHEmergencyModeCause readFrom:]
+ -[ORCHSchemaORCHEmergencyModeCause setDesiredOrchestrationMode:]
+ -[ORCHSchemaORCHEmergencyModeCause setHasDesiredOrchestrationMode:]
+ -[ORCHSchemaORCHEmergencyModeCause setMissingAssets:]
+ -[ORCHSchemaORCHEmergencyModeCause writeTo:]
+ -[ORCHSchemaORCHRequestStarted deleteEmergencyModeCause]
+ -[ORCHSchemaORCHRequestStarted emergencyModeCause]
+ -[ORCHSchemaORCHRequestStarted hasEmergencyModeCause]
+ -[ORCHSchemaORCHRequestStarted setEmergencyModeCause:]
+ -[ORCHSchemaORCHRequestStarted setHasEmergencyModeCause:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived deleteTimeSinceLastSeenInSeconds]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived hasTimeSinceLastSeenInSeconds]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setHasTimeSinceLastSeenInSeconds:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived setTimeSinceLastSeenInSeconds:]
+ -[ORCHSchemaORCHSpeakerIdentificationResultReceived timeSinceLastSeenInSeconds]
+ -[PLANNERSchemaPLANNERDirectResponseReference .cxx_destruct]
+ -[PLANNERSchemaPLANNERDirectResponseReference deleteEntity]
+ -[PLANNERSchemaPLANNERDirectResponseReference deleteReferenceKind]
+ -[PLANNERSchemaPLANNERDirectResponseReference dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERDirectResponseReference entity]
+ -[PLANNERSchemaPLANNERDirectResponseReference hasEntity]
+ -[PLANNERSchemaPLANNERDirectResponseReference hasReferenceKind]
+ -[PLANNERSchemaPLANNERDirectResponseReference hash]
+ -[PLANNERSchemaPLANNERDirectResponseReference initWithDictionary:]
+ -[PLANNERSchemaPLANNERDirectResponseReference initWithJSON:]
+ -[PLANNERSchemaPLANNERDirectResponseReference isEqual:]
+ -[PLANNERSchemaPLANNERDirectResponseReference jsonData]
+ -[PLANNERSchemaPLANNERDirectResponseReference readFrom:]
+ -[PLANNERSchemaPLANNERDirectResponseReference referenceKind]
+ -[PLANNERSchemaPLANNERDirectResponseReference setEntity:]
+ -[PLANNERSchemaPLANNERDirectResponseReference setHasEntity:]
+ -[PLANNERSchemaPLANNERDirectResponseReference setHasReferenceKind:]
+ -[PLANNERSchemaPLANNERDirectResponseReference setReferenceKind:]
+ -[PLANNERSchemaPLANNERDirectResponseReference writeTo:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded addDirectResponseReferences:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded clearDirectResponseReferences]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded deleteDirectResponseReferences]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded deleteThoughtTokenCount]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded directResponseReferencesAtIndex:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded directResponseReferencesCount]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded directResponseReferences]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded hasThoughtTokenCount]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded setDirectResponseReferences:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded setHasThoughtTokenCount:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded setThoughtTokenCount:]
+ -[PLANNERSchemaPLANNERPlanningModelInferenceEnded thoughtTokenCount]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent deleteSearchTagEvaluated]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent hasSearchTagEvaluated]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent searchTagEvaluated]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent setHasSearchTagEvaluated:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent setSearchTagEvaluated:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated .cxx_destruct]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated deleteSamRequestId]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated deleteSearchTaggingResult]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated dictionaryRepresentation]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated hasSamRequestId]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated hasSearchTaggingResult]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated hash]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated initWithDictionary:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated initWithJSON:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated isEqual:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated jsonData]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated readFrom:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated samRequestId]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated searchTaggingResult]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated setHasSamRequestId:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated setHasSearchTaggingResult:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated setSamRequestId:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated setSearchTaggingResult:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated writeTo:]
+ -[SISchemaClientEvent deleteUeiUserFeedbackProvided]
+ -[SISchemaClientEvent hasUeiUserFeedbackProvided]
+ -[SISchemaClientEvent setHasUeiUserFeedbackProvided:]
+ -[SISchemaClientEvent setUeiUserFeedbackProvided:]
+ -[SISchemaClientEvent ueiUserFeedbackProvided]
+ -[SISchemaFreeFormText addEvaluationTexts:]
+ -[SISchemaFreeFormText clearEvaluationTexts]
+ -[SISchemaFreeFormText deleteEvaluationTexts]
+ -[SISchemaFreeFormText evaluationTextsAtIndex:]
+ -[SISchemaFreeFormText evaluationTextsCount]
+ -[SISchemaFreeFormText evaluationTexts]
+ -[SISchemaFreeFormText setEvaluationTexts:]
+ -[SISchemaUEILinkTapped .cxx_destruct]
+ -[SISchemaUEILinkTapped deleteUrl]
+ -[SISchemaUEILinkTapped hasUrl]
+ -[SISchemaUEILinkTapped setHasUrl:]
+ -[SISchemaUEILinkTapped setUrl:]
+ -[SISchemaUEILinkTapped url]
+ -[SISchemaUEIUserFeedbackProvided deleteFeedbackType]
+ -[SISchemaUEIUserFeedbackProvided dictionaryRepresentation]
+ -[SISchemaUEIUserFeedbackProvided feedbackType]
+ -[SISchemaUEIUserFeedbackProvided hasFeedbackType]
+ -[SISchemaUEIUserFeedbackProvided hash]
+ -[SISchemaUEIUserFeedbackProvided initWithDictionary:]
+ -[SISchemaUEIUserFeedbackProvided initWithJSON:]
+ -[SISchemaUEIUserFeedbackProvided isEqual:]
+ -[SISchemaUEIUserFeedbackProvided jsonData]
+ -[SISchemaUEIUserFeedbackProvided readFrom:]
+ -[SISchemaUEIUserFeedbackProvided setFeedbackType:]
+ -[SISchemaUEIUserFeedbackProvided setHasFeedbackType:]
+ -[SISchemaUEIUserFeedbackProvided writeTo:]
+ -[STSchemaSTEvent deleteStHomeKitHomeGraphLoadContext]
+ -[STSchemaSTEvent deleteStHomeKitSearchContext]
+ -[STSchemaSTEvent hasStHomeKitHomeGraphLoadContext]
+ -[STSchemaSTEvent hasStHomeKitSearchContext]
+ -[STSchemaSTEvent setHasStHomeKitHomeGraphLoadContext:]
+ -[STSchemaSTEvent setHasStHomeKitSearchContext:]
+ -[STSchemaSTEvent setStHomeKitHomeGraphLoadContext:]
+ -[STSchemaSTEvent setStHomeKitSearchContext:]
+ -[STSchemaSTEvent stHomeKitHomeGraphLoadContext]
+ -[STSchemaSTEvent stHomeKitSearchContext]
+ -[STSchemaSTGlobalBatchSearchRequestEnded deletePegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestEnded hasPegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestEnded pegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestEnded setHasPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalBatchSearchRequestEnded setPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalBatchSearchRequestFailed deletePegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestFailed hasPegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestFailed pegasusCallClientMetrics]
+ -[STSchemaSTGlobalBatchSearchRequestFailed setHasPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalBatchSearchRequestFailed setPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalSearchRequestEnded deletePegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestEnded hasPegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestEnded pegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestEnded setHasPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalSearchRequestEnded setPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalSearchRequestFailed deletePegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestFailed hasPegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestFailed pegasusCallClientMetrics]
+ -[STSchemaSTGlobalSearchRequestFailed setHasPegasusCallClientMetrics:]
+ -[STSchemaSTGlobalSearchRequestFailed setPegasusCallClientMetrics:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled deleteExists]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled dictionaryRepresentation]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled exists]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled hasExists]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled hash]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled initWithDictionary:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled initWithJSON:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled isEqual:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled jsonData]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled readFrom:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled setExists:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled setHasExists:]
+ -[STSchemaSTHomeKitHomeGraphLoadCanceled writeTo:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext .cxx_destruct]
+ -[STSchemaSTHomeKitHomeGraphLoadContext canceled]
+ -[STSchemaSTHomeKitHomeGraphLoadContext deleteCanceled]
+ -[STSchemaSTHomeKitHomeGraphLoadContext deleteEnded]
+ -[STSchemaSTHomeKitHomeGraphLoadContext deleteFailed]
+ -[STSchemaSTHomeKitHomeGraphLoadContext deleteStartedOrChanged]
+ -[STSchemaSTHomeKitHomeGraphLoadContext dictionaryRepresentation]
+ -[STSchemaSTHomeKitHomeGraphLoadContext ended]
+ -[STSchemaSTHomeKitHomeGraphLoadContext failed]
+ -[STSchemaSTHomeKitHomeGraphLoadContext hasCanceled]
+ -[STSchemaSTHomeKitHomeGraphLoadContext hasEnded]
+ -[STSchemaSTHomeKitHomeGraphLoadContext hasFailed]
+ -[STSchemaSTHomeKitHomeGraphLoadContext hasStartedOrChanged]
+ -[STSchemaSTHomeKitHomeGraphLoadContext hash]
+ -[STSchemaSTHomeKitHomeGraphLoadContext initWithDictionary:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext initWithJSON:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext isEqual:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext jsonData]
+ -[STSchemaSTHomeKitHomeGraphLoadContext readFrom:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setCanceled:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setEnded:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setFailed:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setHasCanceled:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setHasEnded:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setHasFailed:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setHasStartedOrChanged:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext setStartedOrChanged:]
+ -[STSchemaSTHomeKitHomeGraphLoadContext startedOrChanged]
+ -[STSchemaSTHomeKitHomeGraphLoadContext whichContextevent]
+ -[STSchemaSTHomeKitHomeGraphLoadContext writeTo:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded deleteHomeGraphSizeBucket]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded dictionaryRepresentation]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded hasHomeGraphSizeBucket]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded hash]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded homeGraphSizeBucket]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded initWithDictionary:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded initWithJSON:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded isEqual:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded jsonData]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded readFrom:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded setHasHomeGraphSizeBucket:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded setHomeGraphSizeBucket:]
+ -[STSchemaSTHomeKitHomeGraphLoadEnded writeTo:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed .cxx_destruct]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed addErrors:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed clearErrors]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed deleteErrors]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed dictionaryRepresentation]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed errorsAtIndex:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed errorsCount]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed errors]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed hash]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed initWithDictionary:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed initWithJSON:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed isEqual:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed jsonData]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed readFrom:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed setErrors:]
+ -[STSchemaSTHomeKitHomeGraphLoadFailed writeTo:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted deleteLoadReason]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted dictionaryRepresentation]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted hasLoadReason]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted hash]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted initWithDictionary:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted initWithJSON:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted isEqual:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted jsonData]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted loadReason]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted readFrom:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted setHasLoadReason:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted setLoadReason:]
+ -[STSchemaSTHomeKitHomeGraphLoadStarted writeTo:]
+ -[STSchemaSTHomeKitSearchCanceled deleteExists]
+ -[STSchemaSTHomeKitSearchCanceled dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchCanceled exists]
+ -[STSchemaSTHomeKitSearchCanceled hasExists]
+ -[STSchemaSTHomeKitSearchCanceled hash]
+ -[STSchemaSTHomeKitSearchCanceled initWithDictionary:]
+ -[STSchemaSTHomeKitSearchCanceled initWithJSON:]
+ -[STSchemaSTHomeKitSearchCanceled isEqual:]
+ -[STSchemaSTHomeKitSearchCanceled jsonData]
+ -[STSchemaSTHomeKitSearchCanceled readFrom:]
+ -[STSchemaSTHomeKitSearchCanceled setExists:]
+ -[STSchemaSTHomeKitSearchCanceled setHasExists:]
+ -[STSchemaSTHomeKitSearchCanceled writeTo:]
+ -[STSchemaSTHomeKitSearchContext .cxx_destruct]
+ -[STSchemaSTHomeKitSearchContext canceled]
+ -[STSchemaSTHomeKitSearchContext deleteCanceled]
+ -[STSchemaSTHomeKitSearchContext deleteEnded]
+ -[STSchemaSTHomeKitSearchContext deleteFailed]
+ -[STSchemaSTHomeKitSearchContext deleteStartedOrChanged]
+ -[STSchemaSTHomeKitSearchContext dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchContext ended]
+ -[STSchemaSTHomeKitSearchContext failed]
+ -[STSchemaSTHomeKitSearchContext hasCanceled]
+ -[STSchemaSTHomeKitSearchContext hasEnded]
+ -[STSchemaSTHomeKitSearchContext hasFailed]
+ -[STSchemaSTHomeKitSearchContext hasStartedOrChanged]
+ -[STSchemaSTHomeKitSearchContext hash]
+ -[STSchemaSTHomeKitSearchContext initWithDictionary:]
+ -[STSchemaSTHomeKitSearchContext initWithJSON:]
+ -[STSchemaSTHomeKitSearchContext isEqual:]
+ -[STSchemaSTHomeKitSearchContext jsonData]
+ -[STSchemaSTHomeKitSearchContext readFrom:]
+ -[STSchemaSTHomeKitSearchContext setCanceled:]
+ -[STSchemaSTHomeKitSearchContext setEnded:]
+ -[STSchemaSTHomeKitSearchContext setFailed:]
+ -[STSchemaSTHomeKitSearchContext setHasCanceled:]
+ -[STSchemaSTHomeKitSearchContext setHasEnded:]
+ -[STSchemaSTHomeKitSearchContext setHasFailed:]
+ -[STSchemaSTHomeKitSearchContext setHasStartedOrChanged:]
+ -[STSchemaSTHomeKitSearchContext setStartedOrChanged:]
+ -[STSchemaSTHomeKitSearchContext startedOrChanged]
+ -[STSchemaSTHomeKitSearchContext whichContextevent]
+ -[STSchemaSTHomeKitSearchContext writeTo:]
+ -[STSchemaSTHomeKitSearchEnded .cxx_destruct]
+ -[STSchemaSTHomeKitSearchEnded addResult:]
+ -[STSchemaSTHomeKitSearchEnded clearResult]
+ -[STSchemaSTHomeKitSearchEnded deleteEmptyResultReason]
+ -[STSchemaSTHomeKitSearchEnded deleteHomeGraphSizeBucket]
+ -[STSchemaSTHomeKitSearchEnded deleteResult]
+ -[STSchemaSTHomeKitSearchEnded dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchEnded emptyResultReason]
+ -[STSchemaSTHomeKitSearchEnded hasEmptyResultReason]
+ -[STSchemaSTHomeKitSearchEnded hasHomeGraphSizeBucket]
+ -[STSchemaSTHomeKitSearchEnded hash]
+ -[STSchemaSTHomeKitSearchEnded homeGraphSizeBucket]
+ -[STSchemaSTHomeKitSearchEnded initWithDictionary:]
+ -[STSchemaSTHomeKitSearchEnded initWithJSON:]
+ -[STSchemaSTHomeKitSearchEnded isEqual:]
+ -[STSchemaSTHomeKitSearchEnded jsonData]
+ -[STSchemaSTHomeKitSearchEnded readFrom:]
+ -[STSchemaSTHomeKitSearchEnded resultAtIndex:]
+ -[STSchemaSTHomeKitSearchEnded resultCount]
+ -[STSchemaSTHomeKitSearchEnded results]
+ -[STSchemaSTHomeKitSearchEnded setEmptyResultReason:]
+ -[STSchemaSTHomeKitSearchEnded setHasEmptyResultReason:]
+ -[STSchemaSTHomeKitSearchEnded setHasHomeGraphSizeBucket:]
+ -[STSchemaSTHomeKitSearchEnded setHomeGraphSizeBucket:]
+ -[STSchemaSTHomeKitSearchEnded setResults:]
+ -[STSchemaSTHomeKitSearchEnded writeTo:]
+ -[STSchemaSTHomeKitSearchFailed .cxx_destruct]
+ -[STSchemaSTHomeKitSearchFailed addErrors:]
+ -[STSchemaSTHomeKitSearchFailed clearErrors]
+ -[STSchemaSTHomeKitSearchFailed deleteErrors]
+ -[STSchemaSTHomeKitSearchFailed dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchFailed errorsAtIndex:]
+ -[STSchemaSTHomeKitSearchFailed errorsCount]
+ -[STSchemaSTHomeKitSearchFailed errors]
+ -[STSchemaSTHomeKitSearchFailed hash]
+ -[STSchemaSTHomeKitSearchFailed initWithDictionary:]
+ -[STSchemaSTHomeKitSearchFailed initWithJSON:]
+ -[STSchemaSTHomeKitSearchFailed isEqual:]
+ -[STSchemaSTHomeKitSearchFailed jsonData]
+ -[STSchemaSTHomeKitSearchFailed readFrom:]
+ -[STSchemaSTHomeKitSearchFailed setErrors:]
+ -[STSchemaSTHomeKitSearchFailed writeTo:]
+ -[STSchemaSTHomeKitSearchResult deleteEntityType]
+ -[STSchemaSTHomeKitSearchResult dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchResult entityType]
+ -[STSchemaSTHomeKitSearchResult hasEntityType]
+ -[STSchemaSTHomeKitSearchResult hash]
+ -[STSchemaSTHomeKitSearchResult initWithDictionary:]
+ -[STSchemaSTHomeKitSearchResult initWithJSON:]
+ -[STSchemaSTHomeKitSearchResult isEqual:]
+ -[STSchemaSTHomeKitSearchResult jsonData]
+ -[STSchemaSTHomeKitSearchResult readFrom:]
+ -[STSchemaSTHomeKitSearchResult setEntityType:]
+ -[STSchemaSTHomeKitSearchResult setHasEntityType:]
+ -[STSchemaSTHomeKitSearchResult writeTo:]
+ -[STSchemaSTHomeKitSearchStarted .cxx_destruct]
+ -[STSchemaSTHomeKitSearchStarted addRequestTypes:]
+ -[STSchemaSTHomeKitSearchStarted clearRequestTypes]
+ -[STSchemaSTHomeKitSearchStarted deleteHomeClauseCount]
+ -[STSchemaSTHomeKitSearchStarted deleteIsHomeGraphCached]
+ -[STSchemaSTHomeKitSearchStarted deleteRequestTypes]
+ -[STSchemaSTHomeKitSearchStarted dictionaryRepresentation]
+ -[STSchemaSTHomeKitSearchStarted hasHomeClauseCount]
+ -[STSchemaSTHomeKitSearchStarted hasIsHomeGraphCached]
+ -[STSchemaSTHomeKitSearchStarted hash]
+ -[STSchemaSTHomeKitSearchStarted homeClauseCount]
+ -[STSchemaSTHomeKitSearchStarted initWithDictionary:]
+ -[STSchemaSTHomeKitSearchStarted initWithJSON:]
+ -[STSchemaSTHomeKitSearchStarted isEqual:]
+ -[STSchemaSTHomeKitSearchStarted isHomeGraphCached]
+ -[STSchemaSTHomeKitSearchStarted jsonData]
+ -[STSchemaSTHomeKitSearchStarted readFrom:]
+ -[STSchemaSTHomeKitSearchStarted requestTypesAtIndex:]
+ -[STSchemaSTHomeKitSearchStarted requestTypesCount]
+ -[STSchemaSTHomeKitSearchStarted requestTypes]
+ -[STSchemaSTHomeKitSearchStarted setHasHomeClauseCount:]
+ -[STSchemaSTHomeKitSearchStarted setHasIsHomeGraphCached:]
+ -[STSchemaSTHomeKitSearchStarted setHomeClauseCount:]
+ -[STSchemaSTHomeKitSearchStarted setIsHomeGraphCached:]
+ -[STSchemaSTHomeKitSearchStarted setRequestTypes:]
+ -[STSchemaSTHomeKitSearchStarted writeTo:]
+ -[STSchemaSTPegasusCallClientConnectivity .cxx_destruct]
+ -[STSchemaSTPegasusCallClientConnectivity deleteFinalStateOffsetMs]
+ -[STSchemaSTPegasusCallClientConnectivity deleteFinalState]
+ -[STSchemaSTPegasusCallClientConnectivity deleteInitialState]
+ -[STSchemaSTPegasusCallClientConnectivity dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientConnectivity finalStateOffsetMs]
+ -[STSchemaSTPegasusCallClientConnectivity finalState]
+ -[STSchemaSTPegasusCallClientConnectivity hasFinalStateOffsetMs]
+ -[STSchemaSTPegasusCallClientConnectivity hasFinalState]
+ -[STSchemaSTPegasusCallClientConnectivity hasInitialState]
+ -[STSchemaSTPegasusCallClientConnectivity hash]
+ -[STSchemaSTPegasusCallClientConnectivity initWithDictionary:]
+ -[STSchemaSTPegasusCallClientConnectivity initWithJSON:]
+ -[STSchemaSTPegasusCallClientConnectivity initialState]
+ -[STSchemaSTPegasusCallClientConnectivity isEqual:]
+ -[STSchemaSTPegasusCallClientConnectivity jsonData]
+ -[STSchemaSTPegasusCallClientConnectivity readFrom:]
+ -[STSchemaSTPegasusCallClientConnectivity setFinalState:]
+ -[STSchemaSTPegasusCallClientConnectivity setFinalStateOffsetMs:]
+ -[STSchemaSTPegasusCallClientConnectivity setHasFinalState:]
+ -[STSchemaSTPegasusCallClientConnectivity setHasFinalStateOffsetMs:]
+ -[STSchemaSTPegasusCallClientConnectivity setHasInitialState:]
+ -[STSchemaSTPegasusCallClientConnectivity setInitialState:]
+ -[STSchemaSTPegasusCallClientConnectivity writeTo:]
+ -[STSchemaSTPegasusCallClientContextFetch deleteEndOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch deleteEngagementState]
+ -[STSchemaSTPegasusCallClientContextFetch deleteFailureReason]
+ -[STSchemaSTPegasusCallClientContextFetch deleteStartOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientContextFetch endOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch engagementState]
+ -[STSchemaSTPegasusCallClientContextFetch failureReason]
+ -[STSchemaSTPegasusCallClientContextFetch hasEndOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch hasEngagementState]
+ -[STSchemaSTPegasusCallClientContextFetch hasFailureReason]
+ -[STSchemaSTPegasusCallClientContextFetch hasStartOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch hash]
+ -[STSchemaSTPegasusCallClientContextFetch initWithDictionary:]
+ -[STSchemaSTPegasusCallClientContextFetch initWithJSON:]
+ -[STSchemaSTPegasusCallClientContextFetch isEqual:]
+ -[STSchemaSTPegasusCallClientContextFetch jsonData]
+ -[STSchemaSTPegasusCallClientContextFetch readFrom:]
+ -[STSchemaSTPegasusCallClientContextFetch setEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientContextFetch setEngagementState:]
+ -[STSchemaSTPegasusCallClientContextFetch setFailureReason:]
+ -[STSchemaSTPegasusCallClientContextFetch setHasEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientContextFetch setHasEngagementState:]
+ -[STSchemaSTPegasusCallClientContextFetch setHasFailureReason:]
+ -[STSchemaSTPegasusCallClientContextFetch setHasStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientContextFetch setStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientContextFetch startOffsetMs]
+ -[STSchemaSTPegasusCallClientContextFetch writeTo:]
+ -[STSchemaSTPegasusCallClientMetrics .cxx_destruct]
+ -[STSchemaSTPegasusCallClientMetrics contextFetch]
+ -[STSchemaSTPegasusCallClientMetrics deleteContextFetch]
+ -[STSchemaSTPegasusCallClientMetrics deleteNetwork]
+ -[STSchemaSTPegasusCallClientMetrics deletePatFetch]
+ -[STSchemaSTPegasusCallClientMetrics deleteSetup]
+ -[STSchemaSTPegasusCallClientMetrics dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientMetrics hasContextFetch]
+ -[STSchemaSTPegasusCallClientMetrics hasNetwork]
+ -[STSchemaSTPegasusCallClientMetrics hasPatFetch]
+ -[STSchemaSTPegasusCallClientMetrics hasSetup]
+ -[STSchemaSTPegasusCallClientMetrics hash]
+ -[STSchemaSTPegasusCallClientMetrics initWithDictionary:]
+ -[STSchemaSTPegasusCallClientMetrics initWithJSON:]
+ -[STSchemaSTPegasusCallClientMetrics isEqual:]
+ -[STSchemaSTPegasusCallClientMetrics jsonData]
+ -[STSchemaSTPegasusCallClientMetrics network]
+ -[STSchemaSTPegasusCallClientMetrics patFetch]
+ -[STSchemaSTPegasusCallClientMetrics readFrom:]
+ -[STSchemaSTPegasusCallClientMetrics setContextFetch:]
+ -[STSchemaSTPegasusCallClientMetrics setHasContextFetch:]
+ -[STSchemaSTPegasusCallClientMetrics setHasNetwork:]
+ -[STSchemaSTPegasusCallClientMetrics setHasPatFetch:]
+ -[STSchemaSTPegasusCallClientMetrics setHasSetup:]
+ -[STSchemaSTPegasusCallClientMetrics setNetwork:]
+ -[STSchemaSTPegasusCallClientMetrics setPatFetch:]
+ -[STSchemaSTPegasusCallClientMetrics setSetup:]
+ -[STSchemaSTPegasusCallClientMetrics setup]
+ -[STSchemaSTPegasusCallClientMetrics writeTo:]
+ -[STSchemaSTPegasusCallClientNetwork .cxx_destruct]
+ -[STSchemaSTPegasusCallClientNetwork connectivity]
+ -[STSchemaSTPegasusCallClientNetwork deleteConnectivity]
+ -[STSchemaSTPegasusCallClientNetwork deleteEndOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork deleteEngagementState]
+ -[STSchemaSTPegasusCallClientNetwork deleteFailureReason]
+ -[STSchemaSTPegasusCallClientNetwork deleteStartOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork deleteStream]
+ -[STSchemaSTPegasusCallClientNetwork dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientNetwork endOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork engagementState]
+ -[STSchemaSTPegasusCallClientNetwork failureReason]
+ -[STSchemaSTPegasusCallClientNetwork hasConnectivity]
+ -[STSchemaSTPegasusCallClientNetwork hasEndOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork hasEngagementState]
+ -[STSchemaSTPegasusCallClientNetwork hasFailureReason]
+ -[STSchemaSTPegasusCallClientNetwork hasStartOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork hasStream]
+ -[STSchemaSTPegasusCallClientNetwork hash]
+ -[STSchemaSTPegasusCallClientNetwork initWithDictionary:]
+ -[STSchemaSTPegasusCallClientNetwork initWithJSON:]
+ -[STSchemaSTPegasusCallClientNetwork isEqual:]
+ -[STSchemaSTPegasusCallClientNetwork jsonData]
+ -[STSchemaSTPegasusCallClientNetwork readFrom:]
+ -[STSchemaSTPegasusCallClientNetwork setConnectivity:]
+ -[STSchemaSTPegasusCallClientNetwork setEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetwork setEngagementState:]
+ -[STSchemaSTPegasusCallClientNetwork setFailureReason:]
+ -[STSchemaSTPegasusCallClientNetwork setHasConnectivity:]
+ -[STSchemaSTPegasusCallClientNetwork setHasEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetwork setHasEngagementState:]
+ -[STSchemaSTPegasusCallClientNetwork setHasFailureReason:]
+ -[STSchemaSTPegasusCallClientNetwork setHasStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetwork setHasStream:]
+ -[STSchemaSTPegasusCallClientNetwork setStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetwork setStream:]
+ -[STSchemaSTPegasusCallClientNetwork startOffsetMs]
+ -[STSchemaSTPegasusCallClientNetwork stream]
+ -[STSchemaSTPegasusCallClientNetwork writeTo:]
+ -[STSchemaSTPegasusCallClientNetworkState deleteIsConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState deleteIsExpensive]
+ -[STSchemaSTPegasusCallClientNetworkState deleteIsUltraConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState deleteLinkQuality]
+ -[STSchemaSTPegasusCallClientNetworkState deletePrimaryInterfaceType]
+ -[STSchemaSTPegasusCallClientNetworkState deleteStatus]
+ -[STSchemaSTPegasusCallClientNetworkState deleteUnsatisfiedReason]
+ -[STSchemaSTPegasusCallClientNetworkState dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientNetworkState hasIsConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState hasIsExpensive]
+ -[STSchemaSTPegasusCallClientNetworkState hasIsUltraConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState hasLinkQuality]
+ -[STSchemaSTPegasusCallClientNetworkState hasPrimaryInterfaceType]
+ -[STSchemaSTPegasusCallClientNetworkState hasStatus]
+ -[STSchemaSTPegasusCallClientNetworkState hasUnsatisfiedReason]
+ -[STSchemaSTPegasusCallClientNetworkState hash]
+ -[STSchemaSTPegasusCallClientNetworkState initWithDictionary:]
+ -[STSchemaSTPegasusCallClientNetworkState initWithJSON:]
+ -[STSchemaSTPegasusCallClientNetworkState isConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState isEqual:]
+ -[STSchemaSTPegasusCallClientNetworkState isExpensive]
+ -[STSchemaSTPegasusCallClientNetworkState isUltraConstrained]
+ -[STSchemaSTPegasusCallClientNetworkState jsonData]
+ -[STSchemaSTPegasusCallClientNetworkState linkQuality]
+ -[STSchemaSTPegasusCallClientNetworkState primaryInterfaceType]
+ -[STSchemaSTPegasusCallClientNetworkState readFrom:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasIsConstrained:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasIsExpensive:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasIsUltraConstrained:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasLinkQuality:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasPrimaryInterfaceType:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasStatus:]
+ -[STSchemaSTPegasusCallClientNetworkState setHasUnsatisfiedReason:]
+ -[STSchemaSTPegasusCallClientNetworkState setIsConstrained:]
+ -[STSchemaSTPegasusCallClientNetworkState setIsExpensive:]
+ -[STSchemaSTPegasusCallClientNetworkState setIsUltraConstrained:]
+ -[STSchemaSTPegasusCallClientNetworkState setLinkQuality:]
+ -[STSchemaSTPegasusCallClientNetworkState setPrimaryInterfaceType:]
+ -[STSchemaSTPegasusCallClientNetworkState setStatus:]
+ -[STSchemaSTPegasusCallClientNetworkState setUnsatisfiedReason:]
+ -[STSchemaSTPegasusCallClientNetworkState status]
+ -[STSchemaSTPegasusCallClientNetworkState unsatisfiedReason]
+ -[STSchemaSTPegasusCallClientNetworkState writeTo:]
+ -[STSchemaSTPegasusCallClientNetworkStream chunkCount]
+ -[STSchemaSTPegasusCallClientNetworkStream deleteChunkCount]
+ -[STSchemaSTPegasusCallClientNetworkStream deleteDownloadedKilobytes]
+ -[STSchemaSTPegasusCallClientNetworkStream deleteFirstChunkOffsetMs]
+ -[STSchemaSTPegasusCallClientNetworkStream dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientNetworkStream downloadedKilobytes]
+ -[STSchemaSTPegasusCallClientNetworkStream firstChunkOffsetMs]
+ -[STSchemaSTPegasusCallClientNetworkStream hasChunkCount]
+ -[STSchemaSTPegasusCallClientNetworkStream hasDownloadedKilobytes]
+ -[STSchemaSTPegasusCallClientNetworkStream hasFirstChunkOffsetMs]
+ -[STSchemaSTPegasusCallClientNetworkStream hash]
+ -[STSchemaSTPegasusCallClientNetworkStream initWithDictionary:]
+ -[STSchemaSTPegasusCallClientNetworkStream initWithJSON:]
+ -[STSchemaSTPegasusCallClientNetworkStream isEqual:]
+ -[STSchemaSTPegasusCallClientNetworkStream jsonData]
+ -[STSchemaSTPegasusCallClientNetworkStream readFrom:]
+ -[STSchemaSTPegasusCallClientNetworkStream setChunkCount:]
+ -[STSchemaSTPegasusCallClientNetworkStream setDownloadedKilobytes:]
+ -[STSchemaSTPegasusCallClientNetworkStream setFirstChunkOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetworkStream setHasChunkCount:]
+ -[STSchemaSTPegasusCallClientNetworkStream setHasDownloadedKilobytes:]
+ -[STSchemaSTPegasusCallClientNetworkStream setHasFirstChunkOffsetMs:]
+ -[STSchemaSTPegasusCallClientNetworkStream writeTo:]
+ -[STSchemaSTPegasusCallClientPatFetch deleteEndOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch deleteEngagementState]
+ -[STSchemaSTPegasusCallClientPatFetch deleteFailureReason]
+ -[STSchemaSTPegasusCallClientPatFetch deleteStartOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientPatFetch endOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch engagementState]
+ -[STSchemaSTPegasusCallClientPatFetch failureReason]
+ -[STSchemaSTPegasusCallClientPatFetch hasEndOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch hasEngagementState]
+ -[STSchemaSTPegasusCallClientPatFetch hasFailureReason]
+ -[STSchemaSTPegasusCallClientPatFetch hasStartOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch hash]
+ -[STSchemaSTPegasusCallClientPatFetch initWithDictionary:]
+ -[STSchemaSTPegasusCallClientPatFetch initWithJSON:]
+ -[STSchemaSTPegasusCallClientPatFetch isEqual:]
+ -[STSchemaSTPegasusCallClientPatFetch jsonData]
+ -[STSchemaSTPegasusCallClientPatFetch readFrom:]
+ -[STSchemaSTPegasusCallClientPatFetch setEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientPatFetch setEngagementState:]
+ -[STSchemaSTPegasusCallClientPatFetch setFailureReason:]
+ -[STSchemaSTPegasusCallClientPatFetch setHasEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientPatFetch setHasEngagementState:]
+ -[STSchemaSTPegasusCallClientPatFetch setHasFailureReason:]
+ -[STSchemaSTPegasusCallClientPatFetch setHasStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientPatFetch setStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientPatFetch startOffsetMs]
+ -[STSchemaSTPegasusCallClientPatFetch writeTo:]
+ -[STSchemaSTPegasusCallClientSetup deleteEndOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup deleteEngagementState]
+ -[STSchemaSTPegasusCallClientSetup deleteStartOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup dictionaryRepresentation]
+ -[STSchemaSTPegasusCallClientSetup endOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup engagementState]
+ -[STSchemaSTPegasusCallClientSetup hasEndOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup hasEngagementState]
+ -[STSchemaSTPegasusCallClientSetup hasStartOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup hash]
+ -[STSchemaSTPegasusCallClientSetup initWithDictionary:]
+ -[STSchemaSTPegasusCallClientSetup initWithJSON:]
+ -[STSchemaSTPegasusCallClientSetup isEqual:]
+ -[STSchemaSTPegasusCallClientSetup jsonData]
+ -[STSchemaSTPegasusCallClientSetup readFrom:]
+ -[STSchemaSTPegasusCallClientSetup setEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientSetup setEngagementState:]
+ -[STSchemaSTPegasusCallClientSetup setHasEndOffsetMs:]
+ -[STSchemaSTPegasusCallClientSetup setHasEngagementState:]
+ -[STSchemaSTPegasusCallClientSetup setHasStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientSetup setStartOffsetMs:]
+ -[STSchemaSTPegasusCallClientSetup startOffsetMs]
+ -[STSchemaSTPegasusCallClientSetup writeTo:]
+ -[TCSchemaTCClientEvent deleteUserGroundingContext]
+ -[TCSchemaTCClientEvent hasUserGroundingContext]
+ -[TCSchemaTCClientEvent setHasUserGroundingContext:]
+ -[TCSchemaTCClientEvent setUserGroundingContext:]
+ -[TCSchemaTCClientEvent userGroundingContext]
+ -[TCSchemaTCUserGroundingCanceled deleteExists]
+ -[TCSchemaTCUserGroundingCanceled dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingCanceled exists]
+ -[TCSchemaTCUserGroundingCanceled hasExists]
+ -[TCSchemaTCUserGroundingCanceled hash]
+ -[TCSchemaTCUserGroundingCanceled initWithDictionary:]
+ -[TCSchemaTCUserGroundingCanceled initWithJSON:]
+ -[TCSchemaTCUserGroundingCanceled isEqual:]
+ -[TCSchemaTCUserGroundingCanceled jsonData]
+ -[TCSchemaTCUserGroundingCanceled readFrom:]
+ -[TCSchemaTCUserGroundingCanceled setExists:]
+ -[TCSchemaTCUserGroundingCanceled setHasExists:]
+ -[TCSchemaTCUserGroundingCanceled writeTo:]
+ -[TCSchemaTCUserGroundingContext .cxx_destruct]
+ -[TCSchemaTCUserGroundingContext canceled]
+ -[TCSchemaTCUserGroundingContext deleteCanceled]
+ -[TCSchemaTCUserGroundingContext deleteEnded]
+ -[TCSchemaTCUserGroundingContext deleteFailed]
+ -[TCSchemaTCUserGroundingContext deleteStartedOrChanged]
+ -[TCSchemaTCUserGroundingContext dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingContext ended]
+ -[TCSchemaTCUserGroundingContext failed]
+ -[TCSchemaTCUserGroundingContext hasCanceled]
+ -[TCSchemaTCUserGroundingContext hasEnded]
+ -[TCSchemaTCUserGroundingContext hasFailed]
+ -[TCSchemaTCUserGroundingContext hasStartedOrChanged]
+ -[TCSchemaTCUserGroundingContext hash]
+ -[TCSchemaTCUserGroundingContext initWithDictionary:]
+ -[TCSchemaTCUserGroundingContext initWithJSON:]
+ -[TCSchemaTCUserGroundingContext isEqual:]
+ -[TCSchemaTCUserGroundingContext jsonData]
+ -[TCSchemaTCUserGroundingContext readFrom:]
+ -[TCSchemaTCUserGroundingContext setCanceled:]
+ -[TCSchemaTCUserGroundingContext setEnded:]
+ -[TCSchemaTCUserGroundingContext setFailed:]
+ -[TCSchemaTCUserGroundingContext setHasCanceled:]
+ -[TCSchemaTCUserGroundingContext setHasEnded:]
+ -[TCSchemaTCUserGroundingContext setHasFailed:]
+ -[TCSchemaTCUserGroundingContext setHasStartedOrChanged:]
+ -[TCSchemaTCUserGroundingContext setStartedOrChanged:]
+ -[TCSchemaTCUserGroundingContext startedOrChanged]
+ -[TCSchemaTCUserGroundingContext whichContextevent]
+ -[TCSchemaTCUserGroundingContext writeTo:]
+ -[TCSchemaTCUserGroundingEnded .cxx_destruct]
+ -[TCSchemaTCUserGroundingEnded addUserGroundingNgramScores:]
+ -[TCSchemaTCUserGroundingEnded clearUserGroundingNgramScores]
+ -[TCSchemaTCUserGroundingEnded deleteStrongThreshold]
+ -[TCSchemaTCUserGroundingEnded deleteUserGroundingNgramScores]
+ -[TCSchemaTCUserGroundingEnded deleteUserGroundingSignal]
+ -[TCSchemaTCUserGroundingEnded deleteWeakThreshold]
+ -[TCSchemaTCUserGroundingEnded dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingEnded hasStrongThreshold]
+ -[TCSchemaTCUserGroundingEnded hasUserGroundingSignal]
+ -[TCSchemaTCUserGroundingEnded hasWeakThreshold]
+ -[TCSchemaTCUserGroundingEnded hash]
+ -[TCSchemaTCUserGroundingEnded initWithDictionary:]
+ -[TCSchemaTCUserGroundingEnded initWithJSON:]
+ -[TCSchemaTCUserGroundingEnded isEqual:]
+ -[TCSchemaTCUserGroundingEnded jsonData]
+ -[TCSchemaTCUserGroundingEnded readFrom:]
+ -[TCSchemaTCUserGroundingEnded setHasStrongThreshold:]
+ -[TCSchemaTCUserGroundingEnded setHasUserGroundingSignal:]
+ -[TCSchemaTCUserGroundingEnded setHasWeakThreshold:]
+ -[TCSchemaTCUserGroundingEnded setStrongThreshold:]
+ -[TCSchemaTCUserGroundingEnded setUserGroundingNgramScores:]
+ -[TCSchemaTCUserGroundingEnded setUserGroundingSignal:]
+ -[TCSchemaTCUserGroundingEnded setWeakThreshold:]
+ -[TCSchemaTCUserGroundingEnded strongThreshold]
+ -[TCSchemaTCUserGroundingEnded userGroundingNgramScoresAtIndex:]
+ -[TCSchemaTCUserGroundingEnded userGroundingNgramScoresCount]
+ -[TCSchemaTCUserGroundingEnded userGroundingNgramScores]
+ -[TCSchemaTCUserGroundingEnded userGroundingSignal]
+ -[TCSchemaTCUserGroundingEnded weakThreshold]
+ -[TCSchemaTCUserGroundingEnded writeTo:]
+ -[TCSchemaTCUserGroundingFailed .cxx_destruct]
+ -[TCSchemaTCUserGroundingFailed addErrors:]
+ -[TCSchemaTCUserGroundingFailed clearErrors]
+ -[TCSchemaTCUserGroundingFailed deleteErrors]
+ -[TCSchemaTCUserGroundingFailed dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingFailed errorsAtIndex:]
+ -[TCSchemaTCUserGroundingFailed errorsCount]
+ -[TCSchemaTCUserGroundingFailed errors]
+ -[TCSchemaTCUserGroundingFailed hash]
+ -[TCSchemaTCUserGroundingFailed initWithDictionary:]
+ -[TCSchemaTCUserGroundingFailed initWithJSON:]
+ -[TCSchemaTCUserGroundingFailed isEqual:]
+ -[TCSchemaTCUserGroundingFailed jsonData]
+ -[TCSchemaTCUserGroundingFailed readFrom:]
+ -[TCSchemaTCUserGroundingFailed setErrors:]
+ -[TCSchemaTCUserGroundingFailed writeTo:]
+ -[TCSchemaTCUserGroundingScore deleteScore]
+ -[TCSchemaTCUserGroundingScore dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingScore hasScore]
+ -[TCSchemaTCUserGroundingScore hash]
+ -[TCSchemaTCUserGroundingScore initWithDictionary:]
+ -[TCSchemaTCUserGroundingScore initWithJSON:]
+ -[TCSchemaTCUserGroundingScore isEqual:]
+ -[TCSchemaTCUserGroundingScore jsonData]
+ -[TCSchemaTCUserGroundingScore readFrom:]
+ -[TCSchemaTCUserGroundingScore score]
+ -[TCSchemaTCUserGroundingScore setHasScore:]
+ -[TCSchemaTCUserGroundingScore setScore:]
+ -[TCSchemaTCUserGroundingScore writeTo:]
+ -[TCSchemaTCUserGroundingStarted deleteIsEnabled]
+ -[TCSchemaTCUserGroundingStarted dictionaryRepresentation]
+ -[TCSchemaTCUserGroundingStarted hasIsEnabled]
+ -[TCSchemaTCUserGroundingStarted hash]
+ -[TCSchemaTCUserGroundingStarted initWithDictionary:]
+ -[TCSchemaTCUserGroundingStarted initWithJSON:]
+ -[TCSchemaTCUserGroundingStarted isEnabled]
+ -[TCSchemaTCUserGroundingStarted isEqual:]
+ -[TCSchemaTCUserGroundingStarted jsonData]
+ -[TCSchemaTCUserGroundingStarted readFrom:]
+ -[TCSchemaTCUserGroundingStarted setHasIsEnabled:]
+ -[TCSchemaTCUserGroundingStarted setIsEnabled:]
+ -[TCSchemaTCUserGroundingStarted writeTo:]
+ -[TMSTurnSchemaTMSTURNUserTurnEnded deleteTrailingSilenceThresholdType]
+ -[TMSTurnSchemaTMSTURNUserTurnEnded hasTrailingSilenceThresholdType]
+ -[TMSTurnSchemaTMSTURNUserTurnEnded setHasTrailingSilenceThresholdType:]
+ -[TMSTurnSchemaTMSTURNUserTurnEnded setTrailingSilenceThresholdType:]
+ -[TMSTurnSchemaTMSTURNUserTurnEnded trailingSilenceThresholdType]
+ _OBJC_CLASS_$_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ _OBJC_CLASS_$_APCTSchemaAPCTODMDevicePressureSignals
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionDecisionMade
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionScoreBoosts
+ _OBJC_CLASS_$_ORCHSchemaORCHEmergencyModeCause
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERDirectResponseReference
+ _OBJC_CLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ _OBJC_CLASS_$_SISchemaUEIUserFeedbackProvided
+ _OBJC_CLASS_$_STSchemaSTHomeKitHomeGraphLoadCanceled
+ _OBJC_CLASS_$_STSchemaSTHomeKitHomeGraphLoadContext
+ _OBJC_CLASS_$_STSchemaSTHomeKitHomeGraphLoadEnded
+ _OBJC_CLASS_$_STSchemaSTHomeKitHomeGraphLoadFailed
+ _OBJC_CLASS_$_STSchemaSTHomeKitHomeGraphLoadStarted
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchCanceled
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchContext
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchEnded
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchFailed
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchResult
+ _OBJC_CLASS_$_STSchemaSTHomeKitSearchStarted
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientConnectivity
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientContextFetch
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientMetrics
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientNetwork
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientNetworkState
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientNetworkStream
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientPatFetch
+ _OBJC_CLASS_$_STSchemaSTPegasusCallClientSetup
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingCanceled
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingContext
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingEnded
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingFailed
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingScore
+ _OBJC_CLASS_$_TCSchemaTCUserGroundingStarted
+ _OBJC_IVAR_$_APCTSchemaAPCTClientEvent._hasOdmDevicePressureGateEvaluated
+ _OBJC_IVAR_$_APCTSchemaAPCTClientEvent._odmDevicePressureGateEvaluated
+ _OBJC_IVAR_$_APCTSchemaAPCTODMDevicePressureGateEvaluated._has
+ _OBJC_IVAR_$_APCTSchemaAPCTODMDevicePressureGateEvaluated._outcome
+ _OBJC_IVAR_$_APCTSchemaAPCTODMDevicePressureGateEvaluated._thermalLevel
+ _OBJC_IVAR_$_APCTSchemaAPCTODMDevicePressureSignals._has
+ _OBJC_IVAR_$_APCTSchemaAPCTODMDevicePressureSignals._thermalLevel
+ _OBJC_IVAR_$_APCTSchemaAPCTRuntimeEnded._agentPassReason
+ _OBJC_IVAR_$_APCTSchemaAPCTRuntimeStartedOrChanged._agentMode
+ _OBJC_IVAR_$_APCTSchemaAPCTRuntimeStartedOrChanged._hasOdmDevicePressureSignals
+ _OBJC_IVAR_$_APCTSchemaAPCTRuntimeStartedOrChanged._odmDevicePressureSignals
+ _OBJC_IVAR_$_CDASchemaCDAClientEvent._deviceSelectionDecisionMade
+ _OBJC_IVAR_$_CDASchemaCDAClientEvent._hasDeviceSelectionDecisionMade
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._audioOrderDeviceCount
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._audioOrderPosition
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._confidence
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._decision
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._decisionLatencyInMs
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._deviceClass
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._deviceGroup
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._error
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._goodness
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._goodnessScoreBoosts
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._has
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._hasError
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._hasGoodnessScoreBoosts
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._outcome
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._productType
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionDecisionMade._rawLoudness
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._alarmOrTimerFiringBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._attentionOverride
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._deviceAdjustmentBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._has
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._inEarOverride
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._liftTimeBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._mediaPlaybackActiveBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._mediaPlaybackRecentPlaybackBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._perceptionBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._perceptionOverride
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._platformBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._raiseToWakeBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._recencyBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._unlockTimeBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._watchGestureBoost
+ _OBJC_IVAR_$_CDASchemaCDADeviceSelectionScoreBoosts._watchLoudnessThresholdOverride
+ _OBJC_IVAR_$_CDASchemaCDAElectionDecisionMade._confidence
+ _OBJC_IVAR_$_CHSchemaCHSpeechCriterionResult._evidence
+ _OBJC_IVAR_$_CHSchemaCHSpeechGradingInferenceMetadata._alternativesPresent
+ _OBJC_IVAR_$_CHSchemaCHSpeechGradingInferenceMetadata._backingSource
+ _OBJC_IVAR_$_CHSchemaCHSpeechGradingInferenceMetadata._onscreenOrLiveContextPresent
+ _OBJC_IVAR_$_CHSchemaCHSpeechGradingInferenceMetadata._onscreenOrLiveContextUsed
+ _OBJC_IVAR_$_CHSchemaCHSpeechGradingInferenceMetadata._plannerResolution
+ _OBJC_IVAR_$_FTDAudioSchemaFTDAudioToolInvoked._contentSource
+ _OBJC_IVAR_$_FTDAudioSchemaFTDAudioToolInvoked._has
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriDigest._turnIds
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantSiriExtensionsDigest._turnIds
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._searchDataOptOutState
+ _OBJC_IVAR_$_ORCHSchemaORCHEmergencyModeCause._desiredOrchestrationMode
+ _OBJC_IVAR_$_ORCHSchemaORCHEmergencyModeCause._has
+ _OBJC_IVAR_$_ORCHSchemaORCHEmergencyModeCause._missingAssets
+ _OBJC_IVAR_$_ORCHSchemaORCHRequestStarted._emergencyModeCause
+ _OBJC_IVAR_$_ORCHSchemaORCHRequestStarted._hasEmergencyModeCause
+ _OBJC_IVAR_$_ORCHSchemaORCHSpeakerIdentificationResultReceived._timeSinceLastSeenInSeconds
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERDirectResponseReference._entity
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERDirectResponseReference._has
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERDirectResponseReference._hasEntity
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERDirectResponseReference._referenceKind
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPlanningModelInferenceEnded._directResponseReferences
+ _OBJC_IVAR_$_PLANNERSchemaPLANNERPlanningModelInferenceEnded._thoughtTokenCount
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSClientEvent._hasSearchTagEvaluated
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSClientEvent._searchTagEvaluated
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated._has
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated._hasSamRequestId
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated._samRequestId
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated._searchTaggingResult
+ _OBJC_IVAR_$_SISchemaClientEvent._hasUeiUserFeedbackProvided
+ _OBJC_IVAR_$_SISchemaClientEvent._ueiUserFeedbackProvided
+ _OBJC_IVAR_$_SISchemaFreeFormText._evaluationTexts
+ _OBJC_IVAR_$_SISchemaUEILinkTapped._hasUrl
+ _OBJC_IVAR_$_SISchemaUEILinkTapped._url
+ _OBJC_IVAR_$_SISchemaUEIUserFeedbackProvided._feedbackType
+ _OBJC_IVAR_$_SISchemaUEIUserFeedbackProvided._has
+ _OBJC_IVAR_$_STSchemaSTEvent._hasStHomeKitHomeGraphLoadContext
+ _OBJC_IVAR_$_STSchemaSTEvent._hasStHomeKitSearchContext
+ _OBJC_IVAR_$_STSchemaSTEvent._stHomeKitHomeGraphLoadContext
+ _OBJC_IVAR_$_STSchemaSTEvent._stHomeKitSearchContext
+ _OBJC_IVAR_$_STSchemaSTGlobalBatchSearchRequestEnded._hasPegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalBatchSearchRequestEnded._pegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalBatchSearchRequestFailed._hasPegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalBatchSearchRequestFailed._pegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalSearchRequestEnded._hasPegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalSearchRequestEnded._pegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalSearchRequestFailed._hasPegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTGlobalSearchRequestFailed._pegasusCallClientMetrics
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadCanceled._exists
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadCanceled._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._canceled
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._ended
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._failed
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._hasCanceled
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._hasEnded
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._hasFailed
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._hasStartedOrChanged
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._startedOrChanged
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadContext._whichContextevent
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadEnded._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadEnded._homeGraphSizeBucket
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadFailed._errors
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadStarted._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitHomeGraphLoadStarted._loadReason
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchCanceled._exists
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchCanceled._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._canceled
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._ended
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._failed
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._hasCanceled
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._hasEnded
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._hasFailed
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._hasStartedOrChanged
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._startedOrChanged
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchContext._whichContextevent
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchEnded._emptyResultReason
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchEnded._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchEnded._homeGraphSizeBucket
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchEnded._results
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchFailed._errors
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchResult._entityType
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchResult._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchStarted._has
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchStarted._homeClauseCount
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchStarted._isHomeGraphCached
+ _OBJC_IVAR_$_STSchemaSTHomeKitSearchStarted._requestTypes
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._finalState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._finalStateOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._hasFinalState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._hasInitialState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientConnectivity._initialState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientContextFetch._endOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientContextFetch._engagementState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientContextFetch._failureReason
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientContextFetch._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientContextFetch._startOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._contextFetch
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._hasContextFetch
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._hasNetwork
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._hasPatFetch
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._hasSetup
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._network
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._patFetch
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientMetrics._setup
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._connectivity
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._endOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._engagementState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._failureReason
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._hasConnectivity
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._hasStream
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._startOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetwork._stream
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._isConstrained
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._isExpensive
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._isUltraConstrained
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._linkQuality
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._primaryInterfaceType
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._status
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkState._unsatisfiedReason
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkStream._chunkCount
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkStream._downloadedKilobytes
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkStream._firstChunkOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientNetworkStream._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientPatFetch._endOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientPatFetch._engagementState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientPatFetch._failureReason
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientPatFetch._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientPatFetch._startOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientSetup._endOffsetMs
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientSetup._engagementState
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientSetup._has
+ _OBJC_IVAR_$_STSchemaSTPegasusCallClientSetup._startOffsetMs
+ _OBJC_IVAR_$_TCSchemaTCClientEvent._hasUserGroundingContext
+ _OBJC_IVAR_$_TCSchemaTCClientEvent._userGroundingContext
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingCanceled._exists
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingCanceled._has
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._canceled
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._ended
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._failed
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._hasCanceled
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._hasEnded
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._hasFailed
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._hasStartedOrChanged
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._startedOrChanged
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingContext._whichContextevent
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._has
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._strongThreshold
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._userGroundingNgramScores
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._userGroundingSignal
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingEnded._weakThreshold
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingFailed._errors
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingScore._has
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingScore._score
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingStarted._has
+ _OBJC_IVAR_$_TCSchemaTCUserGroundingStarted._isEnabled
+ _OBJC_IVAR_$_TMSTurnSchemaTMSTURNUserTurnEnded._trailingSilenceThresholdType
+ _OBJC_METACLASS_$_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ _OBJC_METACLASS_$_APCTSchemaAPCTODMDevicePressureSignals
+ _OBJC_METACLASS_$_CDASchemaCDADeviceSelectionDecisionMade
+ _OBJC_METACLASS_$_CDASchemaCDADeviceSelectionScoreBoosts
+ _OBJC_METACLASS_$_ORCHSchemaORCHEmergencyModeCause
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERDirectResponseReference
+ _OBJC_METACLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ _OBJC_METACLASS_$_SISchemaUEIUserFeedbackProvided
+ _OBJC_METACLASS_$_STSchemaSTHomeKitHomeGraphLoadCanceled
+ _OBJC_METACLASS_$_STSchemaSTHomeKitHomeGraphLoadContext
+ _OBJC_METACLASS_$_STSchemaSTHomeKitHomeGraphLoadEnded
+ _OBJC_METACLASS_$_STSchemaSTHomeKitHomeGraphLoadFailed
+ _OBJC_METACLASS_$_STSchemaSTHomeKitHomeGraphLoadStarted
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchCanceled
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchContext
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchEnded
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchFailed
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchResult
+ _OBJC_METACLASS_$_STSchemaSTHomeKitSearchStarted
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientConnectivity
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientContextFetch
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientMetrics
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientNetwork
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientNetworkState
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientNetworkStream
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientPatFetch
+ _OBJC_METACLASS_$_STSchemaSTPegasusCallClientSetup
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingCanceled
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingContext
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingEnded
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingFailed
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingScore
+ _OBJC_METACLASS_$_TCSchemaTCUserGroundingStarted
+ __OBJC_$_INSTANCE_METHODS_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ __OBJC_$_INSTANCE_METHODS_APCTSchemaAPCTODMDevicePressureSignals
+ __OBJC_$_INSTANCE_METHODS_CDASchemaCDADeviceSelectionDecisionMade
+ __OBJC_$_INSTANCE_METHODS_CDASchemaCDADeviceSelectionScoreBoosts
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHEmergencyModeCause
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERDirectResponseReference
+ __OBJC_$_INSTANCE_METHODS_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIUserFeedbackProvided
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitHomeGraphLoadCanceled
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitHomeGraphLoadContext
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitHomeGraphLoadEnded
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitHomeGraphLoadFailed
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitHomeGraphLoadStarted
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchCanceled
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchContext
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchEnded
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchFailed
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchResult
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTHomeKitSearchStarted
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientConnectivity
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientContextFetch
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientMetrics
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientNetwork
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientNetworkState
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientNetworkStream
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientPatFetch
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTPegasusCallClientSetup
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingCanceled
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingContext
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingEnded
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingFailed
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingScore
+ __OBJC_$_INSTANCE_METHODS_TCSchemaTCUserGroundingStarted
+ __OBJC_$_INSTANCE_VARIABLES_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ __OBJC_$_INSTANCE_VARIABLES_APCTSchemaAPCTODMDevicePressureSignals
+ __OBJC_$_INSTANCE_VARIABLES_CDASchemaCDADeviceSelectionDecisionMade
+ __OBJC_$_INSTANCE_VARIABLES_CDASchemaCDADeviceSelectionScoreBoosts
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHEmergencyModeCause
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERDirectResponseReference
+ __OBJC_$_INSTANCE_VARIABLES_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIUserFeedbackProvided
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitHomeGraphLoadCanceled
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitHomeGraphLoadContext
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitHomeGraphLoadEnded
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitHomeGraphLoadFailed
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitHomeGraphLoadStarted
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchCanceled
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchContext
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchEnded
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchFailed
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchResult
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTHomeKitSearchStarted
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientConnectivity
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientContextFetch
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientMetrics
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientNetwork
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientNetworkState
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientNetworkStream
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientPatFetch
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTPegasusCallClientSetup
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingCanceled
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingContext
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingEnded
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingFailed
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingScore
+ __OBJC_$_INSTANCE_VARIABLES_TCSchemaTCUserGroundingStarted
+ __OBJC_$_PROP_LIST_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ __OBJC_$_PROP_LIST_APCTSchemaAPCTODMDevicePressureSignals
+ __OBJC_$_PROP_LIST_CDASchemaCDADeviceSelectionDecisionMade
+ __OBJC_$_PROP_LIST_CDASchemaCDADeviceSelectionScoreBoosts
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHEmergencyModeCause
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERDirectResponseReference
+ __OBJC_$_PROP_LIST_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ __OBJC_$_PROP_LIST_SISchemaUEIUserFeedbackProvided
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitHomeGraphLoadCanceled
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitHomeGraphLoadContext
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitHomeGraphLoadEnded
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitHomeGraphLoadFailed
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitHomeGraphLoadStarted
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchCanceled
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchContext
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchEnded
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchFailed
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchResult
+ __OBJC_$_PROP_LIST_STSchemaSTHomeKitSearchStarted
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientConnectivity
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientContextFetch
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientMetrics
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientNetwork
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientNetworkState
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientNetworkStream
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientPatFetch
+ __OBJC_$_PROP_LIST_STSchemaSTPegasusCallClientSetup
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingCanceled
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingContext
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingEnded
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingFailed
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingScore
+ __OBJC_$_PROP_LIST_TCSchemaTCUserGroundingStarted
+ __OBJC_CLASS_RO_$_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ __OBJC_CLASS_RO_$_APCTSchemaAPCTODMDevicePressureSignals
+ __OBJC_CLASS_RO_$_CDASchemaCDADeviceSelectionDecisionMade
+ __OBJC_CLASS_RO_$_CDASchemaCDADeviceSelectionScoreBoosts
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHEmergencyModeCause
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERDirectResponseReference
+ __OBJC_CLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ __OBJC_CLASS_RO_$_SISchemaUEIUserFeedbackProvided
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadCanceled
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadContext
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadEnded
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadFailed
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadStarted
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchCanceled
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchContext
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchEnded
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchFailed
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchResult
+ __OBJC_CLASS_RO_$_STSchemaSTHomeKitSearchStarted
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientConnectivity
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientContextFetch
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientMetrics
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientNetwork
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientNetworkState
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientNetworkStream
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientPatFetch
+ __OBJC_CLASS_RO_$_STSchemaSTPegasusCallClientSetup
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingCanceled
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingContext
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingEnded
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingFailed
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingScore
+ __OBJC_CLASS_RO_$_TCSchemaTCUserGroundingStarted
+ __OBJC_METACLASS_RO_$_APCTSchemaAPCTODMDevicePressureGateEvaluated
+ __OBJC_METACLASS_RO_$_APCTSchemaAPCTODMDevicePressureSignals
+ __OBJC_METACLASS_RO_$_CDASchemaCDADeviceSelectionDecisionMade
+ __OBJC_METACLASS_RO_$_CDASchemaCDADeviceSelectionScoreBoosts
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHEmergencyModeCause
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERDirectResponseReference
+ __OBJC_METACLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSSearchTagEvaluated
+ __OBJC_METACLASS_RO_$_SISchemaUEIUserFeedbackProvided
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadCanceled
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadContext
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadEnded
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadFailed
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitHomeGraphLoadStarted
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchCanceled
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchContext
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchEnded
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchFailed
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchResult
+ __OBJC_METACLASS_RO_$_STSchemaSTHomeKitSearchStarted
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientConnectivity
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientContextFetch
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientMetrics
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientNetwork
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientNetworkState
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientNetworkStream
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientPatFetch
+ __OBJC_METACLASS_RO_$_STSchemaSTPegasusCallClientSetup
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingCanceled
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingContext
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingEnded
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingFailed
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingScore
+ __OBJC_METACLASS_RO_$_TCSchemaTCUserGroundingStarted
+ _symbolic _____ So23APCTSchemaAPCTAgentModeV
+ _symbolic _____ So27SISchemaUEIUserFeedbackTypeV
+ _symbolic _____ So29APCTSchemaAPCTAgentPassReasonV
+ _symbolic _____ So29CHSchemaCHSpeechBackingSourceV
+ _symbolic _____ So29TCSchemaTCUserGroundingSignalV
+ _symbolic _____ So31CHSchemaCHSpeechGradingEvidenceV
+ _symbolic _____ So33CHSchemaCHSpeechPlannerResolutionV
+ _symbolic _____ So33STSchemaSTHomeKitSearchEntityTypeV
+ _symbolic _____ So34CDASchemaCDADeviceSelectionOutcomeV
+ _symbolic _____ So34STSchemaSTHomeKitSearchRequestTypeV
+ _symbolic _____ So36STSchemaSTHomeKitHomeGraphLoadReasonV
+ _symbolic _____ So36STSchemaSTHomeKitHomeGraphSizeBucketV
+ _symbolic _____ So37STSchemaSTPegasusPhaseEngagementStateV
+ _symbolic _____ So38STSchemaSTPegasusCallClientLinkQualityV
+ _symbolic _____ So40STSchemaSTHomeKitSearchEmptyResultReasonV
+ _symbolic _____ So42APCTSchemaAPCTODMDevicePressureGateOutcomeV
+ _symbolic _____ So45STSchemaSTPegasusCallClientConnectivityStatusV
+ _symbolic _____ So47PLANNERSchemaPLANNERDirectResponseReferenceKindV
+ _symbolic _____ So47STSchemaSTPegasusCallClientNetworkFailureReasonV
+ _symbolic _____ So47STSchemaSTPegasusCallClientNetworkInterfaceTypeV
+ _symbolic _____ So48STSchemaSTPegasusCallClientPatFetchFailureReasonV
+ _symbolic _____ So48TMSTurnSchemaTMSTURNTrailingSilenceThresholdTypeV
+ _symbolic _____ So51RESPONSETOOLSSchemaRESPONSETOOLSSearchTaggingResultV
+ _symbolic _____ So51STSchemaSTPegasusCallClientNetworkUnsatisfiedReasonV
+ _symbolic _____ So52STSchemaSTPegasusCallClientContextFetchFailureReasonV
CStrings:
+ "APCTAGENTMODE_ONDEVICEPLANNER_OFFLINE"
+ "APCTAGENTMODE_ONDEVICEPLANNER_ONLINE"
+ "APCTAGENTMODE_UNKNOWN"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_EXPLICIT_ATTACHMENTS"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_FIND_RETURNED"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_LOW_BATTERY"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_LOW_POWER_MODE"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_MAKE_CALL_GLOBAL_DISAMBIGUATION"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_MEMORY_PRESSURE"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_MODEL_NOT_SUPPORTED"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_NOT_FIRST_TASK"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_OTHER"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_OTHER_AGENT_TOOL_CALLS"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_PLANNING_FAILED"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_PLAY_TITLE_DISAMBIGUATION"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_PRIOR_SESSION"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_REPEATED_TOOL_CALL"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_THERMAL_PRESSURE"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_VISUAL_CONTENT"
+ "APCTAGENTPASSREASON_ONDEVICEPLANNER_ONLINE_VOICE_DISAMBIGUATION"
+ "APCTAGENTPASSREASON_UNKNOWN"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_LOW_BATTERY"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_LOW_POWER_MODE"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_MEMORY_PRESSURE"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_NOT_GATED"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_THERMAL_PRESSURE"
+ "APCTODMDEVICEPRESSUREGATEOUTCOME_UNKNOWN"
+ "CDADEVICESELECTIONOUTCOME_CANCELED"
+ "CDADEVICESELECTIONOUTCOME_DECIDED"
+ "CDADEVICESELECTIONOUTCOME_ERRORED"
+ "CDADEVICESELECTIONOUTCOME_NOT_RUN"
+ "CDADEVICESELECTIONOUTCOME_TIMED_OUT"
+ "CDADEVICESELECTIONOUTCOME_UNKNOWN"
+ "CDMSERVICEGRAPHNAME_EMBEDDED_ASSET"
+ "CHSPEECHBACKINGSOURCE_ENTITY_RESOLUTION"
+ "CHSPEECHBACKINGSOURCE_LIVE_ENTITY"
+ "CHSPEECHBACKINGSOURCE_NONE"
+ "CHSPEECHBACKINGSOURCE_ON_SCREEN_CONTEXT"
+ "CHSPEECHBACKINGSOURCE_SEARCH_RESULT"
+ "CHSPEECHBACKINGSOURCE_UNKNOWN"
+ "CHSPEECHCRITERIONID_EVIDENCE_FOUND"
+ "CHSPEECHCRITERIONID_PLANNER_CONDUCT"
+ "CHSPEECHGRADINGEVIDENCE_FOUND"
+ "CHSPEECHGRADINGEVIDENCE_NOT_FOUND"
+ "CHSPEECHGRADINGEVIDENCE_UNKNOWN"
+ "CHSPEECHPLANNERRESOLUTION_ALT_2_3"
+ "CHSPEECHPLANNERRESOLUTION_DISAMBIGUATION_REQUESTED"
+ "CHSPEECHPLANNERRESOLUTION_NOT_IN_NBEST"
+ "CHSPEECHPLANNERRESOLUTION_TAIL"
+ "CHSPEECHPLANNERRESOLUTION_TOP"
+ "CHSPEECHPLANNERRESOLUTION_UNKNOWN"
+ "DEVICE_SENSITIVITY_STATE_LIVE_REWIND"
+ "INVOCATIONSOURCE_SHARE_SHEET"
+ "ORCHORCHESTRATIONMODE_EMERGENCY"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_CITATION"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_COVER_BLOCK"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_IMAGE"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_KEY_ENTITY"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_LINK"
+ "PLANNERDIRECTRESPONSEREFERENCEKIND_UNKNOWN"
+ "PLANNERUSERIDENTITYCHECKOUTCOME_ANTI_SPOOFING_LOCKOUT"
+ "PLANNERUSERIDENTITYCHECKOUTCOME_COMPANION_OS_NOT_SUPPORTED"
+ "RESPONSETOOLSSEARCHTAGGINGRESULT_NOT_TAGGED"
+ "RESPONSETOOLSSEARCHTAGGINGRESULT_TAGGED"
+ "RESPONSETOOLSSEARCHTAGGINGRESULT_UNKNOWN"
+ "SADSIRIMODE_EMERGENCY"
+ "STGENERALSEARCHRESULTTYPE_HOMEKIT"
+ "STGENERALSEARCHRESULTTYPE_HYBRID_LOCAL"
+ "STHOMEKITHOMEGRAPHLOADREASON_CACHE_EXPIRED"
+ "STHOMEKITHOMEGRAPHLOADREASON_NO_CACHED_HOME_GRAPH"
+ "STHOMEKITHOMEGRAPHLOADREASON_UNKNOWN"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_129_TO_256"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_17_TO_32"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_1_TO_8"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_257_TO_512"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_33_TO_64"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_513_TO_1024"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_65_TO_128"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_9_TO_16"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_EMPTY"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_MORE_THAN_1024"
+ "STHOMEKITHOMEGRAPHSIZEBUCKET_UNKNOWN"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_EMPTY_HOME_GRAPH"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_HOME_APP_RESTRICTED"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_NOT_HOME_ENTITY_REQUEST"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_NO_HOME_IN_SCOPE"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_NO_MATCH"
+ "STHOMEKITSEARCHEMPTYRESULTREASON_UNKNOWN"
+ "STHOMEKITSEARCHENTITYTYPE_COLOR"
+ "STHOMEKITSEARCHENTITYTYPE_DEVICE"
+ "STHOMEKITSEARCHENTITYTYPE_GROUP"
+ "STHOMEKITSEARCHENTITYTYPE_HOME"
+ "STHOMEKITSEARCHENTITYTYPE_INTERCOM_DESTINATION"
+ "STHOMEKITSEARCHENTITYTYPE_INTERCOM_HOME"
+ "STHOMEKITSEARCHENTITYTYPE_ROOM"
+ "STHOMEKITSEARCHENTITYTYPE_SCENE"
+ "STHOMEKITSEARCHENTITYTYPE_TARGET_LOCATION"
+ "STHOMEKITSEARCHENTITYTYPE_UNKNOWN"
+ "STHOMEKITSEARCHENTITYTYPE_ZONE"
+ "STHOMEKITSEARCHREQUESTTYPE_COLOR"
+ "STHOMEKITSEARCHREQUESTTYPE_GENERIC_KEYWORD"
+ "STHOMEKITSEARCHREQUESTTYPE_HOME_ENTITY"
+ "STHOMEKITSEARCHREQUESTTYPE_INTERCOM"
+ "STHOMEKITSEARCHREQUESTTYPE_UNKNOWN"
+ "STPEGASUSCALLCLIENTCONNECTIVITYSTATUS_REQUIRES_CONNECTION"
+ "STPEGASUSCALLCLIENTCONNECTIVITYSTATUS_SATISFIED"
+ "STPEGASUSCALLCLIENTCONNECTIVITYSTATUS_UNKNOWN"
+ "STPEGASUSCALLCLIENTCONNECTIVITYSTATUS_UNSATISFIED"
+ "STPEGASUSCALLCLIENTCONTEXTFETCHFAILUREREASON_BAD_RESPONSE"
+ "STPEGASUSCALLCLIENTCONTEXTFETCHFAILUREREASON_CONTEXT_FETCH_FAILED"
+ "STPEGASUSCALLCLIENTCONTEXTFETCHFAILUREREASON_OTHER_CONTEXT_ERROR"
+ "STPEGASUSCALLCLIENTCONTEXTFETCHFAILUREREASON_UNKNOWN"
+ "STPEGASUSCALLCLIENTCONTEXTFETCHFAILUREREASON_XPC_ERROR"
+ "STPEGASUSCALLCLIENTLINKQUALITY_GOOD"
+ "STPEGASUSCALLCLIENTLINKQUALITY_MINIMAL"
+ "STPEGASUSCALLCLIENTLINKQUALITY_MODERATE"
+ "STPEGASUSCALLCLIENTLINKQUALITY_UNKNOWN"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_CLIENT_THROTTLED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_DATA_TASK_FAILURE"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_NETWORK_ERROR"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_ABORTED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_ALREADY_EXISTS"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_CANCELED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_DATA_LOSS"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_DEADLINE_EXCEEDED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_FAILED_PRECONDITION"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_INTERNAL"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_INVALID_ARGUMENT"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_NOT_FOUND"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_OUT_OF_RANGE"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_PERMISSION_DENIED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_RESOURCE_EXHAUSTED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_UNAUTHENTICATED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_UNAVAILABLE"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_UNIMPLEMENTED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_RPC_ERROR_UNKNOWN"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_SERVER_RESPONSE_ERROR"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_TASK_CANCELED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_UNKNOWN"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_BAD_URL"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_CANCELED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_CANNOT_FIND_HOST"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_DATA_NOT_ALLOWED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_DNS_LOOKUP_FAILED"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_HTTP_TOO_MANY_REDIRECTS"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_NETWORK_CONNECTION_LOST"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_NOT_CONNECTED_TO_INTERNET"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_REDIRECT_TO_NON_EXISTENT_LOCATION"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_RESOURCE_UNAVAILABLE"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_TIMED_OUT"
+ "STPEGASUSCALLCLIENTNETWORKFAILUREREASON_URL_ERROR_UNSUPPORTED_URL"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_CELLULAR"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_LOOPBACK"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_OTHER"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_UNKNOWN"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_WIFI"
+ "STPEGASUSCALLCLIENTNETWORKINTERFACETYPE_WIRED_ETHERNET"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_CELLULAR_DENIED"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_LOCAL_NETWORK_DENIED"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_NOT_AVAILABLE"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_UNKNOWN"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_VPN_INACTIVE"
+ "STPEGASUSCALLCLIENTNETWORKUNSATISFIEDREASON_WIFI_DENIED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_CHALLENGE_DATA_MISSING"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_CHALLENGE_FAILED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_FEATURE_DISABLED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_FETCHER_INIT_FAILED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_FETCH_FAILED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_AUTHENTICATION"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_CONFIG_DATA"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_CONFIG_DATA_SIGN"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_CONFIG_DATES"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_PARAM"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_REQUEST"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_RESPONSE"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_INVALID_USER_TIER"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_IPC_FAILED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_NETWORK_ERROR"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_PERMISSION_DENIED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_RATE_LIMITED"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_SERVER_ERROR"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_TDM_FAILURE"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_TRANSPARENCY_FAILURE"
+ "STPEGASUSCALLCLIENTPATFETCHFAILUREREASON_UNKNOWN"
+ "STPEGASUSPHASEENGAGEMENTSTATE_COLD"
+ "STPEGASUSPHASEENGAGEMENTSTATE_FIRST_TIME_WARM"
+ "STPEGASUSPHASEENGAGEMENTSTATE_UNKNOWN"
+ "STPEGASUSPHASEENGAGEMENTSTATE_WARM"
+ "STPEGASUSPHASEENGAGEMENTSTATE_WARMING_UP"
+ "TCUSERGROUNDINGSIGNAL_NONE"
+ "TCUSERGROUNDINGSIGNAL_STRONG"
+ "TCUSERGROUNDINGSIGNAL_UNKNOWN"
+ "TCUSERGROUNDINGSIGNAL_WEAK"
+ "TMSTURNTRAILINGSILENCETHRESHOLDTYPE_LONG_FORM"
+ "TMSTURNTRAILINGSILENCETHRESHOLDTYPE_MAX"
+ "TMSTURNTRAILINGSILENCETHRESHOLDTYPE_MIN"
+ "TMSTURNTRAILINGSILENCETHRESHOLDTYPE_NO_TRP_ARRIVAL"
+ "TMSTURNTRAILINGSILENCETHRESHOLDTYPE_UNKNOWN"
+ "UEIUSERFEEDBACKTYPE_NEGATIVE"
+ "UEIUSERFEEDBACKTYPE_POSITIVE"
+ "UEIUSERFEEDBACKTYPE_UNKNOWN"
+ "agentMode"
+ "agentPassReason"
+ "alarmOrTimerFiringBoost"
+ "alternativesPresent"
+ "assistantLLMSiriDigestsReported.digests.turnIds"
+ "assistantSiriExtensionsDigestsReported.digests.turnIds"
+ "attentionOverride"
+ "audioOrderDeviceCount"
+ "audioOrderPosition"
+ "backingSource"
+ "com.apple.aiml.siri.apct.APCTClientEvent.APCTODMDevicePressureGateEvaluated"
+ "com.apple.aiml.siri.cda.CDAClientEvent.CDADeviceSelectionDecisionMade"
+ "com.apple.aiml.siri.responsetools.RESPONSETOOLSClientEvent.RESPONSETOOLSSearchTagEvaluated"
+ "com.apple.aiml.siri.searchtool.STEvent.STHomeKitHomeGraphLoadContext"
+ "com.apple.aiml.siri.searchtool.STEvent.STHomeKitSearchContext"
+ "com.apple.aiml.siri.tc.TCClientEvent.TCUserGroundingContext"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIUserFeedbackProvided"
+ "connectivity"
+ "contextFetch"
+ "decisionLatencyInMs"
+ "desiredOrchestrationMode"
+ "deviceAdjustmentBoost"
+ "deviceSelectionDecisionMade"
+ "directResponseReferences"
+ "downloadedKilobytes"
+ "emergencyModeCause"
+ "emptyResultReason"
+ "endOffsetMs"
+ "engagementState"
+ "evaluationTexts"
+ "evidence"
+ "executionContext.startedOrChanged.plannerToolInputs.parameterValues.evaluationTexts"
+ "feedbackType"
+ "finalState"
+ "finalStateOffsetMs"
+ "firstChunkOffsetMs"
+ "freeFormText.freeFormText.evaluationTexts"
+ "freeFormTextTier1.freeFormText.evaluationTexts"
+ "goodness"
+ "homeClauseCount"
+ "homeGraphSizeBucket"
+ "inEarOverride"
+ "initialState"
+ "isHomeGraphCached"
+ "isUltraConstrained"
+ "liftTimeBoost"
+ "linkQuality"
+ "loadReason"
+ "mediaPlaybackActiveBoost"
+ "mediaPlaybackRecentPlaybackBoost"
+ "odmDevicePressureGateEvaluated"
+ "odmDevicePressureSignals"
+ "onscreenOrLiveContextPresent"
+ "onscreenOrLiveContextUsed"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.promptRequested.inputPromptText.evaluationTexts"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.requestReceivedTier1.textToSpeak.evaluationTexts"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.speechContext.startedOrChanged.textToSpeak.evaluationTexts"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.streamingRequest.textToSpeak.evaluationTexts"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.synthesisContext.startedOrChanged.textToSpeak.evaluationTexts"
+ "orderedMessages.siriEventTypeUnion.ueiClientEvent.ueiLinkTapped.url"
+ "patFetch"
+ "pegasusCallClientMetrics"
+ "perceptionBoost"
+ "perceptionOverride"
+ "plannerResolution"
+ "planningModelInferenceContext.ended.directResponseReferences.entity.entityKind"
+ "platformBoost"
+ "primaryInterfaceType"
+ "promptRequested.inputPromptText.evaluationTexts"
+ "raiseToWakeBoost"
+ "rawLoudness"
+ "recencyBoost"
+ "referenceKind"
+ "requestContext.ended.responseStringOutput.evaluationTexts"
+ "requestContext.startedOrChanged.responseStringInput.evaluationTexts"
+ "requestReceivedTier1.textToSpeak.evaluationTexts"
+ "requestTypes"
+ "saRequestContext.startedOrChanged.structuredQueryToolCall.primaryTool.toolArguments.value.evaluationTexts"
+ "saRequestContext.startedOrChanged.structuredQueryToolCall.secondaryTools.toolArguments.value.evaluationTexts"
+ "searchTagEvaluated"
+ "searchTaggingResult"
+ "setup"
+ "speechContext.startedOrChanged.textToSpeak.evaluationTexts"
+ "stGlobalBatchSearchContext.startedOrChanged.domainRequests.query.evaluationTexts"
+ "stHomeKitHomeGraphLoadContext"
+ "stHomeKitSearchContext"
+ "stSpotlightContext.ended.modelResponse.evaluationTexts"
+ "startOffsetMs"
+ "stream"
+ "streamingRequest.textToSpeak.evaluationTexts"
+ "strongThreshold"
+ "synthesisContext.startedOrChanged.textToSpeak.evaluationTexts"
+ "thoughtTokenCount"
+ "timeSinceLastSeenInSeconds"
+ "trailingSilenceThresholdType"
+ "ueiLinkTapped.url"
+ "ueiUserFeedbackProvided"
+ "unlockTimeBoost"
+ "unsatisfiedReason"
+ "userGroundingContext"
+ "userGroundingNgramScores"
+ "userGroundingSignal"
+ "videoFindThirdPartyVideoInvoked.searchTerm.evaluationTexts"
+ "watchGestureBoost"
+ "watchLoudnessThresholdOverride"
+ "weakThreshold"
```
