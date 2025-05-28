## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3303.2.1.0.0
-  __TEXT.__text: 0x63b734
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x89f30
-  __TEXT.__const: 0xac3c
-  __TEXT.__constg_swiftt: 0x46b4
-  __TEXT.__swift5_typeref: 0x10db
-  __TEXT.__swift5_builtin: 0x288c
-  __TEXT.__swift5_reflstr: 0x182
+3304.54.1.0.0
+  __TEXT.__text: 0x67aa8c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x8f880
+  __TEXT.__const: 0xb064
+  __TEXT.__constg_swiftt: 0x4870
+  __TEXT.__swift5_typeref: 0x11c2
+  __TEXT.__swift5_builtin: 0x2990
+  __TEXT.__swift5_reflstr: 0x192
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x89c
-  __TEXT.__swift5_types: 0x858
-  __TEXT.__cstring: 0x43409
-  __TEXT.__swift5_fieldmd: 0x2c0
+  __TEXT.__swift5_proto: 0x8d0
+  __TEXT.__swift5_types: 0x890
+  __TEXT.__cstring: 0x45d08
+  __TEXT.__swift5_fieldmd: 0x2e8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1bf6c
-  __TEXT.__eh_frame: 0x680
-  __TEXT.__objc_classname: 0xe238
-  __TEXT.__objc_methname: 0xc7271
-  __TEXT.__objc_methtype: 0x1bae9
-  __TEXT.__objc_stubs: 0x48f80
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x250c0
-  __DATA_CONST.__objc_classlist: 0x31c0
+  __TEXT.__unwind_info: 0x1d084
+  __TEXT.__eh_frame: 0x6f0
+  __TEXT.__objc_classname: 0xea95
+  __TEXT.__objc_methname: 0xcec64
+  __TEXT.__objc_methtype: 0x1cfda
+  __TEXT.__objc_stubs: 0x4bb80
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x26770
+  __DATA_CONST.__objc_classlist: 0x3378
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9d500
-  __DATA_CONST.__objc_selrefs: 0x265c8
-  __AUTH_CONST.__const: 0x918
-  __AUTH_CONST.__cfstring: 0x4ae80
+  __DATA_CONST.__objc_const: 0xa3918
+  __DATA_CONST.__objc_selrefs: 0x27cc0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x3320
+  __DATA_CONST.__objc_superrefs: 0x4e40
+  __AUTH_CONST.__const: 0xb70
+  __AUTH_CONST.__cfstring: 0x4dc40
   __AUTH_CONST.__auth_ptr: 0x58
-  __AUTH_CONST.__objc_const: 0x1b40
+  __AUTH_CONST.__objc_const: 0x2b48
   __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__auth_got: 0x758
-  __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3168
-  __DATA.__objc_superrefs: 0x4b50
-  __DATA.__objc_ivar: 0x9314
-  __DATA.__data: 0x13b8
-  __DATA.__bss: 0x10f80
-  __DATA.__common: 0x28
+  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH.__objc_data: 0x29e0
+  __DATA.__objc_ivar: 0x9914
+  __DATA.__data: 0x17d0
+  __DATA.__bss: 0x11600
+  __DATA.__common: 0x20
   __DATA_DIRTY.__const: 0x40d8
   __DATA_DIRTY.__objc_const: 0x1ba58
-  __DATA_DIRTY.__objc_data: 0x1d9c8
-  __DATA_DIRTY.__data: 0x5e8
-  __DATA_DIRTY.__bss: 0x300
-  __DATA_DIRTY.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x1db08
+  __DATA_DIRTY.__data: 0x5a8
+  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 49985
-  Symbols:   124569
-  CStrings:  44426
+  Functions: 51987
+  Symbols:   129507
+  CStrings:  46101
 
Symbols:
+ +[ODBATCHSiriSchemaODBATCHClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ +[PFAPFAClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[ASRSchemaASREntityMetadata deleteEntityRank]
+ -[ASRSchemaASREntityMetadata dictionaryRepresentation]
+ -[ASRSchemaASREntityMetadata entityRank]
+ -[ASRSchemaASREntityMetadata hasEntityRank]
+ -[ASRSchemaASREntityMetadata hash]
+ -[ASRSchemaASREntityMetadata initWithDictionary:]
+ -[ASRSchemaASREntityMetadata initWithJSON:]
+ -[ASRSchemaASREntityMetadata isEqual:]
+ -[ASRSchemaASREntityMetadata jsonData]
+ -[ASRSchemaASREntityMetadata readFrom:]
+ -[ASRSchemaASREntityMetadata setEntityRank:]
+ -[ASRSchemaASREntityMetadata setHasEntityRank:]
+ -[ASRSchemaASREntityMetadata writeTo:]
+ -[ASRSchemaASREntityMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRRecognitionMetrics deleteNumIngestedNeuralContextualBiasingEmbeddings]
+ -[ASRSchemaASRRecognitionMetrics hasNumIngestedNeuralContextualBiasingEmbeddings]
+ -[ASRSchemaASRRecognitionMetrics numIngestedNeuralContextualBiasingEmbeddings]
+ -[ASRSchemaASRRecognitionMetrics setHasNumIngestedNeuralContextualBiasingEmbeddings:]
+ -[ASRSchemaASRRecognitionMetrics setNumIngestedNeuralContextualBiasingEmbeddings:]
+ -[ASRSchemaASRToken deleteEntityMetadata]
+ -[ASRSchemaASRToken entityMetadata]
+ -[ASRSchemaASRToken hasEntityMetadata]
+ -[ASRSchemaASRToken setEntityMetadata:]
+ -[ASRSchemaASRToken setHasEntityMetadata:]
+ -[ASRSchemaASRToken(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMClientEvent deleteExperimentContext]
+ -[DIMSchemaDIMClientEvent experimentContext]
+ -[DIMSchemaDIMClientEvent hasExperimentContext]
+ -[DIMSchemaDIMClientEvent setExperimentContext:]
+ -[DIMSchemaDIMClientEvent setHasExperimentContext:]
+ -[DIMSchemaDIMExperimentContext .cxx_destruct]
+ -[DIMSchemaDIMExperimentContext addExperimentInfo:]
+ -[DIMSchemaDIMExperimentContext clearExperimentInfo]
+ -[DIMSchemaDIMExperimentContext deleteExperimentInfo]
+ -[DIMSchemaDIMExperimentContext dictionaryRepresentation]
+ -[DIMSchemaDIMExperimentContext experimentInfoAtIndex:]
+ -[DIMSchemaDIMExperimentContext experimentInfoCount]
+ -[DIMSchemaDIMExperimentContext experimentInfos]
+ -[DIMSchemaDIMExperimentContext hash]
+ -[DIMSchemaDIMExperimentContext initWithDictionary:]
+ -[DIMSchemaDIMExperimentContext initWithJSON:]
+ -[DIMSchemaDIMExperimentContext isEqual:]
+ -[DIMSchemaDIMExperimentContext jsonData]
+ -[DIMSchemaDIMExperimentContext readFrom:]
+ -[DIMSchemaDIMExperimentContext setExperimentInfos:]
+ -[DIMSchemaDIMExperimentContext writeTo:]
+ -[DIMSchemaDIMExperimentContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMExperimentContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[DIMSchemaDIMExperimentInfo .cxx_destruct]
+ -[DIMSchemaDIMExperimentInfo deleteDeploymentId]
+ -[DIMSchemaDIMExperimentInfo deleteExperimentId]
+ -[DIMSchemaDIMExperimentInfo deleteTreatmentId]
+ -[DIMSchemaDIMExperimentInfo deploymentId]
+ -[DIMSchemaDIMExperimentInfo dictionaryRepresentation]
+ -[DIMSchemaDIMExperimentInfo experimentId]
+ -[DIMSchemaDIMExperimentInfo hasDeploymentId]
+ -[DIMSchemaDIMExperimentInfo hasExperimentId]
+ -[DIMSchemaDIMExperimentInfo hasTreatmentId]
+ -[DIMSchemaDIMExperimentInfo hash]
+ -[DIMSchemaDIMExperimentInfo initWithDictionary:]
+ -[DIMSchemaDIMExperimentInfo initWithJSON:]
+ -[DIMSchemaDIMExperimentInfo isEqual:]
+ -[DIMSchemaDIMExperimentInfo jsonData]
+ -[DIMSchemaDIMExperimentInfo readFrom:]
+ -[DIMSchemaDIMExperimentInfo setDeploymentId:]
+ -[DIMSchemaDIMExperimentInfo setExperimentId:]
+ -[DIMSchemaDIMExperimentInfo setHasDeploymentId:]
+ -[DIMSchemaDIMExperimentInfo setHasExperimentId:]
+ -[DIMSchemaDIMExperimentInfo setHasTreatmentId:]
+ -[DIMSchemaDIMExperimentInfo setTreatmentId:]
+ -[DIMSchemaDIMExperimentInfo treatmentId]
+ -[DIMSchemaDIMExperimentInfo writeTo:]
+ -[DIMSchemaDIMExperimentInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMExperimentInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[INFERENCESchemaINFERENCECRRTrainingSampleCollected crrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECRRTrainingSampleCollected deleteCrrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECRRTrainingSampleCollected hasCrrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECRRTrainingSampleCollected setCrrCommsAppSelectionJointId:]
+ -[INFERENCESchemaINFERENCECRRTrainingSampleCollected setHasCrrCommsAppSelectionJointId:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated crrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated deleteCrrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated hasCrrCommsAppSelectionJointId]
+ -[INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated setCrrCommsAppSelectionJointId:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated setHasCrrCommsAppSelectionJointId:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals appFreqForMessagesForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals appFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals appFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals deleteAppFreqForMessagesForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals deleteAppFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals deleteAppFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals hasAppFreqForMessagesForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals hasAppFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals hasAppFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setAppFreqForMessages:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setAppFreqForMessagesForCountryCode:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setAppFreqForMessagesUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setHasAppFreqForMessages:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setHasAppFreqForMessagesForCountryCode:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals setHasAppFreqForMessagesUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals appFreqForPhoneCallForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals appFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals appFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals deleteAppFreqForPhoneCallForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals deleteAppFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals deleteAppFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals hasAppFreqForPhoneCallForCountryCode]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals hasAppFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals hasAppFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setAppFreqForPhoneCall:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setAppFreqForPhoneCallForCountryCode:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setAppFreqForPhoneCallUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setHasAppFreqForPhoneCall:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setHasAppFreqForPhoneCallForCountryCode:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals setHasAppFreqForPhoneCallUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals appTimeSpentInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals deleteAppTimeSpentInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals deleteTimeSinceAppContactLastLaunchedInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals hasAppTimeSpentInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals hasTimeSinceAppContactLastLaunchedInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setAppTimeSpentInSec:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setHasAppTimeSpentInSec:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setHasTimeSinceAppContactLastLaunchedInSec:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setTimeSinceAppContactLastLaunchedInSec:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals timeSinceAppContactLastLaunchedInSec]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessagesHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessagesInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals appContactFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessagesHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessagesInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals deleteAppContactFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessagesHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessagesInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessagesUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals hasAppContactFreqForMessages]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages10Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages1Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages1Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages28Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages2Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages6Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages7Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessages:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessagesHaptic:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessagesInf:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setAppContactFreqForMessagesUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages10Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages1Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages1Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages28Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages2Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages6Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages7Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessages:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessagesHaptic:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessagesInf:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals setHasAppContactFreqForMessagesUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCallHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCallInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals appContactFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCallHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCallInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals deleteAppContactFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall10Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall1Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall1Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall28Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall2Min]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall6Hr]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall7Day]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCallHaptic]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCallInf]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCallUsingSiri]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals hasAppContactFreqForPhoneCall]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall10Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall1Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall1Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall28Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall2Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall6Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall7Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCall:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCallHaptic:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCallInf:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setAppContactFreqForPhoneCallUsingSiri:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall10Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall1Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall1Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall28Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall2Min:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall6Hr:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall7Day:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCall:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCallHaptic:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCallInf:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals setHasAppContactFreqForPhoneCallUsingSiri:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteEntitySearchBundleScoreRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteUsageScoreBooksRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteUsageScoreMusicRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteUsageScoreMusicWithoutRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteUsageScorePodcastsRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteUsageScoreRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals entitySearchBundleScoreRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasEntitySearchBundleScoreRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasUsageScoreBooksRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasUsageScoreMusicRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasUsageScoreMusicWithoutRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasUsageScorePodcastsRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasUsageScoreRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setEntitySearchBundleScoreRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasEntitySearchBundleScoreRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasUsageScoreBooksRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasUsageScoreMusicRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasUsageScoreMusicWithoutRadioRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasUsageScorePodcastsRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasUsageScoreRadioRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setUsageScoreBooksRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setUsageScoreMusicRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setUsageScoreMusicWithoutRadioRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setUsageScorePodcastsRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setUsageScoreRadioRemote:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals usageScoreBooksRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals usageScoreMusicRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals usageScoreMusicWithoutRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals usageScorePodcastsRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals usageScoreRadioRemote]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteServerSearchResultsMediaType]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasServerSearchResultsMediaType]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals serverSearchResultsMediaType]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasServerSearchResultsMediaType:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setServerSearchResultsMediaType:]
+ -[MHSchemaMHOdldFalseTriggerMitigated anchorRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated anchorSocialScore]
+ -[MHSchemaMHOdldFalseTriggerMitigated deleteAnchorRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated deleteAnchorSocialScore]
+ -[MHSchemaMHOdldFalseTriggerMitigated deletePreviousRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated hasAnchorRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated hasAnchorSocialScore]
+ -[MHSchemaMHOdldFalseTriggerMitigated hasPreviousRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated previousRequestId]
+ -[MHSchemaMHOdldFalseTriggerMitigated setAnchorRequestId:]
+ -[MHSchemaMHOdldFalseTriggerMitigated setAnchorSocialScore:]
+ -[MHSchemaMHOdldFalseTriggerMitigated setHasAnchorRequestId:]
+ -[MHSchemaMHOdldFalseTriggerMitigated setHasAnchorSocialScore:]
+ -[MHSchemaMHOdldFalseTriggerMitigated setHasPreviousRequestId:]
+ -[MHSchemaMHOdldFalseTriggerMitigated setPreviousRequestId:]
+ -[MHSchemaMHOdldFalseTriggerMitigated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NETSchemaNETClientEventMetadata deleteNetworkConnectionId]
+ -[NETSchemaNETClientEventMetadata deleteProvider]
+ -[NETSchemaNETClientEventMetadata hasNetworkConnectionId]
+ -[NETSchemaNETClientEventMetadata hasProvider]
+ -[NETSchemaNETClientEventMetadata networkConnectionId]
+ -[NETSchemaNETClientEventMetadata provider]
+ -[NETSchemaNETClientEventMetadata setHasNetworkConnectionId:]
+ -[NETSchemaNETClientEventMetadata setHasProvider:]
+ -[NETSchemaNETClientEventMetadata setNetworkConnectionId:]
+ -[NETSchemaNETClientEventMetadata setProvider:]
+ -[NETSchemaNETDebugNetworkInterface .cxx_destruct]
+ -[NETSchemaNETDebugNetworkInterface deleteNetworkInterface]
+ -[NETSchemaNETDebugNetworkInterface hasNetworkInterface]
+ -[NETSchemaNETDebugNetworkInterface networkInterface]
+ -[NETSchemaNETDebugNetworkInterface setHasNetworkInterface:]
+ -[NETSchemaNETDebugNetworkInterface setNetworkInterface:]
+ -[NETSchemaNETDebugNetworkInterface(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent .cxx_destruct]
+ -[ODBATCHSiriSchemaODBATCHClientEvent deleteEventMetadata]
+ -[ODBATCHSiriSchemaODBATCHClientEvent deleteOdbatchDataReported]
+ -[ODBATCHSiriSchemaODBATCHClientEvent dictionaryRepresentation]
+ -[ODBATCHSiriSchemaODBATCHClientEvent eventMetadata]
+ -[ODBATCHSiriSchemaODBATCHClientEvent hasEventMetadata]
+ -[ODBATCHSiriSchemaODBATCHClientEvent hasOdbatchDataReported]
+ -[ODBATCHSiriSchemaODBATCHClientEvent hash]
+ -[ODBATCHSiriSchemaODBATCHClientEvent initWithDictionary:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent initWithJSON:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent isEqual:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent jsonData]
+ -[ODBATCHSiriSchemaODBATCHClientEvent odbatchDataReported]
+ -[ODBATCHSiriSchemaODBATCHClientEvent qualifiedMessageName]
+ -[ODBATCHSiriSchemaODBATCHClientEvent readFrom:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent setEventMetadata:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent setHasEventMetadata:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent setHasOdbatchDataReported:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent setOdbatchDataReported:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent whichEvent_Type]
+ -[ODBATCHSiriSchemaODBATCHClientEvent writeTo:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(InnerEventContainer) innerEvent]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(InnerEventContainer) whichInnerEventType]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(IsolationLevel) clockIsolationLevel]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODBATCHSiriSchemaODBATCHClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata .cxx_destruct]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata deleteOdbatchId]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata dictionaryRepresentation]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata hasOdbatchId]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata hash]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata initWithDictionary:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata initWithJSON:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata isEqual:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata jsonData]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata odbatchId]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata readFrom:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata setHasOdbatchId:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata setOdbatchId:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata writeTo:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODBATCHSiriSchemaODBATCHClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODBATCHSiriSchemaODBATCHDataReported .cxx_destruct]
+ -[ODBATCHSiriSchemaODBATCHDataReported daysWithTwoAssistantSpeechRequestsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported daysWithTwoValidAssistantTurnsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported deleteDaysWithTwoAssistantSpeechRequestsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported deleteDaysWithTwoValidAssistantTurnsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported deleteOriginalClockId]
+ -[ODBATCHSiriSchemaODBATCHDataReported dictionaryRepresentation]
+ -[ODBATCHSiriSchemaODBATCHDataReported hasDaysWithTwoAssistantSpeechRequestsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported hasDaysWithTwoValidAssistantTurnsPerWeek]
+ -[ODBATCHSiriSchemaODBATCHDataReported hasOriginalClockId]
+ -[ODBATCHSiriSchemaODBATCHDataReported hash]
+ -[ODBATCHSiriSchemaODBATCHDataReported initWithDictionary:]
+ -[ODBATCHSiriSchemaODBATCHDataReported initWithJSON:]
+ -[ODBATCHSiriSchemaODBATCHDataReported isEqual:]
+ -[ODBATCHSiriSchemaODBATCHDataReported jsonData]
+ -[ODBATCHSiriSchemaODBATCHDataReported originalClockId]
+ -[ODBATCHSiriSchemaODBATCHDataReported readFrom:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setDaysWithTwoAssistantSpeechRequestsPerWeek:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setDaysWithTwoValidAssistantTurnsPerWeek:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setHasDaysWithTwoAssistantSpeechRequestsPerWeek:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setHasDaysWithTwoValidAssistantTurnsPerWeek:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setHasOriginalClockId:]
+ -[ODBATCHSiriSchemaODBATCHDataReported setOriginalClockId:]
+ -[ODBATCHSiriSchemaODBATCHDataReported writeTo:]
+ -[ODBATCHSiriSchemaODBATCHDataReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODBATCHSiriSchemaODBATCHDataReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties adaptiveVolume]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties deleteAdaptiveVolume]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties deleteIsAdaptiveVolumeEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties deleteIsPermanentOffsetEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties deletePermanentOffsetFactor]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties hasAdaptiveVolume]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties hasIsAdaptiveVolumeEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties hasIsPermanentOffsetEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties hasPermanentOffsetFactor]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties hash]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties initWithDictionary:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties initWithJSON:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties isAdaptiveVolumeEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties isEqual:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties isPermanentOffsetEnabled]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties jsonData]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties permanentOffsetFactor]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties readFrom:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setAdaptiveVolume:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setHasAdaptiveVolume:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setHasIsAdaptiveVolumeEnabled:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setHasIsPermanentOffsetEnabled:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setHasPermanentOffsetFactor:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setIsAdaptiveVolumeEnabled:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setIsPermanentOffsetEnabled:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties setPermanentOffsetFactor:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties writeTo:]
+ -[ODDSiriSchemaODDAdaptiveVolumeProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAnnounceProperties carPlayStatus]
+ -[ODDSiriSchemaODDAnnounceProperties deleteCarPlayStatus]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsAnnounceCallsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsAnnounceNotificationsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsCarPlayMuted]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsEnabledForHeadphones]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsProximityCardSeen]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsReplyWithoutConfirmationEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties deleteIsSpokenNotificationsControlCenterModuleEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDAnnounceProperties hasCarPlayStatus]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsAnnounceCallsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsAnnounceNotificationsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsCarPlayMuted]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsEnabledForHeadphones]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsProximityCardSeen]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsReplyWithoutConfirmationEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties hasIsSpokenNotificationsControlCenterModuleEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties hash]
+ -[ODDSiriSchemaODDAnnounceProperties initWithDictionary:]
+ -[ODDSiriSchemaODDAnnounceProperties initWithJSON:]
+ -[ODDSiriSchemaODDAnnounceProperties isAnnounceCallsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties isAnnounceNotificationsEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties isCarPlayMuted]
+ -[ODDSiriSchemaODDAnnounceProperties isEnabledForHeadphones]
+ -[ODDSiriSchemaODDAnnounceProperties isEqual:]
+ -[ODDSiriSchemaODDAnnounceProperties isProximityCardSeen]
+ -[ODDSiriSchemaODDAnnounceProperties isReplyWithoutConfirmationEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties isSpokenNotificationsControlCenterModuleEnabled]
+ -[ODDSiriSchemaODDAnnounceProperties jsonData]
+ -[ODDSiriSchemaODDAnnounceProperties readFrom:]
+ -[ODDSiriSchemaODDAnnounceProperties setCarPlayStatus:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasCarPlayStatus:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsAnnounceCallsEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsAnnounceNotificationsEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsCarPlayMuted:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsEnabledForHeadphones:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsProximityCardSeen:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsReplyWithoutConfirmationEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setHasIsSpokenNotificationsControlCenterModuleEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsAnnounceCallsEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsAnnounceNotificationsEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsCarPlayMuted:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsEnabledForHeadphones:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsProximityCardSeen:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsReplyWithoutConfirmationEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties setIsSpokenNotificationsControlCenterModuleEnabled:]
+ -[ODDSiriSchemaODDAnnounceProperties writeTo:]
+ -[ODDSiriSchemaODDAnnounceProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest appTaskCounts]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest deleteAppTaskCounts]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest deleteDimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest dimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest hasAppTaskCounts]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest hasDimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest hash]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest initWithJSON:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest isEqual:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest jsonData]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest readFrom:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest setAppTaskCounts:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest setDimensions:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest setHasAppTaskCounts:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest writeTo:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported digests]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported hash]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported jsonData]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDimensions deleteResponseCategory]
+ -[ODDSiriSchemaODDAssistantDimensions hasResponseCategory]
+ -[ODDSiriSchemaODDAssistantDimensions responseCategory]
+ -[ODDSiriSchemaODDAssistantDimensions setHasResponseCategory:]
+ -[ODDSiriSchemaODDAssistantDimensions setResponseCategory:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantExperimentCounts deleteReliabilityCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts deleteSessionCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts deleteTaskCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts deleteTurnCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantExperimentCounts hasReliabilityCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts hasSessionCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts hasTaskCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts hasTurnCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts hash]
+ -[ODDSiriSchemaODDAssistantExperimentCounts initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts initWithJSON:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts isEqual:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts jsonData]
+ -[ODDSiriSchemaODDAssistantExperimentCounts readFrom:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts reliabilityCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts sessionCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setHasReliabilityCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setHasSessionCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setHasTaskCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setHasTurnCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setReliabilityCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setSessionCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setTaskCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts setTurnCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts taskCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts turnCounts]
+ -[ODDSiriSchemaODDAssistantExperimentCounts writeTo:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantExperimentCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantExperimentDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantExperimentDigest counts]
+ -[ODDSiriSchemaODDAssistantExperimentDigest deleteCounts]
+ -[ODDSiriSchemaODDAssistantExperimentDigest deleteDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigest deleteTuples]
+ -[ODDSiriSchemaODDAssistantExperimentDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantExperimentDigest dimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigest hasCounts]
+ -[ODDSiriSchemaODDAssistantExperimentDigest hasDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigest hasTuples]
+ -[ODDSiriSchemaODDAssistantExperimentDigest hash]
+ -[ODDSiriSchemaODDAssistantExperimentDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest initWithJSON:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest isEqual:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest jsonData]
+ -[ODDSiriSchemaODDAssistantExperimentDigest readFrom:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setHasCounts:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setHasTuples:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest setTuples:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest tuples]
+ -[ODDSiriSchemaODDAssistantExperimentDigest writeTo:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantExperimentDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported deleteDigestType]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported deleteExperimentFixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported digestType]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported digests]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported experimentFixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported hasDigestType]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported hasExperimentFixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported hash]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported jsonData]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setDigestType:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setExperimentFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setHasDigestType:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setHasExperimentFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantExperimentDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions assistantDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions codePathId]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions deleteAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions deleteCodePathId]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions deleteExperimentAllocationStatus]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions deleteIsFirstTriggerOrAfterFirstTrigger]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions deleteIsTriggered]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions experimentAllocationStatus]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hasAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hasCodePathId]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hasExperimentAllocationStatus]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hasIsFirstTriggerOrAfterFirstTrigger]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hasIsTriggered]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions hash]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions initWithJSON:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions isEqual:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions isFirstTriggerOrAfterFirstTrigger]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions isTriggered]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions jsonData]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions readFrom:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setCodePathId:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setExperimentAllocationStatus:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setHasAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setHasCodePathId:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setHasExperimentAllocationStatus:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setHasIsFirstTriggerOrAfterFirstTrigger:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setHasIsTriggered:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setIsFirstTriggerOrAfterFirstTrigger:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions setIsTriggered:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions writeTo:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantExperimentDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantExperimentTuples .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantExperimentTuples addEndpointDelayInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples addLaunchTimeInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples addSiriResponseTimeInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples addTimeToFirstWordInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples addTimeToUufrInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples clearEndpointDelayInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples clearLaunchTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples clearSiriResponseTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples clearTimeToFirstWordInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples clearTimeToUufrInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples deleteEndpointDelayInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples deleteLaunchTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples deleteSiriResponseTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples deleteTimeToFirstWordInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples deleteTimeToUufrInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantExperimentTuples endpointDelayInMsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples endpointDelayInMsCount]
+ -[ODDSiriSchemaODDAssistantExperimentTuples endpointDelayInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples hash]
+ -[ODDSiriSchemaODDAssistantExperimentTuples initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples initWithJSON:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples isEqual:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples jsonData]
+ -[ODDSiriSchemaODDAssistantExperimentTuples launchTimeInMsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples launchTimeInMsCount]
+ -[ODDSiriSchemaODDAssistantExperimentTuples launchTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples readFrom:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples setEndpointDelayInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples setLaunchTimeInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples setSiriResponseTimeInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples setTimeToFirstWordInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples setTimeToUufrInMs:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples siriResponseTimeInMsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples siriResponseTimeInMsCount]
+ -[ODDSiriSchemaODDAssistantExperimentTuples siriResponseTimeInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToFirstWordInMsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToFirstWordInMsCount]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToFirstWordInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToUufrInMsAtIndex:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToUufrInMsCount]
+ -[ODDSiriSchemaODDAssistantExperimentTuples timeToUufrInMs]
+ -[ODDSiriSchemaODDAssistantExperimentTuples writeTo:]
+ -[ODDSiriSchemaODDAssistantExperimentTuples(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantProperties .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantProperties deleteHomeKit]
+ -[ODDSiriSchemaODDAssistantProperties deleteInputLocale]
+ -[ODDSiriSchemaODDAssistantProperties deleteIsAssistantEnabled]
+ -[ODDSiriSchemaODDAssistantProperties deleteIsPreciseLocationEnabled]
+ -[ODDSiriSchemaODDAssistantProperties deleteListenFor]
+ -[ODDSiriSchemaODDAssistantProperties deleteNumSiriShortcutsEnabled]
+ -[ODDSiriSchemaODDAssistantProperties deleteOptIn]
+ -[ODDSiriSchemaODDAssistantProperties deleteVoice]
+ -[ODDSiriSchemaODDAssistantProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantProperties hasHomeKit]
+ -[ODDSiriSchemaODDAssistantProperties hasInputLocale]
+ -[ODDSiriSchemaODDAssistantProperties hasIsAssistantEnabled]
+ -[ODDSiriSchemaODDAssistantProperties hasIsPreciseLocationEnabled]
+ -[ODDSiriSchemaODDAssistantProperties hasListenFor]
+ -[ODDSiriSchemaODDAssistantProperties hasNumSiriShortcutsEnabled]
+ -[ODDSiriSchemaODDAssistantProperties hasOptIn]
+ -[ODDSiriSchemaODDAssistantProperties hasVoice]
+ -[ODDSiriSchemaODDAssistantProperties hash]
+ -[ODDSiriSchemaODDAssistantProperties homeKit]
+ -[ODDSiriSchemaODDAssistantProperties initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantProperties initWithJSON:]
+ -[ODDSiriSchemaODDAssistantProperties inputLocale]
+ -[ODDSiriSchemaODDAssistantProperties isAssistantEnabled]
+ -[ODDSiriSchemaODDAssistantProperties isEqual:]
+ -[ODDSiriSchemaODDAssistantProperties isPreciseLocationEnabled]
+ -[ODDSiriSchemaODDAssistantProperties jsonData]
+ -[ODDSiriSchemaODDAssistantProperties listenFor]
+ -[ODDSiriSchemaODDAssistantProperties numSiriShortcutsEnabled]
+ -[ODDSiriSchemaODDAssistantProperties optIn]
+ -[ODDSiriSchemaODDAssistantProperties readFrom:]
+ -[ODDSiriSchemaODDAssistantProperties setHasHomeKit:]
+ -[ODDSiriSchemaODDAssistantProperties setHasInputLocale:]
+ -[ODDSiriSchemaODDAssistantProperties setHasIsAssistantEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setHasIsPreciseLocationEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setHasListenFor:]
+ -[ODDSiriSchemaODDAssistantProperties setHasNumSiriShortcutsEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setHasOptIn:]
+ -[ODDSiriSchemaODDAssistantProperties setHasVoice:]
+ -[ODDSiriSchemaODDAssistantProperties setHomeKit:]
+ -[ODDSiriSchemaODDAssistantProperties setInputLocale:]
+ -[ODDSiriSchemaODDAssistantProperties setIsAssistantEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setIsPreciseLocationEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setListenFor:]
+ -[ODDSiriSchemaODDAssistantProperties setNumSiriShortcutsEnabled:]
+ -[ODDSiriSchemaODDAssistantProperties setOptIn:]
+ -[ODDSiriSchemaODDAssistantProperties setVoice:]
+ -[ODDSiriSchemaODDAssistantProperties voice]
+ -[ODDSiriSchemaODDAssistantProperties writeTo:]
+ -[ODDSiriSchemaODDAssistantProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAutoSendMessageProperties deleteIsAutomaticallySendMessagesEnabled]
+ -[ODDSiriSchemaODDAutoSendMessageProperties deleteIsEnabledForCarPlay]
+ -[ODDSiriSchemaODDAutoSendMessageProperties deleteIsEnabledForHeadphones]
+ -[ODDSiriSchemaODDAutoSendMessageProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDAutoSendMessageProperties hasIsAutomaticallySendMessagesEnabled]
+ -[ODDSiriSchemaODDAutoSendMessageProperties hasIsEnabledForCarPlay]
+ -[ODDSiriSchemaODDAutoSendMessageProperties hasIsEnabledForHeadphones]
+ -[ODDSiriSchemaODDAutoSendMessageProperties hash]
+ -[ODDSiriSchemaODDAutoSendMessageProperties initWithDictionary:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties initWithJSON:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties isAutomaticallySendMessagesEnabled]
+ -[ODDSiriSchemaODDAutoSendMessageProperties isEnabledForCarPlay]
+ -[ODDSiriSchemaODDAutoSendMessageProperties isEnabledForHeadphones]
+ -[ODDSiriSchemaODDAutoSendMessageProperties isEqual:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties jsonData]
+ -[ODDSiriSchemaODDAutoSendMessageProperties readFrom:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setHasIsAutomaticallySendMessagesEnabled:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setHasIsEnabledForCarPlay:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setHasIsEnabledForHeadphones:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setIsAutomaticallySendMessagesEnabled:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setIsEnabledForCarPlay:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties setIsEnabledForHeadphones:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties writeTo:]
+ -[ODDSiriSchemaODDAutoSendMessageProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDCarPlayProperties deleteIsShowAppsBehindSiriEnabledOnCarPlay]
+ -[ODDSiriSchemaODDCarPlayProperties deleteIsSiriCapableDigitalCarKeyAvailable]
+ -[ODDSiriSchemaODDCarPlayProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDCarPlayProperties hasIsShowAppsBehindSiriEnabledOnCarPlay]
+ -[ODDSiriSchemaODDCarPlayProperties hasIsSiriCapableDigitalCarKeyAvailable]
+ -[ODDSiriSchemaODDCarPlayProperties hash]
+ -[ODDSiriSchemaODDCarPlayProperties initWithDictionary:]
+ -[ODDSiriSchemaODDCarPlayProperties initWithJSON:]
+ -[ODDSiriSchemaODDCarPlayProperties isEqual:]
+ -[ODDSiriSchemaODDCarPlayProperties isShowAppsBehindSiriEnabledOnCarPlay]
+ -[ODDSiriSchemaODDCarPlayProperties isSiriCapableDigitalCarKeyAvailable]
+ -[ODDSiriSchemaODDCarPlayProperties jsonData]
+ -[ODDSiriSchemaODDCarPlayProperties readFrom:]
+ -[ODDSiriSchemaODDCarPlayProperties setHasIsShowAppsBehindSiriEnabledOnCarPlay:]
+ -[ODDSiriSchemaODDCarPlayProperties setHasIsSiriCapableDigitalCarKeyAvailable:]
+ -[ODDSiriSchemaODDCarPlayProperties setIsShowAppsBehindSiriEnabledOnCarPlay:]
+ -[ODDSiriSchemaODDCarPlayProperties setIsSiriCapableDigitalCarKeyAvailable:]
+ -[ODDSiriSchemaODDCarPlayProperties writeTo:]
+ -[ODDSiriSchemaODDCarPlayProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts cancelledSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts completedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts completedUIAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts deleteCancelledSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts deleteCompletedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts deleteCompletedUIAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts deleteFailedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts failedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts hasCancelledSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts hasCompletedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts hasCompletedUIAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts hasFailedSiriAppTaskCount]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts hash]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts initWithJSON:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts isEqual:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts jsonData]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts readFrom:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setCancelledSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setCompletedSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setCompletedUIAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setFailedSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setHasCancelledSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setHasCompletedSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setHasCompletedUIAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts setHasFailedSiriAppTaskCount:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts writeTo:]
+ -[ODDSiriSchemaODDDeviceAndUsageAppTaskCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions appTaskType]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions audioInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions deleteAppTaskType]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions deleteAudioInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions deleteSiriInputLocale]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions deleteTaskAppBundleId]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions deleteViewInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hasAppTaskType]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hasAudioInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hasSiriInputLocale]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hasTaskAppBundleId]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hasViewInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions hash]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions initWithJSON:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions isEqual:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions jsonData]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions readFrom:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setAppTaskType:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setAudioInterface:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setHasAppTaskType:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setHasAudioInterface:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setHasSiriInputLocale:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setHasTaskAppBundleId:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setHasViewInterface:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setSiriInputLocale:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setTaskAppBundleId:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions setViewInterface:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions siriInputLocale]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions taskAppBundleId]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions viewInterface]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions writeTo:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDeviceAndUsageDynamicDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationProperties .cxx_destruct]
+ -[ODDSiriSchemaODDDictationProperties addEnabledDictationLocales:]
+ -[ODDSiriSchemaODDDictationProperties clearEnabledDictationLocales]
+ -[ODDSiriSchemaODDDictationProperties deleteEnabledDictationLocales]
+ -[ODDSiriSchemaODDDictationProperties deleteIsAutoPunctuationEnabled]
+ -[ODDSiriSchemaODDDictationProperties deleteIsDictationEnabled]
+ -[ODDSiriSchemaODDDictationProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDDictationProperties enabledDictationLocalesAtIndex:]
+ -[ODDSiriSchemaODDDictationProperties enabledDictationLocalesCount]
+ -[ODDSiriSchemaODDDictationProperties enabledDictationLocales]
+ -[ODDSiriSchemaODDDictationProperties hasIsAutoPunctuationEnabled]
+ -[ODDSiriSchemaODDDictationProperties hasIsDictationEnabled]
+ -[ODDSiriSchemaODDDictationProperties hash]
+ -[ODDSiriSchemaODDDictationProperties initWithDictionary:]
+ -[ODDSiriSchemaODDDictationProperties initWithJSON:]
+ -[ODDSiriSchemaODDDictationProperties isAutoPunctuationEnabled]
+ -[ODDSiriSchemaODDDictationProperties isDictationEnabled]
+ -[ODDSiriSchemaODDDictationProperties isEqual:]
+ -[ODDSiriSchemaODDDictationProperties jsonData]
+ -[ODDSiriSchemaODDDictationProperties readFrom:]
+ -[ODDSiriSchemaODDDictationProperties setEnabledDictationLocales:]
+ -[ODDSiriSchemaODDDictationProperties setHasIsAutoPunctuationEnabled:]
+ -[ODDSiriSchemaODDDictationProperties setHasIsDictationEnabled:]
+ -[ODDSiriSchemaODDDictationProperties setIsAutoPunctuationEnabled:]
+ -[ODDSiriSchemaODDDictationProperties setIsDictationEnabled:]
+ -[ODDSiriSchemaODDDictationProperties writeTo:]
+ -[ODDSiriSchemaODDDictationProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDictationProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDExperimentFixedDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDExperimentFixedDimensions deleteDeploymentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions deleteExperimentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions deleteTreatmentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions deploymentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDExperimentFixedDimensions experimentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions hasDeploymentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions hasExperimentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions hasTreatmentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions hash]
+ -[ODDSiriSchemaODDExperimentFixedDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions initWithJSON:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions isEqual:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions jsonData]
+ -[ODDSiriSchemaODDExperimentFixedDimensions readFrom:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setDeploymentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setExperimentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setHasDeploymentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setHasExperimentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setHasTreatmentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions setTreatmentId:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions treatmentId]
+ -[ODDSiriSchemaODDExperimentFixedDimensions writeTo:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDExperimentFixedDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDGeneralProperties .cxx_destruct]
+ -[ODDSiriSchemaODDGeneralProperties UTCOffset]
+ -[ODDSiriSchemaODDGeneralProperties deleteDeviceOS]
+ -[ODDSiriSchemaODDGeneralProperties deleteDeviceType]
+ -[ODDSiriSchemaODDGeneralProperties deleteIsStoreDemoMode]
+ -[ODDSiriSchemaODDGeneralProperties deleteModelNumber]
+ -[ODDSiriSchemaODDGeneralProperties deleteStorefrontId]
+ -[ODDSiriSchemaODDGeneralProperties deleteSystemLocale]
+ -[ODDSiriSchemaODDGeneralProperties deleteUTCOffset]
+ -[ODDSiriSchemaODDGeneralProperties deviceOS]
+ -[ODDSiriSchemaODDGeneralProperties deviceType]
+ -[ODDSiriSchemaODDGeneralProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDGeneralProperties hasDeviceOS]
+ -[ODDSiriSchemaODDGeneralProperties hasDeviceType]
+ -[ODDSiriSchemaODDGeneralProperties hasIsStoreDemoMode]
+ -[ODDSiriSchemaODDGeneralProperties hasModelNumber]
+ -[ODDSiriSchemaODDGeneralProperties hasStorefrontId]
+ -[ODDSiriSchemaODDGeneralProperties hasSystemLocale]
+ -[ODDSiriSchemaODDGeneralProperties hasUTCOffset]
+ -[ODDSiriSchemaODDGeneralProperties hash]
+ -[ODDSiriSchemaODDGeneralProperties initWithDictionary:]
+ -[ODDSiriSchemaODDGeneralProperties initWithJSON:]
+ -[ODDSiriSchemaODDGeneralProperties isEqual:]
+ -[ODDSiriSchemaODDGeneralProperties isStoreDemoMode]
+ -[ODDSiriSchemaODDGeneralProperties jsonData]
+ -[ODDSiriSchemaODDGeneralProperties modelNumber]
+ -[ODDSiriSchemaODDGeneralProperties readFrom:]
+ -[ODDSiriSchemaODDGeneralProperties setDeviceOS:]
+ -[ODDSiriSchemaODDGeneralProperties setDeviceType:]
+ -[ODDSiriSchemaODDGeneralProperties setHasDeviceOS:]
+ -[ODDSiriSchemaODDGeneralProperties setHasDeviceType:]
+ -[ODDSiriSchemaODDGeneralProperties setHasIsStoreDemoMode:]
+ -[ODDSiriSchemaODDGeneralProperties setHasModelNumber:]
+ -[ODDSiriSchemaODDGeneralProperties setHasStorefrontId:]
+ -[ODDSiriSchemaODDGeneralProperties setHasSystemLocale:]
+ -[ODDSiriSchemaODDGeneralProperties setHasUTCOffset:]
+ -[ODDSiriSchemaODDGeneralProperties setIsStoreDemoMode:]
+ -[ODDSiriSchemaODDGeneralProperties setModelNumber:]
+ -[ODDSiriSchemaODDGeneralProperties setStorefrontId:]
+ -[ODDSiriSchemaODDGeneralProperties setSystemLocale:]
+ -[ODDSiriSchemaODDGeneralProperties setUTCOffset:]
+ -[ODDSiriSchemaODDGeneralProperties storefrontId]
+ -[ODDSiriSchemaODDGeneralProperties systemLocale]
+ -[ODDSiriSchemaODDGeneralProperties writeTo:]
+ -[ODDSiriSchemaODDGeneralProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDGeneralProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDHomeKitProperties deleteHasHomekitHome]
+ -[ODDSiriSchemaODDHomeKitProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDHomeKitProperties hasHasHomekitHome]
+ -[ODDSiriSchemaODDHomeKitProperties hasHomekitHome]
+ -[ODDSiriSchemaODDHomeKitProperties hash]
+ -[ODDSiriSchemaODDHomeKitProperties initWithDictionary:]
+ -[ODDSiriSchemaODDHomeKitProperties initWithJSON:]
+ -[ODDSiriSchemaODDHomeKitProperties isEqual:]
+ -[ODDSiriSchemaODDHomeKitProperties jsonData]
+ -[ODDSiriSchemaODDHomeKitProperties readFrom:]
+ -[ODDSiriSchemaODDHomeKitProperties setHasHasHomekitHome:]
+ -[ODDSiriSchemaODDHomeKitProperties setHasHomekitHome:]
+ -[ODDSiriSchemaODDHomeKitProperties writeTo:]
+ -[ODDSiriSchemaODDHomeKitProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDHomePodProperties .cxx_destruct]
+ -[ODDSiriSchemaODDHomePodProperties adaptiveVolume]
+ -[ODDSiriSchemaODDHomePodProperties deleteAdaptiveVolume]
+ -[ODDSiriSchemaODDHomePodProperties deleteIsPersonalDomainsEnabled]
+ -[ODDSiriSchemaODDHomePodProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDHomePodProperties hasAdaptiveVolume]
+ -[ODDSiriSchemaODDHomePodProperties hasIsPersonalDomainsEnabled]
+ -[ODDSiriSchemaODDHomePodProperties hash]
+ -[ODDSiriSchemaODDHomePodProperties initWithDictionary:]
+ -[ODDSiriSchemaODDHomePodProperties initWithJSON:]
+ -[ODDSiriSchemaODDHomePodProperties isEqual:]
+ -[ODDSiriSchemaODDHomePodProperties isPersonalDomainsEnabled]
+ -[ODDSiriSchemaODDHomePodProperties jsonData]
+ -[ODDSiriSchemaODDHomePodProperties readFrom:]
+ -[ODDSiriSchemaODDHomePodProperties setAdaptiveVolume:]
+ -[ODDSiriSchemaODDHomePodProperties setHasAdaptiveVolume:]
+ -[ODDSiriSchemaODDHomePodProperties setHasIsPersonalDomainsEnabled:]
+ -[ODDSiriSchemaODDHomePodProperties setIsPersonalDomainsEnabled:]
+ -[ODDSiriSchemaODDHomePodProperties writeTo:]
+ -[ODDSiriSchemaODDHomePodProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDHomePodProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumGuestsAccepted]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumParticipantsWithTrust]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWhoSyncedRecognizeMyVoice]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWithLocationServicesEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWithMatchingSiriLanguage]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWithPersonalRequestsEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWithRecognizeMyVoiceEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumUsersWithSiriCloudSyncEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus deleteNumVoiceProfilesAvailable]
+ -[ODDSiriSchemaODDMultiUserSetupStatus dictionaryRepresentation]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumGuestsAccepted]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumParticipantsWithTrust]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWhoSyncedRecognizeMyVoice]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWithLocationServicesEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWithMatchingSiriLanguage]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWithPersonalRequestsEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWithRecognizeMyVoiceEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumUsersWithSiriCloudSyncEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hasNumVoiceProfilesAvailable]
+ -[ODDSiriSchemaODDMultiUserSetupStatus hash]
+ -[ODDSiriSchemaODDMultiUserSetupStatus initWithDictionary:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus initWithJSON:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus isEqual:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus jsonData]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numGuestsAccepted]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numParticipantsWithTrust]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWhoSyncedRecognizeMyVoice]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWithLocationServicesEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWithMatchingSiriLanguage]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWithPersonalRequestsEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWithRecognizeMyVoiceEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numUsersWithSiriCloudSyncEnabled]
+ -[ODDSiriSchemaODDMultiUserSetupStatus numVoiceProfilesAvailable]
+ -[ODDSiriSchemaODDMultiUserSetupStatus readFrom:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumGuestsAccepted:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumParticipantsWithTrust:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWhoSyncedRecognizeMyVoice:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWithLocationServicesEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWithMatchingSiriLanguage:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWithPersonalRequestsEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWithRecognizeMyVoiceEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumUsersWithSiriCloudSyncEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setHasNumVoiceProfilesAvailable:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumGuestsAccepted:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumParticipantsWithTrust:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWhoSyncedRecognizeMyVoice:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWithLocationServicesEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWithMatchingSiriLanguage:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWithPersonalRequestsEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWithRecognizeMyVoiceEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumUsersWithSiriCloudSyncEnabled:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus setNumVoiceProfilesAvailable:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus writeTo:]
+ -[ODDSiriSchemaODDMultiUserSetupStatus(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDMultiUserState .cxx_destruct]
+ -[ODDSiriSchemaODDMultiUserState addEnrolledUsers:]
+ -[ODDSiriSchemaODDMultiUserState clearEnrolledUsers]
+ -[ODDSiriSchemaODDMultiUserState deleteEnrolledUsers]
+ -[ODDSiriSchemaODDMultiUserState deleteMultiUserSetupStatus]
+ -[ODDSiriSchemaODDMultiUserState dictionaryRepresentation]
+ -[ODDSiriSchemaODDMultiUserState enrolledUsersAtIndex:]
+ -[ODDSiriSchemaODDMultiUserState enrolledUsersCount]
+ -[ODDSiriSchemaODDMultiUserState enrolledUsers]
+ -[ODDSiriSchemaODDMultiUserState hasMultiUserSetupStatus]
+ -[ODDSiriSchemaODDMultiUserState hash]
+ -[ODDSiriSchemaODDMultiUserState initWithDictionary:]
+ -[ODDSiriSchemaODDMultiUserState initWithJSON:]
+ -[ODDSiriSchemaODDMultiUserState isEqual:]
+ -[ODDSiriSchemaODDMultiUserState jsonData]
+ -[ODDSiriSchemaODDMultiUserState multiUserSetupStatus]
+ -[ODDSiriSchemaODDMultiUserState readFrom:]
+ -[ODDSiriSchemaODDMultiUserState setEnrolledUsers:]
+ -[ODDSiriSchemaODDMultiUserState setHasMultiUserSetupStatus:]
+ -[ODDSiriSchemaODDMultiUserState setMultiUserSetupStatus:]
+ -[ODDSiriSchemaODDMultiUserState writeTo:]
+ -[ODDSiriSchemaODDMultiUserState(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDMultiUserState(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDOptInProperties .cxx_destruct]
+ -[ODDSiriSchemaODDOptInProperties addGradingOptInStateChanges:]
+ -[ODDSiriSchemaODDOptInProperties clearGradingOptInStateChanges]
+ -[ODDSiriSchemaODDOptInProperties dataSharingOptInStatus]
+ -[ODDSiriSchemaODDOptInProperties deleteDataSharingOptInStatus]
+ -[ODDSiriSchemaODDOptInProperties deleteGradingOptInStateChanges]
+ -[ODDSiriSchemaODDOptInProperties deleteIsMteUploadEnabled]
+ -[ODDSiriSchemaODDOptInProperties deleteIsServerUserDataSyncEnabled]
+ -[ODDSiriSchemaODDOptInProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDOptInProperties gradingOptInStateChangesAtIndex:]
+ -[ODDSiriSchemaODDOptInProperties gradingOptInStateChangesCount]
+ -[ODDSiriSchemaODDOptInProperties gradingOptInStateChanges]
+ -[ODDSiriSchemaODDOptInProperties hasDataSharingOptInStatus]
+ -[ODDSiriSchemaODDOptInProperties hasIsMteUploadEnabled]
+ -[ODDSiriSchemaODDOptInProperties hasIsServerUserDataSyncEnabled]
+ -[ODDSiriSchemaODDOptInProperties hash]
+ -[ODDSiriSchemaODDOptInProperties initWithDictionary:]
+ -[ODDSiriSchemaODDOptInProperties initWithJSON:]
+ -[ODDSiriSchemaODDOptInProperties isEqual:]
+ -[ODDSiriSchemaODDOptInProperties isMteUploadEnabled]
+ -[ODDSiriSchemaODDOptInProperties isServerUserDataSyncEnabled]
+ -[ODDSiriSchemaODDOptInProperties jsonData]
+ -[ODDSiriSchemaODDOptInProperties readFrom:]
+ -[ODDSiriSchemaODDOptInProperties setDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDOptInProperties setGradingOptInStateChanges:]
+ -[ODDSiriSchemaODDOptInProperties setHasDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDOptInProperties setHasIsMteUploadEnabled:]
+ -[ODDSiriSchemaODDOptInProperties setHasIsServerUserDataSyncEnabled:]
+ -[ODDSiriSchemaODDOptInProperties setIsMteUploadEnabled:]
+ -[ODDSiriSchemaODDOptInProperties setIsServerUserDataSyncEnabled:]
+ -[ODDSiriSchemaODDOptInProperties writeTo:]
+ -[ODDSiriSchemaODDOptInProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDOptInProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSessionCounts deleteUsdxSessionCount]
+ -[ODDSiriSchemaODDSessionCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDSessionCounts hasUsdxSessionCount]
+ -[ODDSiriSchemaODDSessionCounts hash]
+ -[ODDSiriSchemaODDSessionCounts initWithDictionary:]
+ -[ODDSiriSchemaODDSessionCounts initWithJSON:]
+ -[ODDSiriSchemaODDSessionCounts isEqual:]
+ -[ODDSiriSchemaODDSessionCounts jsonData]
+ -[ODDSiriSchemaODDSessionCounts readFrom:]
+ -[ODDSiriSchemaODDSessionCounts setHasUsdxSessionCount:]
+ -[ODDSiriSchemaODDSessionCounts setUsdxSessionCount:]
+ -[ODDSiriSchemaODDSessionCounts usdxSessionCount]
+ -[ODDSiriSchemaODDSessionCounts writeTo:]
+ -[ODDSiriSchemaODDSessionCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriClientEvent assistantDiagnosticAndUsageOptInDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent assistantExperimentDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssistantDiagnosticAndUsageOptInDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssistantExperimentDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteIOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteMacOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteTvOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteVisionOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteWatchOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssistantDiagnosticAndUsageOptInDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssistantExperimentDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasIOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasMacOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasTvOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasVisionOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasWatchOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent iOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent macOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent setAssistantDiagnosticAndUsageOptInDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setAssistantExperimentDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssistantDiagnosticAndUsageOptInDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssistantExperimentDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasIOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasMacOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasTvOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasVisionOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasWatchOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setIOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setMacOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setTvOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setVisionOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setWatchOSDevicePropertiesReported:]
+ -[ODDSiriSchemaODDSiriClientEvent tvOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent visionOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriClientEvent watchOSDevicePropertiesReported]
+ -[ODDSiriSchemaODDSiriInCallProperties deleteHeySiriHangupEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties deleteSiriInCallEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDSiriInCallProperties hasHeySiriHangupEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties hasSiriInCallEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties hash]
+ -[ODDSiriSchemaODDSiriInCallProperties heySiriHangupEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties initWithDictionary:]
+ -[ODDSiriSchemaODDSiriInCallProperties initWithJSON:]
+ -[ODDSiriSchemaODDSiriInCallProperties isEqual:]
+ -[ODDSiriSchemaODDSiriInCallProperties jsonData]
+ -[ODDSiriSchemaODDSiriInCallProperties readFrom:]
+ -[ODDSiriSchemaODDSiriInCallProperties setHasHeySiriHangupEnablementState:]
+ -[ODDSiriSchemaODDSiriInCallProperties setHasSiriInCallEnablementState:]
+ -[ODDSiriSchemaODDSiriInCallProperties setHeySiriHangupEnablementState:]
+ -[ODDSiriSchemaODDSiriInCallProperties setSiriInCallEnablementState:]
+ -[ODDSiriSchemaODDSiriInCallProperties siriInCallEnablementState]
+ -[ODDSiriSchemaODDSiriInCallProperties writeTo:]
+ -[ODDSiriSchemaODDSiriInCallProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDUserPersonalization .cxx_destruct]
+ -[ODDSiriSchemaODDUserPersonalization activeSubscriptionsAtIndex:]
+ -[ODDSiriSchemaODDUserPersonalization activeSubscriptionsCount]
+ -[ODDSiriSchemaODDUserPersonalization activeSubscriptions]
+ -[ODDSiriSchemaODDUserPersonalization addActiveSubscriptions:]
+ -[ODDSiriSchemaODDUserPersonalization clearActiveSubscriptions]
+ -[ODDSiriSchemaODDUserPersonalization deleteActiveSubscriptions]
+ -[ODDSiriSchemaODDUserPersonalization deleteIsPersonalDomainRequestsEnabled]
+ -[ODDSiriSchemaODDUserPersonalization deleteVoiceSettings]
+ -[ODDSiriSchemaODDUserPersonalization dictionaryRepresentation]
+ -[ODDSiriSchemaODDUserPersonalization hasIsPersonalDomainRequestsEnabled]
+ -[ODDSiriSchemaODDUserPersonalization hasVoiceSettings]
+ -[ODDSiriSchemaODDUserPersonalization hash]
+ -[ODDSiriSchemaODDUserPersonalization initWithDictionary:]
+ -[ODDSiriSchemaODDUserPersonalization initWithJSON:]
+ -[ODDSiriSchemaODDUserPersonalization isEqual:]
+ -[ODDSiriSchemaODDUserPersonalization isPersonalDomainRequestsEnabled]
+ -[ODDSiriSchemaODDUserPersonalization jsonData]
+ -[ODDSiriSchemaODDUserPersonalization readFrom:]
+ -[ODDSiriSchemaODDUserPersonalization setActiveSubscriptions:]
+ -[ODDSiriSchemaODDUserPersonalization setHasIsPersonalDomainRequestsEnabled:]
+ -[ODDSiriSchemaODDUserPersonalization setHasVoiceSettings:]
+ -[ODDSiriSchemaODDUserPersonalization setIsPersonalDomainRequestsEnabled:]
+ -[ODDSiriSchemaODDUserPersonalization setVoiceSettings:]
+ -[ODDSiriSchemaODDUserPersonalization voiceSettings]
+ -[ODDSiriSchemaODDUserPersonalization writeTo:]
+ -[ODDSiriSchemaODDUserPersonalization(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDUserPersonalization(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDVoiceProperties .cxx_destruct]
+ -[ODDSiriSchemaODDVoiceProperties accent]
+ -[ODDSiriSchemaODDVoiceProperties addInstalledVoices:]
+ -[ODDSiriSchemaODDVoiceProperties clearInstalledVoices]
+ -[ODDSiriSchemaODDVoiceProperties deleteAccent]
+ -[ODDSiriSchemaODDVoiceProperties deleteGender]
+ -[ODDSiriSchemaODDVoiceProperties deleteInstalledVoices]
+ -[ODDSiriSchemaODDVoiceProperties deleteName]
+ -[ODDSiriSchemaODDVoiceProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDVoiceProperties gender]
+ -[ODDSiriSchemaODDVoiceProperties hasAccent]
+ -[ODDSiriSchemaODDVoiceProperties hasGender]
+ -[ODDSiriSchemaODDVoiceProperties hasName]
+ -[ODDSiriSchemaODDVoiceProperties hash]
+ -[ODDSiriSchemaODDVoiceProperties initWithDictionary:]
+ -[ODDSiriSchemaODDVoiceProperties initWithJSON:]
+ -[ODDSiriSchemaODDVoiceProperties installedVoicesAtIndex:]
+ -[ODDSiriSchemaODDVoiceProperties installedVoicesCount]
+ -[ODDSiriSchemaODDVoiceProperties installedVoices]
+ -[ODDSiriSchemaODDVoiceProperties isEqual:]
+ -[ODDSiriSchemaODDVoiceProperties jsonData]
+ -[ODDSiriSchemaODDVoiceProperties name]
+ -[ODDSiriSchemaODDVoiceProperties readFrom:]
+ -[ODDSiriSchemaODDVoiceProperties setAccent:]
+ -[ODDSiriSchemaODDVoiceProperties setGender:]
+ -[ODDSiriSchemaODDVoiceProperties setHasAccent:]
+ -[ODDSiriSchemaODDVoiceProperties setHasGender:]
+ -[ODDSiriSchemaODDVoiceProperties setHasName:]
+ -[ODDSiriSchemaODDVoiceProperties setInstalledVoices:]
+ -[ODDSiriSchemaODDVoiceProperties setName:]
+ -[ODDSiriSchemaODDVoiceProperties writeTo:]
+ -[ODDSiriSchemaODDVoiceProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDVoiceProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteIsAlwaysListenForHeySiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteIsShowAppsBehindSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteIsTypeToSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteIsVoiceOverEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteSiriPauseTimeState]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteSiriSpeechRate]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties deleteVoiceFeedback]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasIsAlwaysListenForHeySiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasIsShowAppsBehindSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasIsTypeToSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasIsVoiceOverEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasSiriPauseTimeState]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasSiriSpeechRate]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hasVoiceFeedback]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties hash]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties initWithDictionary:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties initWithJSON:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties isAlwaysListenForHeySiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties isEqual:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties isShowAppsBehindSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties isTypeToSiriEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties isVoiceOverEnabled]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties jsonData]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties readFrom:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasIsAlwaysListenForHeySiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasIsShowAppsBehindSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasIsTypeToSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasIsVoiceOverEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasSiriPauseTimeState:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasSiriSpeechRate:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setHasVoiceFeedback:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setIsAlwaysListenForHeySiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setIsShowAppsBehindSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setIsTypeToSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setIsVoiceOverEnabled:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setSiriPauseTimeState:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setSiriSpeechRate:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties setVoiceFeedback:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties siriPauseTimeState]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties siriSpeechRate]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties voiceFeedback]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties writeTo:]
+ -[ODDSiriSchemaODDiOSAccessibilityProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDiOSAssistantProperties .cxx_destruct]
+ -[ODDSiriSchemaODDiOSAssistantProperties accessibility]
+ -[ODDSiriSchemaODDiOSAssistantProperties activeSubscriptionsAtIndex:]
+ -[ODDSiriSchemaODDiOSAssistantProperties activeSubscriptionsCount]
+ -[ODDSiriSchemaODDiOSAssistantProperties activeSubscriptions]
+ -[ODDSiriSchemaODDiOSAssistantProperties addActiveSubscriptions:]
+ -[ODDSiriSchemaODDiOSAssistantProperties announce]
+ -[ODDSiriSchemaODDiOSAssistantProperties autoSendMessage]
+ -[ODDSiriSchemaODDiOSAssistantProperties carPlay]
+ -[ODDSiriSchemaODDiOSAssistantProperties clearActiveSubscriptions]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteAccessibility]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteActiveSubscriptions]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteAnnounce]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteAutoSendMessage]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteCarPlay]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteIsAllowSiriWhenLockedEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteIsPressSideButtonForSiriEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteResponse]
+ -[ODDSiriSchemaODDiOSAssistantProperties deleteSiriInCall]
+ -[ODDSiriSchemaODDiOSAssistantProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasAccessibility]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasAnnounce]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasAutoSendMessage]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasCarPlay]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasIsAllowSiriWhenLockedEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasIsPressSideButtonForSiriEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasResponse]
+ -[ODDSiriSchemaODDiOSAssistantProperties hasSiriInCall]
+ -[ODDSiriSchemaODDiOSAssistantProperties hash]
+ -[ODDSiriSchemaODDiOSAssistantProperties initWithDictionary:]
+ -[ODDSiriSchemaODDiOSAssistantProperties initWithJSON:]
+ -[ODDSiriSchemaODDiOSAssistantProperties isAllowSiriWhenLockedEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties isEqual:]
+ -[ODDSiriSchemaODDiOSAssistantProperties isPressSideButtonForSiriEnabled]
+ -[ODDSiriSchemaODDiOSAssistantProperties jsonData]
+ -[ODDSiriSchemaODDiOSAssistantProperties readFrom:]
+ -[ODDSiriSchemaODDiOSAssistantProperties response]
+ -[ODDSiriSchemaODDiOSAssistantProperties setAccessibility:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setActiveSubscriptions:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setAnnounce:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setAutoSendMessage:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setCarPlay:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasAccessibility:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasAnnounce:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasAutoSendMessage:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasCarPlay:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasIsAllowSiriWhenLockedEnabled:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasIsPressSideButtonForSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasResponse:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setHasSiriInCall:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setIsAllowSiriWhenLockedEnabled:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setIsPressSideButtonForSiriEnabled:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setResponse:]
+ -[ODDSiriSchemaODDiOSAssistantProperties setSiriInCall:]
+ -[ODDSiriSchemaODDiOSAssistantProperties siriInCall]
+ -[ODDSiriSchemaODDiOSAssistantProperties writeTo:]
+ -[ODDSiriSchemaODDiOSAssistantProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDiOSAssistantProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported .cxx_destruct]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported assistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported deleteAssistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported deleteDictation]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported deleteGeneral]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported deleteIOSAssistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported dictation]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported general]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported hasAssistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported hasDictation]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported hasGeneral]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported hasIOSAssistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported hash]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported iOSAssistant]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported initWithDictionary:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported initWithJSON:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported isEqual:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported jsonData]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported readFrom:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setAssistant:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setDictation:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setGeneral:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setHasAssistant:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setHasDictation:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setHasGeneral:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setHasIOSAssistant:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported setIOSAssistant:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported writeTo:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDiOSDevicePropertiesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDiOSResponseProperties deleteIsAlwaysShowSiriCaptionsEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties deleteIsAlwaysShowSpeechEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDiOSResponseProperties hasIsAlwaysShowSiriCaptionsEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties hasIsAlwaysShowSpeechEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties hash]
+ -[ODDSiriSchemaODDiOSResponseProperties initWithDictionary:]
+ -[ODDSiriSchemaODDiOSResponseProperties initWithJSON:]
+ -[ODDSiriSchemaODDiOSResponseProperties isAlwaysShowSiriCaptionsEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties isAlwaysShowSpeechEnabled]
+ -[ODDSiriSchemaODDiOSResponseProperties isEqual:]
+ -[ODDSiriSchemaODDiOSResponseProperties jsonData]
+ -[ODDSiriSchemaODDiOSResponseProperties readFrom:]
+ -[ODDSiriSchemaODDiOSResponseProperties setHasIsAlwaysShowSiriCaptionsEnabled:]
+ -[ODDSiriSchemaODDiOSResponseProperties setHasIsAlwaysShowSpeechEnabled:]
+ -[ODDSiriSchemaODDiOSResponseProperties setIsAlwaysShowSiriCaptionsEnabled:]
+ -[ODDSiriSchemaODDiOSResponseProperties setIsAlwaysShowSpeechEnabled:]
+ -[ODDSiriSchemaODDiOSResponseProperties writeTo:]
+ -[ODDSiriSchemaODDiOSResponseProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDmacOSAssistantProperties deleteIsExternalMicrophoneHSEnabled]
+ -[ODDSiriSchemaODDmacOSAssistantProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDmacOSAssistantProperties hasIsExternalMicrophoneHSEnabled]
+ -[ODDSiriSchemaODDmacOSAssistantProperties hash]
+ -[ODDSiriSchemaODDmacOSAssistantProperties initWithDictionary:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties initWithJSON:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties isEqual:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties isExternalMicrophoneHSEnabled]
+ -[ODDSiriSchemaODDmacOSAssistantProperties jsonData]
+ -[ODDSiriSchemaODDmacOSAssistantProperties readFrom:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties setHasIsExternalMicrophoneHSEnabled:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties setIsExternalMicrophoneHSEnabled:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties writeTo:]
+ -[ODDSiriSchemaODDmacOSAssistantProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported .cxx_destruct]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported assistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported deleteAssistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported deleteDictation]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported deleteGeneral]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported deleteMacOSAssistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported dictation]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported general]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported hasAssistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported hasDictation]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported hasGeneral]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported hasMacOSAssistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported hash]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported initWithDictionary:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported initWithJSON:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported isEqual:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported jsonData]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported macOSAssistant]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported readFrom:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setAssistant:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setDictation:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setGeneral:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setHasAssistant:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setHasDictation:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setHasGeneral:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setHasMacOSAssistant:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported setMacOSAssistant:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported writeTo:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDmacOSDevicePropertiesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDtvOSAssistantProperties .cxx_destruct]
+ -[ODDSiriSchemaODDtvOSAssistantProperties deleteHomePodProperties]
+ -[ODDSiriSchemaODDtvOSAssistantProperties deleteMultiUserState]
+ -[ODDSiriSchemaODDtvOSAssistantProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDtvOSAssistantProperties hasHomePodProperties]
+ -[ODDSiriSchemaODDtvOSAssistantProperties hasMultiUserState]
+ -[ODDSiriSchemaODDtvOSAssistantProperties hash]
+ -[ODDSiriSchemaODDtvOSAssistantProperties homePodProperties]
+ -[ODDSiriSchemaODDtvOSAssistantProperties initWithDictionary:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties initWithJSON:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties isEqual:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties jsonData]
+ -[ODDSiriSchemaODDtvOSAssistantProperties multiUserState]
+ -[ODDSiriSchemaODDtvOSAssistantProperties readFrom:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties setHasHomePodProperties:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties setHasMultiUserState:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties setHomePodProperties:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties setMultiUserState:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties writeTo:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDtvOSAssistantProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported .cxx_destruct]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported assistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported deleteAssistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported deleteDictation]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported deleteGeneral]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported deleteTvOSAssistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported dictation]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported general]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported hasAssistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported hasDictation]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported hasGeneral]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported hasTvOSAssistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported hash]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported initWithDictionary:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported initWithJSON:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported isEqual:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported jsonData]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported readFrom:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setAssistant:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setDictation:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setGeneral:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setHasAssistant:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setHasDictation:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setHasGeneral:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setHasTvOSAssistant:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported setTvOSAssistant:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported tvOSAssistant]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported writeTo:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDtvOSDevicePropertiesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported .cxx_destruct]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported assistant]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported deleteAssistant]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported deleteDictation]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported deleteGeneral]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported dictation]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported general]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported hasAssistant]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported hasDictation]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported hasGeneral]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported hash]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported initWithDictionary:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported initWithJSON:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported isEqual:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported jsonData]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported readFrom:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setAssistant:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setDictation:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setGeneral:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setHasAssistant:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setHasDictation:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported setHasGeneral:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported writeTo:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDvisionOSDevicePropertiesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties deleteIsRaiseToSpeakEnabled]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties dictionaryRepresentation]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties hasIsRaiseToSpeakEnabled]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties hash]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties initWithDictionary:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties initWithJSON:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties isEqual:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties isRaiseToSpeakEnabled]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties jsonData]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties readFrom:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties setHasIsRaiseToSpeakEnabled:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties setIsRaiseToSpeakEnabled:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties writeTo:]
+ -[ODDSiriSchemaODDwatchOSAssistantProperties(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported .cxx_destruct]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported assistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported deleteAssistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported deleteDictation]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported deleteGeneral]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported deleteWatchOSAssistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported dictation]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported general]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported hasAssistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported hasDictation]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported hasGeneral]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported hasWatchOSAssistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported hash]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported initWithDictionary:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported initWithJSON:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported isEqual:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported jsonData]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported readFrom:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setAssistant:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setDictation:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setGeneral:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setHasAssistant:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setHasDictation:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setHasGeneral:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setHasWatchOSAssistant:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported setWatchOSAssistant:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported watchOSAssistant]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported writeTo:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDwatchOSDevicePropertiesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHMUXBridgeContext deleteEphemeralToAggregationIdentifierMap]
+ -[ORCHSchemaORCHMUXBridgeContext ephemeralToAggregationIdentifierMap]
+ -[ORCHSchemaORCHMUXBridgeContext hasEphemeralToAggregationIdentifierMap]
+ -[ORCHSchemaORCHMUXBridgeContext setEphemeralToAggregationIdentifierMap:]
+ -[ORCHSchemaORCHMUXBridgeContext setHasEphemeralToAggregationIdentifierMap:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap .cxx_destruct]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deleteDeviceAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deleteUserAggregationIdExpirationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deleteUserAggregationIdRotationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deleteUserAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deleteUserEphemeralId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap deviceAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap dictionaryRepresentation]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hasDeviceAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hasUserAggregationIdExpirationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hasUserAggregationIdRotationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hasUserAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hasUserEphemeralId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap hash]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap initWithDictionary:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap initWithJSON:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap isEqual:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap jsonData]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap readFrom:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setDeviceAggregationId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setHasDeviceAggregationId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setHasUserAggregationId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setHasUserAggregationIdExpirationTimestampMs:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setHasUserAggregationIdRotationTimestampMs:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setHasUserEphemeralId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setUserAggregationId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setUserAggregationIdExpirationTimestampMs:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setUserAggregationIdRotationTimestampMs:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap setUserEphemeralId:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap userAggregationIdExpirationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap userAggregationIdRotationTimestampMs]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap userAggregationId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap userEphemeralId]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap writeTo:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext .cxx_destruct]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext deleteSelectedUser]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext dictionaryRepresentation]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext hasSelectedUser]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext hash]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext initWithDictionary:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext initWithJSON:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext isEqual:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext jsonData]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext readFrom:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext selectedUser]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext setHasSelectedUser:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext setSelectedUser:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext writeTo:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSCrossIntentRankerResponse cirFallbackTriggered]
+ -[PEGASUSSchemaPEGASUSCrossIntentRankerResponse deleteCirFallbackTriggered]
+ -[PEGASUSSchemaPEGASUSCrossIntentRankerResponse hasCirFallbackTriggered]
+ -[PEGASUSSchemaPEGASUSCrossIntentRankerResponse setCirFallbackTriggered:]
+ -[PEGASUSSchemaPEGASUSCrossIntentRankerResponse setHasCirFallbackTriggered:]
+ -[PFAClockEnvelopeStatistics deleteMessageCount]
+ -[PFAClockEnvelopeStatistics deleteTotalBytes]
+ -[PFAClockEnvelopeStatistics dictionaryRepresentation]
+ -[PFAClockEnvelopeStatistics hasMessageCount]
+ -[PFAClockEnvelopeStatistics hasTotalBytes]
+ -[PFAClockEnvelopeStatistics hash]
+ -[PFAClockEnvelopeStatistics initWithDictionary:]
+ -[PFAClockEnvelopeStatistics initWithJSON:]
+ -[PFAClockEnvelopeStatistics isEqual:]
+ -[PFAClockEnvelopeStatistics jsonData]
+ -[PFAClockEnvelopeStatistics messageCount]
+ -[PFAClockEnvelopeStatistics readFrom:]
+ -[PFAClockEnvelopeStatistics setHasMessageCount:]
+ -[PFAClockEnvelopeStatistics setHasTotalBytes:]
+ -[PFAClockEnvelopeStatistics setMessageCount:]
+ -[PFAClockEnvelopeStatistics setTotalBytes:]
+ -[PFAClockEnvelopeStatistics totalBytes]
+ -[PFAClockEnvelopeStatistics writeTo:]
+ -[PFAClockEnvelopeStatistics(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFAPFAClientEvent .cxx_destruct]
+ -[PFAPFAClientEvent deleteRepackagingExecution]
+ -[PFAPFAClientEvent dictionaryRepresentation]
+ -[PFAPFAClientEvent hasRepackagingExecution]
+ -[PFAPFAClientEvent hash]
+ -[PFAPFAClientEvent initWithDictionary:]
+ -[PFAPFAClientEvent initWithJSON:]
+ -[PFAPFAClientEvent isEqual:]
+ -[PFAPFAClientEvent jsonData]
+ -[PFAPFAClientEvent qualifiedMessageName]
+ -[PFAPFAClientEvent readFrom:]
+ -[PFAPFAClientEvent repackagingExecution]
+ -[PFAPFAClientEvent setHasRepackagingExecution:]
+ -[PFAPFAClientEvent setRepackagingExecution:]
+ -[PFAPFAClientEvent whichEvent_Type]
+ -[PFAPFAClientEvent writeTo:]
+ -[PFAPFAClientEvent(InnerEventContainer) innerEvent]
+ -[PFAPFAClientEvent(InnerEventContainer) whichInnerEventType]
+ -[PFAPFAClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[PFAPFAClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PFAPFAClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFARepackagingExecution .cxx_destruct]
+ -[PFARepackagingExecution clockIdentifier]
+ -[PFARepackagingExecution deleteClockIdentifier]
+ -[PFARepackagingExecution deleteEnvelopeStatistics]
+ -[PFARepackagingExecution deleteResult]
+ -[PFARepackagingExecution dictionaryRepresentation]
+ -[PFARepackagingExecution envelopeStatistics]
+ -[PFARepackagingExecution hasClockIdentifier]
+ -[PFARepackagingExecution hasEnvelopeStatistics]
+ -[PFARepackagingExecution hasResult]
+ -[PFARepackagingExecution hash]
+ -[PFARepackagingExecution initWithDictionary:]
+ -[PFARepackagingExecution initWithJSON:]
+ -[PFARepackagingExecution isEqual:]
+ -[PFARepackagingExecution jsonData]
+ -[PFARepackagingExecution readFrom:]
+ -[PFARepackagingExecution result]
+ -[PFARepackagingExecution setClockIdentifier:]
+ -[PFARepackagingExecution setEnvelopeStatistics:]
+ -[PFARepackagingExecution setHasClockIdentifier:]
+ -[PFARepackagingExecution setHasEnvelopeStatistics:]
+ -[PFARepackagingExecution setHasResult:]
+ -[PFARepackagingExecution setResult:]
+ -[PFARepackagingExecution writeTo:]
+ -[PFARepackagingExecution(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PFARepackagingExecution(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFARepackagingExecutionFBFFailure deleteFlErrorCode]
+ -[PFARepackagingExecutionFBFFailure dictionaryRepresentation]
+ -[PFARepackagingExecutionFBFFailure flErrorCode]
+ -[PFARepackagingExecutionFBFFailure hasFlErrorCode]
+ -[PFARepackagingExecutionFBFFailure hash]
+ -[PFARepackagingExecutionFBFFailure initWithDictionary:]
+ -[PFARepackagingExecutionFBFFailure initWithJSON:]
+ -[PFARepackagingExecutionFBFFailure isEqual:]
+ -[PFARepackagingExecutionFBFFailure jsonData]
+ -[PFARepackagingExecutionFBFFailure readFrom:]
+ -[PFARepackagingExecutionFBFFailure setFlErrorCode:]
+ -[PFARepackagingExecutionFBFFailure setHasFlErrorCode:]
+ -[PFARepackagingExecutionFBFFailure writeTo:]
+ -[PFARepackagingExecutionFBFFailure(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFARepackagingExecutionFailure .cxx_destruct]
+ -[PFARepackagingExecutionFailure deleteFbfFailure]
+ -[PFARepackagingExecutionFailure deleteSandboxError]
+ -[PFARepackagingExecutionFailure dictionaryRepresentation]
+ -[PFARepackagingExecutionFailure fbfFailure]
+ -[PFARepackagingExecutionFailure hasFbfFailure]
+ -[PFARepackagingExecutionFailure hasSandboxError]
+ -[PFARepackagingExecutionFailure hash]
+ -[PFARepackagingExecutionFailure initWithDictionary:]
+ -[PFARepackagingExecutionFailure initWithJSON:]
+ -[PFARepackagingExecutionFailure isEqual:]
+ -[PFARepackagingExecutionFailure jsonData]
+ -[PFARepackagingExecutionFailure readFrom:]
+ -[PFARepackagingExecutionFailure sandboxError]
+ -[PFARepackagingExecutionFailure setFbfFailure:]
+ -[PFARepackagingExecutionFailure setHasFbfFailure:]
+ -[PFARepackagingExecutionFailure setHasSandboxError:]
+ -[PFARepackagingExecutionFailure setSandboxError:]
+ -[PFARepackagingExecutionFailure whichKind]
+ -[PFARepackagingExecutionFailure writeTo:]
+ -[PFARepackagingExecutionFailure(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PFARepackagingExecutionFailure(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFARepackagingExecutionResult .cxx_destruct]
+ -[PFARepackagingExecutionResult deleteFailure]
+ -[PFARepackagingExecutionResult deleteSamplingResult]
+ -[PFARepackagingExecutionResult deleteSuccess]
+ -[PFARepackagingExecutionResult dictionaryRepresentation]
+ -[PFARepackagingExecutionResult failure]
+ -[PFARepackagingExecutionResult hasFailure]
+ -[PFARepackagingExecutionResult hasSamplingResult]
+ -[PFARepackagingExecutionResult hasSuccess]
+ -[PFARepackagingExecutionResult hash]
+ -[PFARepackagingExecutionResult initWithDictionary:]
+ -[PFARepackagingExecutionResult initWithJSON:]
+ -[PFARepackagingExecutionResult isEqual:]
+ -[PFARepackagingExecutionResult jsonData]
+ -[PFARepackagingExecutionResult readFrom:]
+ -[PFARepackagingExecutionResult samplingResult]
+ -[PFARepackagingExecutionResult setFailure:]
+ -[PFARepackagingExecutionResult setHasFailure:]
+ -[PFARepackagingExecutionResult setHasSamplingResult:]
+ -[PFARepackagingExecutionResult setHasSuccess:]
+ -[PFARepackagingExecutionResult setSamplingResult:]
+ -[PFARepackagingExecutionResult setSuccess:]
+ -[PFARepackagingExecutionResult success]
+ -[PFARepackagingExecutionResult whichSuccessorfail]
+ -[PFARepackagingExecutionResult writeTo:]
+ -[PFARepackagingExecutionResult(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PFARepackagingExecutionResult(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFARepackagingExecutionSandboxError deleteErrorNumber]
+ -[PFARepackagingExecutionSandboxError dictionaryRepresentation]
+ -[PFARepackagingExecutionSandboxError errorNumber]
+ -[PFARepackagingExecutionSandboxError hasErrorNumber]
+ -[PFARepackagingExecutionSandboxError hash]
+ -[PFARepackagingExecutionSandboxError initWithDictionary:]
+ -[PFARepackagingExecutionSandboxError initWithJSON:]
+ -[PFARepackagingExecutionSandboxError isEqual:]
+ -[PFARepackagingExecutionSandboxError jsonData]
+ -[PFARepackagingExecutionSandboxError readFrom:]
+ -[PFARepackagingExecutionSandboxError setErrorNumber:]
+ -[PFARepackagingExecutionSandboxError setHasErrorNumber:]
+ -[PFARepackagingExecutionSandboxError writeTo:]
+ -[PFARepackagingExecutionSandboxError(SensitiveConditions) suppressMessageUnderConditions]
+ -[PSESchemaPSECall contactMatch]
+ -[PSESchemaPSECall deleteContactMatch]
+ -[PSESchemaPSECall hasContactMatch]
+ -[PSESchemaPSECall setContactMatch:]
+ -[PSESchemaPSECall setHasContactMatch:]
+ -[RFSchemaRFClientEvent deleteRfGradingDialogReportedTier1]
+ -[RFSchemaRFClientEvent hasRfGradingDialogReportedTier1]
+ -[RFSchemaRFClientEvent rfGradingDialogReportedTier1]
+ -[RFSchemaRFClientEvent setHasRfGradingDialogReportedTier1:]
+ -[RFSchemaRFClientEvent setRfGradingDialogReportedTier1:]
+ -[RFSchemaRFGradingDialogLineTier1 .cxx_destruct]
+ -[RFSchemaRFGradingDialogLineTier1 deleteDialogId]
+ -[RFSchemaRFGradingDialogLineTier1 deleteDisplayedDialog]
+ -[RFSchemaRFGradingDialogLineTier1 deleteIsApprovedForGrading]
+ -[RFSchemaRFGradingDialogLineTier1 deleteSpokenDialog]
+ -[RFSchemaRFGradingDialogLineTier1 dialogId]
+ -[RFSchemaRFGradingDialogLineTier1 dictionaryRepresentation]
+ -[RFSchemaRFGradingDialogLineTier1 displayedDialog]
+ -[RFSchemaRFGradingDialogLineTier1 hasDialogId]
+ -[RFSchemaRFGradingDialogLineTier1 hasDisplayedDialog]
+ -[RFSchemaRFGradingDialogLineTier1 hasIsApprovedForGrading]
+ -[RFSchemaRFGradingDialogLineTier1 hasSpokenDialog]
+ -[RFSchemaRFGradingDialogLineTier1 hash]
+ -[RFSchemaRFGradingDialogLineTier1 initWithDictionary:]
+ -[RFSchemaRFGradingDialogLineTier1 initWithJSON:]
+ -[RFSchemaRFGradingDialogLineTier1 isApprovedForGrading]
+ -[RFSchemaRFGradingDialogLineTier1 isEqual:]
+ -[RFSchemaRFGradingDialogLineTier1 jsonData]
+ -[RFSchemaRFGradingDialogLineTier1 readFrom:]
+ -[RFSchemaRFGradingDialogLineTier1 setDialogId:]
+ -[RFSchemaRFGradingDialogLineTier1 setDisplayedDialog:]
+ -[RFSchemaRFGradingDialogLineTier1 setHasDialogId:]
+ -[RFSchemaRFGradingDialogLineTier1 setHasDisplayedDialog:]
+ -[RFSchemaRFGradingDialogLineTier1 setHasIsApprovedForGrading:]
+ -[RFSchemaRFGradingDialogLineTier1 setHasSpokenDialog:]
+ -[RFSchemaRFGradingDialogLineTier1 setIsApprovedForGrading:]
+ -[RFSchemaRFGradingDialogLineTier1 setSpokenDialog:]
+ -[RFSchemaRFGradingDialogLineTier1 spokenDialog]
+ -[RFSchemaRFGradingDialogLineTier1 writeTo:]
+ -[RFSchemaRFGradingDialogLineTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[RFSchemaRFGradingDialogLineTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[RFSchemaRFGradingDialogReportedTier1 .cxx_destruct]
+ -[RFSchemaRFGradingDialogReportedTier1 addDialogLines:]
+ -[RFSchemaRFGradingDialogReportedTier1 clearDialogLines]
+ -[RFSchemaRFGradingDialogReportedTier1 deleteDialogLines]
+ -[RFSchemaRFGradingDialogReportedTier1 dialogLinesAtIndex:]
+ -[RFSchemaRFGradingDialogReportedTier1 dialogLinesCount]
+ -[RFSchemaRFGradingDialogReportedTier1 dialogLines]
+ -[RFSchemaRFGradingDialogReportedTier1 dictionaryRepresentation]
+ -[RFSchemaRFGradingDialogReportedTier1 hash]
+ -[RFSchemaRFGradingDialogReportedTier1 initWithDictionary:]
+ -[RFSchemaRFGradingDialogReportedTier1 initWithJSON:]
+ -[RFSchemaRFGradingDialogReportedTier1 isEqual:]
+ -[RFSchemaRFGradingDialogReportedTier1 jsonData]
+ -[RFSchemaRFGradingDialogReportedTier1 readFrom:]
+ -[RFSchemaRFGradingDialogReportedTier1 setDialogLines:]
+ -[RFSchemaRFGradingDialogReportedTier1 writeTo:]
+ -[RFSchemaRFGradingDialogReportedTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[RFSchemaRFGradingDialogReportedTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaDailyDeviceStatus addInstalledVoices:]
+ -[SISchemaDailyDeviceStatus clearInstalledVoices]
+ -[SISchemaDailyDeviceStatus deleteInstalledVoices]
+ -[SISchemaDailyDeviceStatus installedVoicesAtIndex:]
+ -[SISchemaDailyDeviceStatus installedVoicesCount]
+ -[SISchemaDailyDeviceStatus installedVoices]
+ -[SISchemaDailyDeviceStatus setInstalledVoices:]
+ -[SISchemaSiriVoiceTriggerSettings deleteIsEnrollmentReprompted]
+ -[SISchemaSiriVoiceTriggerSettings hasIsEnrollmentReprompted]
+ -[SISchemaSiriVoiceTriggerSettings isEnrollmentReprompted]
+ -[SISchemaSiriVoiceTriggerSettings setHasIsEnrollmentReprompted:]
+ -[SISchemaSiriVoiceTriggerSettings setIsEnrollmentReprompted:]
+ -[SISchemaUUFRSaid deleteResponseCategory]
+ -[SISchemaUUFRSaid hasResponseCategory]
+ -[SISchemaUUFRSaid responseCategory]
+ -[SISchemaUUFRSaid setHasResponseCategory:]
+ -[SISchemaUUFRSaid setResponseCategory:]
+ -[SISchemaUUFRShown deleteResponseCategory]
+ -[SISchemaUUFRShown hasResponseCategory]
+ -[SISchemaUUFRShown responseCategory]
+ -[SISchemaUUFRShown setHasResponseCategory:]
+ -[SISchemaUUFRShown setResponseCategory:]
+ -[TTSSchemaTTSVoiceContext deleteVoiceName]
+ -[TTSSchemaTTSVoiceContext hasVoiceName]
+ -[TTSSchemaTTSVoiceContext setHasVoiceName:]
+ -[TTSSchemaTTSVoiceContext setVoiceName:]
+ -[TTSSchemaTTSVoiceContext voiceName]
+ -[UAFSchemaUAFAsset assetDownloadSizeInBytes]
+ -[UAFSchemaUAFAsset assetPath]
+ -[UAFSchemaUAFAsset assetUnarchivedSizeInBytes]
+ -[UAFSchemaUAFAsset deleteAssetDownloadSizeInBytes]
+ -[UAFSchemaUAFAsset deleteAssetPath]
+ -[UAFSchemaUAFAsset deleteAssetUnarchivedSizeInBytes]
+ -[UAFSchemaUAFAsset hasAssetDownloadSizeInBytes]
+ -[UAFSchemaUAFAsset hasAssetPath]
+ -[UAFSchemaUAFAsset hasAssetUnarchivedSizeInBytes]
+ -[UAFSchemaUAFAsset setAssetDownloadSizeInBytes:]
+ -[UAFSchemaUAFAsset setAssetPath:]
+ -[UAFSchemaUAFAsset setAssetUnarchivedSizeInBytes:]
+ -[UAFSchemaUAFAsset setHasAssetDownloadSizeInBytes:]
+ -[UAFSchemaUAFAsset setHasAssetPath:]
+ -[UAFSchemaUAFAsset setHasAssetUnarchivedSizeInBytes:]
+ -[UAFSchemaUAFAssetMetadata .cxx_destruct]
+ -[UAFSchemaUAFAssetMetadata assetName]
+ -[UAFSchemaUAFAssetMetadata assetSizeInBytes]
+ -[UAFSchemaUAFAssetMetadata deleteAssetName]
+ -[UAFSchemaUAFAssetMetadata deleteAssetSizeInBytes]
+ -[UAFSchemaUAFAssetMetadata dictionaryRepresentation]
+ -[UAFSchemaUAFAssetMetadata hasAssetName]
+ -[UAFSchemaUAFAssetMetadata hasAssetSizeInBytes]
+ -[UAFSchemaUAFAssetMetadata hash]
+ -[UAFSchemaUAFAssetMetadata initWithDictionary:]
+ -[UAFSchemaUAFAssetMetadata initWithJSON:]
+ -[UAFSchemaUAFAssetMetadata isEqual:]
+ -[UAFSchemaUAFAssetMetadata jsonData]
+ -[UAFSchemaUAFAssetMetadata readFrom:]
+ -[UAFSchemaUAFAssetMetadata setAssetName:]
+ -[UAFSchemaUAFAssetMetadata setAssetSizeInBytes:]
+ -[UAFSchemaUAFAssetMetadata setHasAssetName:]
+ -[UAFSchemaUAFAssetMetadata setHasAssetSizeInBytes:]
+ -[UAFSchemaUAFAssetMetadata writeTo:]
+ -[UAFSchemaUAFAssetMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[UAFSchemaUAFAssetSetStatus addAllAssets:]
+ -[UAFSchemaUAFAssetSetStatus allAssetsAtIndex:]
+ -[UAFSchemaUAFAssetSetStatus allAssetsCount]
+ -[UAFSchemaUAFAssetSetStatus allAssets]
+ -[UAFSchemaUAFAssetSetStatus clearAllAssets]
+ -[UAFSchemaUAFAssetSetStatus deleteAllAssets]
+ -[UAFSchemaUAFAssetSetStatus setAllAssets:]
+ OBJC_IVAR_$_ASRSchemaASREntityMetadata._entityRank
+ OBJC_IVAR_$_ASRSchemaASREntityMetadata._has
+ OBJC_IVAR_$_ASRSchemaASRRecognitionMetrics._numIngestedNeuralContextualBiasingEmbeddings
+ OBJC_IVAR_$_ASRSchemaASRToken._entityMetadata
+ OBJC_IVAR_$_DIMSchemaDIMClientEvent._experimentContext
+ OBJC_IVAR_$_DIMSchemaDIMExperimentContext._experimentInfos
+ OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._deploymentId
+ OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._experimentId
+ OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._has
+ OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._treatmentId
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECRRTrainingSampleCollected._crrCommsAppSelectionJointId
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated._crrCommsAppSelectionJointId
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals._appFreqForMessages
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals._appFreqForMessagesForCountryCode
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentMessageSignals._appFreqForMessagesUsingSiri
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals._appFreqForPhoneCall
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals._appFreqForPhoneCallForCountryCode
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentPhoneCallSignals._appFreqForPhoneCallUsingSiri
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals._appTimeSpentInSec
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals._timeSinceAppContactLastLaunchedInSec
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages10Min
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages1Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages1Hr
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages28Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages2Min
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages6Hr
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessages7Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessagesHaptic
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessagesInf
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentMessageSignals._appContactFreqForMessagesUsingSiri
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall10Min
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall1Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall1Hr
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall28Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall2Min
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall6Hr
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCall7Day
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCallHaptic
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCallInf
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingContactDependentPhoneCallSignals._appContactFreqForPhoneCallUsingSiri
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._entitySearchBundleScoreRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._usageScoreBooksRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._usageScoreMusicRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._usageScoreMusicWithoutRadioRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._usageScorePodcastsRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._usageScoreRadioRemote
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._serverSearchResultsMediaType
+ OBJC_IVAR_$_MHSchemaMHOdldFalseTriggerMitigated._anchorRequestId
+ OBJC_IVAR_$_MHSchemaMHOdldFalseTriggerMitigated._anchorSocialScore
+ OBJC_IVAR_$_MHSchemaMHOdldFalseTriggerMitigated._previousRequestId
+ OBJC_IVAR_$_NETSchemaNETClientEventMetadata._has
+ OBJC_IVAR_$_NETSchemaNETClientEventMetadata._networkConnectionId
+ OBJC_IVAR_$_NETSchemaNETClientEventMetadata._provider
+ OBJC_IVAR_$_NETSchemaNETDebugNetworkInterface._networkInterface
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEvent._eventMetadata
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEvent._odbatchDataReported
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEventMetadata._odbatchId
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHDataReported._daysWithTwoAssistantSpeechRequestsPerWeek
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHDataReported._daysWithTwoValidAssistantTurnsPerWeek
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHDataReported._has
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHDataReported._originalClockId
+ OBJC_IVAR_$_ODDSiriSchemaODDAdaptiveVolumeProperties._adaptiveVolume
+ OBJC_IVAR_$_ODDSiriSchemaODDAdaptiveVolumeProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAdaptiveVolumeProperties._isAdaptiveVolumeEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAdaptiveVolumeProperties._isPermanentOffsetEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAdaptiveVolumeProperties._permanentOffsetFactor
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._carPlayStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isAnnounceCallsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isAnnounceNotificationsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isCarPlayMuted
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isEnabledForHeadphones
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isProximityCardSeen
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isReplyWithoutConfirmationEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAnnounceProperties._isSpokenNotificationsControlCenterModuleEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest._appTaskCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._responseCategory
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._reliabilityCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._sessionCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._taskCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._turnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._tuples
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._digestType
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._experimentFixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._assistantDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._codePathId
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._experimentAllocationStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._isFirstTriggerOrAfterFirstTrigger
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._isTriggered
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentTuples._endpointDelayInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentTuples._launchTimeInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentTuples._siriResponseTimeInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentTuples._timeToFirstWordInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentTuples._timeToUufrInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._homeKit
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._inputLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._isAssistantEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._isPreciseLocationEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._listenFor
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._numSiriShortcutsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._optIn
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._voice
+ OBJC_IVAR_$_ODDSiriSchemaODDAutoSendMessageProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAutoSendMessageProperties._isAutomaticallySendMessagesEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDAutoSendMessageProperties._isEnabledForCarPlay
+ OBJC_IVAR_$_ODDSiriSchemaODDAutoSendMessageProperties._isEnabledForHeadphones
+ OBJC_IVAR_$_ODDSiriSchemaODDCarPlayProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDCarPlayProperties._isShowAppsBehindSiriEnabledOnCarPlay
+ OBJC_IVAR_$_ODDSiriSchemaODDCarPlayProperties._isSiriCapableDigitalCarKeyAvailable
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts._cancelledSiriAppTaskCount
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts._completedSiriAppTaskCount
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts._completedUIAppTaskCount
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts._failedSiriAppTaskCount
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._appTaskType
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._audioInterface
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._siriInputLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._taskAppBundleId
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._viewInterface
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationProperties._enabledDictationLocales
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationProperties._isAutoPunctuationEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationProperties._isDictationEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._deploymentId
+ OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._experimentId
+ OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._treatmentId
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._UTCOffset
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._deviceOS
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._deviceType
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._isStoreDemoMode
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._modelNumber
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._storefrontId
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._systemLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDHomeKitProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDHomeKitProperties._hasHomekitHome
+ OBJC_IVAR_$_ODDSiriSchemaODDHomePodProperties._adaptiveVolume
+ OBJC_IVAR_$_ODDSiriSchemaODDHomePodProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDHomePodProperties._isPersonalDomainsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._has
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numGuestsAccepted
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numParticipantsWithTrust
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWhoSyncedRecognizeMyVoice
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWithLocationServicesEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWithMatchingSiriLanguage
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWithPersonalRequestsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWithRecognizeMyVoiceEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numUsersWithSiriCloudSyncEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserSetupStatus._numVoiceProfilesAvailable
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserState._enrolledUsers
+ OBJC_IVAR_$_ODDSiriSchemaODDMultiUserState._multiUserSetupStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDOptInProperties._dataSharingOptInStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDOptInProperties._gradingOptInStateChanges
+ OBJC_IVAR_$_ODDSiriSchemaODDOptInProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDOptInProperties._isMteUploadEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDOptInProperties._isServerUserDataSyncEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDSessionCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDSessionCounts._usdxSessionCount
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assistantDiagnosticAndUsageOptInDigestReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assistantExperimentDigestReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._iOSDevicePropertiesReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._macOSDevicePropertiesReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._tvOSDevicePropertiesReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._visionOSDevicePropertiesReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._watchOSDevicePropertiesReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriInCallProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriInCallProperties._heySiriHangupEnablementState
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriInCallProperties._siriInCallEnablementState
+ OBJC_IVAR_$_ODDSiriSchemaODDUserPersonalization._activeSubscriptions
+ OBJC_IVAR_$_ODDSiriSchemaODDUserPersonalization._has
+ OBJC_IVAR_$_ODDSiriSchemaODDUserPersonalization._isPersonalDomainRequestsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDUserPersonalization._voiceSettings
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._accent
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._gender
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._installedVoices
+ OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._name
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._isAlwaysListenForHeySiriEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._isShowAppsBehindSiriEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._isTypeToSiriEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._isVoiceOverEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._siriPauseTimeState
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._siriSpeechRate
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAccessibilityProperties._voiceFeedback
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._accessibility
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._activeSubscriptions
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._announce
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._autoSendMessage
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._carPlay
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._isAllowSiriWhenLockedEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._isPressSideButtonForSiriEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._response
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._siriInCall
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._assistant
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._dictation
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._general
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._iOSAssistant
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSResponseProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSResponseProperties._isAlwaysShowSiriCaptionsEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDiOSResponseProperties._isAlwaysShowSpeechEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSAssistantProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSAssistantProperties._isExternalMicrophoneHSEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._assistant
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._dictation
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._general
+ OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._macOSAssistant
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSAssistantProperties._homePodProperties
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSAssistantProperties._multiUserState
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._assistant
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._dictation
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._general
+ OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._tvOSAssistant
+ OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._assistant
+ OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._dictation
+ OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._general
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSAssistantProperties._has
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSAssistantProperties._isRaiseToSpeakEnabled
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._assistant
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._dictation
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._general
+ OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._watchOSAssistant
+ OBJC_IVAR_$_ORCHSchemaORCHMUXBridgeContext._ephemeralToAggregationIdentifierMap
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._deviceAggregationId
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._has
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._userAggregationId
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._userAggregationIdExpirationTimestampMs
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._userAggregationIdRotationTimestampMs
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._userEphemeralId
+ OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext._selectedUser
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCrossIntentRankerResponse._cirFallbackTriggered
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCrossIntentRankerResponse._has
+ OBJC_IVAR_$_PFAClockEnvelopeStatistics._has
+ OBJC_IVAR_$_PFAClockEnvelopeStatistics._messageCount
+ OBJC_IVAR_$_PFAClockEnvelopeStatistics._totalBytes
+ OBJC_IVAR_$_PFAPFAClientEvent._repackagingExecution
+ OBJC_IVAR_$_PFARepackagingExecution._clockIdentifier
+ OBJC_IVAR_$_PFARepackagingExecution._envelopeStatistics
+ OBJC_IVAR_$_PFARepackagingExecution._result
+ OBJC_IVAR_$_PFARepackagingExecutionFBFFailure._flErrorCode
+ OBJC_IVAR_$_PFARepackagingExecutionFBFFailure._has
+ OBJC_IVAR_$_PFARepackagingExecutionFailure._fbfFailure
+ OBJC_IVAR_$_PFARepackagingExecutionFailure._sandboxError
+ OBJC_IVAR_$_PFARepackagingExecutionResult._failure
+ OBJC_IVAR_$_PFARepackagingExecutionResult._has
+ OBJC_IVAR_$_PFARepackagingExecutionResult._samplingResult
+ OBJC_IVAR_$_PFARepackagingExecutionResult._success
+ OBJC_IVAR_$_PFARepackagingExecutionSandboxError._errorNumber
+ OBJC_IVAR_$_PFARepackagingExecutionSandboxError._has
+ OBJC_IVAR_$_PSESchemaPSECall._contactMatch
+ OBJC_IVAR_$_RFSchemaRFClientEvent._rfGradingDialogReportedTier1
+ OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._dialogId
+ OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._displayedDialog
+ OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._has
+ OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._isApprovedForGrading
+ OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._spokenDialog
+ OBJC_IVAR_$_RFSchemaRFGradingDialogReportedTier1._dialogLines
+ OBJC_IVAR_$_SISchemaDailyDeviceStatus._installedVoices
+ OBJC_IVAR_$_SISchemaSiriVoiceTriggerSettings._isEnrollmentReprompted
+ OBJC_IVAR_$_SISchemaUUFRSaid._responseCategory
+ OBJC_IVAR_$_SISchemaUUFRShown._responseCategory
+ OBJC_IVAR_$_TTSSchemaTTSVoiceContext._voiceName
+ OBJC_IVAR_$_UAFSchemaUAFAsset._assetDownloadSizeInBytes
+ OBJC_IVAR_$_UAFSchemaUAFAsset._assetPath
+ OBJC_IVAR_$_UAFSchemaUAFAsset._assetUnarchivedSizeInBytes
+ OBJC_IVAR_$_UAFSchemaUAFAssetMetadata._assetName
+ OBJC_IVAR_$_UAFSchemaUAFAssetMetadata._assetSizeInBytes
+ OBJC_IVAR_$_UAFSchemaUAFAssetMetadata._has
+ OBJC_IVAR_$_UAFSchemaUAFAssetSetStatus._allAssets
+ _ASRSchemaASREntityMetadataReadFrom
+ _DIMSchemaDIMExperimentContextReadFrom
+ _DIMSchemaDIMExperimentInfoReadFrom
+ _OBJC_CLASS_$_ASRSchemaASREntityMetadata
+ _OBJC_CLASS_$_DIMSchemaDIMExperimentContext
+ _OBJC_CLASS_$_DIMSchemaDIMExperimentInfo
+ _OBJC_CLASS_$_ODBATCHSiriSchemaODBATCHClientEvent
+ _OBJC_CLASS_$_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ _OBJC_CLASS_$_ODBATCHSiriSchemaODBATCHDataReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAdaptiveVolumeProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDAnnounceProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantExperimentCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantExperimentDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantExperimentDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantExperimentTuples
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDAutoSendMessageProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDCarPlayProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDDictationProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDExperimentFixedDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDGeneralProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDHomeKitProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDHomePodProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDMultiUserSetupStatus
+ _OBJC_CLASS_$_ODDSiriSchemaODDMultiUserState
+ _OBJC_CLASS_$_ODDSiriSchemaODDOptInProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDSessionCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDSiriInCallProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDUserPersonalization
+ _OBJC_CLASS_$_ODDSiriSchemaODDVoiceProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDiOSAccessibilityProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDiOSAssistantProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDiOSDevicePropertiesReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDiOSResponseProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDmacOSAssistantProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDtvOSAssistantProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDwatchOSAssistantProperties
+ _OBJC_CLASS_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ _OBJC_CLASS_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ _OBJC_CLASS_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ _OBJC_CLASS_$_PFAClockEnvelopeStatistics
+ _OBJC_CLASS_$_PFAPFAClientEvent
+ _OBJC_CLASS_$_PFARepackagingExecution
+ _OBJC_CLASS_$_PFARepackagingExecutionFBFFailure
+ _OBJC_CLASS_$_PFARepackagingExecutionFailure
+ _OBJC_CLASS_$_PFARepackagingExecutionResult
+ _OBJC_CLASS_$_PFARepackagingExecutionSandboxError
+ _OBJC_CLASS_$_RFSchemaRFGradingDialogLineTier1
+ _OBJC_CLASS_$_RFSchemaRFGradingDialogReportedTier1
+ _OBJC_CLASS_$_UAFSchemaUAFAssetMetadata
+ _OBJC_IVAR_$_ASRSchemaASRToken._hasEntityMetadata
+ _OBJC_IVAR_$_DIMSchemaDIMClientEvent._hasExperimentContext
+ _OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._hasExperimentId
+ _OBJC_IVAR_$_DIMSchemaDIMExperimentInfo._hasTreatmentId
+ _OBJC_IVAR_$_INFERENCESchemaINFERENCECRRTrainingSampleCollected._hasCrrCommsAppSelectionJointId
+ _OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionGroundTruthGenerated._hasCrrCommsAppSelectionJointId
+ _OBJC_IVAR_$_MHSchemaMHOdldFalseTriggerMitigated._hasAnchorRequestId
+ _OBJC_IVAR_$_MHSchemaMHOdldFalseTriggerMitigated._hasPreviousRequestId
+ _OBJC_IVAR_$_NETSchemaNETClientEventMetadata._hasNetworkConnectionId
+ _OBJC_IVAR_$_NETSchemaNETDebugNetworkInterface._hasNetworkInterface
+ _OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEvent._hasOdbatchDataReported
+ _OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHClientEventMetadata._hasOdbatchId
+ _OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHDataReported._hasOriginalClockId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest._hasAppTaskCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._hasReliabilityCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._hasSessionCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._hasTaskCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentCounts._hasTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigest._hasTuples
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._hasExperimentFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._hasAssistantDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantExperimentDimensions._hasCodePathId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._hasHomeKit
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._hasInputLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._hasOptIn
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._hasVoice
+ _OBJC_IVAR_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions._hasSiriInputLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._hasExperimentId
+ _OBJC_IVAR_$_ODDSiriSchemaODDExperimentFixedDimensions._hasTreatmentId
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._hasDeviceOS
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._hasDeviceType
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._hasModelNumber
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._hasSystemLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDHomePodProperties._hasAdaptiveVolume
+ _OBJC_IVAR_$_ODDSiriSchemaODDMultiUserState._hasMultiUserSetupStatus
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssistantDiagnosticAndUsageOptInDigestReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssistantExperimentDigestReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasIOSDevicePropertiesReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasMacOSDevicePropertiesReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasTvOSDevicePropertiesReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasVisionOSDevicePropertiesReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasWatchOSDevicePropertiesReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDUserPersonalization._hasVoiceSettings
+ _OBJC_IVAR_$_ODDSiriSchemaODDVoiceProperties._hasAccent
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasAccessibility
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasAnnounce
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasAutoSendMessage
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasCarPlay
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasResponse
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSAssistantProperties._hasSiriInCall
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._hasAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._hasDictation
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._hasGeneral
+ _OBJC_IVAR_$_ODDSiriSchemaODDiOSDevicePropertiesReported._hasIOSAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._hasAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._hasDictation
+ _OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._hasGeneral
+ _OBJC_IVAR_$_ODDSiriSchemaODDmacOSDevicePropertiesReported._hasMacOSAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSAssistantProperties._hasHomePodProperties
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSAssistantProperties._hasMultiUserState
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._hasAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._hasDictation
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._hasGeneral
+ _OBJC_IVAR_$_ODDSiriSchemaODDtvOSDevicePropertiesReported._hasTvOSAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._hasAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._hasDictation
+ _OBJC_IVAR_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported._hasGeneral
+ _OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._hasAssistant
+ _OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._hasDictation
+ _OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._hasGeneral
+ _OBJC_IVAR_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported._hasWatchOSAssistant
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXBridgeContext._hasEphemeralToAggregationIdentifierMap
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._hasDeviceAggregationId
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._hasUserAggregationId
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap._hasUserEphemeralId
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext._hasSelectedUser
+ _OBJC_IVAR_$_PFAPFAClientEvent._hasRepackagingExecution
+ _OBJC_IVAR_$_PFAPFAClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_PFARepackagingExecution._hasClockIdentifier
+ _OBJC_IVAR_$_PFARepackagingExecution._hasEnvelopeStatistics
+ _OBJC_IVAR_$_PFARepackagingExecution._hasResult
+ _OBJC_IVAR_$_PFARepackagingExecutionFailure._hasFbfFailure
+ _OBJC_IVAR_$_PFARepackagingExecutionFailure._hasSandboxError
+ _OBJC_IVAR_$_PFARepackagingExecutionFailure._whichKind
+ _OBJC_IVAR_$_PFARepackagingExecutionResult._hasFailure
+ _OBJC_IVAR_$_PFARepackagingExecutionResult._hasSuccess
+ _OBJC_IVAR_$_PFARepackagingExecutionResult._whichSuccessorfail
+ _OBJC_IVAR_$_RFSchemaRFClientEvent._hasRfGradingDialogReportedTier1
+ _OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._hasDialogId
+ _OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._hasDisplayedDialog
+ _OBJC_IVAR_$_RFSchemaRFGradingDialogLineTier1._hasSpokenDialog
+ _OBJC_IVAR_$_UAFSchemaUAFAsset._hasAssetPath
+ _OBJC_IVAR_$_UAFSchemaUAFAssetMetadata._hasAssetName
+ _OBJC_METACLASS_$_ASRSchemaASREntityMetadata
+ _OBJC_METACLASS_$_DIMSchemaDIMExperimentContext
+ _OBJC_METACLASS_$_DIMSchemaDIMExperimentInfo
+ _OBJC_METACLASS_$_ODBATCHSiriSchemaODBATCHClientEvent
+ _OBJC_METACLASS_$_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ _OBJC_METACLASS_$_ODBATCHSiriSchemaODBATCHDataReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAdaptiveVolumeProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAnnounceProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantExperimentCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantExperimentDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantExperimentDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantExperimentTuples
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAutoSendMessageProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDCarPlayProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDictationProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDExperimentFixedDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDGeneralProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDHomeKitProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDHomePodProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMultiUserSetupStatus
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMultiUserState
+ _OBJC_METACLASS_$_ODDSiriSchemaODDOptInProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDSessionCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDSiriInCallProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDUserPersonalization
+ _OBJC_METACLASS_$_ODDSiriSchemaODDVoiceProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDiOSAccessibilityProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDiOSAssistantProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDiOSDevicePropertiesReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDiOSResponseProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDmacOSAssistantProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDtvOSAssistantProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDwatchOSAssistantProperties
+ _OBJC_METACLASS_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ _OBJC_METACLASS_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ _OBJC_METACLASS_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ _OBJC_METACLASS_$_PFAClockEnvelopeStatistics
+ _OBJC_METACLASS_$_PFAPFAClientEvent
+ _OBJC_METACLASS_$_PFARepackagingExecution
+ _OBJC_METACLASS_$_PFARepackagingExecutionFBFFailure
+ _OBJC_METACLASS_$_PFARepackagingExecutionFailure
+ _OBJC_METACLASS_$_PFARepackagingExecutionResult
+ _OBJC_METACLASS_$_PFARepackagingExecutionSandboxError
+ _OBJC_METACLASS_$_RFSchemaRFGradingDialogLineTier1
+ _OBJC_METACLASS_$_RFSchemaRFGradingDialogReportedTier1
+ _OBJC_METACLASS_$_UAFSchemaUAFAssetMetadata
+ _ODBATCHSiriSchemaODBATCHClientEventMetadataReadFrom
+ _ODBATCHSiriSchemaODBATCHClientEventReadFrom
+ _ODBATCHSiriSchemaODBATCHDataReportedReadFrom
+ _ODDSiriSchemaODDAdaptiveVolumePropertiesReadFrom
+ _ODDSiriSchemaODDAnnouncePropertiesReadFrom
+ _ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestReadFrom
+ _ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReportedReadFrom
+ _ODDSiriSchemaODDAssistantExperimentCountsReadFrom
+ _ODDSiriSchemaODDAssistantExperimentDigestReadFrom
+ _ODDSiriSchemaODDAssistantExperimentDigestsReportedReadFrom
+ _ODDSiriSchemaODDAssistantExperimentDimensionsReadFrom
+ _ODDSiriSchemaODDAssistantExperimentTuplesReadFrom
+ _ODDSiriSchemaODDAssistantPropertiesReadFrom
+ _ODDSiriSchemaODDAutoSendMessagePropertiesReadFrom
+ _ODDSiriSchemaODDCarPlayPropertiesReadFrom
+ _ODDSiriSchemaODDDeviceAndUsageAppTaskCountsReadFrom
+ _ODDSiriSchemaODDDeviceAndUsageDynamicDimensionsReadFrom
+ _ODDSiriSchemaODDDictationPropertiesReadFrom
+ _ODDSiriSchemaODDExperimentFixedDimensionsReadFrom
+ _ODDSiriSchemaODDGeneralPropertiesReadFrom
+ _ODDSiriSchemaODDHomeKitPropertiesReadFrom
+ _ODDSiriSchemaODDHomePodPropertiesReadFrom
+ _ODDSiriSchemaODDMultiUserSetupStatusReadFrom
+ _ODDSiriSchemaODDMultiUserStateReadFrom
+ _ODDSiriSchemaODDOptInPropertiesReadFrom
+ _ODDSiriSchemaODDSessionCountsReadFrom
+ _ODDSiriSchemaODDSiriInCallPropertiesReadFrom
+ _ODDSiriSchemaODDUserPersonalizationReadFrom
+ _ODDSiriSchemaODDVoicePropertiesReadFrom
+ _ODDSiriSchemaODDiOSAccessibilityPropertiesReadFrom
+ _ODDSiriSchemaODDiOSAssistantPropertiesReadFrom
+ _ODDSiriSchemaODDiOSDevicePropertiesReportedReadFrom
+ _ODDSiriSchemaODDiOSResponsePropertiesReadFrom
+ _ODDSiriSchemaODDmacOSAssistantPropertiesReadFrom
+ _ODDSiriSchemaODDmacOSDevicePropertiesReportedReadFrom
+ _ODDSiriSchemaODDtvOSAssistantPropertiesReadFrom
+ _ODDSiriSchemaODDtvOSDevicePropertiesReportedReadFrom
+ _ODDSiriSchemaODDvisionOSDevicePropertiesReportedReadFrom
+ _ODDSiriSchemaODDwatchOSAssistantPropertiesReadFrom
+ _ODDSiriSchemaODDwatchOSDevicePropertiesReportedReadFrom
+ _ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContextReadFrom
+ _ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapReadFrom
+ _PFAClockEnvelopeStatisticsReadFrom
+ _PFAPFAClientEventReadFrom
+ _PFARepackagingExecutionFBFFailureReadFrom
+ _PFARepackagingExecutionFailureReadFrom
+ _PFARepackagingExecutionReadFrom
+ _PFARepackagingExecutionResultReadFrom
+ _PFARepackagingExecutionSandboxErrorReadFrom
+ _RFSchemaRFGradingDialogLineTier1ReadFrom
+ _RFSchemaRFGradingDialogReportedTier1ReadFrom
+ _UAFSchemaUAFAssetMetadataReadFrom
+ __OBJC_$_CLASS_METHODS_ODBATCHSiriSchemaODBATCHClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_CLASS_METHODS_PFAPFAClientEvent(SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASREntityMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DIMSchemaDIMExperimentContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DIMSchemaDIMExperimentInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODBATCHSiriSchemaODBATCHClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ODBATCHSiriSchemaODBATCHClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODBATCHSiriSchemaODBATCHDataReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAdaptiveVolumeProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAnnounceProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantExperimentCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantExperimentDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantExperimentDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantExperimentDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantExperimentTuples(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAutoSendMessageProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDCarPlayProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDictationProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDExperimentFixedDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDGeneralProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDHomeKitProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDHomePodProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMultiUserSetupStatus(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMultiUserState(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDOptInProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDSessionCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDSiriInCallProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDUserPersonalization(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDVoiceProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDiOSAccessibilityProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDiOSAssistantProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDiOSDevicePropertiesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDiOSResponseProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDmacOSAssistantProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDmacOSDevicePropertiesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDtvOSAssistantProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDtvOSDevicePropertiesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDvisionOSDevicePropertiesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDwatchOSAssistantProperties(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDwatchOSDevicePropertiesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFAClockEnvelopeStatistics(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFAPFAClientEvent(SensitiveConditions|InnerEventContainer|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_PFARepackagingExecution(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFARepackagingExecutionFBFFailure(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFARepackagingExecutionFailure(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFARepackagingExecutionResult(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFARepackagingExecutionSandboxError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_RFSchemaRFGradingDialogLineTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_RFSchemaRFGradingDialogReportedTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_UAFSchemaUAFAssetMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASREntityMetadata
+ __OBJC_$_INSTANCE_VARIABLES_DIMSchemaDIMExperimentContext
+ __OBJC_$_INSTANCE_VARIABLES_DIMSchemaDIMExperimentInfo
+ __OBJC_$_INSTANCE_VARIABLES_ODBATCHSiriSchemaODBATCHClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ODBATCHSiriSchemaODBATCHDataReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAdaptiveVolumeProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAnnounceProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantExperimentCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantExperimentDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantExperimentDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantExperimentTuples
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAutoSendMessageProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDCarPlayProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDictationProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDExperimentFixedDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDGeneralProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDHomeKitProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDHomePodProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMultiUserSetupStatus
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMultiUserState
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDOptInProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDSessionCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDSiriInCallProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDUserPersonalization
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDVoiceProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDiOSAccessibilityProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDiOSAssistantProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDiOSDevicePropertiesReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDiOSResponseProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDmacOSAssistantProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDtvOSAssistantProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDwatchOSAssistantProperties
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ __OBJC_$_INSTANCE_VARIABLES_PFAClockEnvelopeStatistics
+ __OBJC_$_INSTANCE_VARIABLES_PFAPFAClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_PFARepackagingExecution
+ __OBJC_$_INSTANCE_VARIABLES_PFARepackagingExecutionFBFFailure
+ __OBJC_$_INSTANCE_VARIABLES_PFARepackagingExecutionFailure
+ __OBJC_$_INSTANCE_VARIABLES_PFARepackagingExecutionResult
+ __OBJC_$_INSTANCE_VARIABLES_PFARepackagingExecutionSandboxError
+ __OBJC_$_INSTANCE_VARIABLES_RFSchemaRFGradingDialogLineTier1
+ __OBJC_$_INSTANCE_VARIABLES_RFSchemaRFGradingDialogReportedTier1
+ __OBJC_$_INSTANCE_VARIABLES_UAFSchemaUAFAssetMetadata
+ __OBJC_$_PROP_LIST_ASRSchemaASREntityMetadata
+ __OBJC_$_PROP_LIST_DIMSchemaDIMExperimentContext
+ __OBJC_$_PROP_LIST_DIMSchemaDIMExperimentInfo
+ __OBJC_$_PROP_LIST_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ __OBJC_$_PROP_LIST_ODBATCHSiriSchemaODBATCHDataReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAdaptiveVolumeProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAnnounceProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantExperimentCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantExperimentDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantExperimentDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantExperimentTuples
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAutoSendMessageProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDCarPlayProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDictationProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDExperimentFixedDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDGeneralProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDHomeKitProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDHomePodProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMultiUserSetupStatus
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMultiUserState
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDOptInProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDSessionCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDSiriInCallProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDUserPersonalization
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDVoiceProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDiOSAccessibilityProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDiOSAssistantProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDiOSDevicePropertiesReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDiOSResponseProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDmacOSAssistantProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDtvOSAssistantProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDwatchOSAssistantProperties
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ __OBJC_$_PROP_LIST_PFAClockEnvelopeStatistics
+ __OBJC_$_PROP_LIST_PFARepackagingExecution
+ __OBJC_$_PROP_LIST_PFARepackagingExecutionFBFFailure
+ __OBJC_$_PROP_LIST_PFARepackagingExecutionFailure
+ __OBJC_$_PROP_LIST_PFARepackagingExecutionResult
+ __OBJC_$_PROP_LIST_PFARepackagingExecutionSandboxError
+ __OBJC_$_PROP_LIST_RFSchemaRFGradingDialogLineTier1
+ __OBJC_$_PROP_LIST_RFSchemaRFGradingDialogReportedTier1
+ __OBJC_$_PROP_LIST_UAFSchemaUAFAssetMetadata
+ __OBJC_CLASS_PROTOCOLS_$_ODBATCHSiriSchemaODBATCHClientEvent(InnerEventContainer)
+ __OBJC_CLASS_PROTOCOLS_$_PFAPFAClientEvent(InnerEventContainer)
+ __OBJC_CLASS_RO_$_ASRSchemaASREntityMetadata
+ __OBJC_CLASS_RO_$_DIMSchemaDIMExperimentContext
+ __OBJC_CLASS_RO_$_DIMSchemaDIMExperimentInfo
+ __OBJC_CLASS_RO_$_ODBATCHSiriSchemaODBATCHClientEvent
+ __OBJC_CLASS_RO_$_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ __OBJC_CLASS_RO_$_ODBATCHSiriSchemaODBATCHDataReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAdaptiveVolumeProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAnnounceProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantExperimentCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantExperimentTuples
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAutoSendMessageProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDCarPlayProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDictationProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDExperimentFixedDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDGeneralProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDHomeKitProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDHomePodProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMultiUserSetupStatus
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMultiUserState
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDOptInProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDSessionCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDSiriInCallProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDUserPersonalization
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDVoiceProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDiOSAccessibilityProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDiOSAssistantProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDiOSDevicePropertiesReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDiOSResponseProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDmacOSAssistantProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDtvOSAssistantProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDwatchOSAssistantProperties
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ __OBJC_CLASS_RO_$_PFAClockEnvelopeStatistics
+ __OBJC_CLASS_RO_$_PFAPFAClientEvent
+ __OBJC_CLASS_RO_$_PFARepackagingExecution
+ __OBJC_CLASS_RO_$_PFARepackagingExecutionFBFFailure
+ __OBJC_CLASS_RO_$_PFARepackagingExecutionFailure
+ __OBJC_CLASS_RO_$_PFARepackagingExecutionResult
+ __OBJC_CLASS_RO_$_PFARepackagingExecutionSandboxError
+ __OBJC_CLASS_RO_$_RFSchemaRFGradingDialogLineTier1
+ __OBJC_CLASS_RO_$_RFSchemaRFGradingDialogReportedTier1
+ __OBJC_CLASS_RO_$_UAFSchemaUAFAssetMetadata
+ __OBJC_METACLASS_RO_$_ASRSchemaASREntityMetadata
+ __OBJC_METACLASS_RO_$_DIMSchemaDIMExperimentContext
+ __OBJC_METACLASS_RO_$_DIMSchemaDIMExperimentInfo
+ __OBJC_METACLASS_RO_$_ODBATCHSiriSchemaODBATCHClientEvent
+ __OBJC_METACLASS_RO_$_ODBATCHSiriSchemaODBATCHClientEventMetadata
+ __OBJC_METACLASS_RO_$_ODBATCHSiriSchemaODBATCHDataReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAdaptiveVolumeProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAnnounceProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantExperimentCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantExperimentDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantExperimentTuples
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAutoSendMessageProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDCarPlayProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceAndUsageAppTaskCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceAndUsageDynamicDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDictationProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDExperimentFixedDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDGeneralProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDHomeKitProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDHomePodProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMultiUserSetupStatus
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMultiUserState
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDOptInProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDSessionCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDSiriInCallProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDUserPersonalization
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDVoiceProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDiOSAccessibilityProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDiOSAssistantProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDiOSDevicePropertiesReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDiOSResponseProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDmacOSAssistantProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDmacOSDevicePropertiesReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDtvOSAssistantProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDtvOSDevicePropertiesReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDvisionOSDevicePropertiesReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDwatchOSAssistantProperties
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDwatchOSDevicePropertiesReported
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext
+ __OBJC_METACLASS_RO_$_PFAClockEnvelopeStatistics
+ __OBJC_METACLASS_RO_$_PFAPFAClientEvent
+ __OBJC_METACLASS_RO_$_PFARepackagingExecution
+ __OBJC_METACLASS_RO_$_PFARepackagingExecutionFBFFailure
+ __OBJC_METACLASS_RO_$_PFARepackagingExecutionFailure
+ __OBJC_METACLASS_RO_$_PFARepackagingExecutionResult
+ __OBJC_METACLASS_RO_$_PFARepackagingExecutionSandboxError
+ __OBJC_METACLASS_RO_$_RFSchemaRFGradingDialogLineTier1
+ __OBJC_METACLASS_RO_$_RFSchemaRFGradingDialogReportedTier1
+ __OBJC_METACLASS_RO_$_UAFSchemaUAFAssetMetadata
+ ___swift_memcpy12_8
+ _objc_msgSend$UTCOffset
+ _objc_msgSend$accent
+ _objc_msgSend$accessibility
+ _objc_msgSend$adaptiveVolume
+ _objc_msgSend$addAllAssets:
+ _objc_msgSend$addDialogLines:
+ _objc_msgSend$addEndpointDelayInMs:
+ _objc_msgSend$addExperimentInfo:
+ _objc_msgSend$addInstalledVoices:
+ _objc_msgSend$addLaunchTimeInMs:
+ _objc_msgSend$addSiriResponseTimeInMs:
+ _objc_msgSend$addTimeToFirstWordInMs:
+ _objc_msgSend$addTimeToUufrInMs:
+ _objc_msgSend$allAssets
+ _objc_msgSend$anchorRequestId
+ _objc_msgSend$anchorSocialScore
+ _objc_msgSend$announce
+ _objc_msgSend$appContactFreqForMessages
+ _objc_msgSend$appContactFreqForMessages10Min
+ _objc_msgSend$appContactFreqForMessages1Day
+ _objc_msgSend$appContactFreqForMessages1Hr
+ _objc_msgSend$appContactFreqForMessages28Day
+ _objc_msgSend$appContactFreqForMessages2Min
+ _objc_msgSend$appContactFreqForMessages6Hr
+ _objc_msgSend$appContactFreqForMessages7Day
+ _objc_msgSend$appContactFreqForMessagesHaptic
+ _objc_msgSend$appContactFreqForMessagesInf
+ _objc_msgSend$appContactFreqForMessagesUsingSiri
+ _objc_msgSend$appContactFreqForPhoneCall
+ _objc_msgSend$appContactFreqForPhoneCall10Min
+ _objc_msgSend$appContactFreqForPhoneCall1Day
+ _objc_msgSend$appContactFreqForPhoneCall1Hr
+ _objc_msgSend$appContactFreqForPhoneCall28Day
+ _objc_msgSend$appContactFreqForPhoneCall2Min
+ _objc_msgSend$appContactFreqForPhoneCall6Hr
+ _objc_msgSend$appContactFreqForPhoneCall7Day
+ _objc_msgSend$appContactFreqForPhoneCallHaptic
+ _objc_msgSend$appContactFreqForPhoneCallInf
+ _objc_msgSend$appContactFreqForPhoneCallUsingSiri
+ _objc_msgSend$appFreqForMessages
+ _objc_msgSend$appFreqForMessagesForCountryCode
+ _objc_msgSend$appFreqForMessagesUsingSiri
+ _objc_msgSend$appFreqForPhoneCall
+ _objc_msgSend$appFreqForPhoneCallForCountryCode
+ _objc_msgSend$appFreqForPhoneCallUsingSiri
+ _objc_msgSend$appTaskCounts
+ _objc_msgSend$appTaskType
+ _objc_msgSend$appTimeSpentInSec
+ _objc_msgSend$assetDownloadSizeInBytes
+ _objc_msgSend$assetPath
+ _objc_msgSend$assetSizeInBytes
+ _objc_msgSend$assetUnarchivedSizeInBytes
+ _objc_msgSend$assistant
+ _objc_msgSend$assistantDiagnosticAndUsageOptInDigestReported
+ _objc_msgSend$assistantDimensions
+ _objc_msgSend$assistantExperimentDigestReported
+ _objc_msgSend$autoSendMessage
+ _objc_msgSend$cancelledSiriAppTaskCount
+ _objc_msgSend$carPlay
+ _objc_msgSend$cirFallbackTriggered
+ _objc_msgSend$clearAllAssets
+ _objc_msgSend$clearDialogLines
+ _objc_msgSend$clearEndpointDelayInMs
+ _objc_msgSend$clearExperimentInfo
+ _objc_msgSend$clearInstalledVoices
+ _objc_msgSend$clearLaunchTimeInMs
+ _objc_msgSend$clearSiriResponseTimeInMs
+ _objc_msgSend$clearTimeToFirstWordInMs
+ _objc_msgSend$clearTimeToUufrInMs
+ _objc_msgSend$codePathId
+ _objc_msgSend$completedSiriAppTaskCount
+ _objc_msgSend$completedUIAppTaskCount
+ _objc_msgSend$crrCommsAppSelectionJointId
+ _objc_msgSend$deleteAccent
+ _objc_msgSend$deleteAccessibility
+ _objc_msgSend$deleteAdaptiveVolume
+ _objc_msgSend$deleteAnchorRequestId
+ _objc_msgSend$deleteAnnounce
+ _objc_msgSend$deleteAppTaskCounts
+ _objc_msgSend$deleteAssistant
+ _objc_msgSend$deleteAssistantDiagnosticAndUsageOptInDigestReported
+ _objc_msgSend$deleteAssistantDimensions
+ _objc_msgSend$deleteAssistantExperimentDigestReported
+ _objc_msgSend$deleteAutoSendMessage
+ _objc_msgSend$deleteCarPlay
+ _objc_msgSend$deleteCodePathId
+ _objc_msgSend$deleteCrrCommsAppSelectionJointId
+ _objc_msgSend$deleteDictation
+ _objc_msgSend$deleteDisplayedDialog
+ _objc_msgSend$deleteEntityMetadata
+ _objc_msgSend$deleteEnvelopeStatistics
+ _objc_msgSend$deleteExperimentContext
+ _objc_msgSend$deleteExperimentFixedDimensions
+ _objc_msgSend$deleteFailure
+ _objc_msgSend$deleteFbfFailure
+ _objc_msgSend$deleteGeneral
+ _objc_msgSend$deleteHomeKit
+ _objc_msgSend$deleteHomePodProperties
+ _objc_msgSend$deleteIOSAssistant
+ _objc_msgSend$deleteIOSDevicePropertiesReported
+ _objc_msgSend$deleteInputLocale
+ _objc_msgSend$deleteMacOSAssistant
+ _objc_msgSend$deleteMacOSDevicePropertiesReported
+ _objc_msgSend$deleteMultiUserSetupStatus
+ _objc_msgSend$deleteNetworkConnectionId
+ _objc_msgSend$deleteNetworkInterface
+ _objc_msgSend$deleteOdbatchDataReported
+ _objc_msgSend$deleteOdbatchId
+ _objc_msgSend$deleteOptIn
+ _objc_msgSend$deleteOriginalClockId
+ _objc_msgSend$deleteRepackagingExecution
+ _objc_msgSend$deleteRfGradingDialogReportedTier1
+ _objc_msgSend$deleteSandboxError
+ _objc_msgSend$deleteSelectedUser
+ _objc_msgSend$deleteSessionCounts
+ _objc_msgSend$deleteSiriInCall
+ _objc_msgSend$deleteSpokenDialog
+ _objc_msgSend$deleteSystemLocale
+ _objc_msgSend$deleteTuples
+ _objc_msgSend$deleteTvOSAssistant
+ _objc_msgSend$deleteTvOSDevicePropertiesReported
+ _objc_msgSend$deleteVisionOSDevicePropertiesReported
+ _objc_msgSend$deleteVoice
+ _objc_msgSend$deleteWatchOSAssistant
+ _objc_msgSend$deleteWatchOSDevicePropertiesReported
+ _objc_msgSend$dialogLines
+ _objc_msgSend$dictation
+ _objc_msgSend$digestType
+ _objc_msgSend$displayedDialog
+ _objc_msgSend$endpointDelayInMs
+ _objc_msgSend$entityMetadata
+ _objc_msgSend$entityRank
+ _objc_msgSend$entitySearchBundleScoreRemote
+ _objc_msgSend$envelopeStatistics
+ _objc_msgSend$errorNumber
+ _objc_msgSend$experimentAllocationStatus
+ _objc_msgSend$experimentContext
+ _objc_msgSend$experimentFixedDimensions
+ _objc_msgSend$experimentInfos
+ _objc_msgSend$failedSiriAppTaskCount
+ _objc_msgSend$failure
+ _objc_msgSend$fbfFailure
+ _objc_msgSend$flErrorCode
+ _objc_msgSend$gender
+ _objc_msgSend$general
+ _objc_msgSend$heySiriHangupEnablementState
+ _objc_msgSend$homeKit
+ _objc_msgSend$homePodProperties
+ _objc_msgSend$iOSAssistant
+ _objc_msgSend$iOSDevicePropertiesReported
+ _objc_msgSend$inputLocale
+ _objc_msgSend$installedVoices
+ _objc_msgSend$isAllowSiriWhenLockedEnabled
+ _objc_msgSend$isAnnounceCallsEnabled
+ _objc_msgSend$isAnnounceNotificationsEnabled
+ _objc_msgSend$isApprovedForGrading
+ _objc_msgSend$isAssistantEnabled
+ _objc_msgSend$isAutomaticallySendMessagesEnabled
+ _objc_msgSend$isEnrollmentReprompted
+ _objc_msgSend$isExternalMicrophoneHSEnabled
+ _objc_msgSend$isFirstTriggerOrAfterFirstTrigger
+ _objc_msgSend$isPersonalDomainRequestsEnabled
+ _objc_msgSend$isPersonalDomainsEnabled
+ _objc_msgSend$isPressSideButtonForSiriEnabled
+ _objc_msgSend$isProximityCardSeen
+ _objc_msgSend$isRaiseToSpeakEnabled
+ _objc_msgSend$isReplyWithoutConfirmationEnabled
+ _objc_msgSend$isSpokenNotificationsControlCenterModuleEnabled
+ _objc_msgSend$isTriggered
+ _objc_msgSend$isTypeToSiriEnabled
+ _objc_msgSend$launchTimeInMs
+ _objc_msgSend$listenFor
+ _objc_msgSend$macOSAssistant
+ _objc_msgSend$macOSDevicePropertiesReported
+ _objc_msgSend$messageCount
+ _objc_msgSend$multiUserSetupStatus
+ _objc_msgSend$networkConnectionId
+ _objc_msgSend$networkInterface
+ _objc_msgSend$numIngestedNeuralContextualBiasingEmbeddings
+ _objc_msgSend$numSiriShortcutsEnabled
+ _objc_msgSend$odbatchDataReported
+ _objc_msgSend$odbatchId
+ _objc_msgSend$optIn
+ _objc_msgSend$originalClockId
+ _objc_msgSend$repackagingExecution
+ _objc_msgSend$responseCategory
+ _objc_msgSend$rfGradingDialogReportedTier1
+ _objc_msgSend$samplingResult
+ _objc_msgSend$sandboxError
+ _objc_msgSend$selectedUser
+ _objc_msgSend$serverSearchResultsMediaType
+ _objc_msgSend$sessionCounts
+ _objc_msgSend$setAccent:
+ _objc_msgSend$setAccessibility:
+ _objc_msgSend$setAdaptiveVolume:
+ _objc_msgSend$setAllAssets:
+ _objc_msgSend$setAnchorRequestId:
+ _objc_msgSend$setAnchorSocialScore:
+ _objc_msgSend$setAnnounce:
+ _objc_msgSend$setAppContactFreqForMessages10Min:
+ _objc_msgSend$setAppContactFreqForMessages1Day:
+ _objc_msgSend$setAppContactFreqForMessages1Hr:
+ _objc_msgSend$setAppContactFreqForMessages28Day:
+ _objc_msgSend$setAppContactFreqForMessages2Min:
+ _objc_msgSend$setAppContactFreqForMessages6Hr:
+ _objc_msgSend$setAppContactFreqForMessages7Day:
+ _objc_msgSend$setAppContactFreqForMessages:
+ _objc_msgSend$setAppContactFreqForMessagesHaptic:
+ _objc_msgSend$setAppContactFreqForMessagesInf:
+ _objc_msgSend$setAppContactFreqForMessagesUsingSiri:
+ _objc_msgSend$setAppContactFreqForPhoneCall10Min:
+ _objc_msgSend$setAppContactFreqForPhoneCall1Day:
+ _objc_msgSend$setAppContactFreqForPhoneCall1Hr:
+ _objc_msgSend$setAppContactFreqForPhoneCall28Day:
+ _objc_msgSend$setAppContactFreqForPhoneCall2Min:
+ _objc_msgSend$setAppContactFreqForPhoneCall6Hr:
+ _objc_msgSend$setAppContactFreqForPhoneCall7Day:
+ _objc_msgSend$setAppContactFreqForPhoneCall:
+ _objc_msgSend$setAppContactFreqForPhoneCallHaptic:
+ _objc_msgSend$setAppContactFreqForPhoneCallInf:
+ _objc_msgSend$setAppContactFreqForPhoneCallUsingSiri:
+ _objc_msgSend$setAppFreqForMessages:
+ _objc_msgSend$setAppFreqForMessagesForCountryCode:
+ _objc_msgSend$setAppFreqForMessagesUsingSiri:
+ _objc_msgSend$setAppFreqForPhoneCall:
+ _objc_msgSend$setAppFreqForPhoneCallForCountryCode:
+ _objc_msgSend$setAppFreqForPhoneCallUsingSiri:
+ _objc_msgSend$setAppTaskCounts:
+ _objc_msgSend$setAppTaskType:
+ _objc_msgSend$setAppTimeSpentInSec:
+ _objc_msgSend$setAssetDownloadSizeInBytes:
+ _objc_msgSend$setAssetPath:
+ _objc_msgSend$setAssetSizeInBytes:
+ _objc_msgSend$setAssetUnarchivedSizeInBytes:
+ _objc_msgSend$setAssistant:
+ _objc_msgSend$setAssistantDiagnosticAndUsageOptInDigestReported:
+ _objc_msgSend$setAssistantDimensions:
+ _objc_msgSend$setAssistantExperimentDigestReported:
+ _objc_msgSend$setAutoSendMessage:
+ _objc_msgSend$setCancelledSiriAppTaskCount:
+ _objc_msgSend$setCarPlay:
+ _objc_msgSend$setCirFallbackTriggered:
+ _objc_msgSend$setCodePathId:
+ _objc_msgSend$setCompletedSiriAppTaskCount:
+ _objc_msgSend$setCompletedUIAppTaskCount:
+ _objc_msgSend$setCrrCommsAppSelectionJointId:
+ _objc_msgSend$setDialogLines:
+ _objc_msgSend$setDictation:
+ _objc_msgSend$setDigestType:
+ _objc_msgSend$setDisplayedDialog:
+ _objc_msgSend$setEntityMetadata:
+ _objc_msgSend$setEntityRank:
+ _objc_msgSend$setEntitySearchBundleScoreRemote:
+ _objc_msgSend$setEnvelopeStatistics:
+ _objc_msgSend$setErrorNumber:
+ _objc_msgSend$setExperimentAllocationStatus:
+ _objc_msgSend$setExperimentContext:
+ _objc_msgSend$setExperimentFixedDimensions:
+ _objc_msgSend$setExperimentInfos:
+ _objc_msgSend$setFailedSiriAppTaskCount:
+ _objc_msgSend$setFailure:
+ _objc_msgSend$setFbfFailure:
+ _objc_msgSend$setFlErrorCode:
+ _objc_msgSend$setGender:
+ _objc_msgSend$setGeneral:
+ _objc_msgSend$setHeySiriHangupEnablementState:
+ _objc_msgSend$setHomeKit:
+ _objc_msgSend$setHomePodProperties:
+ _objc_msgSend$setIOSAssistant:
+ _objc_msgSend$setIOSDevicePropertiesReported:
+ _objc_msgSend$setInputLocale:
+ _objc_msgSend$setIsAllowSiriWhenLockedEnabled:
+ _objc_msgSend$setIsAnnounceCallsEnabled:
+ _objc_msgSend$setIsAnnounceNotificationsEnabled:
+ _objc_msgSend$setIsApprovedForGrading:
+ _objc_msgSend$setIsAssistantEnabled:
+ _objc_msgSend$setIsAutomaticallySendMessagesEnabled:
+ _objc_msgSend$setIsEnrollmentReprompted:
+ _objc_msgSend$setIsExternalMicrophoneHSEnabled:
+ _objc_msgSend$setIsFirstTriggerOrAfterFirstTrigger:
+ _objc_msgSend$setIsPersonalDomainRequestsEnabled:
+ _objc_msgSend$setIsPersonalDomainsEnabled:
+ _objc_msgSend$setIsPressSideButtonForSiriEnabled:
+ _objc_msgSend$setIsProximityCardSeen:
+ _objc_msgSend$setIsRaiseToSpeakEnabled:
+ _objc_msgSend$setIsReplyWithoutConfirmationEnabled:
+ _objc_msgSend$setIsSpokenNotificationsControlCenterModuleEnabled:
+ _objc_msgSend$setIsTriggered:
+ _objc_msgSend$setIsTypeToSiriEnabled:
+ _objc_msgSend$setListenFor:
+ _objc_msgSend$setMacOSAssistant:
+ _objc_msgSend$setMacOSDevicePropertiesReported:
+ _objc_msgSend$setMessageCount:
+ _objc_msgSend$setMultiUserSetupStatus:
+ _objc_msgSend$setNetworkConnectionId:
+ _objc_msgSend$setNetworkInterface:
+ _objc_msgSend$setNumIngestedNeuralContextualBiasingEmbeddings:
+ _objc_msgSend$setNumSiriShortcutsEnabled:
+ _objc_msgSend$setOdbatchDataReported:
+ _objc_msgSend$setOdbatchId:
+ _objc_msgSend$setOptIn:
+ _objc_msgSend$setOriginalClockId:
+ _objc_msgSend$setRepackagingExecution:
+ _objc_msgSend$setResponseCategory:
+ _objc_msgSend$setRfGradingDialogReportedTier1:
+ _objc_msgSend$setSamplingResult:
+ _objc_msgSend$setSandboxError:
+ _objc_msgSend$setSelectedUser:
+ _objc_msgSend$setServerSearchResultsMediaType:
+ _objc_msgSend$setSessionCounts:
+ _objc_msgSend$setSiriInCall:
+ _objc_msgSend$setSpokenDialog:
+ _objc_msgSend$setSuccess:
+ _objc_msgSend$setTimeSinceAppContactLastLaunchedInSec:
+ _objc_msgSend$setTotalBytes:
+ _objc_msgSend$setTuples:
+ _objc_msgSend$setTvOSAssistant:
+ _objc_msgSend$setTvOSDevicePropertiesReported:
+ _objc_msgSend$setUTCOffset:
+ _objc_msgSend$setUsageScoreBooksRemote:
+ _objc_msgSend$setUsageScoreMusicRemote:
+ _objc_msgSend$setUsageScoreMusicWithoutRadioRemote:
+ _objc_msgSend$setUsageScorePodcastsRemote:
+ _objc_msgSend$setUsageScoreRadioRemote:
+ _objc_msgSend$setUsdxSessionCount:
+ _objc_msgSend$setVisionOSDevicePropertiesReported:
+ _objc_msgSend$setVoice:
+ _objc_msgSend$setWatchOSAssistant:
+ _objc_msgSend$setWatchOSDevicePropertiesReported:
+ _objc_msgSend$siriInCall
+ _objc_msgSend$siriResponseTimeInMs
+ _objc_msgSend$spokenDialog
+ _objc_msgSend$success
+ _objc_msgSend$timeSinceAppContactLastLaunchedInSec
+ _objc_msgSend$timeToFirstWordInMs
+ _objc_msgSend$timeToUufrInMs
+ _objc_msgSend$totalBytes
+ _objc_msgSend$tuples
+ _objc_msgSend$tvOSAssistant
+ _objc_msgSend$tvOSDevicePropertiesReported
+ _objc_msgSend$usageScoreBooksRemote
+ _objc_msgSend$usageScoreMusicRemote
+ _objc_msgSend$usageScoreMusicWithoutRadioRemote
+ _objc_msgSend$usageScorePodcastsRemote
+ _objc_msgSend$usageScoreRadioRemote
+ _objc_msgSend$usdxSessionCount
+ _objc_msgSend$visionOSDevicePropertiesReported
+ _objc_msgSend$voice
+ _objc_msgSend$watchOSAssistant
+ _objc_msgSend$watchOSDevicePropertiesReported
+ _objc_msgSend$whichKind
+ _objc_msgSend$whichSuccessorfail
+ _objc_retain_x9
+ _qname_DIMSchemaDIMClientEvent_WhichEvent_Type_experimentContext
+ _qname_ODBATCHSiriSchemaODBATCHClientEvent_WhichEvent_Type_None
+ _qname_ODBATCHSiriSchemaODBATCHClientEvent_WhichEvent_Type_odbatchDataReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assistantDiagnosticAndUsageOptInDigestReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assistantExperimentDigestReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_iOSDevicePropertiesReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_macOSDevicePropertiesReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_tvOSDevicePropertiesReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_visionOSDevicePropertiesReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_watchOSDevicePropertiesReported
+ _qname_PFAPFAClientEvent_WhichEvent_Type_None
+ _qname_PFAPFAClientEvent_WhichEvent_Type_repackagingExecution
+ _qname_RFSchemaRFClientEvent_WhichEvent_Type_rfGradingDialogReportedTier1
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_initStaticObject
+ _swift_release_n
+ _swift_unexpectedError
+ _symbolic So16SISchemaAnyEventCSg6mapped______12messageCountt s6UInt32V
+ _symbolic _____ 19SiriInstrumentation14EnvelopeResultO
+ _symbolic _____ So013ODDSiriSchemaA21InCallEnablementStateV
+ _symbolic _____ So17SISchemaUTCOffsetV
+ _symbolic _____ So17SISchemaVoiceNameV
+ _symbolic _____ So24SISchemaResponseCategoryV
+ _symbolic _____ So25ODDSiriSchemaODDListenForV
+ _symbolic _____ So27ODDSiriSchemaODDAppTaskTypeV
+ _symbolic _____ So31ODDSiriSchemaODDTaskAppBundleIdV
+ _symbolic _____ So36ODDSiriSchemaODDExperimentDigestTypeV
+ _symbolic _____ So37PFARepackagingExecutionSamplingResultV
+ _symbolic _____ So40ODDSiriSchemaODDAdaptiveVolumeUserIntentV
+ _symbolic _____ So43ODDSiriSchemaODDAudibleVoiceFeedbackSettingV
+ _symbolic _____ So44ODDSiriSchemaODDHeySiriHangupEnablementStateV
+ _symbolic _____ So50ODDSiriSchemaODDAnnounceNotificationsCarPlayStatusV
+ _symbolic ___________t 10Foundation4UUIDV 19SiriInstrumentation14EnvelopeResultO
+ _symbolic ___________tSg 10Foundation4UUIDV 19SiriInstrumentation14EnvelopeResultO
+ _symbolic ______p s5ErrorP
+ _symbolic _____y__________G s17_NativeDictionaryV 10Foundation4UUIDV 19SiriInstrumentation14EnvelopeResultO
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 19SiriInstrumentation14EnvelopeResultO
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 10Foundation4UUIDV 19SiriInstrumentation14EnvelopeResultO
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _swift_bridgeObjectRetain_n
CStrings:
+ "\x01\x11\x12"
+ "\x03!"
+ "\x03(\x12\x11!$"
+ "\x05\x12\x11\x11"
+ "\x11#"
+ "\x17"
+ "@\"ASRSchemaASREntityMetadata\""
+ "@\"DIMSchemaDIMExperimentContext\""
+ "@\"NETSchemaNETNetworkInterface\""
+ "@\"ODBATCHSiriSchemaODBATCHClientEventMetadata\""
+ "@\"ODBATCHSiriSchemaODBATCHDataReported\""
+ "@\"ODDSiriSchemaODDAdaptiveVolumeProperties\""
+ "@\"ODDSiriSchemaODDAnnounceProperties\""
+ "@\"ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported\""
+ "@\"ODDSiriSchemaODDAssistantExperimentCounts\""
+ "@\"ODDSiriSchemaODDAssistantExperimentDigestsReported\""
+ "@\"ODDSiriSchemaODDAssistantExperimentDimensions\""
+ "@\"ODDSiriSchemaODDAssistantExperimentTuples\""
+ "@\"ODDSiriSchemaODDAssistantProperties\""
+ "@\"ODDSiriSchemaODDAutoSendMessageProperties\""
+ "@\"ODDSiriSchemaODDCarPlayProperties\""
+ "@\"ODDSiriSchemaODDDeviceAndUsageAppTaskCounts\""
+ "@\"ODDSiriSchemaODDDeviceAndUsageDynamicDimensions\""
+ "@\"ODDSiriSchemaODDDictationProperties\""
+ "@\"ODDSiriSchemaODDExperimentFixedDimensions\""
+ "@\"ODDSiriSchemaODDGeneralProperties\""
+ "@\"ODDSiriSchemaODDHomeKitProperties\""
+ "@\"ODDSiriSchemaODDHomePodProperties\""
+ "@\"ODDSiriSchemaODDMultiUserSetupStatus\""
+ "@\"ODDSiriSchemaODDMultiUserState\""
+ "@\"ODDSiriSchemaODDOptInProperties\""
+ "@\"ODDSiriSchemaODDSessionCounts\""
+ "@\"ODDSiriSchemaODDSiriInCallProperties\""
+ "@\"ODDSiriSchemaODDVoiceProperties\""
+ "@\"ODDSiriSchemaODDiOSAccessibilityProperties\""
+ "@\"ODDSiriSchemaODDiOSAssistantProperties\""
+ "@\"ODDSiriSchemaODDiOSDevicePropertiesReported\""
+ "@\"ODDSiriSchemaODDiOSResponseProperties\""
+ "@\"ODDSiriSchemaODDmacOSAssistantProperties\""
+ "@\"ODDSiriSchemaODDmacOSDevicePropertiesReported\""
+ "@\"ODDSiriSchemaODDtvOSAssistantProperties\""
+ "@\"ODDSiriSchemaODDtvOSDevicePropertiesReported\""
+ "@\"ODDSiriSchemaODDvisionOSDevicePropertiesReported\""
+ "@\"ODDSiriSchemaODDwatchOSAssistantProperties\""
+ "@\"ODDSiriSchemaODDwatchOSDevicePropertiesReported\""
+ "@\"ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap\""
+ "@\"ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext\""
+ "@\"PFAClockEnvelopeStatistics\""
+ "@\"PFARepackagingExecution\""
+ "@\"PFARepackagingExecutionFBFFailure\""
+ "@\"PFARepackagingExecutionFailure\""
+ "@\"PFARepackagingExecutionResult\""
+ "@\"PFARepackagingExecutionSandboxError\""
+ "@\"RFSchemaRFGradingDialogReportedTier1\""
+ "ASRSchemaASREntityMetadata"
+ "COMPONENTINVOCATIONSOURCE_REMINDERS"
+ "DIMSchemaDIMExperimentContext"
+ "DIMSchemaDIMExperimentInfo"
+ "DISMISSALREASON_UNDIRECTED_SPEECH_DURING_ATTENDING"
+ "Division by zero"
+ "Division results in an overflow"
+ "Duplicate values for key: '"
+ "Fatal error"
+ "INFERENCEFORCEPROMPTTYPE_COMMS_HAS_FORCE_PROMPTED"
+ "Insufficient space allocated to copy string contents"
+ "MTINVOCATIONTYPE_DEVELOPER_API"
+ "NETPROVIDER_SN_NETWORK_CONNECTION"
+ "NETPROVIDER_SN_RPC_CONNECTION"
+ "Negative value is not representable"
+ "NotSampled"
+ "ODBATCHSiriSchemaODBATCHClientEvent"
+ "ODBATCHSiriSchemaODBATCHClientEventMetadata"
+ "ODBATCHSiriSchemaODBATCHDataReported"
+ "ODBATCH_CLIENT_EVENT"
+ "ODDADAPTIVEVOLUMEUSERINTENT_DECREASE"
+ "ODDADAPTIVEVOLUMEUSERINTENT_DEFAULT"
+ "ODDADAPTIVEVOLUMEUSERINTENT_INCREASE"
+ "ODDADAPTIVEVOLUMEUSERINTENT_SET"
+ "ODDADAPTIVEVOLUMEUSERINTENT_UNKNOWN"
+ "ODDANNOUNCENOTIFICATIONSCARPLAYSTATUS_ANNOUNCE_NEW_MESSAGES"
+ "ODDANNOUNCENOTIFICATIONSCARPLAYSTATUS_DISABLED"
+ "ODDANNOUNCENOTIFICATIONSCARPLAYSTATUS_MUTE_ANNOUNCEMENTS"
+ "ODDANNOUNCENOTIFICATIONSCARPLAYSTATUS_REMEMBER_PREVIOUS_SETTINGS"
+ "ODDANNOUNCENOTIFICATIONSCARPLAYSTATUS_UNKNOWN"
+ "ODDAPPTASKTYPE_NOT_APPLICABLE"
+ "ODDAPPTASKTYPE_SEND_SMS"
+ "ODDAPPTASKTYPE_SET_REMINDER"
+ "ODDAPPTASKTYPE_START_CALL"
+ "ODDAPPTASKTYPE_UNKNOWN"
+ "ODDEXPERIMENTDIGESTTYPE_COMPLETE"
+ "ODDEXPERIMENTDIGESTTYPE_DAILY"
+ "ODDEXPERIMENTDIGESTTYPE_POST"
+ "ODDEXPERIMENTDIGESTTYPE_PRE"
+ "ODDEXPERIMENTDIGESTTYPE_UNKNOWN"
+ "ODDHEYSIRIHANGUPENABLEMENTSTATE_DEFAULT_OFF"
+ "ODDHEYSIRIHANGUPENABLEMENTSTATE_ENABLED"
+ "ODDHEYSIRIHANGUPENABLEMENTSTATE_SWITCHED_OFF"
+ "ODDHEYSIRIHANGUPENABLEMENTSTATE_UNKNOWN"
+ "ODDLISTENFOR_HEY_SIRI"
+ "ODDLISTENFOR_OFF"
+ "ODDLISTENFOR_SIRI_OR_HEY_SIRI"
+ "ODDLISTENFOR_UNKNOWN"
+ "ODDSIRIINCALLENABLEMENTSTATE_DEFAULT_DISABLED"
+ "ODDSIRIINCALLENABLEMENTSTATE_UNKNOWN"
+ "ODDSIRIINCALLENABLEMENTSTATE_USER_DISABLED"
+ "ODDSIRIINCALLENABLEMENTSTATE_USER_ENABLED"
+ "ODDSiriSchemaODDAdaptiveVolumeProperties"
+ "ODDSiriSchemaODDAnnounceProperties"
+ "ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigest"
+ "ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported"
+ "ODDSiriSchemaODDAssistantExperimentCounts"
+ "ODDSiriSchemaODDAssistantExperimentDigest"
+ "ODDSiriSchemaODDAssistantExperimentDigestsReported"
+ "ODDSiriSchemaODDAssistantExperimentDimensions"
+ "ODDSiriSchemaODDAssistantExperimentTuples"
+ "ODDSiriSchemaODDAssistantProperties"
+ "ODDSiriSchemaODDAutoSendMessageProperties"
+ "ODDSiriSchemaODDCarPlayProperties"
+ "ODDSiriSchemaODDDeviceAndUsageAppTaskCounts"
+ "ODDSiriSchemaODDDeviceAndUsageDynamicDimensions"
+ "ODDSiriSchemaODDDictationProperties"
+ "ODDSiriSchemaODDExperimentFixedDimensions"
+ "ODDSiriSchemaODDGeneralProperties"
+ "ODDSiriSchemaODDHomeKitProperties"
+ "ODDSiriSchemaODDHomePodProperties"
+ "ODDSiriSchemaODDMultiUserSetupStatus"
+ "ODDSiriSchemaODDMultiUserState"
+ "ODDSiriSchemaODDOptInProperties"
+ "ODDSiriSchemaODDSessionCounts"
+ "ODDSiriSchemaODDSiriInCallProperties"
+ "ODDSiriSchemaODDUserPersonalization"
+ "ODDSiriSchemaODDVoiceProperties"
+ "ODDSiriSchemaODDiOSAccessibilityProperties"
+ "ODDSiriSchemaODDiOSAssistantProperties"
+ "ODDSiriSchemaODDiOSDevicePropertiesReported"
+ "ODDSiriSchemaODDiOSResponseProperties"
+ "ODDSiriSchemaODDmacOSAssistantProperties"
+ "ODDSiriSchemaODDmacOSDevicePropertiesReported"
+ "ODDSiriSchemaODDtvOSAssistantProperties"
+ "ODDSiriSchemaODDtvOSDevicePropertiesReported"
+ "ODDSiriSchemaODDvisionOSDevicePropertiesReported"
+ "ODDSiriSchemaODDwatchOSAssistantProperties"
+ "ODDSiriSchemaODDwatchOSDevicePropertiesReported"
+ "ODDTASKAPPBUNDLEID_COM_APPLE_INCALLSERVICE"
+ "ODDTASKAPPBUNDLEID_COM_APPLE_MOBILESMS"
+ "ODDTASKAPPBUNDLEID_COM_APPLE_REMINDERS"
+ "ODDTASKAPPBUNDLEID_UNKNOWN"
+ "ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap"
+ "ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext"
+ "PFAClockEnvelopeStatistics"
+ "PFAPFAClientEvent"
+ "PFARepackagingExecution"
+ "PFARepackagingExecutionFBFFailure"
+ "PFARepackagingExecutionFailure"
+ "PFARepackagingExecutionResult"
+ "PFARepackagingExecutionSandboxError"
+ "PFA_CLIENT_EVENT"
+ "PSECALLDISCONNECTEDREASON_APPLICATION_NOT_FOREGROUNDED"
+ "PSECALLDISCONNECTEDREASON_AVCONFERENCED_CRASHED"
+ "PSECALLDISCONNECTEDREASON_CALL_AGAIN"
+ "PSECALLDISCONNECTEDREASON_CALL_FAILED_NIL_CALL_PROVIDER"
+ "PSECALLDISCONNECTEDREASON_CALL_SCREENING_TIMEOUT"
+ "PSECALLDISCONNECTEDREASON_CONVERSATION_LINKS_DISABLED"
+ "PSECALLDISCONNECTEDREASON_DECLINED_WITH_TEXT"
+ "PSECALLDISCONNECTEDREASON_DECRYPTION_TIMEOUT"
+ "PSECALLDISCONNECTEDREASON_FILTERED_OUT"
+ "PSECALLDISCONNECTEDREASON_HANDED_OFF"
+ "PSECALLDISCONNECTEDREASON_IDS_QUERY_RATE_LIMITED"
+ "PSECALLDISCONNECTEDREASON_INVALID_CONVERSATION_LINK"
+ "PSECALLDISCONNECTEDREASON_KICKED"
+ "PSECALLDISCONNECTEDREASON_LET_ME_IN_REQUEST_REJECTED"
+ "PSECALLDISCONNECTEDREASON_MANAGED_DEVICE_POLICY_RESTRICTED"
+ "PSECALLDISCONNECTEDREASON_MEDIA_SERVER_CRASHED"
+ "PSECALLDISCONNECTEDREASON_MEDIA_START_FAILED"
+ "PSECALLDISCONNECTEDREASON_MMI_OR_USSD_LIKELY"
+ "PSECALLDISCONNECTEDREASON_NO_DESTINATIONS_AVAILABLE"
+ "PSECALLDISCONNECTEDREASON_PROVIDER_CRASHED"
+ "PSECALLDISCONNECTEDREASON_UNKNOWN_PARTICIPANT_ADDED"
+ "RESPONSECATEGORY_APPLE"
+ "RESPONSECATEGORY_CANT_DO"
+ "RESPONSECATEGORY_CANT_UNDERSTAND"
+ "RESPONSECATEGORY_CONFIRM"
+ "RESPONSECATEGORY_DISAMBIGUATE"
+ "RESPONSECATEGORY_FATAL"
+ "RESPONSECATEGORY_HANDLED"
+ "RESPONSECATEGORY_INTERSTITIAL"
+ "RESPONSECATEGORY_PROMPT"
+ "RESPONSECATEGORY_SIRI_INITIATED"
+ "RESPONSECATEGORY_SOCIAL"
+ "RESPONSECATEGORY_SYSTEM_ERROR"
+ "RESPONSECATEGORY_UNKNOWN"
+ "RESPONSECATEGORY_USER_DECLINED"
+ "RFSchemaRFGradingDialogLineTier1"
+ "RFSchemaRFGradingDialogReportedTier1"
+ "SUGSUPPRESSIONREASON_EXPERIMENT_DONOTSHOW"
+ "Sampled"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Dictionary.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/NativeDictionary.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"ASRSchemaASREntityMetadata\",&,N,V_entityMetadata"
+ "T@\"DIMSchemaDIMExperimentContext\",&,N,V_experimentContext"
+ "T@\"NETSchemaNETNetworkInterface\",&,N,V_networkInterface"
+ "T@\"NSArray\",C,N,V_allAssets"
+ "T@\"NSArray\",C,N,V_dialogLines"
+ "T@\"NSArray\",C,N,V_endpointDelayInMs"
+ "T@\"NSArray\",C,N,V_experimentInfos"
+ "T@\"NSArray\",C,N,V_installedVoices"
+ "T@\"NSArray\",C,N,V_launchTimeInMs"
+ "T@\"NSArray\",C,N,V_siriResponseTimeInMs"
+ "T@\"NSArray\",C,N,V_timeToFirstWordInMs"
+ "T@\"NSArray\",C,N,V_timeToUufrInMs"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_assetPath"
+ "T@\"NSString\",C,N,V_displayedDialog"
+ "T@\"NSString\",C,N,V_spokenDialog"
+ "T@\"ODBATCHSiriSchemaODBATCHClientEventMetadata\",&,N,V_eventMetadata"
+ "T@\"ODBATCHSiriSchemaODBATCHDataReported\",&,N,V_odbatchDataReported"
+ "T@\"ODDSiriSchemaODDAdaptiveVolumeProperties\",&,N,V_adaptiveVolume"
+ "T@\"ODDSiriSchemaODDAnnounceProperties\",&,N,V_announce"
+ "T@\"ODDSiriSchemaODDAssistantDiagnosticAndUsageOptInDigestsReported\",&,N,V_assistantDiagnosticAndUsageOptInDigestReported"
+ "T@\"ODDSiriSchemaODDAssistantDimensions\",&,N,V_assistantDimensions"
+ "T@\"ODDSiriSchemaODDAssistantExperimentCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDAssistantExperimentDigestsReported\",&,N,V_assistantExperimentDigestReported"
+ "T@\"ODDSiriSchemaODDAssistantExperimentDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDAssistantExperimentTuples\",&,N,V_tuples"
+ "T@\"ODDSiriSchemaODDAssistantProperties\",&,N,V_assistant"
+ "T@\"ODDSiriSchemaODDAutoSendMessageProperties\",&,N,V_autoSendMessage"
+ "T@\"ODDSiriSchemaODDCarPlayProperties\",&,N,V_carPlay"
+ "T@\"ODDSiriSchemaODDDeviceAndUsageAppTaskCounts\",&,N,V_appTaskCounts"
+ "T@\"ODDSiriSchemaODDDeviceAndUsageDynamicDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDDictationProperties\",&,N,V_dictation"
+ "T@\"ODDSiriSchemaODDExperimentFixedDimensions\",&,N,V_experimentFixedDimensions"
+ "T@\"ODDSiriSchemaODDGeneralProperties\",&,N,V_general"
+ "T@\"ODDSiriSchemaODDHomeKitProperties\",&,N,V_homeKit"
+ "T@\"ODDSiriSchemaODDHomePodProperties\",&,N,V_homePodProperties"
+ "T@\"ODDSiriSchemaODDMultiUserSetupStatus\",&,N,V_multiUserSetupStatus"
+ "T@\"ODDSiriSchemaODDMultiUserState\",&,N,V_multiUserState"
+ "T@\"ODDSiriSchemaODDOptInProperties\",&,N,V_optIn"
+ "T@\"ODDSiriSchemaODDSessionCounts\",&,N,V_sessionCounts"
+ "T@\"ODDSiriSchemaODDSiriInCallProperties\",&,N,V_siriInCall"
+ "T@\"ODDSiriSchemaODDVoiceProperties\",&,N,V_voice"
+ "T@\"ODDSiriSchemaODDiOSAccessibilityProperties\",&,N,V_accessibility"
+ "T@\"ODDSiriSchemaODDiOSAssistantProperties\",&,N,V_iOSAssistant"
+ "T@\"ODDSiriSchemaODDiOSDevicePropertiesReported\",&,N,V_iOSDevicePropertiesReported"
+ "T@\"ODDSiriSchemaODDiOSResponseProperties\",&,N,V_response"
+ "T@\"ODDSiriSchemaODDmacOSAssistantProperties\",&,N,V_macOSAssistant"
+ "T@\"ODDSiriSchemaODDmacOSDevicePropertiesReported\",&,N,V_macOSDevicePropertiesReported"
+ "T@\"ODDSiriSchemaODDtvOSAssistantProperties\",&,N,V_tvOSAssistant"
+ "T@\"ODDSiriSchemaODDtvOSDevicePropertiesReported\",&,N,V_tvOSDevicePropertiesReported"
+ "T@\"ODDSiriSchemaODDvisionOSDevicePropertiesReported\",&,N,V_visionOSDevicePropertiesReported"
+ "T@\"ODDSiriSchemaODDwatchOSAssistantProperties\",&,N,V_watchOSAssistant"
+ "T@\"ODDSiriSchemaODDwatchOSDevicePropertiesReported\",&,N,V_watchOSDevicePropertiesReported"
+ "T@\"ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMap\",&,N,V_selectedUser"
+ "T@\"ORCHSchemaORCHMUXEphemeralToAggregationIdentifierMapContext\",&,N,V_ephemeralToAggregationIdentifierMap"
+ "T@\"PFAClockEnvelopeStatistics\",&,N,V_envelopeStatistics"
+ "T@\"PFARepackagingExecution\",&,N,V_repackagingExecution"
+ "T@\"PFARepackagingExecutionFBFFailure\",&,N,V_fbfFailure"
+ "T@\"PFARepackagingExecutionFailure\",&,N,V_failure"
+ "T@\"PFARepackagingExecutionResult\",&,N,V_result"
+ "T@\"PFARepackagingExecutionSandboxError\",&,N,V_sandboxError"
+ "T@\"RFSchemaRFGradingDialogReportedTier1\",&,N,V_rfGradingDialogReportedTier1"
+ "T@\"SISchemaISOLocale\",&,N,V_accent"
+ "T@\"SISchemaISOLocale\",&,N,V_inputLocale"
+ "T@\"SISchemaISOLocale\",&,N,V_systemLocale"
+ "T@\"SISchemaUUID\",&,N,V_anchorRequestId"
+ "T@\"SISchemaUUID\",&,N,V_codePathId"
+ "T@\"SISchemaUUID\",&,N,V_crrCommsAppSelectionJointId"
+ "T@\"SISchemaUUID\",&,N,V_networkConnectionId"
+ "T@\"SISchemaUUID\",&,N,V_odbatchId"
+ "T@\"SISchemaUUID\",&,N,V_originalClockId"
+ "TB,N,V_cirFallbackTriggered"
+ "TB,N,V_hasAccent"
+ "TB,N,V_hasAccessibility"
+ "TB,N,V_hasAdaptiveVolume"
+ "TB,N,V_hasAnchorRequestId"
+ "TB,N,V_hasAnnounce"
+ "TB,N,V_hasAppTaskCounts"
+ "TB,N,V_hasAssetPath"
+ "TB,N,V_hasAssistant"
+ "TB,N,V_hasAssistantDiagnosticAndUsageOptInDigestReported"
+ "TB,N,V_hasAssistantDimensions"
+ "TB,N,V_hasAssistantExperimentDigestReported"
+ "TB,N,V_hasAutoSendMessage"
+ "TB,N,V_hasCarPlay"
+ "TB,N,V_hasCodePathId"
+ "TB,N,V_hasCrrCommsAppSelectionJointId"
+ "TB,N,V_hasDictation"
+ "TB,N,V_hasDisplayedDialog"
+ "TB,N,V_hasEntityMetadata"
+ "TB,N,V_hasEnvelopeStatistics"
+ "TB,N,V_hasExperimentContext"
+ "TB,N,V_hasExperimentFixedDimensions"
+ "TB,N,V_hasFailure"
+ "TB,N,V_hasFbfFailure"
+ "TB,N,V_hasGeneral"
+ "TB,N,V_hasHomeKit"
+ "TB,N,V_hasHomePodProperties"
+ "TB,N,V_hasIOSAssistant"
+ "TB,N,V_hasIOSDevicePropertiesReported"
+ "TB,N,V_hasInputLocale"
+ "TB,N,V_hasMacOSAssistant"
+ "TB,N,V_hasMacOSDevicePropertiesReported"
+ "TB,N,V_hasMultiUserSetupStatus"
+ "TB,N,V_hasNetworkConnectionId"
+ "TB,N,V_hasNetworkInterface"
+ "TB,N,V_hasOdbatchDataReported"
+ "TB,N,V_hasOdbatchId"
+ "TB,N,V_hasOptIn"
+ "TB,N,V_hasOriginalClockId"
+ "TB,N,V_hasRepackagingExecution"
+ "TB,N,V_hasRfGradingDialogReportedTier1"
+ "TB,N,V_hasSandboxError"
+ "TB,N,V_hasSelectedUser"
+ "TB,N,V_hasSessionCounts"
+ "TB,N,V_hasSiriInCall"
+ "TB,N,V_hasSpokenDialog"
+ "TB,N,V_hasSuccess"
+ "TB,N,V_hasTuples"
+ "TB,N,V_hasTvOSAssistant"
+ "TB,N,V_hasTvOSDevicePropertiesReported"
+ "TB,N,V_hasVisionOSDevicePropertiesReported"
+ "TB,N,V_hasVoice"
+ "TB,N,V_hasWatchOSAssistant"
+ "TB,N,V_hasWatchOSDevicePropertiesReported"
+ "TB,N,V_isAllowSiriWhenLockedEnabled"
+ "TB,N,V_isAnnounceCallsEnabled"
+ "TB,N,V_isAnnounceNotificationsEnabled"
+ "TB,N,V_isApprovedForGrading"
+ "TB,N,V_isAssistantEnabled"
+ "TB,N,V_isAutomaticallySendMessagesEnabled"
+ "TB,N,V_isEnrollmentReprompted"
+ "TB,N,V_isExternalMicrophoneHSEnabled"
+ "TB,N,V_isFirstTriggerOrAfterFirstTrigger"
+ "TB,N,V_isPersonalDomainRequestsEnabled"
+ "TB,N,V_isPersonalDomainsEnabled"
+ "TB,N,V_isPressSideButtonForSiriEnabled"
+ "TB,N,V_isProximityCardSeen"
+ "TB,N,V_isRaiseToSpeakEnabled"
+ "TB,N,V_isReplyWithoutConfirmationEnabled"
+ "TB,N,V_isSpokenNotificationsControlCenterModuleEnabled"
+ "TB,N,V_isTriggered"
+ "TB,N,V_isTypeToSiriEnabled"
+ "TB,N,V_success"
+ "TI,N,V_cancelledSiriAppTaskCount"
+ "TI,N,V_completedSiriAppTaskCount"
+ "TI,N,V_completedUIAppTaskCount"
+ "TI,N,V_entityRank"
+ "TI,N,V_failedSiriAppTaskCount"
+ "TI,N,V_messageCount"
+ "TI,N,V_numIngestedNeuralContextualBiasingEmbeddings"
+ "TI,N,V_usdxSessionCount"
+ "TQ,N,V_assetDownloadSizeInBytes"
+ "TQ,N,V_assetSizeInBytes"
+ "TQ,N,V_assetUnarchivedSizeInBytes"
+ "TQ,N,V_totalBytes"
+ "TQ,R,N,V_whichKind"
+ "TQ,R,N,V_whichSuccessorfail"
+ "Td,N,V_entitySearchBundleScoreRemote"
+ "Td,N,V_usageScoreBooksRemote"
+ "Td,N,V_usageScoreMusicRemote"
+ "Td,N,V_usageScoreMusicWithoutRadioRemote"
+ "Td,N,V_usageScorePodcastsRemote"
+ "Td,N,V_usageScoreRadioRemote"
+ "Tf,N,V_anchorSocialScore"
+ "Ti,N,V_UTCOffset"
+ "Ti,N,V_adaptiveVolume"
+ "Ti,N,V_appContactFreqForMessages"
+ "Ti,N,V_appContactFreqForMessages10Min"
+ "Ti,N,V_appContactFreqForMessages1Day"
+ "Ti,N,V_appContactFreqForMessages1Hr"
+ "Ti,N,V_appContactFreqForMessages28Day"
+ "Ti,N,V_appContactFreqForMessages2Min"
+ "Ti,N,V_appContactFreqForMessages6Hr"
+ "Ti,N,V_appContactFreqForMessages7Day"
+ "Ti,N,V_appContactFreqForMessagesHaptic"
+ "Ti,N,V_appContactFreqForMessagesInf"
+ "Ti,N,V_appContactFreqForMessagesUsingSiri"
+ "Ti,N,V_appContactFreqForPhoneCall"
+ "Ti,N,V_appContactFreqForPhoneCall10Min"
+ "Ti,N,V_appContactFreqForPhoneCall1Day"
+ "Ti,N,V_appContactFreqForPhoneCall1Hr"
+ "Ti,N,V_appContactFreqForPhoneCall28Day"
+ "Ti,N,V_appContactFreqForPhoneCall2Min"
+ "Ti,N,V_appContactFreqForPhoneCall6Hr"
+ "Ti,N,V_appContactFreqForPhoneCall7Day"
+ "Ti,N,V_appContactFreqForPhoneCallHaptic"
+ "Ti,N,V_appContactFreqForPhoneCallInf"
+ "Ti,N,V_appContactFreqForPhoneCallUsingSiri"
+ "Ti,N,V_appFreqForMessages"
+ "Ti,N,V_appFreqForMessagesForCountryCode"
+ "Ti,N,V_appFreqForMessagesUsingSiri"
+ "Ti,N,V_appFreqForPhoneCall"
+ "Ti,N,V_appFreqForPhoneCallForCountryCode"
+ "Ti,N,V_appFreqForPhoneCallUsingSiri"
+ "Ti,N,V_appTaskType"
+ "Ti,N,V_digestType"
+ "Ti,N,V_errorNumber"
+ "Ti,N,V_experimentAllocationStatus"
+ "Ti,N,V_flErrorCode"
+ "Ti,N,V_gender"
+ "Ti,N,V_heySiriHangupEnablementState"
+ "Ti,N,V_listenFor"
+ "Ti,N,V_numSiriShortcutsEnabled"
+ "Ti,N,V_responseCategory"
+ "Ti,N,V_samplingResult"
+ "Ti,N,V_serverSearchResultsMediaType"
+ "Ti,N,V_storefrontId"
+ "Ti,N,V_timeSinceAppContactLastLaunchedInSec"
+ "Ti,N,V_voiceName"
+ "Tq,N,V_appTimeSpentInSec"
+ "UAFSchemaUAFAssetMetadata"
+ "UTCOFFSET_00_00_Z"
+ "UTCOFFSET_MINUS_01_00_N"
+ "UTCOFFSET_MINUS_02_00_O"
+ "UTCOFFSET_MINUS_03_00_P"
+ "UTCOFFSET_MINUS_03_30_P_DAGGER"
+ "UTCOFFSET_MINUS_04_00_Q"
+ "UTCOFFSET_MINUS_05_00_R"
+ "UTCOFFSET_MINUS_06_00_S"
+ "UTCOFFSET_MINUS_07_00_T"
+ "UTCOFFSET_MINUS_08_00_U"
+ "UTCOFFSET_MINUS_09_00_V"
+ "UTCOFFSET_MINUS_09_30_V_DAGGER"
+ "UTCOFFSET_MINUS_10_00_W"
+ "UTCOFFSET_MINUS_11_00_X"
+ "UTCOFFSET_MINUS_12_00_Y"
+ "UTCOFFSET_PLUS_01_00_A"
+ "UTCOFFSET_PLUS_02_00_B"
+ "UTCOFFSET_PLUS_03_00_C"
+ "UTCOFFSET_PLUS_03_30_C_DAGGER"
+ "UTCOFFSET_PLUS_04_00_D"
+ "UTCOFFSET_PLUS_04_30_D_DAGGER"
+ "UTCOFFSET_PLUS_05_00_E"
+ "UTCOFFSET_PLUS_05_30_E_DAGGER"
+ "UTCOFFSET_PLUS_05_45_E_STAR"
+ "UTCOFFSET_PLUS_06_00_F"
+ "UTCOFFSET_PLUS_06_30_F_DAGGER"
+ "UTCOFFSET_PLUS_07_00_G"
+ "UTCOFFSET_PLUS_08_00_H"
+ "UTCOFFSET_PLUS_08_45_H_STAR"
+ "UTCOFFSET_PLUS_09_00_I"
+ "UTCOFFSET_PLUS_09_30_I_DAGGER"
+ "UTCOFFSET_PLUS_10_00_K"
+ "UTCOFFSET_PLUS_10_30_K_DAGGER"
+ "UTCOFFSET_PLUS_11_00_L"
+ "UTCOFFSET_PLUS_12_00_M"
+ "UTCOFFSET_PLUS_12_45_M_STAR"
+ "UTCOFFSET_PLUS_13_00_M_DAGGER"
+ "UTCOFFSET_PLUS_14_00_M_DAGGER"
+ "UTCOFFSET_UNKNOWN"
+ "UTCOffset"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "VOICEFEEDBACK_UNKNOWN"
+ "VOICENAME_AARON"
+ "VOICENAME_AIDAN"
+ "VOICENAME_AKASH"
+ "VOICENAME_ALEKSEI"
+ "VOICENAME_ALVA"
+ "VOICENAME_AMELIE"
+ "VOICENAME_ANGEL"
+ "VOICENAME_ARTHUR"
+ "VOICENAME_AXEL"
+ "VOICENAME_BEATRIZ"
+ "VOICENAME_CARMEN"
+ "VOICENAME_CARMIT"
+ "VOICENAME_CATHERINE"
+ "VOICENAME_CHENGHAN"
+ "VOICENAME_DAMAYANTI"
+ "VOICENAME_DAMON"
+ "VOICENAME_DANIEL"
+ "VOICENAME_DEDEC"
+ "VOICENAME_DEDED"
+ "VOICENAME_ELIF"
+ "VOICENAME_ELLEN"
+ "VOICENAME_ELSE"
+ "VOICENAME_ENGBC"
+ "VOICENAME_ENGBD"
+ "VOICENAME_FRANCESCA"
+ "VOICENAME_GORDON"
+ "VOICENAME_HATTORI"
+ "VOICENAME_HELENA"
+ "VOICENAME_HIRO"
+ "VOICENAME_HOYIN"
+ "VOICENAME_INGRID"
+ "VOICENAME_JENS"
+ "VOICENAME_JINSOO"
+ "VOICENAME_KAAN"
+ "VOICENAME_KANYA"
+ "VOICENAME_KAYAN"
+ "VOICENAME_KLAAR"
+ "VOICENAME_LEONA"
+ "VOICENAME_LIMU"
+ "VOICENAME_LINFEI"
+ "VOICENAME_LUCIANA"
+ "VOICENAME_LUISA"
+ "VOICENAME_MAEVE"
+ "VOICENAME_MAGED"
+ "VOICENAME_MARIE"
+ "VOICENAME_MARIUS"
+ "VOICENAME_MARTHA"
+ "VOICENAME_MARTIN"
+ "VOICENAME_MEIJIA"
+ "VOICENAME_MINJI"
+ "VOICENAME_MOIRA"
+ "VOICENAME_MSMYA"
+ "VOICENAME_MSMYB"
+ "VOICENAME_NANDO"
+ "VOICENAME_NICKY"
+ "VOICENAME_NORA"
+ "VOICENAME_OREN"
+ "VOICENAME_PAOLO"
+ "VOICENAME_PAULINA"
+ "VOICENAME_PIERRE"
+ "VOICENAME_PIETER"
+ "VOICENAME_QUINN"
+ "VOICENAME_RIYA"
+ "VOICENAME_SAKURA"
+ "VOICENAME_SAMER"
+ "VOICENAME_SANDRA"
+ "VOICENAME_SARA"
+ "VOICENAME_SATU"
+ "VOICENAME_SHUFEN"
+ "VOICENAME_SIMONE"
+ "VOICENAME_SINJI"
+ "VOICENAME_SOHA"
+ "VOICENAME_SOPHIE"
+ "VOICENAME_SUVI"
+ "VOICENAME_TESSA"
+ "VOICENAME_THTHA"
+ "VOICENAME_THTHB"
+ "VOICENAME_TILDE"
+ "VOICENAME_TOPI"
+ "VOICENAME_UNKNOWN"
+ "VOICENAME_VINCENT"
+ "VOICENAME_XANDER"
+ "VOICENAME_YASMIN"
+ "VOICENAME_YELDA"
+ "VOICENAME_YELENA"
+ "VOICENAME_YUNA"
+ "VOICENAME_YUSHU"
+ "VOICENAME_ZIV"
+ "_UTCOffset"
+ "_accent"
+ "_accessibility"
+ "_adaptiveVolume"
+ "_allAssets"
+ "_anchorRequestId"
+ "_anchorSocialScore"
+ "_announce"
+ "_appContactFreqForMessages"
+ "_appContactFreqForMessages10Min"
+ "_appContactFreqForMessages1Day"
+ "_appContactFreqForMessages1Hr"
+ "_appContactFreqForMessages28Day"
+ "_appContactFreqForMessages2Min"
+ "_appContactFreqForMessages6Hr"
+ "_appContactFreqForMessages7Day"
+ "_appContactFreqForMessagesHaptic"
+ "_appContactFreqForMessagesInf"
+ "_appContactFreqForMessagesUsingSiri"
+ "_appContactFreqForPhoneCall"
+ "_appContactFreqForPhoneCall10Min"
+ "_appContactFreqForPhoneCall1Day"
+ "_appContactFreqForPhoneCall1Hr"
+ "_appContactFreqForPhoneCall28Day"
+ "_appContactFreqForPhoneCall2Min"
+ "_appContactFreqForPhoneCall6Hr"
+ "_appContactFreqForPhoneCall7Day"
+ "_appContactFreqForPhoneCallHaptic"
+ "_appContactFreqForPhoneCallInf"
+ "_appContactFreqForPhoneCallUsingSiri"
+ "_appFreqForMessages"
+ "_appFreqForMessagesForCountryCode"
+ "_appFreqForMessagesUsingSiri"
+ "_appFreqForPhoneCall"
+ "_appFreqForPhoneCallForCountryCode"
+ "_appFreqForPhoneCallUsingSiri"
+ "_appTaskCounts"
+ "_appTaskType"
+ "_appTimeSpentInSec"
+ "_assetDownloadSizeInBytes"
+ "_assetPath"
+ "_assetSizeInBytes"
+ "_assetUnarchivedSizeInBytes"
+ "_assistant"
+ "_assistantDiagnosticAndUsageOptInDigestReported"
+ "_assistantDimensions"
+ "_assistantExperimentDigestReported"
+ "_autoSendMessage"
+ "_cancelledSiriAppTaskCount"
+ "_carPlay"
+ "_cirFallbackTriggered"
+ "_codePathId"
+ "_completedSiriAppTaskCount"
+ "_completedUIAppTaskCount"
+ "_crrCommsAppSelectionJointId"
+ "_dialogLines"
+ "_dictation"
+ "_digestType"
+ "_displayedDialog"
+ "_endpointDelayInMs"
+ "_entityMetadata"
+ "_entityRank"
+ "_entitySearchBundleScoreRemote"
+ "_envelopeStatistics"
+ "_errorNumber"
+ "_experimentAllocationStatus"
+ "_experimentContext"
+ "_experimentFixedDimensions"
+ "_experimentInfos"
+ "_failedSiriAppTaskCount"
+ "_failure"
+ "_fbfFailure"
+ "_flErrorCode"
+ "_gender"
+ "_general"
+ "_hasAccent"
+ "_hasAccessibility"
+ "_hasAdaptiveVolume"
+ "_hasAnchorRequestId"
+ "_hasAnnounce"
+ "_hasAppTaskCounts"
+ "_hasAssetPath"
+ "_hasAssistant"
+ "_hasAssistantDiagnosticAndUsageOptInDigestReported"
+ "_hasAssistantDimensions"
+ "_hasAssistantExperimentDigestReported"
+ "_hasAutoSendMessage"
+ "_hasCarPlay"
+ "_hasCodePathId"
+ "_hasCrrCommsAppSelectionJointId"
+ "_hasDictation"
+ "_hasDisplayedDialog"
+ "_hasEntityMetadata"
+ "_hasEnvelopeStatistics"
+ "_hasExperimentContext"
+ "_hasExperimentFixedDimensions"
+ "_hasFailure"
+ "_hasFbfFailure"
+ "_hasGeneral"
+ "_hasHomeKit"
+ "_hasHomePodProperties"
+ "_hasIOSAssistant"
+ "_hasIOSDevicePropertiesReported"
+ "_hasInputLocale"
+ "_hasMacOSAssistant"
+ "_hasMacOSDevicePropertiesReported"
+ "_hasMultiUserSetupStatus"
+ "_hasNetworkConnectionId"
+ "_hasNetworkInterface"
+ "_hasOdbatchDataReported"
+ "_hasOdbatchId"
+ "_hasOptIn"
+ "_hasOriginalClockId"
+ "_hasRepackagingExecution"
+ "_hasRfGradingDialogReportedTier1"
+ "_hasSandboxError"
+ "_hasSelectedUser"
+ "_hasSessionCounts"
+ "_hasSiriInCall"
+ "_hasSpokenDialog"
+ "_hasSuccess"
+ "_hasTuples"
+ "_hasTvOSAssistant"
+ "_hasTvOSDevicePropertiesReported"
+ "_hasVisionOSDevicePropertiesReported"
+ "_hasVoice"
+ "_hasWatchOSAssistant"
+ "_hasWatchOSDevicePropertiesReported"
+ "_heySiriHangupEnablementState"
+ "_homeKit"
+ "_homePodProperties"
+ "_iOSAssistant"
+ "_iOSDevicePropertiesReported"
+ "_inputLocale"
+ "_installedVoices"
+ "_isAllowSiriWhenLockedEnabled"
+ "_isAnnounceCallsEnabled"
+ "_isAnnounceNotificationsEnabled"
+ "_isApprovedForGrading"
+ "_isAssistantEnabled"
+ "_isAutomaticallySendMessagesEnabled"
+ "_isEnrollmentReprompted"
+ "_isExternalMicrophoneHSEnabled"
+ "_isFirstTriggerOrAfterFirstTrigger"
+ "_isPersonalDomainRequestsEnabled"
+ "_isPersonalDomainsEnabled"
+ "_isPressSideButtonForSiriEnabled"
+ "_isProximityCardSeen"
+ "_isRaiseToSpeakEnabled"
+ "_isReplyWithoutConfirmationEnabled"
+ "_isSpokenNotificationsControlCenterModuleEnabled"
+ "_isTriggered"
+ "_isTypeToSiriEnabled"
+ "_launchTimeInMs"
+ "_listenFor"
+ "_macOSAssistant"
+ "_macOSDevicePropertiesReported"
+ "_messageCount"
+ "_multiUserSetupStatus"
+ "_networkConnectionId"
+ "_networkInterface"
+ "_numIngestedNeuralContextualBiasingEmbeddings"
+ "_numSiriShortcutsEnabled"
+ "_odbatchDataReported"
+ "_odbatchId"
+ "_optIn"
+ "_originalClockId"
+ "_repackagingExecution"
+ "_responseCategory"
+ "_rfGradingDialogReportedTier1"
+ "_samplingResult"
+ "_sandboxError"
+ "_selectedUser"
+ "_serverSearchResultsMediaType"
+ "_sessionCounts"
+ "_siriInCall"
+ "_siriResponseTimeInMs"
+ "_spokenDialog"
+ "_success"
+ "_timeSinceAppContactLastLaunchedInSec"
+ "_timeToFirstWordInMs"
+ "_timeToUufrInMs"
+ "_totalBytes"
+ "_tuples"
+ "_tvOSAssistant"
+ "_tvOSDevicePropertiesReported"
+ "_usageScoreBooksRemote"
+ "_usageScoreMusicRemote"
+ "_usageScoreMusicWithoutRadioRemote"
+ "_usageScorePodcastsRemote"
+ "_usageScoreRadioRemote"
+ "_usdxSessionCount"
+ "_visionOSDevicePropertiesReported"
+ "_voice"
+ "_watchOSAssistant"
+ "_watchOSDevicePropertiesReported"
+ "_whichKind"
+ "_whichSuccessorfail"
+ "a1"
+ "accent"
+ "accessibility"
+ "adaptiveVolume"
+ "addAllAssets:"
+ "addDialogLines:"
+ "addEndpointDelayInMs:"
+ "addExperimentInfo:"
+ "addInstalledVoices:"
+ "addLaunchTimeInMs:"
+ "addSiriResponseTimeInMs:"
+ "addTimeToFirstWordInMs:"
+ "addTimeToUufrInMs:"
+ "allAssets"
+ "allAssetsAtIndex:"
+ "allAssetsCount"
+ "anchorRequestId"
+ "anchorSocialScore"
+ "announce"
+ "appContactFreqForMessages"
+ "appContactFreqForMessages10Min"
+ "appContactFreqForMessages1Day"
+ "appContactFreqForMessages1Hr"
+ "appContactFreqForMessages28Day"
+ "appContactFreqForMessages2Min"
+ "appContactFreqForMessages6Hr"
+ "appContactFreqForMessages7Day"
+ "appContactFreqForMessagesHaptic"
+ "appContactFreqForMessagesInf"
+ "appContactFreqForMessagesUsingSiri"
+ "appContactFreqForPhoneCall"
+ "appContactFreqForPhoneCall10Min"
+ "appContactFreqForPhoneCall1Day"
+ "appContactFreqForPhoneCall1Hr"
+ "appContactFreqForPhoneCall28Day"
+ "appContactFreqForPhoneCall2Min"
+ "appContactFreqForPhoneCall6Hr"
+ "appContactFreqForPhoneCall7Day"
+ "appContactFreqForPhoneCallHaptic"
+ "appContactFreqForPhoneCallInf"
+ "appContactFreqForPhoneCallUsingSiri"
+ "appFreqForMessages"
+ "appFreqForMessagesForCountryCode"
+ "appFreqForMessagesUsingSiri"
+ "appFreqForPhoneCall"
+ "appFreqForPhoneCallForCountryCode"
+ "appFreqForPhoneCallUsingSiri"
+ "appTaskCounts"
+ "appTaskType"
+ "appTimeSpentInSec"
+ "assetDownloadSizeInBytes"
+ "assetPath"
+ "assetSizeInBytes"
+ "assetUnarchivedSizeInBytes"
+ "assistant"
+ "assistantDiagnosticAndUsageOptInDigestReported"
+ "assistantDimensions"
+ "assistantExperimentDigestReported"
+ "autoSendMessage"
+ "cancelledSiriAppTaskCount"
+ "carPlay"
+ "cirFallbackTriggered"
+ "clearAllAssets"
+ "clearDialogLines"
+ "clearEndpointDelayInMs"
+ "clearExperimentInfo"
+ "clearInstalledVoices"
+ "clearLaunchTimeInMs"
+ "clearSiriResponseTimeInMs"
+ "clearTimeToFirstWordInMs"
+ "clearTimeToUufrInMs"
+ "codePathId"
+ "com.apple.aiml.lighthouse.pfa.PFAClientEvent"
+ "com.apple.aiml.lighthouse.pfa.PFAClientEvent.RepackagingExecution"
+ "com.apple.aiml.siri.dim.DIMClientEvent.DIMExperimentContext"
+ "com.apple.aiml.siri.odbatch.ODBATCHClientEvent"
+ "com.apple.aiml.siri.odbatch.ODBATCHClientEvent.ODBATCHDataReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssistantDiagnosticAndUsageOptInDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssistantExperimentDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDiOSDevicePropertiesReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDmacOSDevicePropertiesReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDtvOSDevicePropertiesReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDvisionOSDevicePropertiesReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDwatchOSDevicePropertiesReported"
+ "com.apple.aiml.siri.rf.RFClientEvent.RFGradingDialogReportedTier1"
+ "completedSiriAppTaskCount"
+ "completedUIAppTaskCount"
+ "crrCommsAppSelectionJointId"
+ "deleteAccent"
+ "deleteAccessibility"
+ "deleteAdaptiveVolume"
+ "deleteAllAssets"
+ "deleteAnchorRequestId"
+ "deleteAnchorSocialScore"
+ "deleteAnnounce"
+ "deleteAppContactFreqForMessages"
+ "deleteAppContactFreqForMessages10Min"
+ "deleteAppContactFreqForMessages1Day"
+ "deleteAppContactFreqForMessages1Hr"
+ "deleteAppContactFreqForMessages28Day"
+ "deleteAppContactFreqForMessages2Min"
+ "deleteAppContactFreqForMessages6Hr"
+ "deleteAppContactFreqForMessages7Day"
+ "deleteAppContactFreqForMessagesHaptic"
+ "deleteAppContactFreqForMessagesInf"
+ "deleteAppContactFreqForMessagesUsingSiri"
+ "deleteAppContactFreqForPhoneCall"
+ "deleteAppContactFreqForPhoneCall10Min"
+ "deleteAppContactFreqForPhoneCall1Day"
+ "deleteAppContactFreqForPhoneCall1Hr"
+ "deleteAppContactFreqForPhoneCall28Day"
+ "deleteAppContactFreqForPhoneCall2Min"
+ "deleteAppContactFreqForPhoneCall6Hr"
+ "deleteAppContactFreqForPhoneCall7Day"
+ "deleteAppContactFreqForPhoneCallHaptic"
+ "deleteAppContactFreqForPhoneCallInf"
+ "deleteAppContactFreqForPhoneCallUsingSiri"
+ "deleteAppFreqForMessages"
+ "deleteAppFreqForMessagesForCountryCode"
+ "deleteAppFreqForMessagesUsingSiri"
+ "deleteAppFreqForPhoneCall"
+ "deleteAppFreqForPhoneCallForCountryCode"
+ "deleteAppFreqForPhoneCallUsingSiri"
+ "deleteAppTaskCounts"
+ "deleteAppTaskType"
+ "deleteAppTimeSpentInSec"
+ "deleteAssetDownloadSizeInBytes"
+ "deleteAssetPath"
+ "deleteAssetSizeInBytes"
+ "deleteAssetUnarchivedSizeInBytes"
+ "deleteAssistant"
+ "deleteAssistantDiagnosticAndUsageOptInDigestReported"
+ "deleteAssistantDimensions"
+ "deleteAssistantExperimentDigestReported"
+ "deleteAutoSendMessage"
+ "deleteCancelledSiriAppTaskCount"
+ "deleteCarPlay"
+ "deleteCirFallbackTriggered"
+ "deleteCodePathId"
+ "deleteCompletedSiriAppTaskCount"
+ "deleteCompletedUIAppTaskCount"
+ "deleteCrrCommsAppSelectionJointId"
+ "deleteDialogLines"
+ "deleteDictation"
+ "deleteDigestType"
+ "deleteDisplayedDialog"
+ "deleteEndpointDelayInMs"
+ "deleteEntityMetadata"
+ "deleteEntityRank"
+ "deleteEntitySearchBundleScoreRemote"
+ "deleteEnvelopeStatistics"
+ "deleteErrorNumber"
+ "deleteExperimentAllocationStatus"
+ "deleteExperimentContext"
+ "deleteExperimentFixedDimensions"
+ "deleteExperimentInfo"
+ "deleteFailedSiriAppTaskCount"
+ "deleteFailure"
+ "deleteFbfFailure"
+ "deleteFlErrorCode"
+ "deleteGender"
+ "deleteGeneral"
+ "deleteHeySiriHangupEnablementState"
+ "deleteHomeKit"
+ "deleteHomePodProperties"
+ "deleteIOSAssistant"
+ "deleteIOSDevicePropertiesReported"
+ "deleteInputLocale"
+ "deleteInstalledVoices"
+ "deleteIsAllowSiriWhenLockedEnabled"
+ "deleteIsAnnounceCallsEnabled"
+ "deleteIsAnnounceNotificationsEnabled"
+ "deleteIsApprovedForGrading"
+ "deleteIsAssistantEnabled"
+ "deleteIsAutomaticallySendMessagesEnabled"
+ "deleteIsEnrollmentReprompted"
+ "deleteIsExternalMicrophoneHSEnabled"
+ "deleteIsFirstTriggerOrAfterFirstTrigger"
+ "deleteIsPersonalDomainRequestsEnabled"
+ "deleteIsPersonalDomainsEnabled"
+ "deleteIsPressSideButtonForSiriEnabled"
+ "deleteIsProximityCardSeen"
+ "deleteIsRaiseToSpeakEnabled"
+ "deleteIsReplyWithoutConfirmationEnabled"
+ "deleteIsSpokenNotificationsControlCenterModuleEnabled"
+ "deleteIsTriggered"
+ "deleteIsTypeToSiriEnabled"
+ "deleteLaunchTimeInMs"
+ "deleteListenFor"
+ "deleteMacOSAssistant"
+ "deleteMacOSDevicePropertiesReported"
+ "deleteMessageCount"
+ "deleteMultiUserSetupStatus"
+ "deleteNetworkConnectionId"
+ "deleteNetworkInterface"
+ "deleteNumIngestedNeuralContextualBiasingEmbeddings"
+ "deleteNumSiriShortcutsEnabled"
+ "deleteOdbatchDataReported"
+ "deleteOdbatchId"
+ "deleteOptIn"
+ "deleteOriginalClockId"
+ "deleteRepackagingExecution"
+ "deleteResponseCategory"
+ "deleteRfGradingDialogReportedTier1"
+ "deleteSamplingResult"
+ "deleteSandboxError"
+ "deleteSelectedUser"
+ "deleteServerSearchResultsMediaType"
+ "deleteSessionCounts"
+ "deleteSiriInCall"
+ "deleteSiriResponseTimeInMs"
+ "deleteSpokenDialog"
+ "deleteSuccess"
+ "deleteTimeSinceAppContactLastLaunchedInSec"
+ "deleteTimeToFirstWordInMs"
+ "deleteTimeToUufrInMs"
+ "deleteTotalBytes"
+ "deleteTuples"
+ "deleteTvOSAssistant"
+ "deleteTvOSDevicePropertiesReported"
+ "deleteUTCOffset"
+ "deleteUsageScoreBooksRemote"
+ "deleteUsageScoreMusicRemote"
+ "deleteUsageScoreMusicWithoutRadioRemote"
+ "deleteUsageScorePodcastsRemote"
+ "deleteUsageScoreRadioRemote"
+ "deleteUsdxSessionCount"
+ "deleteVisionOSDevicePropertiesReported"
+ "deleteVoice"
+ "deleteWatchOSAssistant"
+ "deleteWatchOSDevicePropertiesReported"
+ "dialogLines"
+ "dialogLinesAtIndex:"
+ "dialogLinesCount"
+ "dictation"
+ "digestType"
+ "displayedDialog"
+ "endpointDelayInMs"
+ "endpointDelayInMsAtIndex:"
+ "endpointDelayInMsCount"
+ "entityMetadata"
+ "entityRank"
+ "entitySearchBundleScoreRemote"
+ "envelopeStatistics"
+ "errorNumber"
+ "experimentAllocationStatus"
+ "experimentContext"
+ "experimentFixedDimensions"
+ "experimentInfo"
+ "experimentInfoAtIndex:"
+ "experimentInfoCount"
+ "experimentInfos"
+ "failedSiriAppTaskCount"
+ "failure"
+ "fbfFailure"
+ "flErrorCode"
+ "gender"
+ "general"
+ "hasAccent"
+ "hasAccessibility"
+ "hasAdaptiveVolume"
+ "hasAnchorRequestId"
+ "hasAnchorSocialScore"
+ "hasAnnounce"
+ "hasAppContactFreqForMessages"
+ "hasAppContactFreqForMessages10Min"
+ "hasAppContactFreqForMessages1Day"
+ "hasAppContactFreqForMessages1Hr"
+ "hasAppContactFreqForMessages28Day"
+ "hasAppContactFreqForMessages2Min"
+ "hasAppContactFreqForMessages6Hr"
+ "hasAppContactFreqForMessages7Day"
+ "hasAppContactFreqForMessagesHaptic"
+ "hasAppContactFreqForMessagesInf"
+ "hasAppContactFreqForMessagesUsingSiri"
+ "hasAppContactFreqForPhoneCall"
+ "hasAppContactFreqForPhoneCall10Min"
+ "hasAppContactFreqForPhoneCall1Day"
+ "hasAppContactFreqForPhoneCall1Hr"
+ "hasAppContactFreqForPhoneCall28Day"
+ "hasAppContactFreqForPhoneCall2Min"
+ "hasAppContactFreqForPhoneCall6Hr"
+ "hasAppContactFreqForPhoneCall7Day"
+ "hasAppContactFreqForPhoneCallHaptic"
+ "hasAppContactFreqForPhoneCallInf"
+ "hasAppContactFreqForPhoneCallUsingSiri"
+ "hasAppFreqForMessages"
+ "hasAppFreqForMessagesForCountryCode"
+ "hasAppFreqForMessagesUsingSiri"
+ "hasAppFreqForPhoneCall"
+ "hasAppFreqForPhoneCallForCountryCode"
+ "hasAppFreqForPhoneCallUsingSiri"
+ "hasAppTaskCounts"
+ "hasAppTaskType"
+ "hasAppTimeSpentInSec"
+ "hasAssetDownloadSizeInBytes"
+ "hasAssetPath"
+ "hasAssetSizeInBytes"
+ "hasAssetUnarchivedSizeInBytes"
+ "hasAssistant"
+ "hasAssistantDiagnosticAndUsageOptInDigestReported"
+ "hasAssistantDimensions"
+ "hasAssistantExperimentDigestReported"
+ "hasAutoSendMessage"
+ "hasCancelledSiriAppTaskCount"
+ "hasCarPlay"
+ "hasCirFallbackTriggered"
+ "hasCodePathId"
+ "hasCompletedSiriAppTaskCount"
+ "hasCompletedUIAppTaskCount"
+ "hasCrrCommsAppSelectionJointId"
+ "hasDictation"
+ "hasDigestType"
+ "hasDisplayedDialog"
+ "hasEntityMetadata"
+ "hasEntityRank"
+ "hasEntitySearchBundleScoreRemote"
+ "hasEnvelopeStatistics"
+ "hasErrorNumber"
+ "hasExperimentAllocationStatus"
+ "hasExperimentContext"
+ "hasExperimentFixedDimensions"
+ "hasFailedSiriAppTaskCount"
+ "hasFailure"
+ "hasFbfFailure"
+ "hasFlErrorCode"
+ "hasGender"
+ "hasGeneral"
+ "hasHeySiriHangupEnablementState"
+ "hasHomeKit"
+ "hasHomePodProperties"
+ "hasIOSAssistant"
+ "hasIOSDevicePropertiesReported"
+ "hasInputLocale"
+ "hasIsAllowSiriWhenLockedEnabled"
+ "hasIsAnnounceCallsEnabled"
+ "hasIsAnnounceNotificationsEnabled"
+ "hasIsApprovedForGrading"
+ "hasIsAssistantEnabled"
+ "hasIsAutomaticallySendMessagesEnabled"
+ "hasIsEnrollmentReprompted"
+ "hasIsExternalMicrophoneHSEnabled"
+ "hasIsFirstTriggerOrAfterFirstTrigger"
+ "hasIsPersonalDomainRequestsEnabled"
+ "hasIsPersonalDomainsEnabled"
+ "hasIsPressSideButtonForSiriEnabled"
+ "hasIsProximityCardSeen"
+ "hasIsRaiseToSpeakEnabled"
+ "hasIsReplyWithoutConfirmationEnabled"
+ "hasIsSpokenNotificationsControlCenterModuleEnabled"
+ "hasIsTriggered"
+ "hasIsTypeToSiriEnabled"
+ "hasListenFor"
+ "hasMacOSAssistant"
+ "hasMacOSDevicePropertiesReported"
+ "hasMessageCount"
+ "hasMultiUserSetupStatus"
+ "hasNetworkConnectionId"
+ "hasNetworkInterface"
+ "hasNumIngestedNeuralContextualBiasingEmbeddings"
+ "hasNumSiriShortcutsEnabled"
+ "hasOdbatchDataReported"
+ "hasOdbatchId"
+ "hasOptIn"
+ "hasOriginalClockId"
+ "hasRepackagingExecution"
+ "hasResponseCategory"
+ "hasRfGradingDialogReportedTier1"
+ "hasSamplingResult"
+ "hasSandboxError"
+ "hasSelectedUser"
+ "hasServerSearchResultsMediaType"
+ "hasSessionCounts"
+ "hasSiriInCall"
+ "hasSpokenDialog"
+ "hasSuccess"
+ "hasTimeSinceAppContactLastLaunchedInSec"
+ "hasTotalBytes"
+ "hasTuples"
+ "hasTvOSAssistant"
+ "hasTvOSDevicePropertiesReported"
+ "hasUTCOffset"
+ "hasUsageScoreBooksRemote"
+ "hasUsageScoreMusicRemote"
+ "hasUsageScoreMusicWithoutRadioRemote"
+ "hasUsageScorePodcastsRemote"
+ "hasUsageScoreRadioRemote"
+ "hasUsdxSessionCount"
+ "hasVisionOSDevicePropertiesReported"
+ "hasVoice"
+ "hasWatchOSAssistant"
+ "hasWatchOSDevicePropertiesReported"
+ "heySiriHangupEnablementState"
+ "homeKit"
+ "homePodProperties"
+ "iOSAssistant"
+ "iOSDevicePropertiesReported"
+ "inputLocale"
+ "installedVoices"
+ "installedVoicesAtIndex:"
+ "installedVoicesCount"
+ "invalid Collection: less than 'count' elements in collection"
+ "isAllowSiriWhenLockedEnabled"
+ "isAnnounceCallsEnabled"
+ "isAnnounceNotificationsEnabled"
+ "isApprovedForGrading"
+ "isAssistantEnabled"
+ "isAutomaticallySendMessagesEnabled"
+ "isEnrollmentReprompted"
+ "isExternalMicrophoneHSEnabled"
+ "isFirstTriggerOrAfterFirstTrigger"
+ "isPersonalDomainRequestsEnabled"
+ "isPersonalDomainsEnabled"
+ "isPressSideButtonForSiriEnabled"
+ "isProximityCardSeen"
+ "isRaiseToSpeakEnabled"
+ "isReplyWithoutConfirmationEnabled"
+ "isSpokenNotificationsControlCenterModuleEnabled"
+ "isTriggered"
+ "isTypeToSiriEnabled"
+ "launchTimeInMs"
+ "launchTimeInMsAtIndex:"
+ "launchTimeInMsCount"
+ "listenFor"
+ "macOSAssistant"
+ "macOSDevicePropertiesReported"
+ "messageCount"
+ "multiUserSetupStatus"
+ "networkConnectionId"
+ "networkInterface"
+ "numIngestedNeuralContextualBiasingEmbeddings"
+ "numSiriShortcutsEnabled"
+ "odbatchDataReported"
+ "odbatchId"
+ "optIn"
+ "originalClockId"
+ "repackagingExecution"
+ "responseCategory"
+ "rfGradingDialogReportedTier1"
+ "samplingResult"
+ "sandboxError"
+ "selectedUser"
+ "serverSearchResultsMediaType"
+ "sessionCounts"
+ "setAccent:"
+ "setAccessibility:"
+ "setAdaptiveVolume:"
+ "setAllAssets:"
+ "setAnchorRequestId:"
+ "setAnchorSocialScore:"
+ "setAnnounce:"
+ "setAppContactFreqForMessages10Min:"
+ "setAppContactFreqForMessages1Day:"
+ "setAppContactFreqForMessages1Hr:"
+ "setAppContactFreqForMessages28Day:"
+ "setAppContactFreqForMessages2Min:"
+ "setAppContactFreqForMessages6Hr:"
+ "setAppContactFreqForMessages7Day:"
+ "setAppContactFreqForMessages:"
+ "setAppContactFreqForMessagesHaptic:"
+ "setAppContactFreqForMessagesInf:"
+ "setAppContactFreqForMessagesUsingSiri:"
+ "setAppContactFreqForPhoneCall10Min:"
+ "setAppContactFreqForPhoneCall1Day:"
+ "setAppContactFreqForPhoneCall1Hr:"
+ "setAppContactFreqForPhoneCall28Day:"
+ "setAppContactFreqForPhoneCall2Min:"
+ "setAppContactFreqForPhoneCall6Hr:"
+ "setAppContactFreqForPhoneCall7Day:"
+ "setAppContactFreqForPhoneCall:"
+ "setAppContactFreqForPhoneCallHaptic:"
+ "setAppContactFreqForPhoneCallInf:"
+ "setAppContactFreqForPhoneCallUsingSiri:"
+ "setAppFreqForMessages:"
+ "setAppFreqForMessagesForCountryCode:"
+ "setAppFreqForMessagesUsingSiri:"
+ "setAppFreqForPhoneCall:"
+ "setAppFreqForPhoneCallForCountryCode:"
+ "setAppFreqForPhoneCallUsingSiri:"
+ "setAppTaskCounts:"
+ "setAppTaskType:"
+ "setAppTimeSpentInSec:"
+ "setAssetDownloadSizeInBytes:"
+ "setAssetPath:"
+ "setAssetSizeInBytes:"
+ "setAssetUnarchivedSizeInBytes:"
+ "setAssistant:"
+ "setAssistantDiagnosticAndUsageOptInDigestReported:"
+ "setAssistantDimensions:"
+ "setAssistantExperimentDigestReported:"
+ "setAutoSendMessage:"
+ "setCancelledSiriAppTaskCount:"
+ "setCarPlay:"
+ "setCirFallbackTriggered:"
+ "setCodePathId:"
+ "setCompletedSiriAppTaskCount:"
+ "setCompletedUIAppTaskCount:"
+ "setCrrCommsAppSelectionJointId:"
+ "setDialogLines:"
+ "setDictation:"
+ "setDigestType:"
+ "setDisplayedDialog:"
+ "setEndpointDelayInMs:"
+ "setEntityMetadata:"
+ "setEntityRank:"
+ "setEntitySearchBundleScoreRemote:"
+ "setEnvelopeStatistics:"
+ "setErrorNumber:"
+ "setExperimentAllocationStatus:"
+ "setExperimentContext:"
+ "setExperimentFixedDimensions:"
+ "setExperimentInfos:"
+ "setFailedSiriAppTaskCount:"
+ "setFailure:"
+ "setFbfFailure:"
+ "setFlErrorCode:"
+ "setGender:"
+ "setGeneral:"
+ "setHasAccent:"
+ "setHasAccessibility:"
+ "setHasAdaptiveVolume:"
+ "setHasAnchorRequestId:"
+ "setHasAnchorSocialScore:"
+ "setHasAnnounce:"
+ "setHasAppContactFreqForMessages10Min:"
+ "setHasAppContactFreqForMessages1Day:"
+ "setHasAppContactFreqForMessages1Hr:"
+ "setHasAppContactFreqForMessages28Day:"
+ "setHasAppContactFreqForMessages2Min:"
+ "setHasAppContactFreqForMessages6Hr:"
+ "setHasAppContactFreqForMessages7Day:"
+ "setHasAppContactFreqForMessages:"
+ "setHasAppContactFreqForMessagesHaptic:"
+ "setHasAppContactFreqForMessagesInf:"
+ "setHasAppContactFreqForMessagesUsingSiri:"
+ "setHasAppContactFreqForPhoneCall10Min:"
+ "setHasAppContactFreqForPhoneCall1Day:"
+ "setHasAppContactFreqForPhoneCall1Hr:"
+ "setHasAppContactFreqForPhoneCall28Day:"
+ "setHasAppContactFreqForPhoneCall2Min:"
+ "setHasAppContactFreqForPhoneCall6Hr:"
+ "setHasAppContactFreqForPhoneCall7Day:"
+ "setHasAppContactFreqForPhoneCall:"
+ "setHasAppContactFreqForPhoneCallHaptic:"
+ "setHasAppContactFreqForPhoneCallInf:"
+ "setHasAppContactFreqForPhoneCallUsingSiri:"
+ "setHasAppFreqForMessages:"
+ "setHasAppFreqForMessagesForCountryCode:"
+ "setHasAppFreqForMessagesUsingSiri:"
+ "setHasAppFreqForPhoneCall:"
+ "setHasAppFreqForPhoneCallForCountryCode:"
+ "setHasAppFreqForPhoneCallUsingSiri:"
+ "setHasAppTaskCounts:"
+ "setHasAppTaskType:"
+ "setHasAppTimeSpentInSec:"
+ "setHasAssetDownloadSizeInBytes:"
+ "setHasAssetPath:"
+ "setHasAssetSizeInBytes:"
+ "setHasAssetUnarchivedSizeInBytes:"
+ "setHasAssistant:"
+ "setHasAssistantDiagnosticAndUsageOptInDigestReported:"
+ "setHasAssistantDimensions:"
+ "setHasAssistantExperimentDigestReported:"
+ "setHasAutoSendMessage:"
+ "setHasCancelledSiriAppTaskCount:"
+ "setHasCarPlay:"
+ "setHasCirFallbackTriggered:"
+ "setHasCodePathId:"
+ "setHasCompletedSiriAppTaskCount:"
+ "setHasCompletedUIAppTaskCount:"
+ "setHasCrrCommsAppSelectionJointId:"
+ "setHasDictation:"
+ "setHasDigestType:"
+ "setHasDisplayedDialog:"
+ "setHasEntityMetadata:"
+ "setHasEntityRank:"
+ "setHasEntitySearchBundleScoreRemote:"
+ "setHasEnvelopeStatistics:"
+ "setHasErrorNumber:"
+ "setHasExperimentAllocationStatus:"
+ "setHasExperimentContext:"
+ "setHasExperimentFixedDimensions:"
+ "setHasFailedSiriAppTaskCount:"
+ "setHasFailure:"
+ "setHasFbfFailure:"
+ "setHasFlErrorCode:"
+ "setHasGender:"
+ "setHasGeneral:"
+ "setHasHeySiriHangupEnablementState:"
+ "setHasHomeKit:"
+ "setHasHomePodProperties:"
+ "setHasIOSAssistant:"
+ "setHasIOSDevicePropertiesReported:"
+ "setHasInputLocale:"
+ "setHasIsAllowSiriWhenLockedEnabled:"
+ "setHasIsAnnounceCallsEnabled:"
+ "setHasIsAnnounceNotificationsEnabled:"
+ "setHasIsApprovedForGrading:"
+ "setHasIsAssistantEnabled:"
+ "setHasIsAutomaticallySendMessagesEnabled:"
+ "setHasIsEnrollmentReprompted:"
+ "setHasIsExternalMicrophoneHSEnabled:"
+ "setHasIsFirstTriggerOrAfterFirstTrigger:"
+ "setHasIsPersonalDomainRequestsEnabled:"
+ "setHasIsPersonalDomainsEnabled:"
+ "setHasIsPressSideButtonForSiriEnabled:"
+ "setHasIsProximityCardSeen:"
+ "setHasIsRaiseToSpeakEnabled:"
+ "setHasIsReplyWithoutConfirmationEnabled:"
+ "setHasIsSpokenNotificationsControlCenterModuleEnabled:"
+ "setHasIsTriggered:"
+ "setHasIsTypeToSiriEnabled:"
+ "setHasListenFor:"
+ "setHasMacOSAssistant:"
+ "setHasMacOSDevicePropertiesReported:"
+ "setHasMessageCount:"
+ "setHasMultiUserSetupStatus:"
+ "setHasNetworkConnectionId:"
+ "setHasNetworkInterface:"
+ "setHasNumIngestedNeuralContextualBiasingEmbeddings:"
+ "setHasNumSiriShortcutsEnabled:"
+ "setHasOdbatchDataReported:"
+ "setHasOdbatchId:"
+ "setHasOptIn:"
+ "setHasOriginalClockId:"
+ "setHasRepackagingExecution:"
+ "setHasResponseCategory:"
+ "setHasRfGradingDialogReportedTier1:"
+ "setHasSamplingResult:"
+ "setHasSandboxError:"
+ "setHasSelectedUser:"
+ "setHasServerSearchResultsMediaType:"
+ "setHasSessionCounts:"
+ "setHasSiriInCall:"
+ "setHasSpokenDialog:"
+ "setHasSuccess:"
+ "setHasTimeSinceAppContactLastLaunchedInSec:"
+ "setHasTotalBytes:"
+ "setHasTuples:"
+ "setHasTvOSAssistant:"
+ "setHasTvOSDevicePropertiesReported:"
+ "setHasUTCOffset:"
+ "setHasUsageScoreBooksRemote:"
+ "setHasUsageScoreMusicRemote:"
+ "setHasUsageScoreMusicWithoutRadioRemote:"
+ "setHasUsageScorePodcastsRemote:"
+ "setHasUsageScoreRadioRemote:"
+ "setHasUsdxSessionCount:"
+ "setHasVisionOSDevicePropertiesReported:"
+ "setHasVoice:"
+ "setHasWatchOSAssistant:"
+ "setHasWatchOSDevicePropertiesReported:"
+ "setHeySiriHangupEnablementState:"
+ "setHomeKit:"
+ "setHomePodProperties:"
+ "setIOSAssistant:"
+ "setIOSDevicePropertiesReported:"
+ "setInputLocale:"
+ "setInstalledVoices:"
+ "setIsAllowSiriWhenLockedEnabled:"
+ "setIsAnnounceCallsEnabled:"
+ "setIsAnnounceNotificationsEnabled:"
+ "setIsApprovedForGrading:"
+ "setIsAssistantEnabled:"
+ "setIsAutomaticallySendMessagesEnabled:"
+ "setIsEnrollmentReprompted:"
+ "setIsExternalMicrophoneHSEnabled:"
+ "setIsFirstTriggerOrAfterFirstTrigger:"
+ "setIsPersonalDomainRequestsEnabled:"
+ "setIsPersonalDomainsEnabled:"
+ "setIsPressSideButtonForSiriEnabled:"
+ "setIsProximityCardSeen:"
+ "setIsRaiseToSpeakEnabled:"
+ "setIsReplyWithoutConfirmationEnabled:"
+ "setIsSpokenNotificationsControlCenterModuleEnabled:"
+ "setIsTriggered:"
+ "setIsTypeToSiriEnabled:"
+ "setLaunchTimeInMs:"
+ "setListenFor:"
+ "setMacOSAssistant:"
+ "setMacOSDevicePropertiesReported:"
+ "setMessageCount:"
+ "setMultiUserSetupStatus:"
+ "setNetworkConnectionId:"
+ "setNetworkInterface:"
+ "setNumIngestedNeuralContextualBiasingEmbeddings:"
+ "setNumSiriShortcutsEnabled:"
+ "setOdbatchDataReported:"
+ "setOdbatchId:"
+ "setOptIn:"
+ "setOriginalClockId:"
+ "setRepackagingExecution:"
+ "setResponseCategory:"
+ "setRfGradingDialogReportedTier1:"
+ "setSamplingResult:"
+ "setSandboxError:"
+ "setSelectedUser:"
+ "setServerSearchResultsMediaType:"
+ "setSessionCounts:"
+ "setSiriInCall:"
+ "setSiriResponseTimeInMs:"
+ "setSpokenDialog:"
+ "setSuccess:"
+ "setTimeSinceAppContactLastLaunchedInSec:"
+ "setTimeToFirstWordInMs:"
+ "setTimeToUufrInMs:"
+ "setTotalBytes:"
+ "setTuples:"
+ "setTvOSAssistant:"
+ "setTvOSDevicePropertiesReported:"
+ "setUTCOffset:"
+ "setUsageScoreBooksRemote:"
+ "setUsageScoreMusicRemote:"
+ "setUsageScoreMusicWithoutRadioRemote:"
+ "setUsageScorePodcastsRemote:"
+ "setUsageScoreRadioRemote:"
+ "setUsdxSessionCount:"
+ "setVisionOSDevicePropertiesReported:"
+ "setVoice:"
+ "setWatchOSAssistant:"
+ "setWatchOSDevicePropertiesReported:"
+ "siriInCall"
+ "siriResponseTimeInMs"
+ "siriResponseTimeInMsAtIndex:"
+ "siriResponseTimeInMsCount"
+ "spokenDialog"
+ "success"
+ "timeSinceAppContactLastLaunchedInSec"
+ "timeToFirstWordInMs"
+ "timeToFirstWordInMsAtIndex:"
+ "timeToFirstWordInMsCount"
+ "timeToUufrInMs"
+ "timeToUufrInMsAtIndex:"
+ "timeToUufrInMsCount"
+ "totalBytes"
+ "tuples"
+ "tvOSAssistant"
+ "tvOSDevicePropertiesReported"
+ "usageScoreBooksRemote"
+ "usageScoreMusicRemote"
+ "usageScoreMusicWithoutRadioRemote"
+ "usageScorePodcastsRemote"
+ "usageScoreRadioRemote"
+ "usdxSessionCount"
+ "visionOSDevicePropertiesReported"
+ "voice"
+ "watchOSAssistant"
+ "watchOSDevicePropertiesReported"
+ "whichKind"
+ "whichSuccessorfail"
+ "{?=\"appAffinityScoreForMessages\"b1\"appAffinityScoreForMessagesUsingSiri\"b1\"appAffinityScoreForMessagesReceived\"b1\"appFreqForMessages\"b1\"appFreqForMessagesUsingSiri\"b1\"appFreqForMessagesForCountryCode\"b1}"
+ "{?=\"appAffinityScoreForPhoneCall\"b1\"appAffinityScoreForPhoneCallUsingSiri\"b1\"appAffinityScoreForPhoneCallReceived\"b1\"appFreqForPhoneCall\"b1\"appFreqForPhoneCallUsingSiri\"b1\"appFreqForPhoneCallForCountryCode\"b1}"
+ "{?=\"appContactAffinityScoreForMessages\"b1\"appContactAffinityScoreForMessagesUsingSiri\"b1\"appContactAffinityScoreForMessagesReceived\"b1\"appContactFreqForMessages2Min\"b1\"appContactFreqForMessages10Min\"b1\"appContactFreqForMessages1Hr\"b1\"appContactFreqForMessages6Hr\"b1\"appContactFreqForMessages1Day\"b1\"appContactFreqForMessages7Day\"b1\"appContactFreqForMessages28Day\"b1\"appContactFreqForMessagesInf\"b1\"appContactFreqForMessages\"b1\"appContactFreqForMessagesUsingSiri\"b1\"appContactFreqForMessagesHaptic\"b1}"
+ "{?=\"appContactAffinityScoreForPhoneCall\"b1\"appContactAffinityScoreForPhoneCallUsingSiri\"b1\"appContactAffinityScoreForPhoneCallReceived\"b1\"appContactFreqForPhoneCall2Min\"b1\"appContactFreqForPhoneCall10Min\"b1\"appContactFreqForPhoneCall1Hr\"b1\"appContactFreqForPhoneCall6Hr\"b1\"appContactFreqForPhoneCall1Day\"b1\"appContactFreqForPhoneCall7Day\"b1\"appContactFreqForPhoneCall28Day\"b1\"appContactFreqForPhoneCallInf\"b1\"appContactFreqForPhoneCall\"b1\"appContactFreqForPhoneCallUsingSiri\"b1\"appContactFreqForPhoneCallHaptic\"b1}"
+ "{?=\"assetLocale\"b1\"assetSource\"b1\"assetSizeOnDisk\"b1\"isAssetPathValid\"b1\"assetDownloadSizeInBytes\"b1\"assetUnarchivedSizeInBytes\"b1}"
+ "{?=\"assetSizeInBytes\"b1}"
+ "{?=\"callDurationInSeconds\"b1\"hasUserInitiatedFollowup\"b1\"timeToEstablishInSeconds\"b1\"recentCallStatus\"b1\"disconnectedReason\"b1\"contactMatch\"b1}"
+ "{?=\"cirFallbackTriggered\"b1}"
+ "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1\"isContentFree\"b1\"isUserRecognized\"b1\"serverSearchResultsMediaType\"b1}"
+ "{?=\"completedSiriAppTaskCount\"b1\"failedSiriAppTaskCount\"b1\"cancelledSiriAppTaskCount\"b1\"completedUIAppTaskCount\"b1}"
+ "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1\"nlLocation\"b1\"responseCategory\"b1}"
+ "{?=\"digestType\"b1}"
+ "{?=\"entityRank\"b1}"
+ "{?=\"errorNumber\"b1}"
+ "{?=\"experimentAllocationStatus\"b1\"isTriggered\"b1\"isFirstTriggerOrAfterFirstTrigger\"b1}"
+ "{?=\"flErrorCode\"b1}"
+ "{?=\"gender\"b1\"name\"b1}"
+ "{?=\"hasHomekitHome\"b1}"
+ "{?=\"heySiriHangupEnablementState\"b1\"siriInCallEnablementState\"b1}"
+ "{?=\"isAdaptiveVolumeEnabled\"b1\"adaptiveVolume\"b1\"isPermanentOffsetEnabled\"b1\"permanentOffsetFactor\"b1}"
+ "{?=\"isAlwaysListenForHeySiriEnabled\"b1\"siriPauseTimeState\"b1\"isShowAppsBehindSiriEnabled\"b1\"siriSpeechRate\"b1\"isVoiceOverEnabled\"b1\"isTypeToSiriEnabled\"b1\"voiceFeedback\"b1}"
+ "{?=\"isAlwaysShowSiriCaptionsEnabled\"b1\"isAlwaysShowSpeechEnabled\"b1}"
+ "{?=\"isAnnounceCallsEnabled\"b1\"isAnnounceNotificationsEnabled\"b1\"isProximityCardSeen\"b1\"isReplyWithoutConfirmationEnabled\"b1\"isEnabledForHeadphones\"b1\"isSpokenNotificationsControlCenterModuleEnabled\"b1\"isCarPlayMuted\"b1\"carPlayStatus\"b1}"
+ "{?=\"isApprovedForGrading\"b1}"
+ "{?=\"isAssistantEnabled\"b1\"listenFor\"b1\"numSiriShortcutsEnabled\"b1\"isPreciseLocationEnabled\"b1}"
+ "{?=\"isAutomaticallySendMessagesEnabled\"b1\"isEnabledForHeadphones\"b1\"isEnabledForCarPlay\"b1}"
+ "{?=\"isClientForegroundActiveBundle\"b1\"compoundActiveBundleScore\"b1\"compoundMediaTypeBundleScore\"b1\"entitySearchBundleRecencyS\"b1\"entitySearchBundleScore\"b1\"isForegroundBundle\"b1\"isNowPlayingBundle\"b1\"nowPlayingBundleCount\"b1\"nowPlayingBundleRecencyS\"b1\"nowPlayingBundleScore\"b1\"isNowPlayingLastBundle\"b1\"nowPlayingUsage1Day\"b1\"nowPlayingUsage7Days\"b1\"nowPlayingUsage14Days\"b1\"isRawLastNowPlayingCoreDuet\"b1\"isRawMediaCategoryAudiobookSignal\"b1\"isRawMediaCategoryMusicSignal\"b1\"isRawMediaCategoryPodcastSignal\"b1\"isRawMediaCategoryRadioSignal\"b1\"isRawMediaCategoryVideoSignal\"b1\"rawMediaTypeUsageSignalBook\"b1\"rawMediaTypeUsageSignalMusic\"b1\"rawMediaTypeUsageSignalPodcast\"b1\"rawMediaTypeUsageSignalVideo\"b1\"rawNowPlayingCountCoreDuet10Min\"b1\"rawNowPlayingCountCoreDuet1Day\"b1\"rawNowPlayingCountCoreDuet1Hr\"b1\"rawNowPlayingCountCoreDuet28Day\"b1\"rawNowPlayingCountCoreDuet2Min\"b1\"rawNowPlayingCountCoreDuet6Hr\"b1\"rawNowPlayingCountCoreDuet7Day\"b1\"rawNowPlayingRecencyCD\"b1\"rawEntitySearchRecency\"b1\"usageScoreBooks\"b1\"usageScoreMusic\"b1\"usageScorePodcasts\"b1\"isAppFirstParty\"b1\"isRequestedApp\"b1\"isNowPlayingBundlePSE1\"b1\"isNowPlayingBundlePSE2\"b1\"vq21Score\"b1\"isSupportedFlag\"b1\"isUnicornFlag\"b1\"isSupportedUnicornMatchFlag\"b1\"isDisambiguationSelectedApp\"b1\"isModelPredictedApp\"b1\"usageScoreRadio\"b1\"usageScoreMusicWithoutRadio\"b1\"rawMediaTypeUsageSignalRadio\"b1\"rawMediaTypeUsageSignalMusicWithoutRadio\"b1\"subscriptionStatus\"b1\"isRawNowPlayingBundle\"b1\"rawNowPlayingTotal\"b1\"rawNowPlayingBundleScore\"b1\"isRawLastNowPlaying\"b1\"rawNowPlaying2Minutes\"b1\"rawNowPlaying10Minutes\"b1\"rawNowPlaying1Hour\"b1\"rawNowPlaying6Hours\"b1\"rawNowPlaying1Day\"b1\"rawNowPlaying7Days\"b1\"rawNowPlaying28Days\"b1\"rawLastNowPlayingRecency\"b1\"commonForegroundBundleApp\"b1\"isRawLastNowPlayingBoolean\"b1\"isCommonForegroundApp\"b1\"isBoltEnabled\"b1\"usageScoreMusicWithoutRadioRemote\"b1\"usageScoreBooksRemote\"b1\"usageScoreRadioRemote\"b1\"usageScorePodcastsRemote\"b1\"entitySearchBundleScoreRemote\"b1\"usageScoreMusicRemote\"b1}"
+ "{?=\"isDictationEnabled\"b1\"isAutoPunctuationEnabled\"b1}"
+ "{?=\"isExternalMicrophoneHSEnabled\"b1}"
+ "{?=\"isHeySiriTriggerPhraseEnabled\"b1\"isJustSiriTriggerPhraseEnabled\"b1\"isEnrollmentReprompted\"b1}"
+ "{?=\"isMteUploadEnabled\"b1\"dataSharingOptInStatus\"b1\"isServerUserDataSyncEnabled\"b1}"
+ "{?=\"isPersonalDomainRequestsEnabled\"b1}"
+ "{?=\"isPersonalDomainsEnabled\"b1}"
+ "{?=\"isPressSideButtonForSiriEnabled\"b1\"isAllowSiriWhenLockedEnabled\"b1}"
+ "{?=\"isRaiseToSpeakEnabled\"b1}"
+ "{?=\"isResolvedApp\"b1\"isResolvedContactInApp\"b1\"appTimeSpentAffinityScore\"b1\"isForegroundApp\"b1\"timeSinceAppLastLaunchedInSec\"b1\"isFirstPartyApp\"b1\"appTimeSpentInSec\"b1\"timeSinceAppContactLastLaunchedInSec\"b1}"
+ "{?=\"isShowAppsBehindSiriEnabledOnCarPlay\"b1\"isSiriCapableDigitalCarKeyAvailable\"b1}"
+ "{?=\"messageCount\"b1\"totalBytes\"b1}"
+ "{?=\"odldScore\"b1\"odldScoreThreshold\"b1\"errorCode\"b1\"anchorSocialScore\"b1}"
+ "{?=\"personalizedLanguageModelAgeInNs\"b1\"personalizedLanguageModelWeight\"b1\"averageActiveTokensPerFrame\"b1\"signalToNoiseRatioInDecibels\"b1\"recognitionDurationInNs\"b1\"audioDurationInNs\"b1\"eagerEnabled\"b1\"utteranceDetectionEnabled\"b1\"utteranceConcatenationEnabled\"b1\"continuousListeningEnabled\"b1\"eagerCustomerPerceivedLatencyInNs\"b1\"cpuRealTimeFactor\"b1\"numLanguageModelEnrollmentDataStreams\"b1\"inverseTextNormalizationDurationInNs\"b1\"inverseTextNormalizationDurationForFinalResultInNs\"b1\"numberOfInverseTextNormalizationRuns\"b1\"secondaryPassDurationInNs\"b1\"numberOfSecondaryPassRuns\"b1\"cpuInstructionsInMillionsPerSecond\"b1\"appleNeuralEngineCpuTimeInNs\"b1\"pageInsWaitTimeInNs\"b1\"recognitionHardware\"b1\"numIngestedNeuralContextualBiasingEmbeddings\"b1}"
+ "{?=\"provider\"b1}"
+ "{?=\"samplingResult\"b1}"
+ "{?=\"siriUILocation\"b1\"viewRegionDesignation\"b1\"responseCategory\"b1}"
+ "{?=\"sonicResponse\"b1\"responseCategory\"b1}"
+ "{?=\"storefrontId\"b1\"UTCOffset\"b1\"isStoreDemoMode\"b1}"
+ "{?=\"usdxSessionCount\"b1}"
+ "{?=\"viewInterface\"b1\"audioInterface\"b1\"appTaskType\"b1\"taskAppBundleId\"b1}"
+ "{?=\"voiceType\"b1\"voiceFootprint\"b1\"voiceVersion\"b1\"resourceVersion\"b1\"voiceName\"b1}"
+ "\xe1"
- "\x03(\x12\x11!#"
- "\x05\x12\x11"
- "{?=\"appAffinityScoreForMessages\"b1\"appAffinityScoreForMessagesUsingSiri\"b1\"appAffinityScoreForMessagesReceived\"b1}"
- "{?=\"appAffinityScoreForPhoneCall\"b1\"appAffinityScoreForPhoneCallUsingSiri\"b1\"appAffinityScoreForPhoneCallReceived\"b1}"
- "{?=\"appContactAffinityScoreForMessages\"b1\"appContactAffinityScoreForMessagesUsingSiri\"b1\"appContactAffinityScoreForMessagesReceived\"b1}"
- "{?=\"appContactAffinityScoreForPhoneCall\"b1\"appContactAffinityScoreForPhoneCallUsingSiri\"b1\"appContactAffinityScoreForPhoneCallReceived\"b1}"
- "{?=\"assetLocale\"b1\"assetSource\"b1\"assetSizeOnDisk\"b1\"isAssetPathValid\"b1}"
- "{?=\"callDurationInSeconds\"b1\"hasUserInitiatedFollowup\"b1\"timeToEstablishInSeconds\"b1\"recentCallStatus\"b1\"disconnectedReason\"b1}"
- "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1\"isContentFree\"b1\"isUserRecognized\"b1}"
- "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1\"nlLocation\"b1}"
- "{?=\"isClientForegroundActiveBundle\"b1\"compoundActiveBundleScore\"b1\"compoundMediaTypeBundleScore\"b1\"entitySearchBundleRecencyS\"b1\"entitySearchBundleScore\"b1\"isForegroundBundle\"b1\"isNowPlayingBundle\"b1\"nowPlayingBundleCount\"b1\"nowPlayingBundleRecencyS\"b1\"nowPlayingBundleScore\"b1\"isNowPlayingLastBundle\"b1\"nowPlayingUsage1Day\"b1\"nowPlayingUsage7Days\"b1\"nowPlayingUsage14Days\"b1\"isRawLastNowPlayingCoreDuet\"b1\"isRawMediaCategoryAudiobookSignal\"b1\"isRawMediaCategoryMusicSignal\"b1\"isRawMediaCategoryPodcastSignal\"b1\"isRawMediaCategoryRadioSignal\"b1\"isRawMediaCategoryVideoSignal\"b1\"rawMediaTypeUsageSignalBook\"b1\"rawMediaTypeUsageSignalMusic\"b1\"rawMediaTypeUsageSignalPodcast\"b1\"rawMediaTypeUsageSignalVideo\"b1\"rawNowPlayingCountCoreDuet10Min\"b1\"rawNowPlayingCountCoreDuet1Day\"b1\"rawNowPlayingCountCoreDuet1Hr\"b1\"rawNowPlayingCountCoreDuet28Day\"b1\"rawNowPlayingCountCoreDuet2Min\"b1\"rawNowPlayingCountCoreDuet6Hr\"b1\"rawNowPlayingCountCoreDuet7Day\"b1\"rawNowPlayingRecencyCD\"b1\"rawEntitySearchRecency\"b1\"usageScoreBooks\"b1\"usageScoreMusic\"b1\"usageScorePodcasts\"b1\"isAppFirstParty\"b1\"isRequestedApp\"b1\"isNowPlayingBundlePSE1\"b1\"isNowPlayingBundlePSE2\"b1\"vq21Score\"b1\"isSupportedFlag\"b1\"isUnicornFlag\"b1\"isSupportedUnicornMatchFlag\"b1\"isDisambiguationSelectedApp\"b1\"isModelPredictedApp\"b1\"usageScoreRadio\"b1\"usageScoreMusicWithoutRadio\"b1\"rawMediaTypeUsageSignalRadio\"b1\"rawMediaTypeUsageSignalMusicWithoutRadio\"b1\"subscriptionStatus\"b1\"isRawNowPlayingBundle\"b1\"rawNowPlayingTotal\"b1\"rawNowPlayingBundleScore\"b1\"isRawLastNowPlaying\"b1\"rawNowPlaying2Minutes\"b1\"rawNowPlaying10Minutes\"b1\"rawNowPlaying1Hour\"b1\"rawNowPlaying6Hours\"b1\"rawNowPlaying1Day\"b1\"rawNowPlaying7Days\"b1\"rawNowPlaying28Days\"b1\"rawLastNowPlayingRecency\"b1\"commonForegroundBundleApp\"b1\"isRawLastNowPlayingBoolean\"b1\"isCommonForegroundApp\"b1\"isBoltEnabled\"b1}"
- "{?=\"isHeySiriTriggerPhraseEnabled\"b1\"isJustSiriTriggerPhraseEnabled\"b1}"
- "{?=\"isResolvedApp\"b1\"isResolvedContactInApp\"b1\"appTimeSpentAffinityScore\"b1\"isForegroundApp\"b1\"timeSinceAppLastLaunchedInSec\"b1\"isFirstPartyApp\"b1}"
- "{?=\"odldScore\"b1\"odldScoreThreshold\"b1\"errorCode\"b1}"
- "{?=\"personalizedLanguageModelAgeInNs\"b1\"personalizedLanguageModelWeight\"b1\"averageActiveTokensPerFrame\"b1\"signalToNoiseRatioInDecibels\"b1\"recognitionDurationInNs\"b1\"audioDurationInNs\"b1\"eagerEnabled\"b1\"utteranceDetectionEnabled\"b1\"utteranceConcatenationEnabled\"b1\"continuousListeningEnabled\"b1\"eagerCustomerPerceivedLatencyInNs\"b1\"cpuRealTimeFactor\"b1\"numLanguageModelEnrollmentDataStreams\"b1\"inverseTextNormalizationDurationInNs\"b1\"inverseTextNormalizationDurationForFinalResultInNs\"b1\"numberOfInverseTextNormalizationRuns\"b1\"secondaryPassDurationInNs\"b1\"numberOfSecondaryPassRuns\"b1\"cpuInstructionsInMillionsPerSecond\"b1\"appleNeuralEngineCpuTimeInNs\"b1\"pageInsWaitTimeInNs\"b1\"recognitionHardware\"b1}"
- "{?=\"siriUILocation\"b1\"viewRegionDesignation\"b1}"
- "{?=\"sonicResponse\"b1}"
- "{?=\"voiceType\"b1\"voiceFootprint\"b1\"voiceVersion\"b1\"resourceVersion\"b1}"

```
