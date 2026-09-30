## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3515.7.1.0.0
-  __TEXT.__text: 0xa57f5c
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0xd58c4
-  __TEXT.__const: 0x12790
-  __TEXT.__constg_swiftt: 0x6580
-  __TEXT.__swift5_typeref: 0x190c
-  __TEXT.__swift5_builtin: 0x3ae8
+3520.65.1.1.1
+  __TEXT.__text: 0xaeb47c
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_methlist: 0xd8c04
+  __TEXT.__const: 0x130b4
+  __TEXT.__swift5_typeref: 0x1a26
+  __TEXT.__cstring: 0x7dbc7
+  __TEXT.__constg_swiftt: 0x6920
   __TEXT.__swift5_reflstr: 0x212
+  __TEXT.__swift5_fieldmd: 0x42c
+  __TEXT.__swift5_builtin: 0x3cf0
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xf44
-  __TEXT.__swift5_types: 0xc18
-  __TEXT.__cstring: 0x7bbb3
-  __TEXT.__swift5_fieldmd: 0x3e8
-  __TEXT.__oslogstring: 0x95
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2b078
-  __TEXT.__eh_frame: 0x24d8
-  __TEXT.__objc_classname: 0x15dc0
-  __TEXT.__objc_methname: 0x1281ea
-  __TEXT.__objc_methtype: 0x293fc
-  __TEXT.__objc_stubs: 0x6b180
-  __DATA_CONST.__got: 0x4d90
-  __DATA_CONST.__const: 0x35908
-  __DATA_CONST.__objc_classlist: 0x4c70
+  __TEXT.__swift5_proto: 0xfc4
+  __TEXT.__swift5_types: 0xc80
+  __TEXT.__oslogstring: 0xc1
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__unwind_info: 0x2da98
+  __TEXT.__eh_frame: 0x3980
+  __TEXT.__objc_classname: 0x161f8
+  __TEXT.__objc_methname: 0x12d1c6
+  __TEXT.__objc_methtype: 0x29e1d
+  __TEXT.__objc_stubs: 0x6cf80
+  __DATA_CONST.__got: 0x4e18
+  __DATA_CONST.__const: 0x36fe8
+  __DATA_CONST.__objc_classlist: 0x4d20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37760
+  __DATA_CONST.__objc_selrefs: 0x386b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7700
-  __AUTH_CONST.__auth_got: 0x858
-  __AUTH_CONST.__const: 0x1c080
-  __AUTH_CONST.__cfstring: 0x6b0c0
-  __AUTH_CONST.__objc_const: 0x120f50
+  __DATA_CONST.__objc_superrefs: 0x7860
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__const: 0x1cf70
+  __AUTH_CONST.__cfstring: 0x6d100
+  __AUTH_CONST.__objc_const: 0x124d30
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11b70
-  __DATA.__objc_ivar: 0xe6a0
-  __DATA.__data: 0x2868
-  __DATA.__bss: 0x19180
+  __AUTH.__objc_data: 0x11170
+  __DATA.__objc_ivar: 0xea30
+  __DATA.__data: 0x2950
+  __DATA.__bss: 0x19e80
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x1e340
-  __DATA_DIRTY.__data: 0x568
-  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0x1f440
+  __DATA_DIRTY.__data: 0x570
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3A1E21FD-F223-3C10-8A4A-BBA8B6C15342
-  Functions: 77813
-  Symbols:   192237
-  CStrings:  79098
+  UUID: A66442B6-747F-34D9-9189-DEDDA3300BF1
+  Functions: 79197
+  Symbols:   195170
+  CStrings:  80389
 
Symbols:
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded addEntityMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded clearEntityMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteEntityMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded entityMetricsAtIndex:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded entityMetricsCount]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded entityMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setEntityMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric deleteEntityCategory]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric deleteNumEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric entityCategory]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric hasEntityCategory]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric hasNumEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric numEntities]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric setEntityCategory:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric setHasEntityCategory:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric setHasNumEntities:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric setNumEntities:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric(SensitiveConditions) suppressMessageUnderConditions]
+ -[DUSchemaDUEvent deleteSpeechDatasetsRecord]
+ -[DUSchemaDUEvent hasSpeechDatasetsRecord]
+ -[DUSchemaDUEvent setHasSpeechDatasetsRecord:]
+ -[DUSchemaDUEvent setSpeechDatasetsRecord:]
+ -[DUSchemaDUEvent speechDatasetsRecord]
+ -[DUSchemaDUSpeechDatasetsRecord .cxx_destruct]
+ -[DUSchemaDUSpeechDatasetsRecord datasetsCapturedTimestampMs]
+ -[DUSchemaDUSpeechDatasetsRecord deleteDatasetsCapturedTimestampMs]
+ -[DUSchemaDUSpeechDatasetsRecord deleteInteractionId]
+ -[DUSchemaDUSpeechDatasetsRecord dictionaryRepresentation]
+ -[DUSchemaDUSpeechDatasetsRecord hasDatasetsCapturedTimestampMs]
+ -[DUSchemaDUSpeechDatasetsRecord hasInteractionId]
+ -[DUSchemaDUSpeechDatasetsRecord hash]
+ -[DUSchemaDUSpeechDatasetsRecord initWithDictionary:]
+ -[DUSchemaDUSpeechDatasetsRecord initWithJSON:]
+ -[DUSchemaDUSpeechDatasetsRecord interactionId]
+ -[DUSchemaDUSpeechDatasetsRecord isEqual:]
+ -[DUSchemaDUSpeechDatasetsRecord jsonData]
+ -[DUSchemaDUSpeechDatasetsRecord readFrom:]
+ -[DUSchemaDUSpeechDatasetsRecord setDatasetsCapturedTimestampMs:]
+ -[DUSchemaDUSpeechDatasetsRecord setHasDatasetsCapturedTimestampMs:]
+ -[DUSchemaDUSpeechDatasetsRecord setHasInteractionId:]
+ -[DUSchemaDUSpeechDatasetsRecord setInteractionId:]
+ -[DUSchemaDUSpeechDatasetsRecord writeTo:]
+ -[DUSchemaDUSpeechDatasetsRecord(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DUSchemaDUSpeechDatasetsRecord(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded deleteExecutorAppIntentMetrics]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded deleteResult]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded executorAppIntentMetrics]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded hasExecutorAppIntentMetrics]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded hasResult]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded result]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded setExecutorAppIntentMetrics:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded setHasExecutorAppIntentMetrics:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded setHasResult:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded setResult:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed addErrors:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed clearErrors]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed deleteErrorKind]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed deleteErrors]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed errorKind]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed errorsAtIndex:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed errorsCount]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed errors]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed hasErrorKind]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed setErrorKind:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed setErrors:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed setHasErrorKind:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics addExecutorAppIntentSegments:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics clearExecutorAppIntentSegments]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics connectionDurationInNanoSeconds]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteConnectionDurationInNanoSeconds]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteExecutorAppIntentSegments]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteExecutorAppIntentTargetType]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteIsAppBroughtToForeground]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteIsProcessLaunchRequired]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics deleteStartedLiveActivity]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics executorAppIntentSegmentsAtIndex:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics executorAppIntentSegmentsCount]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics executorAppIntentSegments]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics executorAppIntentTargetType]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hasConnectionDurationInNanoSeconds]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hasExecutorAppIntentTargetType]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hasIsAppBroughtToForeground]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hasIsProcessLaunchRequired]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hasStartedLiveActivity]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics hash]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics initWithJSON:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics isAppBroughtToForeground]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics isEqual:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics isProcessLaunchRequired]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics jsonData]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics readFrom:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setConnectionDurationInNanoSeconds:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setExecutorAppIntentSegments:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setExecutorAppIntentTargetType:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setHasConnectionDurationInNanoSeconds:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setHasExecutorAppIntentTargetType:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setHasIsAppBroughtToForeground:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setHasIsProcessLaunchRequired:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setHasStartedLiveActivity:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setIsAppBroughtToForeground:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setIsProcessLaunchRequired:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics setStartedLiveActivity:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics startedLiveActivity]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics writeTo:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorAppIntentMetrics(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteExecutorAppIntentAttribution]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteExecutorAppIntentTask]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteMachTimeEnd]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteMachTimeStart]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteRequestUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment deleteSessionUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment executorAppIntentAttribution]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment executorAppIntentTask]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasExecutorAppIntentAttribution]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasExecutorAppIntentTask]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasMachTimeEnd]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasMachTimeStart]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasRequestUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hasSessionUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment hash]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment initWithJSON:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment isEqual:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment jsonData]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment machTimeEnd]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment machTimeStart]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment readFrom:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment requestUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment sessionUUID]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setExecutorAppIntentAttribution:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setExecutorAppIntentTask:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasExecutorAppIntentAttribution:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasExecutorAppIntentTask:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasMachTimeEnd:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasMachTimeStart:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasRequestUUID:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setHasSessionUUID:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setMachTimeEnd:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setMachTimeStart:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setRequestUUID:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment setSessionUUID:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment writeTo:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorAppIntentSegment(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFPlatformRequestSchemaIFPlatformRequestClientEvent deleteIfPlatformRequestStructuredError]
+ -[IFPlatformRequestSchemaIFPlatformRequestClientEvent hasIfPlatformRequestStructuredError]
+ -[IFPlatformRequestSchemaIFPlatformRequestClientEvent ifPlatformRequestStructuredError]
+ -[IFPlatformRequestSchemaIFPlatformRequestClientEvent setHasIfPlatformRequestStructuredError:]
+ -[IFPlatformRequestSchemaIFPlatformRequestClientEvent setIfPlatformRequestStructuredError:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError .cxx_destruct]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError addErrors:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError clearErrors]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError deleteErrors]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError dictionaryRepresentation]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError errorsAtIndex:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError errorsCount]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError errors]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError hash]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError initWithDictionary:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError initWithJSON:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError isEqual:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError jsonData]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError readFrom:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError setErrors:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError writeTo:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFPlatformRequestSchemaIFPlatformRequestStructuredError(SensitiveConditions) suppressMessageUnderConditions]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals .cxx_destruct]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals addModelSelectedOptions:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals clearModelSelectedOptions]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals deleteIsModelConfirmation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals deleteIsModelDisambiguation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals deleteModelSelectedOptions]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals deleteModelVersion]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals hasIsModelConfirmation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals hasIsModelDisambiguation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals hasModelVersion]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals isModelConfirmation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals isModelDisambiguation]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals modelSelectedOptionsAtIndex:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals modelSelectedOptionsCount]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals modelSelectedOptions]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals modelVersion]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setHasIsModelConfirmation:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setHasIsModelDisambiguation:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setHasModelVersion:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setIsModelConfirmation:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setIsModelDisambiguation:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setModelSelectedOptions:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals setModelVersion:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals .cxx_destruct]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals addModelSelectedOptions:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals clearModelSelectedOptions]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteIsModelConfirmation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteIsModelDisambiguation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteModelSelectedOptions]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteModelVersionStr]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteUserPersona]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasIsModelConfirmation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasIsModelDisambiguation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasModelVersionStr]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasUserPersona]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals isModelConfirmation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals isModelDisambiguation]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals modelSelectedOptionsAtIndex:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals modelSelectedOptionsCount]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals modelSelectedOptions]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals modelVersionStr]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasIsModelConfirmation:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasIsModelDisambiguation:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasModelVersionStr:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasUserPersona:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setIsModelConfirmation:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setIsModelDisambiguation:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setModelSelectedOptions:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setModelVersionStr:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setUserPersona:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals userPersona]
+ -[LRSchemaLRDataClassificationManifest .cxx_destruct]
+ -[LRSchemaLRDataClassificationManifest addExplainabilityIdentifiers:]
+ -[LRSchemaLRDataClassificationManifest classifiedString]
+ -[LRSchemaLRDataClassificationManifest clearExplainabilityIdentifiers]
+ -[LRSchemaLRDataClassificationManifest deleteClassifiedString]
+ -[LRSchemaLRDataClassificationManifest deleteExplainabilityIdentifiers]
+ -[LRSchemaLRDataClassificationManifest deleteIsRedacted]
+ -[LRSchemaLRDataClassificationManifest deleteMetadata]
+ -[LRSchemaLRDataClassificationManifest dictionaryRepresentation]
+ -[LRSchemaLRDataClassificationManifest explainabilityIdentifiersAtIndex:]
+ -[LRSchemaLRDataClassificationManifest explainabilityIdentifiersCount]
+ -[LRSchemaLRDataClassificationManifest explainabilityIdentifiers]
+ -[LRSchemaLRDataClassificationManifest hasClassifiedString]
+ -[LRSchemaLRDataClassificationManifest hasIsRedacted]
+ -[LRSchemaLRDataClassificationManifest hasMetadata]
+ -[LRSchemaLRDataClassificationManifest hash]
+ -[LRSchemaLRDataClassificationManifest initWithDictionary:]
+ -[LRSchemaLRDataClassificationManifest initWithJSON:]
+ -[LRSchemaLRDataClassificationManifest isEqual:]
+ -[LRSchemaLRDataClassificationManifest isRedacted]
+ -[LRSchemaLRDataClassificationManifest jsonData]
+ -[LRSchemaLRDataClassificationManifest metadata]
+ -[LRSchemaLRDataClassificationManifest readFrom:]
+ -[LRSchemaLRDataClassificationManifest setClassifiedString:]
+ -[LRSchemaLRDataClassificationManifest setExplainabilityIdentifiers:]
+ -[LRSchemaLRDataClassificationManifest setHasClassifiedString:]
+ -[LRSchemaLRDataClassificationManifest setHasIsRedacted:]
+ -[LRSchemaLRDataClassificationManifest setHasMetadata:]
+ -[LRSchemaLRDataClassificationManifest setIsRedacted:]
+ -[LRSchemaLRDataClassificationManifest setMetadata:]
+ -[LRSchemaLRDataClassificationManifest writeTo:]
+ -[LRSchemaLRDataClassificationManifest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[LRSchemaLRDataClassificationManifest(SensitiveConditions) suppressMessageUnderConditions]
+ -[LRSchemaLRDataClassificationMetadata deleteGeneral]
+ -[LRSchemaLRDataClassificationMetadata deleteKind]
+ -[LRSchemaLRDataClassificationMetadata deleteOnDevice]
+ -[LRSchemaLRDataClassificationMetadata deletePartOfARequest]
+ -[LRSchemaLRDataClassificationMetadata deleteSensor]
+ -[LRSchemaLRDataClassificationMetadata deleteTool]
+ -[LRSchemaLRDataClassificationMetadata dictionaryRepresentation]
+ -[LRSchemaLRDataClassificationMetadata general]
+ -[LRSchemaLRDataClassificationMetadata hasGeneral]
+ -[LRSchemaLRDataClassificationMetadata hasKind]
+ -[LRSchemaLRDataClassificationMetadata hasOnDevice]
+ -[LRSchemaLRDataClassificationMetadata hasPartOfARequest]
+ -[LRSchemaLRDataClassificationMetadata hasSensor]
+ -[LRSchemaLRDataClassificationMetadata hasTool]
+ -[LRSchemaLRDataClassificationMetadata hash]
+ -[LRSchemaLRDataClassificationMetadata initWithDictionary:]
+ -[LRSchemaLRDataClassificationMetadata initWithJSON:]
+ -[LRSchemaLRDataClassificationMetadata isEqual:]
+ -[LRSchemaLRDataClassificationMetadata jsonData]
+ -[LRSchemaLRDataClassificationMetadata kind]
+ -[LRSchemaLRDataClassificationMetadata onDevice]
+ -[LRSchemaLRDataClassificationMetadata partOfARequest]
+ -[LRSchemaLRDataClassificationMetadata readFrom:]
+ -[LRSchemaLRDataClassificationMetadata sensor]
+ -[LRSchemaLRDataClassificationMetadata setGeneral:]
+ -[LRSchemaLRDataClassificationMetadata setHasGeneral:]
+ -[LRSchemaLRDataClassificationMetadata setHasKind:]
+ -[LRSchemaLRDataClassificationMetadata setHasOnDevice:]
+ -[LRSchemaLRDataClassificationMetadata setHasPartOfARequest:]
+ -[LRSchemaLRDataClassificationMetadata setHasSensor:]
+ -[LRSchemaLRDataClassificationMetadata setHasTool:]
+ -[LRSchemaLRDataClassificationMetadata setKind:]
+ -[LRSchemaLRDataClassificationMetadata setOnDevice:]
+ -[LRSchemaLRDataClassificationMetadata setPartOfARequest:]
+ -[LRSchemaLRDataClassificationMetadata setSensor:]
+ -[LRSchemaLRDataClassificationMetadata setTool:]
+ -[LRSchemaLRDataClassificationMetadata tool]
+ -[LRSchemaLRDataClassificationMetadata whichProvenance_Type]
+ -[LRSchemaLRDataClassificationMetadata writeTo:]
+ -[LRSchemaLRDataClassificationMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[LRSchemaLRRedactionSummaryReported addDataClassificationManifests:]
+ -[LRSchemaLRRedactionSummaryReported clearDataClassificationManifests]
+ -[LRSchemaLRRedactionSummaryReported dataClassificationManifestsAtIndex:]
+ -[LRSchemaLRRedactionSummaryReported dataClassificationManifestsCount]
+ -[LRSchemaLRRedactionSummaryReported dataClassificationManifests]
+ -[LRSchemaLRRedactionSummaryReported deleteDataClassificationManifests]
+ -[LRSchemaLRRedactionSummaryReported setDataClassificationManifests:]
+ -[MTSchemaMTFrameworkRequestSent deleteModelVersion]
+ -[MTSchemaMTFrameworkRequestSent hasModelVersion]
+ -[MTSchemaMTFrameworkRequestSent modelVersion]
+ -[MTSchemaMTFrameworkRequestSent setHasModelVersion:]
+ -[MTSchemaMTFrameworkRequestSent setModelVersion:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported digests]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported hash]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported jsonData]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssetBringUpDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssetBringUpStatus .cxx_destruct]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetBringUpErrorCode]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetBringUpErrorDescription]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetBringUpErrorDomain]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetBringUpState]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetBringUpType]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetSetIdentifier]
+ -[ODDSiriSchemaODDAssetBringUpStatus assetSetName]
+ -[ODDSiriSchemaODDAssetBringUpStatus countOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus countOfPSUSAssetsPromotedInCurrentOS]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetBringUpErrorCode]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetBringUpErrorDescription]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetBringUpErrorDomain]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetBringUpState]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetBringUpType]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetSetIdentifier]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteAssetSetName]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteCountOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteCountOfPSUSAssetsPromotedInCurrentOS]
+ -[ODDSiriSchemaODDAssetBringUpStatus deletePreviousBuildVersion]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteTimeInSecondsSinceSoftwareUpdate]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteTotalSizeOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus deleteUafAssetSource]
+ -[ODDSiriSchemaODDAssetBringUpStatus dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetBringUpErrorCode]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetBringUpErrorDescription]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetBringUpErrorDomain]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetBringUpState]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetBringUpType]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetSetIdentifier]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasAssetSetName]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasCountOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasCountOfPSUSAssetsPromotedInCurrentOS]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasPreviousBuildVersion]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasTimeInSecondsSinceSoftwareUpdate]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasTotalSizeOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus hasUafAssetSource]
+ -[ODDSiriSchemaODDAssetBringUpStatus hash]
+ -[ODDSiriSchemaODDAssetBringUpStatus initWithDictionary:]
+ -[ODDSiriSchemaODDAssetBringUpStatus initWithJSON:]
+ -[ODDSiriSchemaODDAssetBringUpStatus isEqual:]
+ -[ODDSiriSchemaODDAssetBringUpStatus jsonData]
+ -[ODDSiriSchemaODDAssetBringUpStatus previousBuildVersion]
+ -[ODDSiriSchemaODDAssetBringUpStatus readFrom:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetBringUpErrorCode:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetBringUpErrorDescription:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetBringUpErrorDomain:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetBringUpState:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetBringUpType:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetSetIdentifier:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setAssetSetName:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setCountOfAssetsInAssetSet:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setCountOfPSUSAssetsPromotedInCurrentOS:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetBringUpErrorCode:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetBringUpErrorDescription:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetBringUpErrorDomain:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetBringUpState:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetBringUpType:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetSetIdentifier:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasAssetSetName:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasCountOfAssetsInAssetSet:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasCountOfPSUSAssetsPromotedInCurrentOS:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasPreviousBuildVersion:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasTimeInSecondsSinceSoftwareUpdate:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasTotalSizeOfAssetsInAssetSet:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setHasUafAssetSource:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setPreviousBuildVersion:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setTimeInSecondsSinceSoftwareUpdate:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setTotalSizeOfAssetsInAssetSet:]
+ -[ODDSiriSchemaODDAssetBringUpStatus setUafAssetSource:]
+ -[ODDSiriSchemaODDAssetBringUpStatus timeInSecondsSinceSoftwareUpdate]
+ -[ODDSiriSchemaODDAssetBringUpStatus totalSizeOfAssetsInAssetSet]
+ -[ODDSiriSchemaODDAssetBringUpStatus uafAssetSource]
+ -[ODDSiriSchemaODDAssetBringUpStatus writeTo:]
+ -[ODDSiriSchemaODDAssetBringUpStatus(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteIsAmbiguousRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteIsGenAIAware]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteIsSuitableForGenAI]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasIsAmbiguousRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasIsGenAIAware]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasIsSuitableForGenAI]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions isAmbiguousRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions isGenAIAware]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions isSuitableForGenAI]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasIsAmbiguousRequest:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasIsGenAIAware:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasIsSuitableForGenAI:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setIsAmbiguousRequest:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setIsGenAIAware:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setIsSuitableForGenAI:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantVoicesCounts deleteNeuralFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts deleteTurnCounts]
+ -[ODDSiriSchemaODDAssistantVoicesCounts deleteVocalizerFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantVoicesCounts hasNeuralFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts hasTurnCounts]
+ -[ODDSiriSchemaODDAssistantVoicesCounts hasVocalizerFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts hash]
+ -[ODDSiriSchemaODDAssistantVoicesCounts initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts initWithJSON:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts isEqual:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts jsonData]
+ -[ODDSiriSchemaODDAssistantVoicesCounts neuralFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts readFrom:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setHasNeuralFallbackCount:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setHasTurnCounts:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setHasVocalizerFallbackCount:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setNeuralFallbackCount:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setTurnCounts:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts setVocalizerFallbackCount:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts turnCounts]
+ -[ODDSiriSchemaODDAssistantVoicesCounts vocalizerFallbackCount]
+ -[ODDSiriSchemaODDAssistantVoicesCounts writeTo:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantVoicesCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantVoicesDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantVoicesDigest counts]
+ -[ODDSiriSchemaODDAssistantVoicesDigest deleteCounts]
+ -[ODDSiriSchemaODDAssistantVoicesDigest deleteDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigest deleteTuples]
+ -[ODDSiriSchemaODDAssistantVoicesDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantVoicesDigest dimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigest hasCounts]
+ -[ODDSiriSchemaODDAssistantVoicesDigest hasDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigest hasTuples]
+ -[ODDSiriSchemaODDAssistantVoicesDigest hash]
+ -[ODDSiriSchemaODDAssistantVoicesDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest initWithJSON:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest isEqual:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest jsonData]
+ -[ODDSiriSchemaODDAssistantVoicesDigest readFrom:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setCounts:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setHasCounts:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setHasTuples:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest setTuples:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest tuples]
+ -[ODDSiriSchemaODDAssistantVoicesDigest writeTo:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantVoicesDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported digests]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported hash]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported jsonData]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantVoicesDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions addErrorCodes:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions assistantDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions clearErrorCodes]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions clientId]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteClientId]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteErrorCodes]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteSynthesisSource]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteTtsStatus]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteVoiceName]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions deleteVoiceType]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions errorCodesAtIndex:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions errorCodesCount]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions errorCodes]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasClientId]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasSynthesisSource]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasTtsStatus]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasVoiceName]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hasVoiceType]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions hash]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions initWithJSON:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions isEqual:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions jsonData]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions readFrom:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setClientId:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setErrorCodes:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasClientId:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasSynthesisSource:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasTtsStatus:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasVoiceName:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setHasVoiceType:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setSynthesisSource:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setTtsStatus:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setVoiceName:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions setVoiceType:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions synthesisSource]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions ttsStatus]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions voiceName]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions voiceType]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions writeTo:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantVoicesDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantVoicesTuples .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantVoicesTuples addAutoMOS:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples addCustomerPerceivedLatencyInSec:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples addSpeakingDurationInSec:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples autoMOSAtIndex:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples autoMOSCount]
+ -[ODDSiriSchemaODDAssistantVoicesTuples autoMOSs]
+ -[ODDSiriSchemaODDAssistantVoicesTuples clearAutoMOS]
+ -[ODDSiriSchemaODDAssistantVoicesTuples clearCustomerPerceivedLatencyInSec]
+ -[ODDSiriSchemaODDAssistantVoicesTuples clearSpeakingDurationInSec]
+ -[ODDSiriSchemaODDAssistantVoicesTuples customerPerceivedLatencyInSecAtIndex:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples customerPerceivedLatencyInSecCount]
+ -[ODDSiriSchemaODDAssistantVoicesTuples customerPerceivedLatencyInSecs]
+ -[ODDSiriSchemaODDAssistantVoicesTuples deleteAutoMOS]
+ -[ODDSiriSchemaODDAssistantVoicesTuples deleteCustomerPerceivedLatencyInSec]
+ -[ODDSiriSchemaODDAssistantVoicesTuples deleteSpeakingDurationInSec]
+ -[ODDSiriSchemaODDAssistantVoicesTuples dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantVoicesTuples hash]
+ -[ODDSiriSchemaODDAssistantVoicesTuples initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples initWithJSON:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples isEqual:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples jsonData]
+ -[ODDSiriSchemaODDAssistantVoicesTuples readFrom:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples setAutoMOSs:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples setCustomerPerceivedLatencyInSecs:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples setSpeakingDurationInSecs:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples speakingDurationInSecAtIndex:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples speakingDurationInSecCount]
+ -[ODDSiriSchemaODDAssistantVoicesTuples speakingDurationInSecs]
+ -[ODDSiriSchemaODDAssistantVoicesTuples writeTo:]
+ -[ODDSiriSchemaODDAssistantVoicesTuples(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAttentionInvocationCounts .cxx_destruct]
+ -[ODDSiriSchemaODDAttentionInvocationCounts acousticMitigatorAcceptPostAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts addNearMissCheckerScoreList:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts addNearMissPitchList:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts addNearMissSNRList:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts addNearMissWithRetryList:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts addNearMissWithTriggerPhraseList:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts clearNearMissCheckerScoreList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts clearNearMissPitchList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts clearNearMissSNRList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts clearNearMissWithRetryList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts clearNearMissWithTriggerPhraseList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts contextualMitigatorAcceptPostContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteAcousticMitigatorAcceptPostAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteContextualMitigatorAcceptPostContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteEstimatedSiriMissCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteFalseWakeWithLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteHasMultiKeyboards]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteLwSpkidMitigatorAcceptPostLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNearMissCheckerScoreList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNearMissPitchList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNearMissSNRList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNearMissWithRetryList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteNearMissWithTriggerPhraseList]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deletePhsRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteSecondPassAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteSecondPassRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts deleteSiriActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts estimatedSiriMissCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts falseWakeWithLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasAcousticMitigatorAcceptPostAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasContextualMitigatorAcceptPostContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasEstimatedSiriMissCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithAcousticMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithContextualMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasFalseWakeWithLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasHasMultiKeyboards]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasLwSpkidMitigatorAcceptPostLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasMultiKeyboards]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasPhsRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasSecondPassAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasSecondPassRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts hasSiriActivationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts lwSpkidMitigatorAcceptPostLwSpkidMitigationCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissCheckerScoreListAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissCheckerScoreListCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissCheckerScoreLists]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissPitchListAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissPitchListCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissPitchLists]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissSNRListAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissSNRListCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissSNRLists]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithRetryListAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithRetryListCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithRetryLists]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithTriggerPhraseListAtIndex:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithTriggerPhraseListCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts nearMissWithTriggerPhraseLists]
+ -[ODDSiriSchemaODDAttentionInvocationCounts phsRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts secondPassAcceptCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts secondPassRejectCount]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setAcousticMitigatorAcceptPostAcousticMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setContextualMitigatorAcceptPostContextualMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setEstimatedSiriMissCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithAcousticMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithContextualMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setFalseWakeWithLwSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasAcousticMitigatorAcceptPostAcousticMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasContextualMitigatorAcceptPostContextualMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasEstimatedSiriMissCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithAcousticMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithContextualMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasFalseWakeWithLwSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasHasMultiKeyboards:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasLwSpkidMitigatorAcceptPostLwSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasMultiKeyboards:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasPhsRejectCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasSecondPassAcceptCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasSecondPassRejectCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setHasSiriActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setLwSpkidMitigatorAcceptPostLwSpkidMitigationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNearMissCheckerScoreLists:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNearMissPitchLists:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNearMissSNRLists:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNearMissWithRetryLists:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setNearMissWithTriggerPhraseLists:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setPhsRejectCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setSecondPassAcceptCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setSecondPassRejectCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts setSiriActivationCount:]
+ -[ODDSiriSchemaODDAttentionInvocationCounts siriActivationCount]
+ -[ODDSiriSchemaODDExecutionMetadataReported deleteScheduleType]
+ -[ODDSiriSchemaODDExecutionMetadataReported hasScheduleType]
+ -[ODDSiriSchemaODDExecutionMetadataReported scheduleType]
+ -[ODDSiriSchemaODDExecutionMetadataReported setHasScheduleType:]
+ -[ODDSiriSchemaODDExecutionMetadataReported setScheduleType:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus deleteTotalNumberOfBytesDownloaded]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus hasTotalNumberOfBytesDownloaded]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setHasTotalNumberOfBytesDownloaded:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus setTotalNumberOfBytesDownloaded:]
+ -[ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus totalNumberOfBytesDownloaded]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions deleteOrchMode]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions hasOrchMode]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions orchMode]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setHasOrchMode:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setOrchMode:]
+ -[ODDSiriSchemaODDSiriClientEvent assetBringUpDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent assistantVoicesDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssetBringUpDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssistantVoicesDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssetBringUpDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssistantVoicesDigestsReported]
+ -[ODDSiriSchemaODDSiriClientEvent setAssetBringUpDigestsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setAssistantVoicesDigestsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssetBringUpDigestsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssistantVoicesDigestsReported:]
+ -[ODDSiriSchemaODDVoiceProperties deleteVoiceName]
+ -[ODDSiriSchemaODDVoiceProperties hasVoiceName]
+ -[ODDSiriSchemaODDVoiceProperties setHasVoiceName:]
+ -[ODDSiriSchemaODDVoiceProperties setVoiceName:]
+ -[ODDSiriSchemaODDVoiceProperties voiceName]
+ -[ORCHSchemaORCHRequestFailed .cxx_destruct]
+ -[ORCHSchemaORCHRequestFailed deleteError]
+ -[ORCHSchemaORCHRequestFailed error]
+ -[ORCHSchemaORCHRequestFailed hasError]
+ -[ORCHSchemaORCHRequestFailed setError:]
+ -[ORCHSchemaORCHRequestFailed setHasError:]
+ -[ORCHSchemaORCHRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODClientEvent deletePnrodSiriMetricsAndDims]
+ -[PNRODSchemaPNRODClientEvent hasPnrodSiriMetricsAndDims]
+ -[PNRODSchemaPNRODClientEvent pnrodSiriMetricsAndDims]
+ -[PNRODSchemaPNRODClientEvent setHasPnrodSiriMetricsAndDims:]
+ -[PNRODSchemaPNRODClientEvent setPnrodSiriMetricsAndDims:]
+ -[PNRODSchemaPNRODDimension .cxx_destruct]
+ -[PNRODSchemaPNRODDimension deleteDimensionNameIndex]
+ -[PNRODSchemaPNRODDimension deleteDimensionValueBoolean]
+ -[PNRODSchemaPNRODDimension deleteDimensionValueFloat]
+ -[PNRODSchemaPNRODDimension deleteDimensionValueInteger]
+ -[PNRODSchemaPNRODDimension deleteModelIdentifier]
+ -[PNRODSchemaPNRODDimension deleteToolId]
+ -[PNRODSchemaPNRODDimension dictionaryRepresentation]
+ -[PNRODSchemaPNRODDimension dimensionNameIndex]
+ -[PNRODSchemaPNRODDimension dimensionValueBoolean]
+ -[PNRODSchemaPNRODDimension dimensionValueFloat]
+ -[PNRODSchemaPNRODDimension dimensionValueInteger]
+ -[PNRODSchemaPNRODDimension hasDimensionNameIndex]
+ -[PNRODSchemaPNRODDimension hasDimensionValueBoolean]
+ -[PNRODSchemaPNRODDimension hasDimensionValueFloat]
+ -[PNRODSchemaPNRODDimension hasDimensionValueInteger]
+ -[PNRODSchemaPNRODDimension hasModelIdentifier]
+ -[PNRODSchemaPNRODDimension hasToolId]
+ -[PNRODSchemaPNRODDimension hash]
+ -[PNRODSchemaPNRODDimension initWithDictionary:]
+ -[PNRODSchemaPNRODDimension initWithJSON:]
+ -[PNRODSchemaPNRODDimension isEqual:]
+ -[PNRODSchemaPNRODDimension jsonData]
+ -[PNRODSchemaPNRODDimension modelIdentifier]
+ -[PNRODSchemaPNRODDimension readFrom:]
+ -[PNRODSchemaPNRODDimension setDimensionNameIndex:]
+ -[PNRODSchemaPNRODDimension setDimensionValueBoolean:]
+ -[PNRODSchemaPNRODDimension setDimensionValueFloat:]
+ -[PNRODSchemaPNRODDimension setDimensionValueInteger:]
+ -[PNRODSchemaPNRODDimension setHasDimensionNameIndex:]
+ -[PNRODSchemaPNRODDimension setHasDimensionValueBoolean:]
+ -[PNRODSchemaPNRODDimension setHasDimensionValueFloat:]
+ -[PNRODSchemaPNRODDimension setHasDimensionValueInteger:]
+ -[PNRODSchemaPNRODDimension setHasModelIdentifier:]
+ -[PNRODSchemaPNRODDimension setHasToolId:]
+ -[PNRODSchemaPNRODDimension setModelIdentifier:]
+ -[PNRODSchemaPNRODDimension setToolId:]
+ -[PNRODSchemaPNRODDimension toolId]
+ -[PNRODSchemaPNRODDimension writeTo:]
+ -[PNRODSchemaPNRODDimension(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODDimension(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODFailureInfo addErrors:]
+ -[PNRODSchemaPNRODFailureInfo clearErrors]
+ -[PNRODSchemaPNRODFailureInfo deleteErrors]
+ -[PNRODSchemaPNRODFailureInfo errorsAtIndex:]
+ -[PNRODSchemaPNRODFailureInfo errorsCount]
+ -[PNRODSchemaPNRODFailureInfo errors]
+ -[PNRODSchemaPNRODFailureInfo setErrors:]
+ -[PNRODSchemaPNRODMetricDuration deleteMetricsNameIndex]
+ -[PNRODSchemaPNRODMetricDuration hasMetricsNameIndex]
+ -[PNRODSchemaPNRODMetricDuration metricsNameIndex]
+ -[PNRODSchemaPNRODMetricDuration setHasMetricsNameIndex:]
+ -[PNRODSchemaPNRODMetricDuration setMetricsNameIndex:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims .cxx_destruct]
+ -[PNRODSchemaPnRODSiriMetricsAndDims componentIndex]
+ -[PNRODSchemaPnRODSiriMetricsAndDims componentInvocationId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteComponentIndex]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteComponentInvocationId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteDimensionValue]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteFailureInfo]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteMetricDuration]
+ -[PNRODSchemaPnRODSiriMetricsAndDims deleteTurnId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims dictionaryRepresentation]
+ -[PNRODSchemaPnRODSiriMetricsAndDims dimensionValue]
+ -[PNRODSchemaPnRODSiriMetricsAndDims failureInfo]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasComponentIndex]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasComponentInvocationId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasDimensionValue]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasFailureInfo]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasMetricDuration]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hasTurnId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims hash]
+ -[PNRODSchemaPnRODSiriMetricsAndDims initWithDictionary:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims initWithJSON:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims isEqual:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims jsonData]
+ -[PNRODSchemaPnRODSiriMetricsAndDims metricDuration]
+ -[PNRODSchemaPnRODSiriMetricsAndDims readFrom:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setComponentIndex:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setComponentInvocationId:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setDimensionValue:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setFailureInfo:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasComponentIndex:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasComponentInvocationId:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasDimensionValue:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasFailureInfo:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasMetricDuration:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setHasTurnId:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setMetricDuration:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims setTurnId:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims turnId]
+ -[PNRODSchemaPnRODSiriMetricsAndDims writeTo:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPnRODSiriMetricsAndDims(SensitiveConditions) suppressMessageUnderConditions]
+ -[RESOLVESchemaRESOLVEClientEventMetadata .cxx_destruct]
+ -[RESOLVESchemaRESOLVEClientEventMetadata deleteResolveId]
+ -[RESOLVESchemaRESOLVEClientEventMetadata dictionaryRepresentation]
+ -[RESOLVESchemaRESOLVEClientEventMetadata hasResolveId]
+ -[RESOLVESchemaRESOLVEClientEventMetadata hash]
+ -[RESOLVESchemaRESOLVEClientEventMetadata initWithDictionary:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata initWithJSON:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata isEqual:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata jsonData]
+ -[RESOLVESchemaRESOLVEClientEventMetadata readFrom:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata resolveId]
+ -[RESOLVESchemaRESOLVEClientEventMetadata setHasResolveId:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata setResolveId:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata writeTo:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[RESOLVESchemaRESOLVEClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[SADSchemaSADAssetBringUpState .cxx_destruct]
+ -[SADSchemaSADAssetBringUpState assetBringUpErrorCode]
+ -[SADSchemaSADAssetBringUpState assetBringUpErrorDescription]
+ -[SADSchemaSADAssetBringUpState assetBringUpErrorDomain]
+ -[SADSchemaSADAssetBringUpState assetBringUpState]
+ -[SADSchemaSADAssetBringUpState assetBringUpType]
+ -[SADSchemaSADAssetBringUpState assetSetIdentifier]
+ -[SADSchemaSADAssetBringUpState assetType]
+ -[SADSchemaSADAssetBringUpState countOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState countOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState countOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState countOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState countOfPSUSAssetsPromotedInCurrentOS]
+ -[SADSchemaSADAssetBringUpState currentBuildVersion]
+ -[SADSchemaSADAssetBringUpState deleteAssetBringUpErrorCode]
+ -[SADSchemaSADAssetBringUpState deleteAssetBringUpErrorDescription]
+ -[SADSchemaSADAssetBringUpState deleteAssetBringUpErrorDomain]
+ -[SADSchemaSADAssetBringUpState deleteAssetBringUpState]
+ -[SADSchemaSADAssetBringUpState deleteAssetBringUpType]
+ -[SADSchemaSADAssetBringUpState deleteAssetSetIdentifier]
+ -[SADSchemaSADAssetBringUpState deleteAssetType]
+ -[SADSchemaSADAssetBringUpState deleteCountOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteCountOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteCountOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteCountOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteCountOfPSUSAssetsPromotedInCurrentOS]
+ -[SADSchemaSADAssetBringUpState deleteCurrentBuildVersion]
+ -[SADSchemaSADAssetBringUpState deletePreviousBuildVersion]
+ -[SADSchemaSADAssetBringUpState deleteTimeInSecondsSinceSoftwareUpdate]
+ -[SADSchemaSADAssetBringUpState deleteTotalSizeOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteTotalSizeOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteTotalSizeOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState deleteTotalSizeOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState dictionaryRepresentation]
+ -[SADSchemaSADAssetBringUpState hasAssetBringUpErrorCode]
+ -[SADSchemaSADAssetBringUpState hasAssetBringUpErrorDescription]
+ -[SADSchemaSADAssetBringUpState hasAssetBringUpErrorDomain]
+ -[SADSchemaSADAssetBringUpState hasAssetBringUpState]
+ -[SADSchemaSADAssetBringUpState hasAssetBringUpType]
+ -[SADSchemaSADAssetBringUpState hasAssetSetIdentifier]
+ -[SADSchemaSADAssetBringUpState hasAssetType]
+ -[SADSchemaSADAssetBringUpState hasCountOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasCountOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasCountOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasCountOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasCountOfPSUSAssetsPromotedInCurrentOS]
+ -[SADSchemaSADAssetBringUpState hasCurrentBuildVersion]
+ -[SADSchemaSADAssetBringUpState hasPreviousBuildVersion]
+ -[SADSchemaSADAssetBringUpState hasTimeInSecondsSinceSoftwareUpdate]
+ -[SADSchemaSADAssetBringUpState hasTotalSizeOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasTotalSizeOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasTotalSizeOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hasTotalSizeOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState hash]
+ -[SADSchemaSADAssetBringUpState initWithDictionary:]
+ -[SADSchemaSADAssetBringUpState initWithJSON:]
+ -[SADSchemaSADAssetBringUpState isEqual:]
+ -[SADSchemaSADAssetBringUpState jsonData]
+ -[SADSchemaSADAssetBringUpState previousBuildVersion]
+ -[SADSchemaSADAssetBringUpState readFrom:]
+ -[SADSchemaSADAssetBringUpState setAssetBringUpErrorCode:]
+ -[SADSchemaSADAssetBringUpState setAssetBringUpErrorDescription:]
+ -[SADSchemaSADAssetBringUpState setAssetBringUpErrorDomain:]
+ -[SADSchemaSADAssetBringUpState setAssetBringUpState:]
+ -[SADSchemaSADAssetBringUpState setAssetBringUpType:]
+ -[SADSchemaSADAssetBringUpState setAssetSetIdentifier:]
+ -[SADSchemaSADAssetBringUpState setAssetType:]
+ -[SADSchemaSADAssetBringUpState setCountOfAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setCountOfFactoryAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setCountOfOTAAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setCountOfPSUSAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setCountOfPSUSAssetsPromotedInCurrentOS:]
+ -[SADSchemaSADAssetBringUpState setCurrentBuildVersion:]
+ -[SADSchemaSADAssetBringUpState setHasAssetBringUpErrorCode:]
+ -[SADSchemaSADAssetBringUpState setHasAssetBringUpErrorDescription:]
+ -[SADSchemaSADAssetBringUpState setHasAssetBringUpErrorDomain:]
+ -[SADSchemaSADAssetBringUpState setHasAssetBringUpState:]
+ -[SADSchemaSADAssetBringUpState setHasAssetBringUpType:]
+ -[SADSchemaSADAssetBringUpState setHasAssetSetIdentifier:]
+ -[SADSchemaSADAssetBringUpState setHasAssetType:]
+ -[SADSchemaSADAssetBringUpState setHasCountOfAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasCountOfFactoryAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasCountOfOTAAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasCountOfPSUSAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasCountOfPSUSAssetsPromotedInCurrentOS:]
+ -[SADSchemaSADAssetBringUpState setHasCurrentBuildVersion:]
+ -[SADSchemaSADAssetBringUpState setHasPreviousBuildVersion:]
+ -[SADSchemaSADAssetBringUpState setHasTimeInSecondsSinceSoftwareUpdate:]
+ -[SADSchemaSADAssetBringUpState setHasTotalSizeOfAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasTotalSizeOfFactoryAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasTotalSizeOfOTAAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setHasTotalSizeOfPSUSAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setPreviousBuildVersion:]
+ -[SADSchemaSADAssetBringUpState setTimeInSecondsSinceSoftwareUpdate:]
+ -[SADSchemaSADAssetBringUpState setTotalSizeOfAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setTotalSizeOfFactoryAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setTotalSizeOfOTAAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState setTotalSizeOfPSUSAssetsInAssetSet:]
+ -[SADSchemaSADAssetBringUpState timeInSecondsSinceSoftwareUpdate]
+ -[SADSchemaSADAssetBringUpState totalSizeOfAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState totalSizeOfFactoryAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState totalSizeOfOTAAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState totalSizeOfPSUSAssetsInAssetSet]
+ -[SADSchemaSADAssetBringUpState writeTo:]
+ -[SADSchemaSADAssetBringUpState(SensitiveConditions) suppressMessageUnderConditions]
+ -[SADSchemaSADClientEvent assetBringUpState]
+ -[SADSchemaSADClientEvent deleteAssetBringUpState]
+ -[SADSchemaSADClientEvent hasAssetBringUpState]
+ -[SADSchemaSADClientEvent setAssetBringUpState:]
+ -[SADSchemaSADClientEvent setHasAssetBringUpState:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus deleteTotalNumberOfBytesDownloaded]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus hasTotalNumberOfBytesDownloaded]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setHasTotalNumberOfBytesDownloaded:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus setTotalNumberOfBytesDownloaded:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus totalNumberOfBytesDownloaded]
+ -[SISchemaErrorInfo .cxx_destruct]
+ -[SISchemaErrorInfo code]
+ -[SISchemaErrorInfo deleteCode]
+ -[SISchemaErrorInfo deleteDomain]
+ -[SISchemaErrorInfo dictionaryRepresentation]
+ -[SISchemaErrorInfo domain]
+ -[SISchemaErrorInfo hasCode]
+ -[SISchemaErrorInfo hasDomain]
+ -[SISchemaErrorInfo hash]
+ -[SISchemaErrorInfo initWithDictionary:]
+ -[SISchemaErrorInfo initWithJSON:]
+ -[SISchemaErrorInfo isEqual:]
+ -[SISchemaErrorInfo jsonData]
+ -[SISchemaErrorInfo readFrom:]
+ -[SISchemaErrorInfo setCode:]
+ -[SISchemaErrorInfo setDomain:]
+ -[SISchemaErrorInfo setHasCode:]
+ -[SISchemaErrorInfo setHasDomain:]
+ -[SISchemaErrorInfo writeTo:]
+ -[SISchemaErrorInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaFreeFormText .cxx_destruct]
+ -[SISchemaFreeFormText deleteExplainabilityIdentifier]
+ -[SISchemaFreeFormText deleteText]
+ -[SISchemaFreeFormText dictionaryRepresentation]
+ -[SISchemaFreeFormText explainabilityIdentifier]
+ -[SISchemaFreeFormText hasExplainabilityIdentifier]
+ -[SISchemaFreeFormText hasText]
+ -[SISchemaFreeFormText hash]
+ -[SISchemaFreeFormText initWithDictionary:]
+ -[SISchemaFreeFormText initWithJSON:]
+ -[SISchemaFreeFormText isEqual:]
+ -[SISchemaFreeFormText jsonData]
+ -[SISchemaFreeFormText readFrom:]
+ -[SISchemaFreeFormText setExplainabilityIdentifier:]
+ -[SISchemaFreeFormText setHasExplainabilityIdentifier:]
+ -[SISchemaFreeFormText setHasText:]
+ -[SISchemaFreeFormText setText:]
+ -[SISchemaFreeFormText text]
+ -[SISchemaFreeFormText writeTo:]
+ -[SISchemaFreeFormText(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SISchemaFreeFormText(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaUEISiriWasUnavailable addSiriUnavailabilityReasons:]
+ -[SISchemaUEISiriWasUnavailable clearSiriUnavailabilityReasons]
+ -[SISchemaUEISiriWasUnavailable deleteOrchestrationMode]
+ -[SISchemaUEISiriWasUnavailable deleteSiriUnavailabilityReasons]
+ -[SISchemaUEISiriWasUnavailable hasOrchestrationMode]
+ -[SISchemaUEISiriWasUnavailable orchestrationMode]
+ -[SISchemaUEISiriWasUnavailable setHasOrchestrationMode:]
+ -[SISchemaUEISiriWasUnavailable setOrchestrationMode:]
+ -[SISchemaUEISiriWasUnavailable setSiriUnavailabilityReasons:]
+ -[SISchemaUEISiriWasUnavailable siriUnavailabilityReasonsAtIndex:]
+ -[SISchemaUEISiriWasUnavailable siriUnavailabilityReasonsCount]
+ -[SISchemaUEISiriWasUnavailable siriUnavailabilityReasons]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata .cxx_destruct]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata deleteIfRequestId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata deleteSkimmerId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata dictionaryRepresentation]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata hasIfRequestId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata hasSkimmerId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata hash]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata ifRequestId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata initWithDictionary:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata initWithJSON:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata isEqual:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata jsonData]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata readFrom:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata setHasIfRequestId:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata setHasSkimmerId:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata setIfRequestId:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata setSkimmerId:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata skimmerId]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata writeTo:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SKIMMERSchemaSKIMMERClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[STSchemaSTGlobalSearchResult .cxx_destruct]
+ -[STSchemaSTGlobalSearchResult deletePegasusDomain]
+ -[STSchemaSTGlobalSearchResult hasPegasusDomain]
+ -[STSchemaSTGlobalSearchResult pegasusDomain]
+ -[STSchemaSTGlobalSearchResult setHasPegasusDomain:]
+ -[STSchemaSTGlobalSearchResult setPegasusDomain:]
+ -[TMSSchemaTMSClientEventMetadata .cxx_destruct]
+ -[TMSSchemaTMSClientEventMetadata deleteTrpId]
+ -[TMSSchemaTMSClientEventMetadata dictionaryRepresentation]
+ -[TMSSchemaTMSClientEventMetadata hasTrpId]
+ -[TMSSchemaTMSClientEventMetadata hash]
+ -[TMSSchemaTMSClientEventMetadata initWithDictionary:]
+ -[TMSSchemaTMSClientEventMetadata initWithJSON:]
+ -[TMSSchemaTMSClientEventMetadata isEqual:]
+ -[TMSSchemaTMSClientEventMetadata jsonData]
+ -[TMSSchemaTMSClientEventMetadata readFrom:]
+ -[TMSSchemaTMSClientEventMetadata setHasTrpId:]
+ -[TMSSchemaTMSClientEventMetadata setTrpId:]
+ -[TMSSchemaTMSClientEventMetadata trpId]
+ -[TMSSchemaTMSClientEventMetadata writeTo:]
+ -[TMSSchemaTMSClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[TMSSchemaTMSClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[TTSSchemaTTSRequestReceivedTier1 deleteTextToSpeak]
+ -[TTSSchemaTTSRequestReceivedTier1 hasTextToSpeak]
+ -[TTSSchemaTTSRequestReceivedTier1 setHasTextToSpeak:]
+ -[TTSSchemaTTSRequestReceivedTier1 setTextToSpeak:]
+ -[TTSSchemaTTSRequestReceivedTier1 textToSpeak]
+ -[TTSSchemaTTSSpeechEnded addErrors:]
+ -[TTSSchemaTTSSpeechEnded clearErrors]
+ -[TTSSchemaTTSSpeechEnded deleteErrors]
+ -[TTSSchemaTTSSpeechEnded errorsAtIndex:]
+ -[TTSSchemaTTSSpeechEnded errorsCount]
+ -[TTSSchemaTTSSpeechEnded errors]
+ -[TTSSchemaTTSSpeechEnded setErrors:]
+ -[TTSSchemaTTSSpeechEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[TTSSchemaTTSSpeechFailed addErrors:]
+ -[TTSSchemaTTSSpeechFailed clearErrors]
+ -[TTSSchemaTTSSpeechFailed deleteErrors]
+ -[TTSSchemaTTSSpeechFailed errorsAtIndex:]
+ -[TTSSchemaTTSSpeechFailed errorsCount]
+ -[TTSSchemaTTSSpeechFailed errors]
+ -[TTSSchemaTTSSpeechFailed setErrors:]
+ -[TTSSchemaTTSSpeechFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[TTSSchemaTTSSpeechStarted deleteTextToSpeak]
+ -[TTSSchemaTTSSpeechStarted hasTextToSpeak]
+ -[TTSSchemaTTSSpeechStarted setHasTextToSpeak:]
+ -[TTSSchemaTTSSpeechStarted setTextToSpeak:]
+ -[TTSSchemaTTSSpeechStarted textToSpeak]
+ -[TTSSchemaTTSSynthesisStarted deleteTextToSpeak]
+ -[TTSSchemaTTSSynthesisStarted hasTextToSpeak]
+ -[TTSSchemaTTSSynthesisStarted setHasTextToSpeak:]
+ -[TTSSchemaTTSSynthesisStarted setTextToSpeak:]
+ -[TTSSchemaTTSSynthesisStarted textToSpeak]
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._entityMetrics
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric._entityCategory
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric._numEntities
+ OBJC_IVAR_$_DUSchemaDUEvent._speechDatasetsRecord
+ OBJC_IVAR_$_DUSchemaDUSpeechDatasetsRecord._datasetsCapturedTimestampMs
+ OBJC_IVAR_$_DUSchemaDUSpeechDatasetsRecord._has
+ OBJC_IVAR_$_DUSchemaDUSpeechDatasetsRecord._interactionId
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallEnded._executorAppIntentMetrics
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallEnded._result
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallFailed._errorKind
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallFailed._errors
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._connectionDurationInNanoSeconds
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._executorAppIntentSegments
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._executorAppIntentTargetType
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._isAppBroughtToForeground
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._isProcessLaunchRequired
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentMetrics._startedLiveActivity
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._executorAppIntentAttribution
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._executorAppIntentTask
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._machTimeEnd
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._machTimeStart
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._requestUUID
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._sessionUUID
+ OBJC_IVAR_$_GATSchemaGATRequestEnded._has
+ OBJC_IVAR_$_IFPlatformRequestSchemaIFPlatformRequestClientEvent._ifPlatformRequestStructuredError
+ OBJC_IVAR_$_IFPlatformRequestSchemaIFPlatformRequestStructuredError._errors
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals._isModelConfirmation
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals._isModelDisambiguation
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals._modelSelectedOptions
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals._modelVersion
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._isModelConfirmation
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._isModelDisambiguation
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._modelSelectedOptions
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._modelVersionStr
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._userPersona
+ OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._classifiedString
+ OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._explainabilityIdentifiers
+ OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._has
+ OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._isRedacted
+ OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._metadata
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._general
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._has
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._kind
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._onDevice
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._partOfARequest
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._sensor
+ OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._tool
+ OBJC_IVAR_$_LRSchemaLRRedactionSummaryReported._dataClassificationManifests
+ OBJC_IVAR_$_MTSchemaMTFrameworkRequestSent._modelVersion
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetBringUpErrorCode
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetBringUpErrorDescription
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetBringUpErrorDomain
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetBringUpState
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetBringUpType
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetSetIdentifier
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._assetSetName
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._countOfAssetsInAssetSet
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._countOfPSUSAssetsPromotedInCurrentOS
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._previousBuildVersion
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._timeInSecondsSinceSoftwareUpdate
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._totalSizeOfAssetsInAssetSet
+ OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._uafAssetSource
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._isAmbiguousRequest
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._isGenAIAware
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._isSuitableForGenAI
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesCounts._neuralFallbackCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesCounts._turnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesCounts._vocalizerFallbackCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._tuples
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._assistantDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._clientId
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._errorCodes
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._synthesisSource
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._ttsStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._voiceName
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._voiceType
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesTuples._autoMOSs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesTuples._customerPerceivedLatencyInSecs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesTuples._speakingDurationInSecs
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._acousticMitigatorAcceptPostAcousticMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._contextualMitigatorAcceptPostContextualMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._estimatedSiriMissCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithAcousticMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithContextualMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._falseWakeWithLwSpkidMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._hasMultiKeyboards
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._lwSpkidMitigatorAcceptPostLwSpkidMitigationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._nearMissCheckerScoreLists
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._nearMissPitchLists
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._nearMissSNRLists
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._nearMissWithRetryLists
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._nearMissWithTriggerPhraseLists
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._phsRejectCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._secondPassAcceptCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._secondPassRejectCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAttentionInvocationCounts._siriActivationCount
+ OBJC_IVAR_$_ODDSiriSchemaODDExecutionMetadataReported._scheduleType
+ OBJC_IVAR_$_ODDSiriSchemaODDIntelligenceFeatureReportingAvailabilityStatus._totalNumberOfBytesDownloaded
+ OBJC_IVAR_$_ODDSiriSchemaODDRequestsWithoutAssetsDimensions._orchMode
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assetBringUpDigestsReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assistantVoicesDigestsReported
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._voiceName
+ OBJC_IVAR_$_ORCHSchemaORCHRequestFailed._error
+ OBJC_IVAR_$_PNRODSchemaPNRODClientEvent._pnrodSiriMetricsAndDims
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._dimensionNameIndex
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._dimensionValueBoolean
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._dimensionValueFloat
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._dimensionValueInteger
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._has
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._modelIdentifier
+ OBJC_IVAR_$_PNRODSchemaPNRODDimension._toolId
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._errors
+ OBJC_IVAR_$_PNRODSchemaPNRODMetricDuration._metricsNameIndex
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._componentIndex
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._componentInvocationId
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._dimensionValue
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._has
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._metricDuration
+ OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._turnId
+ OBJC_IVAR_$_RESOLVESchemaRESOLVEClientEventMetadata._resolveId
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetBringUpErrorCode
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetBringUpErrorDescription
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetBringUpErrorDomain
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetBringUpState
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetBringUpType
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetSetIdentifier
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._assetType
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._countOfAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._countOfFactoryAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._countOfOTAAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._countOfPSUSAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._countOfPSUSAssetsPromotedInCurrentOS
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._currentBuildVersion
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._has
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._previousBuildVersion
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._timeInSecondsSinceSoftwareUpdate
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._totalSizeOfAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._totalSizeOfFactoryAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._totalSizeOfOTAAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADAssetBringUpState._totalSizeOfPSUSAssetsInAssetSet
+ OBJC_IVAR_$_SADSchemaSADClientEvent._assetBringUpState
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityDetailedStatus._totalNumberOfBytesDownloaded
+ OBJC_IVAR_$_SISchemaErrorInfo._code
+ OBJC_IVAR_$_SISchemaErrorInfo._domain
+ OBJC_IVAR_$_SISchemaErrorInfo._has
+ OBJC_IVAR_$_SISchemaFreeFormText._explainabilityIdentifier
+ OBJC_IVAR_$_SISchemaFreeFormText._text
+ OBJC_IVAR_$_SISchemaUEISiriWasUnavailable._orchestrationMode
+ OBJC_IVAR_$_SISchemaUEISiriWasUnavailable._siriUnavailabilityReasons
+ OBJC_IVAR_$_SKIMMERSchemaSKIMMERClientEventMetadata._ifRequestId
+ OBJC_IVAR_$_SKIMMERSchemaSKIMMERClientEventMetadata._skimmerId
+ OBJC_IVAR_$_STSchemaSTGlobalSearchRequestEnded._has
+ OBJC_IVAR_$_STSchemaSTGlobalSearchResult._pegasusDomain
+ OBJC_IVAR_$_STSchemaSTSpotlightRequestEnded._has
+ OBJC_IVAR_$_TMSSchemaTMSClientEventMetadata._trpId
+ OBJC_IVAR_$_TTSSchemaTTSRequestReceivedTier1._textToSpeak
+ OBJC_IVAR_$_TTSSchemaTTSSpeechEnded._errors
+ OBJC_IVAR_$_TTSSchemaTTSSpeechFailed._errors
+ OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._textToSpeak
+ OBJC_IVAR_$_TTSSchemaTTSSynthesisStarted._textToSpeak
+ _ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetricReadFrom
+ _DUSchemaDUSpeechDatasetsRecordReadFrom
+ _ExecutorSiriSchemaExecutorAppIntentMetricsReadFrom
+ _ExecutorSiriSchemaExecutorAppIntentSegmentReadFrom
+ _IFPlatformRequestSchemaIFPlatformRequestStructuredErrorReadFrom
+ _LRSchemaLRDataClassificationManifestReadFrom
+ _LRSchemaLRDataClassificationMetadataReadFrom
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ _OBJC_CLASS_$_DUSchemaDUSpeechDatasetsRecord
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorAppIntentMetrics
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorAppIntentSegment
+ _OBJC_CLASS_$_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ _OBJC_CLASS_$_LRSchemaLRDataClassificationManifest
+ _OBJC_CLASS_$_LRSchemaLRDataClassificationMetadata
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssetBringUpDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssetBringUpStatus
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantVoicesCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantVoicesDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantVoicesDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantVoicesTuples
+ _OBJC_CLASS_$_PNRODSchemaPNRODDimension
+ _OBJC_CLASS_$_PNRODSchemaPnRODSiriMetricsAndDims
+ _OBJC_CLASS_$_RESOLVESchemaRESOLVEClientEventMetadata
+ _OBJC_CLASS_$_SADSchemaSADAssetBringUpState
+ _OBJC_CLASS_$_SISchemaErrorInfo
+ _OBJC_CLASS_$_SISchemaFreeFormText
+ _OBJC_CLASS_$_SKIMMERSchemaSKIMMERClientEventMetadata
+ _OBJC_CLASS_$_TMSSchemaTMSClientEventMetadata
+ _OBJC_IVAR_$_DUSchemaDUEvent._hasSpeechDatasetsRecord
+ _OBJC_IVAR_$_DUSchemaDUSpeechDatasetsRecord._hasInteractionId
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallEnded._hasExecutorAppIntentMetrics
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._hasRequestUUID
+ _OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentSegment._hasSessionUUID
+ _OBJC_IVAR_$_IFPlatformRequestSchemaIFPlatformRequestClientEvent._hasIfPlatformRequestStructuredError
+ _OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppIndependentSignals._hasModelVersion
+ _OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._hasModelVersionStr
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._hasClassifiedString
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationManifest._hasMetadata
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._hasGeneral
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._hasOnDevice
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._hasSensor
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._hasTool
+ _OBJC_IVAR_$_LRSchemaLRDataClassificationMetadata._whichProvenance_Type
+ _OBJC_IVAR_$_MTSchemaMTFrameworkRequestSent._hasModelVersion
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._hasAssetBringUpErrorDescription
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._hasAssetBringUpErrorDomain
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._hasAssetSetIdentifier
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._hasAssetSetName
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssetBringUpStatus._hasPreviousBuildVersion
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesCounts._hasTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigest._hasTuples
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._hasAssistantDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantVoicesDimensions._hasVoiceName
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssetBringUpDigestsReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssistantVoicesDigestsReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._hasVoiceName
+ _OBJC_IVAR_$_ORCHSchemaORCHRequestFailed._hasError
+ _OBJC_IVAR_$_PNRODSchemaPNRODClientEvent._hasPnrodSiriMetricsAndDims
+ _OBJC_IVAR_$_PNRODSchemaPNRODDimension._hasModelIdentifier
+ _OBJC_IVAR_$_PNRODSchemaPNRODDimension._hasToolId
+ _OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._hasComponentInvocationId
+ _OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._hasDimensionValue
+ _OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._hasFailureInfo
+ _OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._hasMetricDuration
+ _OBJC_IVAR_$_PNRODSchemaPnRODSiriMetricsAndDims._hasTurnId
+ _OBJC_IVAR_$_RESOLVESchemaRESOLVEClientEventMetadata._hasResolveId
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasAssetBringUpErrorDescription
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasAssetBringUpErrorDomain
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasAssetSetIdentifier
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasAssetType
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasCurrentBuildVersion
+ _OBJC_IVAR_$_SADSchemaSADAssetBringUpState._hasPreviousBuildVersion
+ _OBJC_IVAR_$_SADSchemaSADClientEvent._hasAssetBringUpState
+ _OBJC_IVAR_$_SISchemaErrorInfo._hasDomain
+ _OBJC_IVAR_$_SISchemaFreeFormText._hasExplainabilityIdentifier
+ _OBJC_IVAR_$_SISchemaFreeFormText._hasText
+ _OBJC_IVAR_$_SKIMMERSchemaSKIMMERClientEventMetadata._hasIfRequestId
+ _OBJC_IVAR_$_SKIMMERSchemaSKIMMERClientEventMetadata._hasSkimmerId
+ _OBJC_IVAR_$_STSchemaSTGlobalSearchResult._hasPegasusDomain
+ _OBJC_IVAR_$_TMSSchemaTMSClientEventMetadata._hasTrpId
+ _OBJC_IVAR_$_TTSSchemaTTSRequestReceivedTier1._hasTextToSpeak
+ _OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._hasTextToSpeak
+ _OBJC_IVAR_$_TTSSchemaTTSSynthesisStarted._hasTextToSpeak
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ _OBJC_METACLASS_$_DUSchemaDUSpeechDatasetsRecord
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorAppIntentMetrics
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorAppIntentSegment
+ _OBJC_METACLASS_$_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ _OBJC_METACLASS_$_LRSchemaLRDataClassificationManifest
+ _OBJC_METACLASS_$_LRSchemaLRDataClassificationMetadata
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssetBringUpDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssetBringUpStatus
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantVoicesCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantVoicesDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantVoicesDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantVoicesTuples
+ _OBJC_METACLASS_$_PNRODSchemaPNRODDimension
+ _OBJC_METACLASS_$_PNRODSchemaPnRODSiriMetricsAndDims
+ _OBJC_METACLASS_$_RESOLVESchemaRESOLVEClientEventMetadata
+ _OBJC_METACLASS_$_SADSchemaSADAssetBringUpState
+ _OBJC_METACLASS_$_SISchemaErrorInfo
+ _OBJC_METACLASS_$_SISchemaFreeFormText
+ _OBJC_METACLASS_$_SKIMMERSchemaSKIMMERClientEventMetadata
+ _OBJC_METACLASS_$_TMSSchemaTMSClientEventMetadata
+ _ODDSiriSchemaODDAssetBringUpDigestsReportedReadFrom
+ _ODDSiriSchemaODDAssetBringUpStatusReadFrom
+ _ODDSiriSchemaODDAssistantVoicesCountsReadFrom
+ _ODDSiriSchemaODDAssistantVoicesDigestReadFrom
+ _ODDSiriSchemaODDAssistantVoicesDigestsReportedReadFrom
+ _ODDSiriSchemaODDAssistantVoicesDimensionsReadFrom
+ _ODDSiriSchemaODDAssistantVoicesTuplesReadFrom
+ _PNRODSchemaPNRODDimensionReadFrom
+ _PNRODSchemaPnRODSiriMetricsAndDimsReadFrom
+ _RESOLVESchemaRESOLVEClientEventMetadataReadFrom
+ _SADSchemaSADAssetBringUpStateReadFrom
+ _SISchemaErrorInfoReadFrom
+ _SISchemaFreeFormTextReadFrom
+ _SKIMMERSchemaSKIMMERClientEventMetadataReadFrom
+ _TMSSchemaTMSClientEventMetadataReadFrom
+ __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DUSchemaDUSpeechDatasetsRecord(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorAppIntentMetrics(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorAppIntentSegment(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFPlatformRequestSchemaIFPlatformRequestStructuredError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_LRSchemaLRDataClassificationManifest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_LRSchemaLRDataClassificationMetadata(SiriInstrumentation|SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssetBringUpDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssetBringUpStatus(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantVoicesCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantVoicesDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantVoicesDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantVoicesDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantVoicesTuples(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODDimension(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPnRODSiriMetricsAndDims(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_RESOLVESchemaRESOLVEClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SADSchemaSADAssetBringUpState(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Mapping|SensitiveConditions|Factory|Introspection|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(SensitiveConditions|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(SensitiveConditions|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaErrorInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaFreeFormText(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaInstrumentationMessage(SensitiveConditions|Introspection|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaOrderedAnyEvent(InstrumentationAdditions|SensitiveConditions|Introspection)
+ __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
+ __OBJC_$_INSTANCE_METHODS_SISchemaUUID(SensitiveConditions|Extensions|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SKIMMERSchemaSKIMMERClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_TMSSchemaTMSClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ __OBJC_$_INSTANCE_VARIABLES_DUSchemaDUSpeechDatasetsRecord
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorAppIntentMetrics
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorAppIntentSegment
+ __OBJC_$_INSTANCE_VARIABLES_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ __OBJC_$_INSTANCE_VARIABLES_LRSchemaLRDataClassificationManifest
+ __OBJC_$_INSTANCE_VARIABLES_LRSchemaLRDataClassificationMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssetBringUpDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssetBringUpStatus
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantVoicesCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantVoicesDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantVoicesDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantVoicesTuples
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODDimension
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPnRODSiriMetricsAndDims
+ __OBJC_$_INSTANCE_VARIABLES_RESOLVESchemaRESOLVEClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_SADSchemaSADAssetBringUpState
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaErrorInfo
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaFreeFormText
+ __OBJC_$_INSTANCE_VARIABLES_SKIMMERSchemaSKIMMERClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_TMSSchemaTMSClientEventMetadata
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ __OBJC_$_PROP_LIST_DUSchemaDUSpeechDatasetsRecord
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorAppIntentMetrics
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorAppIntentSegment
+ __OBJC_$_PROP_LIST_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ __OBJC_$_PROP_LIST_LRSchemaLRDataClassificationManifest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssetBringUpDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssetBringUpStatus
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantVoicesCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantVoicesDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantVoicesDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantVoicesTuples
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODDimension
+ __OBJC_$_PROP_LIST_PNRODSchemaPnRODSiriMetricsAndDims
+ __OBJC_$_PROP_LIST_RESOLVESchemaRESOLVEClientEventMetadata
+ __OBJC_$_PROP_LIST_SADSchemaSADAssetBringUpState
+ __OBJC_$_PROP_LIST_SISchemaErrorInfo
+ __OBJC_$_PROP_LIST_SISchemaFreeFormText
+ __OBJC_$_PROP_LIST_SKIMMERSchemaSKIMMERClientEventMetadata
+ __OBJC_$_PROP_LIST_TMSSchemaTMSClientEventMetadata
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ __OBJC_CLASS_RO_$_DUSchemaDUSpeechDatasetsRecord
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorAppIntentMetrics
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorAppIntentSegment
+ __OBJC_CLASS_RO_$_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ __OBJC_CLASS_RO_$_LRSchemaLRDataClassificationManifest
+ __OBJC_CLASS_RO_$_LRSchemaLRDataClassificationMetadata
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssetBringUpDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssetBringUpStatus
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantVoicesCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantVoicesTuples
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODDimension
+ __OBJC_CLASS_RO_$_PNRODSchemaPnRODSiriMetricsAndDims
+ __OBJC_CLASS_RO_$_RESOLVESchemaRESOLVEClientEventMetadata
+ __OBJC_CLASS_RO_$_SADSchemaSADAssetBringUpState
+ __OBJC_CLASS_RO_$_SISchemaErrorInfo
+ __OBJC_CLASS_RO_$_SISchemaFreeFormText
+ __OBJC_CLASS_RO_$_SKIMMERSchemaSKIMMERClientEventMetadata
+ __OBJC_CLASS_RO_$_TMSSchemaTMSClientEventMetadata
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric
+ __OBJC_METACLASS_RO_$_DUSchemaDUSpeechDatasetsRecord
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorAppIntentMetrics
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorAppIntentSegment
+ __OBJC_METACLASS_RO_$_IFPlatformRequestSchemaIFPlatformRequestStructuredError
+ __OBJC_METACLASS_RO_$_LRSchemaLRDataClassificationManifest
+ __OBJC_METACLASS_RO_$_LRSchemaLRDataClassificationMetadata
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssetBringUpDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssetBringUpStatus
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantVoicesCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantVoicesDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantVoicesTuples
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODDimension
+ __OBJC_METACLASS_RO_$_PNRODSchemaPnRODSiriMetricsAndDims
+ __OBJC_METACLASS_RO_$_RESOLVESchemaRESOLVEClientEventMetadata
+ __OBJC_METACLASS_RO_$_SADSchemaSADAssetBringUpState
+ __OBJC_METACLASS_RO_$_SISchemaErrorInfo
+ __OBJC_METACLASS_RO_$_SISchemaFreeFormText
+ __OBJC_METACLASS_RO_$_SKIMMERSchemaSKIMMERClientEventMetadata
+ __OBJC_METACLASS_RO_$_TMSSchemaTMSClientEventMetadata
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _objc_msgSend$acousticMitigatorAcceptPostAcousticMitigationCount
+ _objc_msgSend$addAutoMOS:
+ _objc_msgSend$addCustomerPerceivedLatencyInSec:
+ _objc_msgSend$addDataClassificationManifests:
+ _objc_msgSend$addEntityMetrics:
+ _objc_msgSend$addErrors:
+ _objc_msgSend$addExecutorAppIntentSegments:
+ _objc_msgSend$addExplainabilityIdentifiers:
+ _objc_msgSend$addModelSelectedOptions:
+ _objc_msgSend$addNearMissCheckerScoreList:
+ _objc_msgSend$addNearMissPitchList:
+ _objc_msgSend$addNearMissSNRList:
+ _objc_msgSend$addNearMissWithRetryList:
+ _objc_msgSend$addNearMissWithTriggerPhraseList:
+ _objc_msgSend$addSiriUnavailabilityReasons:
+ _objc_msgSend$addSpeakingDurationInSec:
+ _objc_msgSend$assetBringUpDigestsReported
+ _objc_msgSend$assetBringUpErrorCode
+ _objc_msgSend$assetBringUpErrorDescription
+ _objc_msgSend$assetBringUpErrorDomain
+ _objc_msgSend$assetBringUpState
+ _objc_msgSend$assetBringUpType
+ _objc_msgSend$assetSetIdentifier
+ _objc_msgSend$assistantVoicesDigestsReported
+ _objc_msgSend$autoMOSs
+ _objc_msgSend$classifiedString
+ _objc_msgSend$clearAutoMOS
+ _objc_msgSend$clearCustomerPerceivedLatencyInSec
+ _objc_msgSend$clearDataClassificationManifests
+ _objc_msgSend$clearEntityMetrics
+ _objc_msgSend$clearErrors
+ _objc_msgSend$clearExecutorAppIntentSegments
+ _objc_msgSend$clearExplainabilityIdentifiers
+ _objc_msgSend$clearModelSelectedOptions
+ _objc_msgSend$clearNearMissCheckerScoreList
+ _objc_msgSend$clearNearMissPitchList
+ _objc_msgSend$clearNearMissSNRList
+ _objc_msgSend$clearNearMissWithRetryList
+ _objc_msgSend$clearNearMissWithTriggerPhraseList
+ _objc_msgSend$clearSiriUnavailabilityReasons
+ _objc_msgSend$clearSpeakingDurationInSec
+ _objc_msgSend$componentInvocationId
+ _objc_msgSend$connectionDurationInNanoSeconds
+ _objc_msgSend$contextualMitigatorAcceptPostContextualMitigationCount
+ _objc_msgSend$countOfAssetsInAssetSet
+ _objc_msgSend$countOfFactoryAssetsInAssetSet
+ _objc_msgSend$countOfOTAAssetsInAssetSet
+ _objc_msgSend$countOfPSUSAssetsInAssetSet
+ _objc_msgSend$countOfPSUSAssetsPromotedInCurrentOS
+ _objc_msgSend$currentBuildVersion
+ _objc_msgSend$customerPerceivedLatencyInSecs
+ _objc_msgSend$dataClassificationManifests
+ _objc_msgSend$datasetsCapturedTimestampMs
+ _objc_msgSend$decodeDataObject
+ _objc_msgSend$deleteActiveExperiments
+ _objc_msgSend$deleteAllocation
+ _objc_msgSend$deleteAllocations
+ _objc_msgSend$deleteAnyEventPayload
+ _objc_msgSend$deleteAssetBringUpDigestsReported
+ _objc_msgSend$deleteAssetBringUpState
+ _objc_msgSend$deleteAssistantVoicesDigestsReported
+ _objc_msgSend$deleteComponentInvocationId
+ _objc_msgSend$deleteCounterfactualAllocation
+ _objc_msgSend$deleteDimensionValue
+ _objc_msgSend$deleteExecutorAppIntentMetrics
+ _objc_msgSend$deleteExplainabilityIdentifier
+ _objc_msgSend$deleteIfPlatformRequestStructuredError
+ _objc_msgSend$deleteMetricDuration
+ _objc_msgSend$deletePnrodSiriMetricsAndDims
+ _objc_msgSend$deleteRequestUUID
+ _objc_msgSend$deleteResolveId
+ _objc_msgSend$deleteRollouts
+ _objc_msgSend$deleteSessionUUID
+ _objc_msgSend$deleteSkimmerId
+ _objc_msgSend$deleteSpeechDatasetsRecord
+ _objc_msgSend$deleteTextToSpeak
+ _objc_msgSend$dimensionNameIndex
+ _objc_msgSend$dimensionValue
+ _objc_msgSend$dimensionValueBoolean
+ _objc_msgSend$dimensionValueFloat
+ _objc_msgSend$dimensionValueInteger
+ _objc_msgSend$entityMetrics
+ _objc_msgSend$errorKind
+ _objc_msgSend$errors
+ _objc_msgSend$estimatedSiriMissCount
+ _objc_msgSend$executorAppIntentAttribution
+ _objc_msgSend$executorAppIntentMetrics
+ _objc_msgSend$executorAppIntentSegments
+ _objc_msgSend$executorAppIntentTargetType
+ _objc_msgSend$executorAppIntentTask
+ _objc_msgSend$explainabilityIdentifier
+ _objc_msgSend$explainabilityIdentifiers
+ _objc_msgSend$falseWakeWithAcousticMitigationCount
+ _objc_msgSend$falseWakeWithContextualMitigationCount
+ _objc_msgSend$falseWakeWithLwSpkidMitigationCount
+ _objc_msgSend$formattedJsonBody
+ _objc_msgSend$getEventType
+ _objc_msgSend$hasMultiKeyboards
+ _objc_msgSend$ifPlatformRequestStructuredError
+ _objc_msgSend$init
+ _objc_msgSend$initWithNSUUID:
+ _objc_msgSend$initWithTimestamp:messageUUID:topLevelUnionType:
+ _objc_msgSend$innerEvent
+ _objc_msgSend$isAmbiguousRequest
+ _objc_msgSend$isAppBroughtToForeground
+ _objc_msgSend$isGenAIAware
+ _objc_msgSend$isProcessLaunchRequired
+ _objc_msgSend$isRedacted
+ _objc_msgSend$isSuitableForGenAI
+ _objc_msgSend$lwSpkidMitigatorAcceptPostLwSpkidMitigationCount
+ _objc_msgSend$machTimeEnd
+ _objc_msgSend$machTimeStart
+ _objc_msgSend$metricDuration
+ _objc_msgSend$metricsNameIndex
+ _objc_msgSend$modelSelectedOptions
+ _objc_msgSend$modelVersionStr
+ _objc_msgSend$nearMissCheckerScoreLists
+ _objc_msgSend$nearMissPitchLists
+ _objc_msgSend$nearMissSNRLists
+ _objc_msgSend$nearMissWithRetryLists
+ _objc_msgSend$nearMissWithTriggerPhraseLists
+ _objc_msgSend$neuralFallbackCount
+ _objc_msgSend$onDevice
+ _objc_msgSend$orchMode
+ _objc_msgSend$orchestrationMode
+ _objc_msgSend$partOfARequest
+ _objc_msgSend$phsRejectCount
+ _objc_msgSend$pnrodSiriMetricsAndDims
+ _objc_msgSend$previousBuildVersion
+ _objc_msgSend$readFrom:
+ _objc_msgSend$readInt32
+ _objc_msgSend$readString
+ _objc_msgSend$readUint64
+ _objc_msgSend$requestUUID
+ _objc_msgSend$resolveId
+ _objc_msgSend$scheduleType
+ _objc_msgSend$secondPassAcceptCount
+ _objc_msgSend$secondPassRejectCount
+ _objc_msgSend$sensor
+ _objc_msgSend$sessionUUID
+ _objc_msgSend$setAcousticMitigatorAcceptPostAcousticMitigationCount:
+ _objc_msgSend$setAssetBringUpDigestsReported:
+ _objc_msgSend$setAssetBringUpErrorCode:
+ _objc_msgSend$setAssetBringUpErrorDescription:
+ _objc_msgSend$setAssetBringUpErrorDomain:
+ _objc_msgSend$setAssetBringUpState:
+ _objc_msgSend$setAssetBringUpType:
+ _objc_msgSend$setAssetSetIdentifier:
+ _objc_msgSend$setAssistantVoicesDigestsReported:
+ _objc_msgSend$setClassifiedString:
+ _objc_msgSend$setComponentInvocationId:
+ _objc_msgSend$setConnectionDurationInNanoSeconds:
+ _objc_msgSend$setContextualMitigatorAcceptPostContextualMitigationCount:
+ _objc_msgSend$setCountOfAssetsInAssetSet:
+ _objc_msgSend$setCountOfFactoryAssetsInAssetSet:
+ _objc_msgSend$setCountOfOTAAssetsInAssetSet:
+ _objc_msgSend$setCountOfPSUSAssetsInAssetSet:
+ _objc_msgSend$setCountOfPSUSAssetsPromotedInCurrentOS:
+ _objc_msgSend$setCurrentBuildVersion:
+ _objc_msgSend$setDataClassificationManifests:
+ _objc_msgSend$setDatasetsCapturedTimestampMs:
+ _objc_msgSend$setDimensionNameIndex:
+ _objc_msgSend$setDimensionValue:
+ _objc_msgSend$setDimensionValueBoolean:
+ _objc_msgSend$setDimensionValueFloat:
+ _objc_msgSend$setDimensionValueInteger:
+ _objc_msgSend$setEntityMetrics:
+ _objc_msgSend$setErrorKind:
+ _objc_msgSend$setErrors:
+ _objc_msgSend$setEstimatedSiriMissCount:
+ _objc_msgSend$setExecutorAppIntentAttribution:
+ _objc_msgSend$setExecutorAppIntentMetrics:
+ _objc_msgSend$setExecutorAppIntentSegments:
+ _objc_msgSend$setExecutorAppIntentTargetType:
+ _objc_msgSend$setExecutorAppIntentTask:
+ _objc_msgSend$setExplainabilityIdentifier:
+ _objc_msgSend$setExplainabilityIdentifiers:
+ _objc_msgSend$setFalseWakeWithAcousticMitigationCount:
+ _objc_msgSend$setFalseWakeWithContextualMitigationCount:
+ _objc_msgSend$setFalseWakeWithLwSpkidMitigationCount:
+ _objc_msgSend$setHasMultiKeyboards:
+ _objc_msgSend$setIfPlatformRequestStructuredError:
+ _objc_msgSend$setIsAmbiguousRequest:
+ _objc_msgSend$setIsAppBroughtToForeground:
+ _objc_msgSend$setIsGenAIAware:
+ _objc_msgSend$setIsProcessLaunchRequired:
+ _objc_msgSend$setIsRedacted:
+ _objc_msgSend$setIsSuitableForGenAI:
+ _objc_msgSend$setLwSpkidMitigatorAcceptPostLwSpkidMitigationCount:
+ _objc_msgSend$setMachTimeEnd:
+ _objc_msgSend$setMachTimeStart:
+ _objc_msgSend$setMetricDuration:
+ _objc_msgSend$setMetricsNameIndex:
+ _objc_msgSend$setModelVersionStr:
+ _objc_msgSend$setNeuralFallbackCount:
+ _objc_msgSend$setOnDevice:
+ _objc_msgSend$setOrchMode:
+ _objc_msgSend$setOrchestrationMode:
+ _objc_msgSend$setPartOfARequest:
+ _objc_msgSend$setPhsRejectCount:
+ _objc_msgSend$setPnrodSiriMetricsAndDims:
+ _objc_msgSend$setPreviousBuildVersion:
+ _objc_msgSend$setRequestUUID:
+ _objc_msgSend$setResolveId:
+ _objc_msgSend$setScheduleType:
+ _objc_msgSend$setSecondPassAcceptCount:
+ _objc_msgSend$setSecondPassRejectCount:
+ _objc_msgSend$setSensor:
+ _objc_msgSend$setSessionUUID:
+ _objc_msgSend$setSiriActivationCount:
+ _objc_msgSend$setSkimmerId:
+ _objc_msgSend$setSpeechDatasetsRecord:
+ _objc_msgSend$setStartedLiveActivity:
+ _objc_msgSend$setTextToSpeak:
+ _objc_msgSend$setTimeInSecondsSinceSoftwareUpdate:
+ _objc_msgSend$setTotalNumberOfBytesDownloaded:
+ _objc_msgSend$setTotalSizeOfAssetsInAssetSet:
+ _objc_msgSend$setTotalSizeOfFactoryAssetsInAssetSet:
+ _objc_msgSend$setTotalSizeOfOTAAssetsInAssetSet:
+ _objc_msgSend$setTotalSizeOfPSUSAssetsInAssetSet:
+ _objc_msgSend$setTtsStatus:
+ _objc_msgSend$setUafAssetSource:
+ _objc_msgSend$setVocalizerFallbackCount:
+ _objc_msgSend$siriActivationCount
+ _objc_msgSend$siriUnavailabilityReasons
+ _objc_msgSend$skimmerId
+ _objc_msgSend$speakingDurationInSecs
+ _objc_msgSend$speechDatasetsRecord
+ _objc_msgSend$startedLiveActivity
+ _objc_msgSend$textToSpeak
+ _objc_msgSend$timeInSecondsSinceSoftwareUpdate
+ _objc_msgSend$topLevelUnionType
+ _objc_msgSend$totalNumberOfBytesDownloaded
+ _objc_msgSend$totalSizeOfAssetsInAssetSet
+ _objc_msgSend$totalSizeOfFactoryAssetsInAssetSet
+ _objc_msgSend$totalSizeOfOTAAssetsInAssetSet
+ _objc_msgSend$totalSizeOfPSUSAssetsInAssetSet
+ _objc_msgSend$ttsStatus
+ _objc_msgSend$uafAssetSource
+ _objc_msgSend$vocalizerFallbackCount
+ _objc_msgSend$whichInnerEventType
+ _objc_msgSend$whichProvenance_Type
+ _objc_msgSend$writeInt32:forTag:
+ _objc_msgSend$writeString:forTag:
+ _objc_msgSend$writeTo:
+ _objc_msgSend$writeUint64:forTag:
+ _qname_DUSchemaDUEvent_WhichEvent_Type_speechDatasetsRecord
+ _qname_IFPlatformRequestSchemaIFPlatformRequestClientEvent_WhichEvent_Type_ifPlatformRequestStructuredError
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assetBringUpDigestsReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assistantVoicesDigestsReported
+ _qname_PNRODSchemaPNRODClientEvent_WhichEvent_Type_pnrodSiriMetricsAndDims
+ _qname_SADSchemaSADClientEvent_WhichEvent_Type_assetBringUpState
+ _swift_bridgeObjectRelease_n
+ _swift_setDeallocating
+ _swift_willThrowTypedImpl
+ _symbolic $s19SiriInstrumentation21RemoteSyncableMessageP
+ _symbolic $s19SiriInstrumentation33MessageContainsTextClassificationP
+ _symbolic SSSg
+ _symbolic _____ So018ExecutorSiriSchemaA13AppIntentTaskV
+ _symbolic _____ So018ExecutorSiriSchemaA15AppIntentResultV
+ _symbolic _____ So018ExecutorSiriSchemaA18AppIntentErrorKindV
+ _symbolic _____ So018ExecutorSiriSchemaA19AppIntentTargetTypeV
+ _symbolic _____ So018ExecutorSiriSchemaA20AppIntentAttributionV
+ _symbolic _____ So18LRSchemaLRDataKindV
+ _symbolic _____ So22SISchemaIntercomTargetV
+ _symbolic _____ So24LRSchemaLRDataProvenanceV
+ _symbolic _____ So24SAMSchemaSAMResponseTypeV
+ _symbolic _____ So24SISchemaUEISonicResponseV
+ _symbolic _____ So26IFTMGRSchemaIFTMGRTurnTypeV
+ _symbolic _____ So28LRSchemaLRToolDataProvenanceV
+ _symbolic _____ So28SADSchemaSADAssetBringUpTypeV
+ _symbolic _____ So28SAMSchemaWKAClassifierOutputV
+ _symbolic _____ So30LRSchemaLRSensorDataProvenanceV
+ _symbolic _____ So30ODDSiriSchemaODDTTSFinalStatusV
+ _symbolic _____ So31ORCHSchemaORCHOrchestrationModeV
+ _symbolic _____ So32IFTMGRSchemaIFTMGRSpeechTurnTypeV
+ _symbolic _____ So32SAMSchemaWKARoleCallFinishReasonV
+ _symbolic _____ So36LRSchemaLROnDeviceInfoDataProvenanceV
+ _symbolic _____ So36ODDSiriSchemaODDAssistantTTSClientIdV
+ _symbolic _____ So37ODDSiriSchemaODDExtensionScheduleTypeV
+ _symbolic _____ So39IFTMGRSchemaIFTMGRUserTurnEndedDecisionV
+ _symbolic _____ So41IFTMGRSchemaIFTMGRUserTurnCancelledReasonV
+ _symbolic _____ So50FLOWSchemaFLOWAppleMusicVoiceUserSubscriptionStateV
+ _symbolic _____ So55FLOWSchemaFLOWAppleMusicVoicePreviewOfferNotShownReasonV
+ _symbolic _____ySSSgG s23_ContiguousArrayStorageC
- -[GATSchemaGATClientEvent confirmationSnippetPresented]
- -[GATSchemaGATClientEvent confirmationSnippetUserActioned]
- -[GATSchemaGATClientEvent deleteConfirmationSnippetPresented]
- -[GATSchemaGATClientEvent deleteConfirmationSnippetUserActioned]
- -[GATSchemaGATClientEvent hasConfirmationSnippetPresented]
- -[GATSchemaGATClientEvent hasConfirmationSnippetUserActioned]
- -[GATSchemaGATClientEvent setConfirmationSnippetPresented:]
- -[GATSchemaGATClientEvent setConfirmationSnippetUserActioned:]
- -[GATSchemaGATClientEvent setHasConfirmationSnippetPresented:]
- -[GATSchemaGATClientEvent setHasConfirmationSnippetUserActioned:]
- OBJC_IVAR_$_GATSchemaGATClientEvent._confirmationSnippetPresented
- OBJC_IVAR_$_GATSchemaGATClientEvent._confirmationSnippetUserActioned
- _OBJC_IVAR_$_GATSchemaGATClientEvent._hasConfirmationSnippetPresented
- _OBJC_IVAR_$_GATSchemaGATClientEvent._hasConfirmationSnippetUserActioned
- _OUTLINED_FUNCTION_118
- _OUTLINED_FUNCTION_119
- _OUTLINED_FUNCTION_120
- _OUTLINED_FUNCTION_121
- _OUTLINED_FUNCTION_122
- _OUTLINED_FUNCTION_123
- _OUTLINED_FUNCTION_124
- _OUTLINED_FUNCTION_125
- _OUTLINED_FUNCTION_126
- _OUTLINED_FUNCTION_127
- _OUTLINED_FUNCTION_128
- __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(AnyEvent|Component|IsolationLevel)
- __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Tailing|Factory|Introspection|Mapping|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(Tailing|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(Tailing|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaInstrumentationMessage(Tailing|SensitiveConditions|Introspection)
- __OBJC_$_INSTANCE_METHODS_SISchemaOrderedAnyEvent(Introspection|InstrumentationAdditions|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(AnyEvent|Component|IsolationLevel)
- __OBJC_$_INSTANCE_METHODS_SISchemaUUID(Extensions|Tailing|SensitiveConditions)
- ___swift_coroFrameAllocStub
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$confirmationSnippetPresented
- _objc_msgSend$confirmationSnippetUserActioned
- _objc_msgSend$deleteConfirmationSnippetPresented
- _objc_msgSend$deleteConfirmationSnippetUserActioned
- _objc_msgSend$setConfirmationSnippetPresented:
- _objc_msgSend$setConfirmationSnippetUserActioned:
- _objc_retain_x1
- _qname_GATSchemaGATClientEvent_WhichEvent_Type_confirmationSnippetPresented
- _qname_GATSchemaGATClientEvent_WhichEvent_Type_confirmationSnippetUserActioned
CStrings:
+ ", partOfARequest:"
+ "@\"DUSchemaDUSpeechDatasetsRecord\""
+ "@\"ExecutorSiriSchemaExecutorAppIntentMetrics\""
+ "@\"IFPlatformRequestSchemaIFPlatformRequestStructuredError\""
+ "@\"LRSchemaLRDataClassificationMetadata\""
+ "@\"ODDSiriSchemaODDAssetBringUpDigestsReported\""
+ "@\"ODDSiriSchemaODDAssistantVoicesCounts\""
+ "@\"ODDSiriSchemaODDAssistantVoicesDigestsReported\""
+ "@\"ODDSiriSchemaODDAssistantVoicesDimensions\""
+ "@\"ODDSiriSchemaODDAssistantVoicesTuples\""
+ "@\"PNRODSchemaPNRODDimension\""
+ "@\"PNRODSchemaPnRODSiriMetricsAndDims\""
+ "@\"SADSchemaSADAssetBringUpState\""
+ "@\"SISchemaErrorInfo\""
+ "@\"SISchemaFreeFormText\""
+ "ASRSpeechProfileSchemaASRSpeechProfileUpdateEntityMetric"
+ "DISMISSALREASON_ANNOUNCE_SPEECH_MANAGER_STOPPED_UNEXPECTEDLY"
+ "DISMISSALREASON_ASSESSMENT_MODE_ACTIVE"
+ "DISMISSALREASON_BLUETOOTH_DEVICE_DEACTIVATION"
+ "DISMISSALREASON_CARPLAY_BORROWED_AUDIO_DURING_ANNOUNCEMENT"
+ "DISMISSALREASON_CARPLAY_UNPAIRED"
+ "DISMISSALREASON_EMERGENCY_BULLETIN_EMPTY_ERROR"
+ "DISMISSALREASON_INCOMING_CALL_ANNOUNCEMENT_TRUMP"
+ "DISMISSALREASON_IN_APP_RESPONSE_TO_TYPE_TO_SIRI_REQUEST"
+ "DISMISSALREASON_PROMPT_FOR_PASSCODE_UNLOCK_FAILURE"
+ "DISMISSALREASON_REMOTE_DEACTIVATION"
+ "DISMISSALREASON_SYESTEM_SHELL_PRESENTATION_FAILURE"
+ "DISMISSALREASON_TEST_CLEAN_UP"
+ "DISMISSALREASON_TIMEOUT_POST_APP_LAUNCH"
+ "DISMISSALREASON_TIMEOUT_POST_SYSTEM_UI_RESPONSE"
+ "DISMISSALREASON_TIMEOUT_POST_TOUCH_OUTSIDE_OF_SIRI"
+ "DISMISSALREASON_UNSUPPORTED_VOICE_PROMPT_STYLE_DURING_ANNOUNCEMENT"
+ "DISMISSALREASON_USER_DISMISSED_ACTIVITY_KIT_ACTIVITY"
+ "DISMISSALREASON_USER_ENTERED_SCREENSHOT_FULL_MODE"
+ "DUSchemaDUSpeechDatasetsRecord"
+ "EXECUTORAPPINTENTATTRIBUTION_APPLICATION"
+ "EXECUTORAPPINTENTATTRIBUTION_APP_DEFAULT"
+ "EXECUTORAPPINTENTATTRIBUTION_APP_INTENT"
+ "EXECUTORAPPINTENTATTRIBUTION_UNKNOWN"
+ "EXECUTORAPPINTENTERRORKIND_CUSTOM"
+ "EXECUTORAPPINTENTERRORKIND_DEFAULT"
+ "EXECUTORAPPINTENTERRORKIND_INTERVENTION_REQUIRED"
+ "EXECUTORAPPINTENTERRORKIND_RETRYABLE"
+ "EXECUTORAPPINTENTERRORKIND_UNKNOWN"
+ "EXECUTORAPPINTENTERRORKIND_UNSUPPORTED"
+ "EXECUTORAPPINTENTRESULT_CHOOSE_FROM_LIST"
+ "EXECUTORAPPINTENTRESULT_CHOOSE_MULTIPLE_FROM_LIST"
+ "EXECUTORAPPINTENTRESULT_CHOOSE_VALUE"
+ "EXECUTORAPPINTENTRESULT_COMPLETE"
+ "EXECUTORAPPINTENTRESULT_REQUEST_PROTECTED_APP_APPROVAL"
+ "EXECUTORAPPINTENTRESULT_SHOW_ACTION_CONFIRMATION"
+ "EXECUTORAPPINTENTRESULT_SHOW_PARAMETER_CONFIRMATION"
+ "EXECUTORAPPINTENTRESULT_UNKNOWN"
+ "EXECUTORAPPINTENTTARGETTYPE_APPLICATION"
+ "EXECUTORAPPINTENTTARGETTYPE_APP_INTENT_EXTENSION"
+ "EXECUTORAPPINTENTTARGETTYPE_DAEMON"
+ "EXECUTORAPPINTENTTARGETTYPE_UNKNOWN"
+ "EXECUTORAPPINTENTTARGETTYPE_WIDGET_EXTENSION"
+ "EXECUTORAPPINTENTTASK_INITIALIZE_INTENT"
+ "EXECUTORAPPINTENTTASK_PERFORM"
+ "EXECUTORAPPINTENTTASK_RESOLVE_PARAMETERS"
+ "EXECUTORAPPINTENTTASK_TOTAL_FRAMEWORK"
+ "EXECUTORAPPINTENTTASK_UNKNOWN"
+ "ExecutorSiriSchemaExecutorAppIntentMetrics"
+ "ExecutorSiriSchemaExecutorAppIntentSegment"
+ "Failed to get redacted bytes: %@"
+ "IFPlatformRequestSchemaIFPlatformRequestStructuredError"
+ "IFTMGRSPEECHTURNTYPE_ACTIVATED"
+ "IFTMGRSPEECHTURNTYPE_CANDIDATE"
+ "IFTMGRSPEECHTURNTYPE_UNKNOWN"
+ "IFTMGRTURNTYPE_BUTTON_TAP"
+ "IFTMGRTURNTYPE_SPEECH"
+ "IFTMGRTURNTYPE_TEXT"
+ "IFTMGRTURNTYPE_UNKNOWN"
+ "IFTMGRUSERTURNCANCELLEDREASON_ACOUSTIC_FTM_MITIGATED"
+ "IFTMGRUSERTURNCANCELLEDREASON_ADBLOCKER_MITIGATED"
+ "IFTMGRUSERTURNCANCELLEDREASON_DEACTIVATION_REQUESTED"
+ "IFTMGRUSERTURNCANCELLEDREASON_MYRIAD_LOSS"
+ "IFTMGRUSERTURNCANCELLEDREASON_NEW_REQUEST_STARTED"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_CANCELED_FROM_UI"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_CANCELLED"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_DELEGATE_REPLACED_FOR_UNKNOWN_REASON"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_FAILED"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_ROLLED_BACK"
+ "IFTMGRUSERTURNCANCELLEDREASON_REQUEST_TIMED_OUT"
+ "IFTMGRUSERTURNCANCELLEDREASON_SESSION_ENDED"
+ "IFTMGRUSERTURNCANCELLEDREASON_SPEECH_CANCELED"
+ "IFTMGRUSERTURNCANCELLEDREASON_UNKNOWN"
+ "IFTMGRUSERTURNCANCELLEDREASON_USER_INTERACTION"
+ "IFTMGRUSERTURNENDEDDECISION_MAYBE_MITIGATED"
+ "IFTMGRUSERTURNENDEDDECISION_MITIGATED"
+ "IFTMGRUSERTURNENDEDDECISION_SELECTED"
+ "IFTMGRUSERTURNENDEDDECISION_UNKNOWN"
+ "LRDATAKIND_BODYTEXT"
+ "LRDATAKIND_DATETIME"
+ "LRDATAKIND_EMAILADDRESS"
+ "LRDATAKIND_FIRSTNAME"
+ "LRDATAKIND_LASTNAME"
+ "LRDATAKIND_OTHER"
+ "LRDATAKIND_OTHERCALENDARINFORMATION"
+ "LRDATAKIND_OTHERCONTACTINFORMATION"
+ "LRDATAKIND_OTHERLOCATIONINFORMATION"
+ "LRDATAKIND_PARTIALNAME"
+ "LRDATAKIND_PHONENUMBER"
+ "LRDATAKIND_PLACENAME"
+ "LRDATAKIND_POSTALADDRESS"
+ "LRDATAKIND_TITLETEXT"
+ "LRDATAKIND_UNKNOWN"
+ "LRDATAKIND_URL"
+ "LRDATAPROVENANCE_NOTIFICATIONS"
+ "LRDATAPROVENANCE_NOWPLAYING"
+ "LRDATAPROVENANCE_ONSCREEN"
+ "LRDATAPROVENANCE_OTHER"
+ "LRDATAPROVENANCE_UNKNOWN"
+ "LRDATAPROVENANCE_USERUTTERANCE"
+ "LRONDEVICEINFODATAPROVENANCE_CALENDAR"
+ "LRONDEVICEINFODATAPROVENANCE_CONTACTS"
+ "LRONDEVICEINFODATAPROVENANCE_MAIL"
+ "LRONDEVICEINFODATAPROVENANCE_MESSAGES"
+ "LRONDEVICEINFODATAPROVENANCE_NOTES"
+ "LRONDEVICEINFODATAPROVENANCE_OTHER"
+ "LRONDEVICEINFODATAPROVENANCE_UNKNOWN"
+ "LRSENSORDATAPROVENANCE_CAMERA"
+ "LRSENSORDATAPROVENANCE_GPS"
+ "LRSENSORDATAPROVENANCE_MICROPHONE"
+ "LRSENSORDATAPROVENANCE_OTHER"
+ "LRSENSORDATAPROVENANCE_UNKNOWN"
+ "LRSchemaLRDataClassificationManifest"
+ "LRSchemaLRDataClassificationMetadata"
+ "LRTOOLDATAPROVENANCE_CALENDAR"
+ "LRTOOLDATAPROVENANCE_CONTACTS"
+ "LRTOOLDATAPROVENANCE_MAIL"
+ "LRTOOLDATAPROVENANCE_MESSAGES"
+ "LRTOOLDATAPROVENANCE_NOTES"
+ "LRTOOLDATAPROVENANCE_OTHER"
+ "LRTOOLDATAPROVENANCE_SEARCH"
+ "LRTOOLDATAPROVENANCE_THIRDPARTY"
+ "LRTOOLDATAPROVENANCE_UNKNOWN"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_ASSISTANT_SERVICES"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_CAROUSEL"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_CARPLAYAPP"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_MRSIRI"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_SIRI"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_SIRI_HEADLESS_SERVICE"
+ "ODDASSISTANTTTSCLIENTID_COM_APPLE_SPRINGBOARD"
+ "ODDASSISTANTTTSCLIENTID_UNKNOWN"
+ "ODDEXTENSIONNAME_ODDI_EXPERIMENTATION_EXTENSION"
+ "ODDEXTENSIONNAME_ODDI_METRICS_EXTENSION"
+ "ODDEXTENSIONNAME_POIROT_METRICS_EXTENSION"
+ "ODDEXTENSIONSCHEDULETYPE_DAILY"
+ "ODDEXTENSIONSCHEDULETYPE_HOURLY"
+ "ODDEXTENSIONSCHEDULETYPE_UNKNOWN"
+ "ODDSiriSchemaODDAssetBringUpDigestsReported"
+ "ODDSiriSchemaODDAssetBringUpStatus"
+ "ODDSiriSchemaODDAssistantVoicesCounts"
+ "ODDSiriSchemaODDAssistantVoicesDigest"
+ "ODDSiriSchemaODDAssistantVoicesDigestsReported"
+ "ODDSiriSchemaODDAssistantVoicesDimensions"
+ "ODDSiriSchemaODDAssistantVoicesTuples"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_ACTION_CONFIRMATION"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_IFREQUESTID_NOT_PRESENT"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_PARAMETER_NEEDS_VALUE"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_PARAMETER_NOT_ALLOWED"
+ "ODDTTSFINALSTATUS_CANCELED"
+ "ODDTTSFINALSTATUS_COMPLETED"
+ "ODDTTSFINALSTATUS_FAILED"
+ "ODDTTSFINALSTATUS_UNKNOWN"
+ "ORCHERRORDOMAIN_SIRIXAGENT"
+ "ORCHORCHESTRATIONMODE_SIRI_CLASSIC"
+ "ORCHORCHESTRATIONMODE_SIRI_X_FULL_UOD"
+ "ORCHORCHESTRATIONMODE_SIRI_X_HYBRID_UOD"
+ "ORCHORCHESTRATIONMODE_SYSTEM_ASSISTANT_EXPERIENCE"
+ "ORCHORCHESTRATIONMODE_UNKNOWN"
+ "PNRODSchemaPNRODDimension"
+ "PNRODSchemaPnRODSiriMetricsAndDims"
+ "RESOLVESchemaRESOLVEClientEventMetadata"
+ "SADASSETBRINGUPTYPE_FACTORY"
+ "SADASSETBRINGUPTYPE_OTA"
+ "SADASSETBRINGUPTYPE_OTHER"
+ "SADASSETBRINGUPTYPE_PSUS"
+ "SADASSETBRINGUPTYPE_UNKNOWN"
+ "SADSchemaSADAssetBringUpState"
+ "SAMRESPONSETYPE_ASK"
+ "SAMRESPONSETYPE_CONFIRMATION"
+ "SAMRESPONSETYPE_DISAMBIGUATION"
+ "SAMRESPONSETYPE_INFORM"
+ "SAMRESPONSETYPE_UNKNOWN"
+ "SIRIUNAVAILABLEREASON_DISABLED"
+ "SISchemaErrorInfo"
+ "SISchemaFreeFormText"
+ "SKIMMERSchemaSKIMMERClientEventMetadata"
+ "STSPOTLIGHTSEARCHRETRIEVALTYPE_HYBRID"
+ "T@\"DUSchemaDUSpeechDatasetsRecord\",&,N,V_speechDatasetsRecord"
+ "T@\"ExecutorSiriSchemaExecutorAppIntentMetrics\",&,N,V_executorAppIntentMetrics"
+ "T@\"IFPlatformRequestSchemaIFPlatformRequestStructuredError\",&,N,V_ifPlatformRequestStructuredError"
+ "T@\"LRSchemaLRDataClassificationMetadata\",&,N,V_metadata"
+ "T@\"NSArray\",C,N,V_autoMOSs"
+ "T@\"NSArray\",C,N,V_customerPerceivedLatencyInSecs"
+ "T@\"NSArray\",C,N,V_dataClassificationManifests"
+ "T@\"NSArray\",C,N,V_entityMetrics"
+ "T@\"NSArray\",C,N,V_errors"
+ "T@\"NSArray\",C,N,V_executorAppIntentSegments"
+ "T@\"NSArray\",C,N,V_explainabilityIdentifiers"
+ "T@\"NSArray\",C,N,V_modelSelectedOptions"
+ "T@\"NSArray\",C,N,V_nearMissCheckerScoreLists"
+ "T@\"NSArray\",C,N,V_nearMissPitchLists"
+ "T@\"NSArray\",C,N,V_nearMissSNRLists"
+ "T@\"NSArray\",C,N,V_nearMissWithRetryLists"
+ "T@\"NSArray\",C,N,V_nearMissWithTriggerPhraseLists"
+ "T@\"NSArray\",C,N,V_siriUnavailabilityReasons"
+ "T@\"NSArray\",C,N,V_speakingDurationInSecs"
+ "T@\"NSString\",C,N,V_assetBringUpErrorDescription"
+ "T@\"NSString\",C,N,V_assetBringUpErrorDomain"
+ "T@\"NSString\",C,N,V_assetSetIdentifier"
+ "T@\"NSString\",C,N,V_classifiedString"
+ "T@\"NSString\",C,N,V_currentBuildVersion"
+ "T@\"NSString\",C,N,V_modelVersionStr"
+ "T@\"NSString\",C,N,V_previousBuildVersion"
+ "T@\"NSString\",N,C"
+ "T@\"ODDSiriSchemaODDAssetBringUpDigestsReported\",&,N,V_assetBringUpDigestsReported"
+ "T@\"ODDSiriSchemaODDAssistantVoicesCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDAssistantVoicesDigestsReported\",&,N,V_assistantVoicesDigestsReported"
+ "T@\"ODDSiriSchemaODDAssistantVoicesDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDAssistantVoicesTuples\",&,N,V_tuples"
+ "T@\"PNRODSchemaPNRODDimension\",&,N,V_dimensionValue"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_metricDuration"
+ "T@\"PNRODSchemaPnRODSiriMetricsAndDims\",&,N,V_pnrodSiriMetricsAndDims"
+ "T@\"SADSchemaSADAssetBringUpState\",&,N,V_assetBringUpState"
+ "T@\"SISchemaErrorInfo\",&,N,V_error"
+ "T@\"SISchemaFreeFormText\",&,N,V_textToSpeak"
+ "T@\"SISchemaUUID\",&,N,V_componentInvocationId"
+ "T@\"SISchemaUUID\",&,N,V_explainabilityIdentifier"
+ "T@\"SISchemaUUID\",&,N,V_requestUUID"
+ "T@\"SISchemaUUID\",&,N,V_resolveId"
+ "T@\"SISchemaUUID\",&,N,V_sessionUUID"
+ "T@\"SISchemaUUID\",&,N,V_skimmerId"
+ "TB,N,V_assetBringUpState"
+ "TB,N,V_dimensionValueBoolean"
+ "TB,N,V_hasAssetBringUpDigestsReported"
+ "TB,N,V_hasAssetBringUpErrorDescription"
+ "TB,N,V_hasAssetBringUpErrorDomain"
+ "TB,N,V_hasAssetBringUpState"
+ "TB,N,V_hasAssetSetIdentifier"
+ "TB,N,V_hasAssistantVoicesDigestsReported"
+ "TB,N,V_hasClassifiedString"
+ "TB,N,V_hasComponentInvocationId"
+ "TB,N,V_hasCurrentBuildVersion"
+ "TB,N,V_hasDimensionValue"
+ "TB,N,V_hasExecutorAppIntentMetrics"
+ "TB,N,V_hasExplainabilityIdentifier"
+ "TB,N,V_hasIfPlatformRequestStructuredError"
+ "TB,N,V_hasMetricDuration"
+ "TB,N,V_hasModelVersionStr"
+ "TB,N,V_hasMultiKeyboards"
+ "TB,N,V_hasOnDevice"
+ "TB,N,V_hasPnrodSiriMetricsAndDims"
+ "TB,N,V_hasPreviousBuildVersion"
+ "TB,N,V_hasRequestUUID"
+ "TB,N,V_hasResolveId"
+ "TB,N,V_hasSensor"
+ "TB,N,V_hasSessionUUID"
+ "TB,N,V_hasSkimmerId"
+ "TB,N,V_hasSpeechDatasetsRecord"
+ "TB,N,V_hasTextToSpeak"
+ "TB,N,V_isAmbiguousRequest"
+ "TB,N,V_isAppBroughtToForeground"
+ "TB,N,V_isGenAIAware"
+ "TB,N,V_isProcessLaunchRequired"
+ "TB,N,V_isRedacted"
+ "TB,N,V_isSuitableForGenAI"
+ "TB,N,V_partOfARequest"
+ "TB,N,V_startedLiveActivity"
+ "TI,N,V_acousticMitigatorAcceptPostAcousticMitigationCount"
+ "TI,N,V_assetBringUpErrorCode"
+ "TI,N,V_contextualMitigatorAcceptPostContextualMitigationCount"
+ "TI,N,V_countOfAssetsInAssetSet"
+ "TI,N,V_countOfFactoryAssetsInAssetSet"
+ "TI,N,V_countOfOTAAssetsInAssetSet"
+ "TI,N,V_countOfPSUSAssetsInAssetSet"
+ "TI,N,V_countOfPSUSAssetsPromotedInCurrentOS"
+ "TI,N,V_estimatedSiriMissCount"
+ "TI,N,V_falseWakeWithAcousticMitigationCount"
+ "TI,N,V_falseWakeWithContextualMitigationCount"
+ "TI,N,V_falseWakeWithLwSpkidMitigationCount"
+ "TI,N,V_lwSpkidMitigatorAcceptPostLwSpkidMitigationCount"
+ "TI,N,V_neuralFallbackCount"
+ "TI,N,V_phsRejectCount"
+ "TI,N,V_secondPassAcceptCount"
+ "TI,N,V_secondPassRejectCount"
+ "TI,N,V_siriActivationCount"
+ "TI,N,V_vocalizerFallbackCount"
+ "TMSSchemaTMSClientEventMetadata"
+ "TQ,N,V_datasetsCapturedTimestampMs"
+ "TQ,N,V_timeInSecondsSinceSoftwareUpdate"
+ "TQ,N,V_totalNumberOfBytesDownloaded"
+ "TQ,N,V_totalSizeOfAssetsInAssetSet"
+ "TQ,N,V_totalSizeOfFactoryAssetsInAssetSet"
+ "TQ,N,V_totalSizeOfOTAAssetsInAssetSet"
+ "TQ,N,V_totalSizeOfPSUSAssetsInAssetSet"
+ "TQ,R,N,V_whichProvenance_Type"
+ "TTSVOICETYPE_FMVOICE"
+ "Td,N,V_connectionDurationInNanoSeconds"
+ "Td,N,V_dimensionValueFloat"
+ "Ti,N,V_assetBringUpType"
+ "Ti,N,V_clientId"
+ "Ti,N,V_entityCategory"
+ "Ti,N,V_errorKind"
+ "Ti,N,V_executorAppIntentAttribution"
+ "Ti,N,V_executorAppIntentTargetType"
+ "Ti,N,V_executorAppIntentTask"
+ "Ti,N,V_general"
+ "Ti,N,V_onDevice"
+ "Ti,N,V_orchMode"
+ "Ti,N,V_orchestrationMode"
+ "Ti,N,V_scheduleType"
+ "Ti,N,V_sensor"
+ "Ti,N,V_tool"
+ "Ti,N,V_ttsStatus"
+ "Ti,N,V_uafAssetSource"
+ "Tq,N,V_componentIndex"
+ "Tq,N,V_dimensionNameIndex"
+ "Tq,N,V_dimensionValueInteger"
+ "Tq,N,V_machTimeEnd"
+ "Tq,N,V_machTimeStart"
+ "Tq,N,V_metricsNameIndex"
+ "U"
+ "WKACLASSIFIEROUTPUT_MULTI_STEP"
+ "WKACLASSIFIEROUTPUT_SINGLE_STEP"
+ "WKACLASSIFIEROUTPUT_UNKNOWN"
+ "WKAROLECALLFINISHREASON_LENGTH"
+ "WKAROLECALLFINISHREASON_STOP"
+ "WKAROLECALLFINISHREASON_TOOL_CALLS"
+ "WKAROLECALLFINISHREASON_UNKNOWN"
+ "_acousticMitigatorAcceptPostAcousticMitigationCount"
+ "_assetBringUpDigestsReported"
+ "_assetBringUpErrorCode"
+ "_assetBringUpErrorDescription"
+ "_assetBringUpErrorDomain"
+ "_assetBringUpState"
+ "_assetBringUpType"
+ "_assetSetIdentifier"
+ "_assistantVoicesDigestsReported"
+ "_autoMOSs"
+ "_classifiedString"
+ "_componentInvocationId"
+ "_connectionDurationInNanoSeconds"
+ "_contextualMitigatorAcceptPostContextualMitigationCount"
+ "_countOfAssetsInAssetSet"
+ "_countOfFactoryAssetsInAssetSet"
+ "_countOfOTAAssetsInAssetSet"
+ "_countOfPSUSAssetsInAssetSet"
+ "_countOfPSUSAssetsPromotedInCurrentOS"
+ "_currentBuildVersion"
+ "_customerPerceivedLatencyInSecs"
+ "_dataClassificationManifests"
+ "_datasetsCapturedTimestampMs"
+ "_dimensionNameIndex"
+ "_dimensionValue"
+ "_dimensionValueBoolean"
+ "_dimensionValueFloat"
+ "_dimensionValueInteger"
+ "_entityMetrics"
+ "_errorKind"
+ "_errors"
+ "_estimatedSiriMissCount"
+ "_executorAppIntentAttribution"
+ "_executorAppIntentMetrics"
+ "_executorAppIntentSegments"
+ "_executorAppIntentTargetType"
+ "_executorAppIntentTask"
+ "_explainabilityIdentifier"
+ "_explainabilityIdentifiers"
+ "_falseWakeWithAcousticMitigationCount"
+ "_falseWakeWithContextualMitigationCount"
+ "_falseWakeWithLwSpkidMitigationCount"
+ "_hasAssetBringUpDigestsReported"
+ "_hasAssetBringUpErrorDescription"
+ "_hasAssetBringUpErrorDomain"
+ "_hasAssetBringUpState"
+ "_hasAssetSetIdentifier"
+ "_hasAssistantVoicesDigestsReported"
+ "_hasClassifiedString"
+ "_hasComponentInvocationId"
+ "_hasCurrentBuildVersion"
+ "_hasDimensionValue"
+ "_hasExecutorAppIntentMetrics"
+ "_hasExplainabilityIdentifier"
+ "_hasIfPlatformRequestStructuredError"
+ "_hasMetricDuration"
+ "_hasModelVersionStr"
+ "_hasMultiKeyboards"
+ "_hasOnDevice"
+ "_hasPnrodSiriMetricsAndDims"
+ "_hasPreviousBuildVersion"
+ "_hasRequestUUID"
+ "_hasResolveId"
+ "_hasSensor"
+ "_hasSessionUUID"
+ "_hasSkimmerId"
+ "_hasSpeechDatasetsRecord"
+ "_hasTextToSpeak"
+ "_ifPlatformRequestStructuredError"
+ "_isAmbiguousRequest"
+ "_isAppBroughtToForeground"
+ "_isGenAIAware"
+ "_isProcessLaunchRequired"
+ "_isRedacted"
+ "_isSuitableForGenAI"
+ "_lwSpkidMitigatorAcceptPostLwSpkidMitigationCount"
+ "_machTimeEnd"
+ "_machTimeStart"
+ "_metricDuration"
+ "_metricsNameIndex"
+ "_modelSelectedOptions"
+ "_modelVersionStr"
+ "_nearMissCheckerScoreLists"
+ "_nearMissPitchLists"
+ "_nearMissSNRLists"
+ "_nearMissWithRetryLists"
+ "_nearMissWithTriggerPhraseLists"
+ "_neuralFallbackCount"
+ "_onDevice"
+ "_orchMode"
+ "_orchestrationMode"
+ "_partOfARequest"
+ "_phsRejectCount"
+ "_pnrodSiriMetricsAndDims"
+ "_previousBuildVersion"
+ "_requestUUID"
+ "_resolveId"
+ "_scheduleType"
+ "_secondPassAcceptCount"
+ "_secondPassRejectCount"
+ "_sensor"
+ "_sessionUUID"
+ "_siriActivationCount"
+ "_siriUnavailabilityReasons"
+ "_skimmerId"
+ "_speakingDurationInSecs"
+ "_speechDatasetsRecord"
+ "_startedLiveActivity"
+ "_textToSpeak"
+ "_timeInSecondsSinceSoftwareUpdate"
+ "_totalNumberOfBytesDownloaded"
+ "_totalSizeOfAssetsInAssetSet"
+ "_totalSizeOfFactoryAssetsInAssetSet"
+ "_totalSizeOfOTAAssetsInAssetSet"
+ "_totalSizeOfPSUSAssetsInAssetSet"
+ "_ttsStatus"
+ "_uafAssetSource"
+ "_vocalizerFallbackCount"
+ "_whichProvenance_Type"
+ "acousticMitigatorAcceptPostAcousticMitigationCount"
+ "addAutoMOS:"
+ "addCustomerPerceivedLatencyInSec:"
+ "addDataClassificationManifests:"
+ "addEntityMetrics:"
+ "addErrors:"
+ "addExecutorAppIntentSegments:"
+ "addExplainabilityIdentifiers:"
+ "addModelSelectedOptions:"
+ "addNearMissCheckerScoreList:"
+ "addNearMissPitchList:"
+ "addNearMissSNRList:"
+ "addNearMissWithRetryList:"
+ "addNearMissWithTriggerPhraseList:"
+ "addSiriUnavailabilityReasons:"
+ "addSpeakingDurationInSec:"
+ "altDsId"
+ "assetBringUpDigestsReported"
+ "assetBringUpErrorCode"
+ "assetBringUpErrorDescription"
+ "assetBringUpErrorDomain"
+ "assetBringUpState"
+ "assetBringUpType"
+ "assetSetIdentifier"
+ "assistantVoicesDigestsReported"
+ "autoMOS"
+ "autoMOSAtIndex:"
+ "autoMOSCount"
+ "autoMOSs"
+ "classifiedString"
+ "clearAutoMOS"
+ "clearCustomerPerceivedLatencyInSec"
+ "clearDataClassificationManifests"
+ "clearEntityMetrics"
+ "clearErrors"
+ "clearExecutorAppIntentSegments"
+ "clearExplainabilityIdentifiers"
+ "clearModelSelectedOptions"
+ "clearNearMissCheckerScoreList"
+ "clearNearMissPitchList"
+ "clearNearMissSNRList"
+ "clearNearMissWithRetryList"
+ "clearNearMissWithTriggerPhraseList"
+ "clearSiriUnavailabilityReasons"
+ "clearSpeakingDurationInSec"
+ "com.apple.aiml.dataupload.DUEvent.DUSpeechDatasetsRecord"
+ "com.apple.aiml.platform.fft.FFTWrapper"
+ "com.apple.aiml.siri.ifPlatformRequest.IFPlatformRequestClientEvent.IFPlatformRequestStructuredError"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssetBringUpDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssistantVoicesDigestsReported"
+ "com.apple.aiml.siri.pnrod.PNRODClientEvent.PnRODSiriMetricsAndDims"
+ "com.apple.aiml.siri.sad.SADClientEvent.SADAssetBringUpState"
+ "com.apple.intelligence_flow.Event"
+ "componentInvocationId"
+ "connectionDurationInNanoSeconds"
+ "contextualMitigatorAcceptPostContextualMitigationCount"
+ "countOfAssetsInAssetSet"
+ "countOfFactoryAssetsInAssetSet"
+ "countOfOTAAssetsInAssetSet"
+ "countOfPSUSAssetsInAssetSet"
+ "countOfPSUSAssetsPromotedInCurrentOS"
+ "currentBuildVersion"
+ "customerPerceivedLatencyInSec"
+ "customerPerceivedLatencyInSecAtIndex:"
+ "customerPerceivedLatencyInSecCount"
+ "customerPerceivedLatencyInSecs"
+ "dataClassificationManifests"
+ "dataClassificationManifestsAtIndex:"
+ "dataClassificationManifestsCount"
+ "datasetsCapturedTimestampMs"
+ "deleteAcousticMitigatorAcceptPostAcousticMitigationCount"
+ "deleteAssetBringUpDigestsReported"
+ "deleteAssetBringUpErrorCode"
+ "deleteAssetBringUpErrorDescription"
+ "deleteAssetBringUpErrorDomain"
+ "deleteAssetBringUpState"
+ "deleteAssetBringUpType"
+ "deleteAssetSetIdentifier"
+ "deleteAssistantVoicesDigestsReported"
+ "deleteAutoMOS"
+ "deleteClassifiedString"
+ "deleteComponentInvocationId"
+ "deleteConnectionDurationInNanoSeconds"
+ "deleteContextualMitigatorAcceptPostContextualMitigationCount"
+ "deleteCountOfAssetsInAssetSet"
+ "deleteCountOfFactoryAssetsInAssetSet"
+ "deleteCountOfOTAAssetsInAssetSet"
+ "deleteCountOfPSUSAssetsInAssetSet"
+ "deleteCountOfPSUSAssetsPromotedInCurrentOS"
+ "deleteCurrentBuildVersion"
+ "deleteCustomerPerceivedLatencyInSec"
+ "deleteDataClassificationManifests"
+ "deleteDatasetsCapturedTimestampMs"
+ "deleteDimensionNameIndex"
+ "deleteDimensionValue"
+ "deleteDimensionValueBoolean"
+ "deleteDimensionValueFloat"
+ "deleteDimensionValueInteger"
+ "deleteEntityMetrics"
+ "deleteErrorKind"
+ "deleteErrors"
+ "deleteEstimatedSiriMissCount"
+ "deleteExecutorAppIntentAttribution"
+ "deleteExecutorAppIntentMetrics"
+ "deleteExecutorAppIntentSegments"
+ "deleteExecutorAppIntentTargetType"
+ "deleteExecutorAppIntentTask"
+ "deleteExplainabilityIdentifier"
+ "deleteExplainabilityIdentifiers"
+ "deleteFalseWakeWithAcousticMitigationCount"
+ "deleteFalseWakeWithContextualMitigationCount"
+ "deleteFalseWakeWithLwSpkidMitigationCount"
+ "deleteHasMultiKeyboards"
+ "deleteIfPlatformRequestStructuredError"
+ "deleteIsAmbiguousRequest"
+ "deleteIsAppBroughtToForeground"
+ "deleteIsGenAIAware"
+ "deleteIsProcessLaunchRequired"
+ "deleteIsRedacted"
+ "deleteIsSuitableForGenAI"
+ "deleteLwSpkidMitigatorAcceptPostLwSpkidMitigationCount"
+ "deleteMachTimeEnd"
+ "deleteMachTimeStart"
+ "deleteMetricDuration"
+ "deleteMetricsNameIndex"
+ "deleteModelSelectedOptions"
+ "deleteModelVersionStr"
+ "deleteNearMissCheckerScoreList"
+ "deleteNearMissPitchList"
+ "deleteNearMissSNRList"
+ "deleteNearMissWithRetryList"
+ "deleteNearMissWithTriggerPhraseList"
+ "deleteNeuralFallbackCount"
+ "deleteOnDevice"
+ "deleteOrchMode"
+ "deleteOrchestrationMode"
+ "deletePartOfARequest"
+ "deletePhsRejectCount"
+ "deletePnrodSiriMetricsAndDims"
+ "deletePreviousBuildVersion"
+ "deleteRequestUUID"
+ "deleteResolveId"
+ "deleteScheduleType"
+ "deleteSecondPassAcceptCount"
+ "deleteSecondPassRejectCount"
+ "deleteSensor"
+ "deleteSessionUUID"
+ "deleteSiriActivationCount"
+ "deleteSiriUnavailabilityReasons"
+ "deleteSkimmerId"
+ "deleteSpeakingDurationInSec"
+ "deleteSpeechDatasetsRecord"
+ "deleteStartedLiveActivity"
+ "deleteTextToSpeak"
+ "deleteTimeInSecondsSinceSoftwareUpdate"
+ "deleteTotalNumberOfBytesDownloaded"
+ "deleteTotalSizeOfAssetsInAssetSet"
+ "deleteTotalSizeOfFactoryAssetsInAssetSet"
+ "deleteTotalSizeOfOTAAssetsInAssetSet"
+ "deleteTotalSizeOfPSUSAssetsInAssetSet"
+ "deleteTtsStatus"
+ "deleteUafAssetSource"
+ "deleteVocalizerFallbackCount"
+ "dimensionNameIndex"
+ "dimensionValue"
+ "dimensionValueBoolean"
+ "dimensionValueFloat"
+ "dimensionValueInteger"
+ "entityMetrics"
+ "entityMetricsAtIndex:"
+ "entityMetricsCount"
+ "errorKind"
+ "errors"
+ "errorsAtIndex:"
+ "errorsCount"
+ "estimatedSiriMissCount"
+ "executorAppIntentAttribution"
+ "executorAppIntentMetrics"
+ "executorAppIntentSegments"
+ "executorAppIntentSegmentsAtIndex:"
+ "executorAppIntentSegmentsCount"
+ "executorAppIntentTargetType"
+ "executorAppIntentTask"
+ "explainabilityIdentifier"
+ "explainabilityIdentifiers"
+ "explainabilityIdentifiersAtIndex:"
+ "explainabilityIdentifiersCount"
+ "falseWakeWithAcousticMitigationCount"
+ "falseWakeWithContextualMitigationCount"
+ "falseWakeWithLwSpkidMitigationCount"
+ "hasAcousticMitigatorAcceptPostAcousticMitigationCount"
+ "hasAssetBringUpDigestsReported"
+ "hasAssetBringUpErrorCode"
+ "hasAssetBringUpErrorDescription"
+ "hasAssetBringUpErrorDomain"
+ "hasAssetBringUpState"
+ "hasAssetBringUpType"
+ "hasAssetSetIdentifier"
+ "hasAssistantVoicesDigestsReported"
+ "hasClassifiedString"
+ "hasComponentInvocationId"
+ "hasConnectionDurationInNanoSeconds"
+ "hasContextualMitigatorAcceptPostContextualMitigationCount"
+ "hasCountOfAssetsInAssetSet"
+ "hasCountOfFactoryAssetsInAssetSet"
+ "hasCountOfOTAAssetsInAssetSet"
+ "hasCountOfPSUSAssetsInAssetSet"
+ "hasCountOfPSUSAssetsPromotedInCurrentOS"
+ "hasCurrentBuildVersion"
+ "hasDatasetsCapturedTimestampMs"
+ "hasDimensionNameIndex"
+ "hasDimensionValue"
+ "hasDimensionValueBoolean"
+ "hasDimensionValueFloat"
+ "hasDimensionValueInteger"
+ "hasErrorKind"
+ "hasEstimatedSiriMissCount"
+ "hasExecutorAppIntentAttribution"
+ "hasExecutorAppIntentMetrics"
+ "hasExecutorAppIntentTargetType"
+ "hasExecutorAppIntentTask"
+ "hasExplainabilityIdentifier"
+ "hasFalseWakeWithAcousticMitigationCount"
+ "hasFalseWakeWithContextualMitigationCount"
+ "hasFalseWakeWithLwSpkidMitigationCount"
+ "hasHasMultiKeyboards"
+ "hasIfPlatformRequestStructuredError"
+ "hasIsAmbiguousRequest"
+ "hasIsAppBroughtToForeground"
+ "hasIsGenAIAware"
+ "hasIsProcessLaunchRequired"
+ "hasIsRedacted"
+ "hasIsSuitableForGenAI"
+ "hasLwSpkidMitigatorAcceptPostLwSpkidMitigationCount"
+ "hasMachTimeEnd"
+ "hasMachTimeStart"
+ "hasMetricDuration"
+ "hasMetricsNameIndex"
+ "hasModelVersionStr"
+ "hasMultiKeyboards"
+ "hasNeuralFallbackCount"
+ "hasOnDevice"
+ "hasOrchMode"
+ "hasOrchestrationMode"
+ "hasPartOfARequest"
+ "hasPhsRejectCount"
+ "hasPnrodSiriMetricsAndDims"
+ "hasPreviousBuildVersion"
+ "hasRequestUUID"
+ "hasResolveId"
+ "hasScheduleType"
+ "hasSecondPassAcceptCount"
+ "hasSecondPassRejectCount"
+ "hasSensor"
+ "hasSessionUUID"
+ "hasSiriActivationCount"
+ "hasSkimmerId"
+ "hasSpeechDatasetsRecord"
+ "hasStartedLiveActivity"
+ "hasTextToSpeak"
+ "hasTimeInSecondsSinceSoftwareUpdate"
+ "hasTotalNumberOfBytesDownloaded"
+ "hasTotalSizeOfAssetsInAssetSet"
+ "hasTotalSizeOfFactoryAssetsInAssetSet"
+ "hasTotalSizeOfOTAAssetsInAssetSet"
+ "hasTotalSizeOfPSUSAssetsInAssetSet"
+ "hasTtsStatus"
+ "hasUafAssetSource"
+ "hasVocalizerFallbackCount"
+ "ifPlatformRequestStructuredError"
+ "isAmbiguousRequest"
+ "isAppBroughtToForeground"
+ "isGenAIAware"
+ "isProcessLaunchRequired"
+ "isRedacted"
+ "isSuitableForGenAI"
+ "lwSpkidMitigatorAcceptPostLwSpkidMitigationCount"
+ "machTimeEnd"
+ "machTimeStart"
+ "metricDuration"
+ "metricsNameIndex"
+ "modelSelectedOptions"
+ "modelSelectedOptionsAtIndex:"
+ "modelSelectedOptionsCount"
+ "modelVersionStr"
+ "nearMissCheckerScoreList"
+ "nearMissCheckerScoreListAtIndex:"
+ "nearMissCheckerScoreListCount"
+ "nearMissCheckerScoreLists"
+ "nearMissPitchList"
+ "nearMissPitchListAtIndex:"
+ "nearMissPitchListCount"
+ "nearMissPitchLists"
+ "nearMissSNRList"
+ "nearMissSNRListAtIndex:"
+ "nearMissSNRListCount"
+ "nearMissSNRLists"
+ "nearMissWithRetryList"
+ "nearMissWithRetryListAtIndex:"
+ "nearMissWithRetryListCount"
+ "nearMissWithRetryLists"
+ "nearMissWithTriggerPhraseList"
+ "nearMissWithTriggerPhraseListAtIndex:"
+ "nearMissWithTriggerPhraseListCount"
+ "nearMissWithTriggerPhraseLists"
+ "neuralFallbackCount"
+ "onDevice"
+ "orchMode"
+ "orchestrationMode"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.requestReceivedTier1.textToSpeak"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.speechContext.startedOrChanged.textToSpeak"
+ "orderedMessages.siriEventTypeUnion.ttsClientEvent.synthesisContext.startedOrChanged.textToSpeak"
+ "partOfARequest"
+ "phsRejectCount"
+ "pnrodSiriMetricsAndDims"
+ "pnrodSiriMetricsAndDims.dimensionValue.toolId"
+ "previousBuildVersion"
+ "readString"
+ "requestReceivedTier1.textToSpeak"
+ "requestUUID"
+ "resolveId"
+ "scheduleType"
+ "secondPassAcceptCount"
+ "secondPassRejectCount"
+ "sensor"
+ "sessionUUID"
+ "setAcousticMitigatorAcceptPostAcousticMitigationCount:"
+ "setAltDsId:"
+ "setAssetBringUpDigestsReported:"
+ "setAssetBringUpErrorCode:"
+ "setAssetBringUpErrorDescription:"
+ "setAssetBringUpErrorDomain:"
+ "setAssetBringUpState:"
+ "setAssetBringUpType:"
+ "setAssetSetIdentifier:"
+ "setAssistantVoicesDigestsReported:"
+ "setAutoMOSs:"
+ "setClassifiedString:"
+ "setComponentInvocationId:"
+ "setConnectionDurationInNanoSeconds:"
+ "setContextualMitigatorAcceptPostContextualMitigationCount:"
+ "setCountOfAssetsInAssetSet:"
+ "setCountOfFactoryAssetsInAssetSet:"
+ "setCountOfOTAAssetsInAssetSet:"
+ "setCountOfPSUSAssetsInAssetSet:"
+ "setCountOfPSUSAssetsPromotedInCurrentOS:"
+ "setCurrentBuildVersion:"
+ "setCustomerPerceivedLatencyInSecs:"
+ "setDataClassificationManifests:"
+ "setDatasetsCapturedTimestampMs:"
+ "setDimensionNameIndex:"
+ "setDimensionValue:"
+ "setDimensionValueBoolean:"
+ "setDimensionValueFloat:"
+ "setDimensionValueInteger:"
+ "setEntityMetrics:"
+ "setErrorKind:"
+ "setErrors:"
+ "setEstimatedSiriMissCount:"
+ "setExecutorAppIntentAttribution:"
+ "setExecutorAppIntentMetrics:"
+ "setExecutorAppIntentSegments:"
+ "setExecutorAppIntentTargetType:"
+ "setExecutorAppIntentTask:"
+ "setExplainabilityIdentifier:"
+ "setExplainabilityIdentifiers:"
+ "setFalseWakeWithAcousticMitigationCount:"
+ "setFalseWakeWithContextualMitigationCount:"
+ "setFalseWakeWithLwSpkidMitigationCount:"
+ "setHasAcousticMitigatorAcceptPostAcousticMitigationCount:"
+ "setHasAssetBringUpDigestsReported:"
+ "setHasAssetBringUpErrorCode:"
+ "setHasAssetBringUpErrorDescription:"
+ "setHasAssetBringUpErrorDomain:"
+ "setHasAssetBringUpState:"
+ "setHasAssetBringUpType:"
+ "setHasAssetSetIdentifier:"
+ "setHasAssistantVoicesDigestsReported:"
+ "setHasClassifiedString:"
+ "setHasComponentInvocationId:"
+ "setHasConnectionDurationInNanoSeconds:"
+ "setHasContextualMitigatorAcceptPostContextualMitigationCount:"
+ "setHasCountOfAssetsInAssetSet:"
+ "setHasCountOfFactoryAssetsInAssetSet:"
+ "setHasCountOfOTAAssetsInAssetSet:"
+ "setHasCountOfPSUSAssetsInAssetSet:"
+ "setHasCountOfPSUSAssetsPromotedInCurrentOS:"
+ "setHasCurrentBuildVersion:"
+ "setHasDatasetsCapturedTimestampMs:"
+ "setHasDimensionNameIndex:"
+ "setHasDimensionValue:"
+ "setHasDimensionValueBoolean:"
+ "setHasDimensionValueFloat:"
+ "setHasDimensionValueInteger:"
+ "setHasErrorKind:"
+ "setHasEstimatedSiriMissCount:"
+ "setHasExecutorAppIntentAttribution:"
+ "setHasExecutorAppIntentMetrics:"
+ "setHasExecutorAppIntentTargetType:"
+ "setHasExecutorAppIntentTask:"
+ "setHasExplainabilityIdentifier:"
+ "setHasFalseWakeWithAcousticMitigationCount:"
+ "setHasFalseWakeWithContextualMitigationCount:"
+ "setHasFalseWakeWithLwSpkidMitigationCount:"
+ "setHasHasMultiKeyboards:"
+ "setHasIfPlatformRequestStructuredError:"
+ "setHasIsAmbiguousRequest:"
+ "setHasIsAppBroughtToForeground:"
+ "setHasIsGenAIAware:"
+ "setHasIsProcessLaunchRequired:"
+ "setHasIsRedacted:"
+ "setHasIsSuitableForGenAI:"
+ "setHasLwSpkidMitigatorAcceptPostLwSpkidMitigationCount:"
+ "setHasMachTimeEnd:"
+ "setHasMachTimeStart:"
+ "setHasMetricDuration:"
+ "setHasMetricsNameIndex:"
+ "setHasModelVersionStr:"
+ "setHasMultiKeyboards:"
+ "setHasNeuralFallbackCount:"
+ "setHasOnDevice:"
+ "setHasOrchMode:"
+ "setHasOrchestrationMode:"
+ "setHasPartOfARequest:"
+ "setHasPhsRejectCount:"
+ "setHasPnrodSiriMetricsAndDims:"
+ "setHasPreviousBuildVersion:"
+ "setHasRequestUUID:"
+ "setHasResolveId:"
+ "setHasScheduleType:"
+ "setHasSecondPassAcceptCount:"
+ "setHasSecondPassRejectCount:"
+ "setHasSensor:"
+ "setHasSessionUUID:"
+ "setHasSiriActivationCount:"
+ "setHasSkimmerId:"
+ "setHasSpeechDatasetsRecord:"
+ "setHasStartedLiveActivity:"
+ "setHasTextToSpeak:"
+ "setHasTimeInSecondsSinceSoftwareUpdate:"
+ "setHasTotalNumberOfBytesDownloaded:"
+ "setHasTotalSizeOfAssetsInAssetSet:"
+ "setHasTotalSizeOfFactoryAssetsInAssetSet:"
+ "setHasTotalSizeOfOTAAssetsInAssetSet:"
+ "setHasTotalSizeOfPSUSAssetsInAssetSet:"
+ "setHasTtsStatus:"
+ "setHasUafAssetSource:"
+ "setHasVocalizerFallbackCount:"
+ "setIfPlatformRequestStructuredError:"
+ "setIsAmbiguousRequest:"
+ "setIsAppBroughtToForeground:"
+ "setIsGenAIAware:"
+ "setIsProcessLaunchRequired:"
+ "setIsRedacted:"
+ "setIsSuitableForGenAI:"
+ "setLwSpkidMitigatorAcceptPostLwSpkidMitigationCount:"
+ "setMachTimeEnd:"
+ "setMachTimeStart:"
+ "setMetricDuration:"
+ "setMetricsNameIndex:"
+ "setModelSelectedOptions:"
+ "setModelVersionStr:"
+ "setNearMissCheckerScoreLists:"
+ "setNearMissPitchLists:"
+ "setNearMissSNRLists:"
+ "setNearMissWithRetryLists:"
+ "setNearMissWithTriggerPhraseLists:"
+ "setNeuralFallbackCount:"
+ "setOnDevice:"
+ "setOrchMode:"
+ "setOrchestrationMode:"
+ "setPartOfARequest:"
+ "setPhsRejectCount:"
+ "setPnrodSiriMetricsAndDims:"
+ "setPreviousBuildVersion:"
+ "setRequestUUID:"
+ "setResolveId:"
+ "setScheduleType:"
+ "setSecondPassAcceptCount:"
+ "setSecondPassRejectCount:"
+ "setSensor:"
+ "setSessionUUID:"
+ "setSiriActivationCount:"
+ "setSiriUnavailabilityReasons:"
+ "setSkimmerId:"
+ "setSpeakingDurationInSecs:"
+ "setSpeechDatasetsRecord:"
+ "setStartedLiveActivity:"
+ "setTextToSpeak:"
+ "setTimeInSecondsSinceSoftwareUpdate:"
+ "setTotalNumberOfBytesDownloaded:"
+ "setTotalSizeOfAssetsInAssetSet:"
+ "setTotalSizeOfFactoryAssetsInAssetSet:"
+ "setTotalSizeOfOTAAssetsInAssetSet:"
+ "setTotalSizeOfPSUSAssetsInAssetSet:"
+ "setTtsStatus:"
+ "setUafAssetSource:"
+ "setVocalizerFallbackCount:"
+ "siriActivationCount"
+ "siriUnavailabilityReasons"
+ "siriUnavailabilityReasonsAtIndex:"
+ "siriUnavailabilityReasonsCount"
+ "skimmerId"
+ "speakingDurationInSec"
+ "speakingDurationInSecAtIndex:"
+ "speakingDurationInSecCount"
+ "speakingDurationInSecs"
+ "speechContext.startedOrChanged.textToSpeak"
+ "speechDatasetsRecord"
+ "speechDatasetsRecord.interactionId"
+ "startedLiveActivity"
+ "synthesisContext.startedOrChanged.textToSpeak"
+ "textToSpeak"
+ "timeInSecondsSinceSoftwareUpdate"
+ "totalNumberOfBytesDownloaded"
+ "totalSizeOfAssetsInAssetSet"
+ "totalSizeOfFactoryAssetsInAssetSet"
+ "totalSizeOfOTAAssetsInAssetSet"
+ "totalSizeOfPSUSAssetsInAssetSet"
+ "ttsStatus"
+ "uafAssetSource"
+ "vocalizerFallbackCount"
+ "whichProvenance_Type"
+ "writeString:forTag:"
+ "{?=\"assetBringUpState\"b1\"assetBringUpType\"b1\"assetBringUpErrorCode\"b1\"countOfPSUSAssetsPromotedInCurrentOS\"b1\"timeInSecondsSinceSoftwareUpdate\"b1\"countOfAssetsInAssetSet\"b1\"totalSizeOfAssetsInAssetSet\"b1\"countOfFactoryAssetsInAssetSet\"b1\"totalSizeOfFactoryAssetsInAssetSet\"b1\"countOfOTAAssetsInAssetSet\"b1\"totalSizeOfOTAAssetsInAssetSet\"b1\"countOfPSUSAssetsInAssetSet\"b1\"totalSizeOfPSUSAssetsInAssetSet\"b1}"
+ "{?=\"assetBringUpState\"b1\"assetBringUpType\"b1\"assetBringUpErrorCode\"b1\"countOfPSUSAssetsPromotedInCurrentOS\"b1\"timeInSecondsSinceSoftwareUpdate\"b1\"uafAssetSource\"b1\"countOfAssetsInAssetSet\"b1\"totalSizeOfAssetsInAssetSet\"b1}"
+ "{?=\"buildInstallationTimestampInSecondsSince1970\"b1\"durationFromBootToFirstRequestSeconds\"b1\"durationFromSoftwareUpdateToFirstRequestSeconds\"b1\"durationFromClassCUnlockToFirstRequestSeconds\"b1\"orchMode\"b1}"
+ "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1\"isContentFree\"b1\"isUserRecognized\"b1\"serverSearchResultsMediaType\"b1\"userPersona\"b1\"isModelDisambiguation\"b1\"isModelConfirmation\"b1}"
+ "{?=\"componentIndex\"b1}"
+ "{?=\"connectionDurationInNanoSeconds\"b1\"executorAppIntentTargetType\"b1\"isProcessLaunchRequired\"b1\"isAppBroughtToForeground\"b1\"startedLiveActivity\"b1}"
+ "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1\"totalNumberOfBytesDownloaded\"b1}"
+ "{?=\"datasetsCapturedTimestampMs\"b1}"
+ "{?=\"dimensionNameIndex\"b1\"dimensionValueInteger\"b1\"dimensionValueFloat\"b1\"dimensionValueBoolean\"b1}"
+ "{?=\"entityCategory\"b1\"numEntities\"b1}"
+ "{?=\"executorAppIntentTask\"b1\"executorAppIntentAttribution\"b1\"machTimeStart\"b1\"machTimeEnd\"b1}"
+ "{?=\"exists\"b1\"result\"b1}"
+ "{?=\"extensionName\"b1\"executionStatus\"b1\"scheduleType\"b1}"
+ "{?=\"isRedacted\"b1}"
+ "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1\"totalNumberOfBytesDownloaded\"b1}"
+ "{?=\"metricValue\"b1\"startTimestamp\"b1\"startEventIndex\"b1\"endEventIndex\"b1\"metricsNameIndex\"b1}"
+ "{?=\"neuralFallbackCount\"b1\"vocalizerFallbackCount\"b1}"
+ "{?=\"partOfARequest\"b1\"kind\"b1}"
+ "{?=\"phsRejectBeforeActivationCount\"b1\"checkerRejectBeforeActivationCount\"b1\"checkerNearMissBeforeAcceptCount\"b1\"falseWakeWithNoTriggerPhraseCount\"b1\"falseWakeWithSpeechNoMatchCount\"b1\"falseWakeWithTTMMitigationCount\"b1\"ncAcceptPostNcMitigationCount\"b1\"spkidAcceptPostSpkidMitigationCount\"b1\"ttmAcceptPostTtmMitigationCount\"b1\"estimatedSiriMissCount\"b1\"secondPassRejectCount\"b1\"secondPassAcceptCount\"b1\"siriActivationCount\"b1\"phsRejectCount\"b1\"hasMultiKeyboards\"b1\"acousticMitigatorAcceptPostAcousticMitigationCount\"b1\"contextualMitigatorAcceptPostContextualMitigationCount\"b1\"lwSpkidMitigatorAcceptPostLwSpkidMitigationCount\"b1\"falseWakeWithAcousticMitigationCount\"b1\"falseWakeWithContextualMitigationCount\"b1\"falseWakeWithLwSpkidMitigationCount\"b1}"
+ "{?=\"product\"b1\"reason\"b1\"orchestrationMode\"b1}"
+ "{?=\"reason\"b1\"errorKind\"b1}"
+ "{?=\"requestOriginLocale\"b1\"requestOriginLanguage\"b1\"communicationType\"b1\"appResolutionType\"b1\"userPersona\"b1\"isModelDisambiguation\"b1\"isModelConfirmation\"b1}"
+ "{?=\"thirdPartyGenAIAgent\"b1\"requestStatus\"b1\"isExplicitGenAIRequest\"b1\"requestType\"b1\"isGenAIAware\"b1\"isSuitableForGenAI\"b1\"isAmbiguousRequest\"b1}"
+ "{?=\"voiceType\"b1\"synthesisSource\"b1\"clientId\"b1\"ttsStatus\"b1}"
+ "{?=}"
- "@\"GATSchemaGATConfirmationSnippetPresented\""
- "@\"GATSchemaGATConfirmationSnippetUserActioned\""
- "T@\"GATSchemaGATConfirmationSnippetPresented\",&,N,V_confirmationSnippetPresented"
- "T@\"GATSchemaGATConfirmationSnippetUserActioned\",&,N,V_confirmationSnippetUserActioned"
- "TB,N,V_hasConfirmationSnippetPresented"
- "TB,N,V_hasConfirmationSnippetUserActioned"
- "_confirmationSnippetPresented"
- "_confirmationSnippetUserActioned"
- "_hasConfirmationSnippetPresented"
- "_hasConfirmationSnippetUserActioned"
- "com.apple.aiml.siri.gat.GATClientEvent.GATConfirmationSnippetPresented"
- "com.apple.aiml.siri.gat.GATClientEvent.GATConfirmationSnippetUserActioned"
- "confirmationSnippetPresented"
- "confirmationSnippetUserActioned"
- "deleteConfirmationSnippetPresented"
- "deleteConfirmationSnippetUserActioned"
- "hasConfirmationSnippetPresented"
- "hasConfirmationSnippetUserActioned"
- "setConfirmationSnippetPresented:"
- "setConfirmationSnippetUserActioned:"
- "setHasConfirmationSnippetPresented:"
- "setHasConfirmationSnippetUserActioned:"
- "{?=\"buildInstallationTimestampInSecondsSince1970\"b1\"durationFromBootToFirstRequestSeconds\"b1\"durationFromSoftwareUpdateToFirstRequestSeconds\"b1\"durationFromClassCUnlockToFirstRequestSeconds\"b1}"
- "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1\"isContentFree\"b1\"isUserRecognized\"b1\"serverSearchResultsMediaType\"b1}"
- "{?=\"currentStatus\"b1\"previousStatus\"b1\"timeSinceLastStatusChangeInSeconds\"b1\"timeSinceLastAvailabilityChangeInSeconds\"b1\"hasModelCatalogSubscriptionHashChangedFromLastStatus\"b1\"isAppleIntelligenceEligible\"b1\"isAppleIntelligenceAllowedThroughWaitlist\"b1\"isAppleIntelligenceToggled\"b1\"timeSinceLastEligibleChangeInSeconds\"b1\"timeSinceLastWaitlistChangeInSeconds\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"downloadState\"b1\"timeSinceLastModelCatalogSubscriptionHashChangeInSeconds\"b1\"useCase\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1}"
- "{?=\"extensionName\"b1\"executionStatus\"b1}"
- "{?=\"locale\"b1\"status\"b1\"currentSubscriptionHash\"b1\"downloadState\"b1\"timeSinceLastMobileAssetDownloadAttemptInSeconds\"b1\"timeSinceLastMobileAssetDownloadErrorInSeconds\"b1\"lastMobileAssetDownloadAttemptErrorCode\"b1\"errorCount\"b1\"sampledErrorCode\"b1\"sampledErrorHash\"b1\"sampledErrorUnderlyingCode\"b1\"timeSinceLastAppleIntelligenceToggleInSeconds\"b1\"timeSinceLastSubscriptionHashChangeInSeconds\"b1\"timeSinceLastBootInSeconds\"b1\"countPSUSAssets\"b1\"countRequiredAssets\"b1\"timeSinceLastSoftwareUpdateInSeconds\"b1\"timeSinceSampledErrorInSeconds\"b1\"buddyStatus\"b1\"invocationsCountWhileNotAvailable\"b1\"lastMobileAssetDownloadAttemptErrorUnderlyingCode\"b1\"mode\"b1\"subscriptionDownloadStatus\"b1\"timeSinceSubscriptionDownloadStatusCompleteInSeconds\"b1\"currentMode\"b1\"invocationsCountWhileAvailable\"b1\"numberOfMobileAssetAlters\"b1\"numberOfMobileAssetEliminates\"b1\"numberOfMobileAssetScans\"b1\"countFactoryAssetInBytes\"b1\"countFactoryAssets\"b1\"sizeInBytesPSUSAssets\"b1\"countPSUSAssetsMobileAsset\"b1\"totalBytesDownloaded\"b1}"
- "{?=\"metricValue\"b1\"startTimestamp\"b1\"startEventIndex\"b1\"endEventIndex\"b1}"
- "{?=\"phsRejectBeforeActivationCount\"b1\"checkerRejectBeforeActivationCount\"b1\"checkerNearMissBeforeAcceptCount\"b1\"falseWakeWithNoTriggerPhraseCount\"b1\"falseWakeWithSpeechNoMatchCount\"b1\"falseWakeWithTTMMitigationCount\"b1\"ncAcceptPostNcMitigationCount\"b1\"spkidAcceptPostSpkidMitigationCount\"b1\"ttmAcceptPostTtmMitigationCount\"b1}"
- "{?=\"product\"b1\"reason\"b1}"
- "{?=\"requestOriginLocale\"b1\"requestOriginLanguage\"b1\"communicationType\"b1\"appResolutionType\"b1\"userPersona\"b1}"
- "{?=\"thirdPartyGenAIAgent\"b1\"requestStatus\"b1\"isExplicitGenAIRequest\"b1\"requestType\"b1}"

```
