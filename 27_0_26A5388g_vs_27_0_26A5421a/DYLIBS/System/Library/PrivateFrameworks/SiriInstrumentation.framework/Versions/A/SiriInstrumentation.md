## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation`

```diff

-3600.80.1.0.0
-  __TEXT.__text: 0xdef7f4
-  __TEXT.__objc_methlist: 0x107c6c
-  __TEXT.__const: 0x17714
-  __TEXT.__swift5_typeref: 0x1ea6
-  __TEXT.__cstring: 0x94176
-  __TEXT.__constg_swiftt: 0x7e54
+3600.85.1.0.0
+  __TEXT.__text: 0xe24c20
+  __TEXT.__objc_methlist: 0x10ad94
+  __TEXT.__const: 0x17bc4
+  __TEXT.__swift5_typeref: 0x1edc
+  __TEXT.__cstring: 0x95c1d
+  __TEXT.__constg_swiftt: 0x7f74
   __TEXT.__swift5_reflstr: 0x21d
   __TEXT.__swift5_fieldmd: 0x45c
-  __TEXT.__swift5_builtin: 0x49ac
+  __TEXT.__swift5_builtin: 0x4a60
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_proto: 0x1374
-  __TEXT.__swift5_types: 0xf10
+  __TEXT.__swift5_proto: 0x139c
+  __TEXT.__swift5_types: 0xf34
   __TEXT.__oslogstring: 0xc1
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x33978
-  __TEXT.__eh_frame: 0x4838
+  __TEXT.__unwind_info: 0x343f0
+  __TEXT.__eh_frame: 0x4df8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3d3d8
-  __DATA_CONST.__objc_classlist: 0x6730
+  __DATA_CONST.__const: 0x3d8b0
+  __DATA_CONST.__objc_classlist: 0x6878
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x420d0
+  __DATA_CONST.__objc_selrefs: 0x42ed0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x66e0
-  __DATA_CONST.__got: 0x6868
-  __AUTH_CONST.__const: 0x24619
-  __AUTH_CONST.__cfstring: 0x7f220
-  __AUTH_CONST.__objc_const: 0x179c20
-  __AUTH_CONST.__objc_intobj: 0xc48
+  __DATA_CONST.__objc_superrefs: 0x6828
+  __DATA_CONST.__got: 0x69b0
+  __AUTH_CONST.__const: 0x25c19
+  __AUTH_CONST.__cfstring: 0x80460
+  __AUTH_CONST.__objc_const: 0x17da90
+  __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x29040
+  __AUTH.__objc_data: 0x29d10
   __AUTH.__data: 0x160
-  __DATA.__objc_ivar: 0x12920
-  __DATA.__data: 0x3448
-  __DATA.__bss: 0x1f480
+  __DATA.__objc_ivar: 0x12be8
+  __DATA.__data: 0x34f8
+  __DATA.__bss: 0x1f900
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x17a10
   __DATA_DIRTY.__data: 0x248

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 92982
-  Symbols:   144671
-  CStrings:  17383
+  Functions: 94065
+  Symbols:   146361
+  CStrings:  17568
 
Symbols:
+ +[COLSchemaCOLClientEvent(Component) joinability]
+ +[COLSchemaCOLClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[CHSchemaCHGoalCompletionInferenceMetadata deleteGoalCompletionConfidence]
+ -[CHSchemaCHGoalCompletionInferenceMetadata goalCompletionConfidence]
+ -[CHSchemaCHGoalCompletionInferenceMetadata hasGoalCompletionConfidence]
+ -[CHSchemaCHGoalCompletionInferenceMetadata setGoalCompletionConfidence:]
+ -[CHSchemaCHGoalCompletionInferenceMetadata setHasGoalCompletionConfidence:]
+ -[COLSchemaCOLClientEvent .cxx_destruct]
+ -[COLSchemaCOLClientEvent deleteEventMetadata]
+ -[COLSchemaCOLClientEvent deleteTrpFinalized]
+ -[COLSchemaCOLClientEvent dictionaryRepresentation]
+ -[COLSchemaCOLClientEvent eventMetadata]
+ -[COLSchemaCOLClientEvent hasEventMetadata]
+ -[COLSchemaCOLClientEvent hasTrpFinalized]
+ -[COLSchemaCOLClientEvent hash]
+ -[COLSchemaCOLClientEvent initWithDictionary:]
+ -[COLSchemaCOLClientEvent initWithJSON:]
+ -[COLSchemaCOLClientEvent isEqual:]
+ -[COLSchemaCOLClientEvent jsonData]
+ -[COLSchemaCOLClientEvent qualifiedMessageName]
+ -[COLSchemaCOLClientEvent readFrom:]
+ -[COLSchemaCOLClientEvent setEventMetadata:]
+ -[COLSchemaCOLClientEvent setHasEventMetadata:]
+ -[COLSchemaCOLClientEvent setHasTrpFinalized:]
+ -[COLSchemaCOLClientEvent setTrpFinalized:]
+ -[COLSchemaCOLClientEvent trpFinalized]
+ -[COLSchemaCOLClientEvent whichEvent_Type]
+ -[COLSchemaCOLClientEvent writeTo:]
+ -[COLSchemaCOLClientEvent(Component) componentName]
+ -[COLSchemaCOLClientEvent(Component) getComponentId]
+ -[COLSchemaCOLClientEvent(InnerEventContainer) innerEvent]
+ -[COLSchemaCOLClientEvent(InnerEventContainer) whichInnerEventType]
+ -[COLSchemaCOLClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[COLSchemaCOLClientEventMetadata .cxx_destruct]
+ -[COLSchemaCOLClientEventMetadata colId]
+ -[COLSchemaCOLClientEventMetadata deleteColId]
+ -[COLSchemaCOLClientEventMetadata dictionaryRepresentation]
+ -[COLSchemaCOLClientEventMetadata hasColId]
+ -[COLSchemaCOLClientEventMetadata hash]
+ -[COLSchemaCOLClientEventMetadata initWithDictionary:]
+ -[COLSchemaCOLClientEventMetadata initWithJSON:]
+ -[COLSchemaCOLClientEventMetadata isEqual:]
+ -[COLSchemaCOLClientEventMetadata jsonData]
+ -[COLSchemaCOLClientEventMetadata readFrom:]
+ -[COLSchemaCOLClientEventMetadata setColId:]
+ -[COLSchemaCOLClientEventMetadata setHasColId:]
+ -[COLSchemaCOLClientEventMetadata writeTo:]
+ -[COLSchemaCOLTrpFinalized .cxx_destruct]
+ -[COLSchemaCOLTrpFinalized deleteFinalizedTrpId]
+ -[COLSchemaCOLTrpFinalized deleteIfUserTurnId]
+ -[COLSchemaCOLTrpFinalized deleteMitigationDecision]
+ -[COLSchemaCOLTrpFinalized dictionaryRepresentation]
+ -[COLSchemaCOLTrpFinalized finalizedTrpId]
+ -[COLSchemaCOLTrpFinalized hasFinalizedTrpId]
+ -[COLSchemaCOLTrpFinalized hasIfUserTurnId]
+ -[COLSchemaCOLTrpFinalized hasMitigationDecision]
+ -[COLSchemaCOLTrpFinalized hash]
+ -[COLSchemaCOLTrpFinalized ifUserTurnId]
+ -[COLSchemaCOLTrpFinalized initWithDictionary:]
+ -[COLSchemaCOLTrpFinalized initWithJSON:]
+ -[COLSchemaCOLTrpFinalized isEqual:]
+ -[COLSchemaCOLTrpFinalized jsonData]
+ -[COLSchemaCOLTrpFinalized mitigationDecision]
+ -[COLSchemaCOLTrpFinalized readFrom:]
+ -[COLSchemaCOLTrpFinalized setFinalizedTrpId:]
+ -[COLSchemaCOLTrpFinalized setHasFinalizedTrpId:]
+ -[COLSchemaCOLTrpFinalized setHasIfUserTurnId:]
+ -[COLSchemaCOLTrpFinalized setHasMitigationDecision:]
+ -[COLSchemaCOLTrpFinalized setIfUserTurnId:]
+ -[COLSchemaCOLTrpFinalized setMitigationDecision:]
+ -[COLSchemaCOLTrpFinalized writeTo:]
+ -[GAASchemaGAARequestStarted .cxx_destruct]
+ -[GAASchemaGAARequestStarted agentActionId]
+ -[GAASchemaGAARequestStarted deleteAgentActionId]
+ -[GAASchemaGAARequestStarted hasAgentActionId]
+ -[GAASchemaGAARequestStarted setAgentActionId:]
+ -[GAASchemaGAARequestStarted setHasAgentActionId:]
+ -[GMSSchemaGMSExtendedInferenceMetrics deleteRequestQueueTimeInMs]
+ -[GMSSchemaGMSExtendedInferenceMetrics deleteTimePerOutputTokenInMs]
+ -[GMSSchemaGMSExtendedInferenceMetrics hasRequestQueueTimeInMs]
+ -[GMSSchemaGMSExtendedInferenceMetrics hasTimePerOutputTokenInMs]
+ -[GMSSchemaGMSExtendedInferenceMetrics requestQueueTimeInMs]
+ -[GMSSchemaGMSExtendedInferenceMetrics setHasRequestQueueTimeInMs:]
+ -[GMSSchemaGMSExtendedInferenceMetrics setHasTimePerOutputTokenInMs:]
+ -[GMSSchemaGMSExtendedInferenceMetrics setRequestQueueTimeInMs:]
+ -[GMSSchemaGMSExtendedInferenceMetrics setTimePerOutputTokenInMs:]
+ -[GMSSchemaGMSExtendedInferenceMetrics timePerOutputTokenInMs]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties deleteIsLLMSiriAvailable]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties hasIsLLMSiriAvailable]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties isLLMSiriAvailable]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setHasIsLLMSiriAvailable:]
+ -[ODDSiriSchemaODDAppleIntelligenceProperties setIsLLMSiriAvailable:]
+ -[ODDSiriSchemaODDAssistantLLMSiriCounts deleteSiriAppOpenCount]
+ -[ODDSiriSchemaODDAssistantLLMSiriCounts hasSiriAppOpenCount]
+ -[ODDSiriSchemaODDAssistantLLMSiriCounts setHasSiriAppOpenCount:]
+ -[ODDSiriSchemaODDAssistantLLMSiriCounts setSiriAppOpenCount:]
+ -[ODDSiriSchemaODDAssistantLLMSiriCounts siriAppOpenCount]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest deleteTuples]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest hasTuples]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest setHasTuples:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest setTuples:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDigest tuples]
+ -[ODDSiriSchemaODDAssistantLLMSiriDimensions appPartyType]
+ -[ODDSiriSchemaODDAssistantLLMSiriDimensions deleteAppPartyType]
+ -[ODDSiriSchemaODDAssistantLLMSiriDimensions hasAppPartyType]
+ -[ODDSiriSchemaODDAssistantLLMSiriDimensions setAppPartyType:]
+ -[ODDSiriSchemaODDAssistantLLMSiriDimensions setHasAppPartyType:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples addTurnIndices:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples clearTurnIndices]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples deleteTurnIndices]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples hash]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples initWithJSON:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples isEqual:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples jsonData]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples readFrom:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples setTurnIndices:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples turnIndicesAtIndex:]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples turnIndicesCount]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples turnIndices]
+ -[ODDSiriSchemaODDAssistantLLMSiriTuples writeTo:]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded .cxx_destruct]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded addMultimediaItems:]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded clearMultimediaItems]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded deleteMultimediaItems]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded multimediaItemsAtIndex:]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded multimediaItemsCount]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded multimediaItems]
+ -[PLANNERSchemaPLANNERBuildPlannerRequestEnded setMultimediaItems:]
+ -[PLANNERSchemaPLANNERMediaItemInfo deleteMediaHeightPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo deleteMediaSizeBytes]
+ -[PLANNERSchemaPLANNERMediaItemInfo deleteMediaType]
+ -[PLANNERSchemaPLANNERMediaItemInfo deleteMediaWidthPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo dictionaryRepresentation]
+ -[PLANNERSchemaPLANNERMediaItemInfo hasMediaHeightPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo hasMediaSizeBytes]
+ -[PLANNERSchemaPLANNERMediaItemInfo hasMediaType]
+ -[PLANNERSchemaPLANNERMediaItemInfo hasMediaWidthPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo hash]
+ -[PLANNERSchemaPLANNERMediaItemInfo initWithDictionary:]
+ -[PLANNERSchemaPLANNERMediaItemInfo initWithJSON:]
+ -[PLANNERSchemaPLANNERMediaItemInfo isEqual:]
+ -[PLANNERSchemaPLANNERMediaItemInfo jsonData]
+ -[PLANNERSchemaPLANNERMediaItemInfo mediaHeightPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo mediaSizeBytes]
+ -[PLANNERSchemaPLANNERMediaItemInfo mediaType]
+ -[PLANNERSchemaPLANNERMediaItemInfo mediaWidthPixels]
+ -[PLANNERSchemaPLANNERMediaItemInfo readFrom:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setHasMediaHeightPixels:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setHasMediaSizeBytes:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setHasMediaType:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setHasMediaWidthPixels:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setMediaHeightPixels:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setMediaSizeBytes:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setMediaType:]
+ -[PLANNERSchemaPLANNERMediaItemInfo setMediaWidthPixels:]
+ -[PLANNERSchemaPLANNERMediaItemInfo writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications addThreadNotificationEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications appNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications clearThreadNotificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications deleteAppNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications deleteThreadNotificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications hasAppNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications setAppNotification:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications setHasAppNotification:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications setThreadNotificationEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications threadNotificationEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications threadNotificationEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications threadNotificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef addAttendees:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef addOrganizers:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef attendeesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef attendeesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef attendees]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef calendar]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef clearAttendees]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef clearOrganizers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef deleteAttendees]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef deleteCalendar]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef deleteOrganizers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef hasCalendar]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef organizersAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef organizersCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef organizers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef setAttendees:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef setCalendar:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef setHasCalendar:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef setOrganizers:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef addParticipants:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef call]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef clearParticipants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef deleteCall]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef deleteParticipants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef hasCall]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef participantsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef participantsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef participants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef setCall:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef setHasCall:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef setParticipants:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef addParticipants:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef clearParticipants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef conversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef deleteConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef deleteParticipants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef hasConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef participantsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef participantsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef participants]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef setConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef setHasConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef setParticipants:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSConversationRef writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection addEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection clearEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection collection]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection deleteCollection]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection deleteEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection entitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection entitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection entities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection hasCollection]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection setCollection:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection setEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection setHasCollection:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef deleteEntityId]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef deleteEntityKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef entityId]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef entityKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef hasEntityId]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef hasEntityKind]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setEntityId:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setEntityKind:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setHasEntityId:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef setHasEntityKind:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSEntityRef writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded calendarToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded callToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteCalendarToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteCallToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteGeneralResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteGetSystemInfoResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteMessageToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deletePrepareCallMessageReadingListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deletePrepareNotificationsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deletePrepareReadConversationResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deletePrepareReadMessagesListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deletePrepareReadRemindersListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteSearchResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteSuccessResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded deleteValidNoIdKindResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded generalResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded getSystemInfoResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasCalendarToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasCallToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasGeneralResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasGetSystemInfoResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasMessageToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasPrepareCallMessageReadingListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasPrepareNotificationsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasPrepareReadConversationResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasPrepareReadMessagesListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasPrepareReadRemindersListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasSearchResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasSuccessResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded hasValidNoIdKindResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded messageToolsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded prepareCallMessageReadingListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded prepareNotificationsResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded prepareReadConversationResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded prepareReadMessagesListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded prepareReadRemindersListResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded searchResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setCalendarToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setCallToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setGeneralResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setGetSystemInfoResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasCalendarToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasCallToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasGeneralResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasGetSystemInfoResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasMessageToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasPrepareCallMessageReadingListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasPrepareNotificationsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasPrepareReadConversationResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasPrepareReadMessagesListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasPrepareReadRemindersListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasSearchResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasSuccessResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setHasValidNoIdKindResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setMessageToolsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setPrepareCallMessageReadingListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setPrepareNotificationsResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setPrepareReadConversationResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setPrepareReadMessagesListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setPrepareReadRemindersListResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setSearchResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setSuccessResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded setValidNoIdKindResult:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded successResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded validNoIdKindResult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded whichPlannertoolsexecutionresult]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult activeNavigationAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult activeNavigationCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult activeNavigations]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addActiveNavigation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addLiveEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addOnscreenText:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addOpenedApps:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addSelectedEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addVisibleAlarms:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addVisibleEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult addVisibleTimers:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearActiveNavigation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearLiveEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearOnscreenText]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearOpenedApps]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearSelectedEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearVisibleAlarms]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearVisibleEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult clearVisibleTimers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult currentTime]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteActiveNavigation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteCurrentTime]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteFocusedApp]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteGazePoint]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteLiveEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteOnscreenText]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteOpenedApps]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteSalientEntity]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteSelectedEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteSpanMatches]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteVisibleAlarms]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteVisibleEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult deleteVisibleTimers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult focusedApp]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult gazePoint]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hasCurrentTime]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hasFocusedApp]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hasGazePoint]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hasSalientEntity]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hasSpanMatches]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult liveEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult liveEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult liveEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult onscreenTextAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult onscreenTextCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult onscreenTexts]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult openedAppsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult openedAppsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult openedApps]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult salientEntity]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult selectedEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult selectedEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult selectedEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setActiveNavigations:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setCurrentTime:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setFocusedApp:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setGazePoint:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setHasCurrentTime:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setHasFocusedApp:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setHasGazePoint:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setHasSalientEntity:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setHasSpanMatches:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setLiveEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setOnscreenTexts:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setOpenedApps:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setSalientEntity:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setSelectedEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setSpanMatches:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setVisibleAlarms:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setVisibleEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult setVisibleTimers:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult spanMatches]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleAlarmsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleAlarmsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleAlarms]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleTimersAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleTimersCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult visibleTimers]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult addReadableMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult clearReadableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult currentConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult deleteCurrentConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult deleteReadableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult hasCurrentConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult readableMessagesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult readableMessagesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult readableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult setCurrentConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult setHasCurrentConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult setReadableMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult addResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult clearResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult deleteResults]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult resultsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult resultsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult results]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult setResults:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult deleteExists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult exists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult hasExists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult setExists:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult setHasExists:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult deleteExists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult exists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult hasExists]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult setExists:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult setHasExists:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef author]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef deleteAuthor]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef deleteMessage]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef hasAuthor]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef hasMessage]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef message]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef setAuthor:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef setHasAuthor:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef setHasMessage:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef setMessage:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage addCallMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage callMessagesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage callMessagesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage callMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage clearCallMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage deleteCallMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage deleteReadableUnit]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage hasReadableUnit]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage readableUnit]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage setCallMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage setHasReadableUnit:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage setReadableUnit:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation addReadableMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation clearReadableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation conversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation deleteConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation deleteReadableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation hasConversation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation readableMessagesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation readableMessagesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation readableMessages]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation setConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation setHasConversation:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation setReadableMessages:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage addSenders:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage clearSenders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage deleteMessage]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage deleteSenders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage hasMessage]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage message]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage sendersAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage sendersCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage senders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage setHasMessage:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage setMessage:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage setSenders:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList addReminders:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList clearReminders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList deleteReminderList]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList deleteReminders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList hasReminderList]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList reminderList]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList remindersAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList remindersCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList reminders]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList setHasReminderList:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList setReminderList:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList setReminders:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup addGlobalEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup addLocalEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup clearGlobalEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup clearLocalEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup deleteGlobalEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup deleteLocalEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup globalEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup globalEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup globalEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup localEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup localEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup localEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup setGlobalEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup setLocalEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches addAppEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches addContactRelationships:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches addHomeDeviceEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches appEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches appEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches appEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches clearAppEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches clearContactRelationships]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches clearHomeDeviceEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches contactRelationshipsAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches contactRelationshipsCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches contactRelationships]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches deleteAppEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches deleteContactRelationships]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches deleteHomeDeviceEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches homeDeviceEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches homeDeviceEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches homeDeviceEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches setAppEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches setContactRelationships:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches setHomeDeviceEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches writeTo:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications .cxx_destruct]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications addNotificationEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications clearNotificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications deleteNotificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications deleteThreadNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications dictionaryRepresentation]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications hasThreadNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications hash]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications initWithDictionary:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications initWithJSON:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications isEqual:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications jsonData]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications notificationEntitiesAtIndex:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications notificationEntitiesCount]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications notificationEntities]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications readFrom:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications setHasThreadNotification:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications setNotificationEntities:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications setThreadNotification:]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications threadNotification]
+ -[PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications writeTo:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation .cxx_destruct]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation deleteUrlToUi]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation deleteUrlType]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation dictionaryRepresentation]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation hasUrlToUi]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation hasUrlType]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation hash]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation initWithDictionary:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation initWithJSON:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation isEqual:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation jsonData]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation readFrom:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation setHasUrlToUi:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation setHasUrlType:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation setUrlToUi:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation setUrlType:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation urlToUi]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation urlType]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitation writeTo:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed .cxx_destruct]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed addCitations:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed citationsAtIndex:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed citationsCount]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed citations]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed clearCitations]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed deleteCitations]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed deleteStorefront]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed dictionaryRepresentation]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed hasStorefront]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed hash]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed initWithDictionary:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed initWithJSON:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed isEqual:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed jsonData]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed readFrom:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed setCitations:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed setHasStorefront:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed setStorefront:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed storefront]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed writeTo:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent citationsAttributed]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent deleteCitationsAttributed]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent hasCitationsAttributed]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent setCitationsAttributed:]
+ -[RESPONSETOOLSSchemaRESPONSETOOLSClientEvent setHasCitationsAttributed:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus buildVersion]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus deleteBuildVersion]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus deleteTimeSinceLastSoftwareUpdateInSeconds]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus hasBuildVersion]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus hasTimeSinceLastSoftwareUpdateInSeconds]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setBuildVersion:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setHasBuildVersion:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setHasTimeSinceLastSoftwareUpdateInSeconds:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus setTimeSinceLastSoftwareUpdateInSeconds:]
+ -[SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus timeSinceLastSoftwareUpdateInSeconds]
+ -[SISchemaClientEvent deleteUeiAsyncInvocationInfoCollected]
+ -[SISchemaClientEvent deleteUeiBreadcrumbReturned]
+ -[SISchemaClientEvent deleteUeiCanvasToAppExpanded]
+ -[SISchemaClientEvent deleteUeiIslandToCanvasExpanded]
+ -[SISchemaClientEvent deleteUeiLinkTapped]
+ -[SISchemaClientEvent deleteUeiResponseDisplayed]
+ -[SISchemaClientEvent deleteUeiSourceListExpanded]
+ -[SISchemaClientEvent hasUeiAsyncInvocationInfoCollected]
+ -[SISchemaClientEvent hasUeiBreadcrumbReturned]
+ -[SISchemaClientEvent hasUeiCanvasToAppExpanded]
+ -[SISchemaClientEvent hasUeiIslandToCanvasExpanded]
+ -[SISchemaClientEvent hasUeiLinkTapped]
+ -[SISchemaClientEvent hasUeiResponseDisplayed]
+ -[SISchemaClientEvent hasUeiSourceListExpanded]
+ -[SISchemaClientEvent setHasUeiAsyncInvocationInfoCollected:]
+ -[SISchemaClientEvent setHasUeiBreadcrumbReturned:]
+ -[SISchemaClientEvent setHasUeiCanvasToAppExpanded:]
+ -[SISchemaClientEvent setHasUeiIslandToCanvasExpanded:]
+ -[SISchemaClientEvent setHasUeiLinkTapped:]
+ -[SISchemaClientEvent setHasUeiResponseDisplayed:]
+ -[SISchemaClientEvent setHasUeiSourceListExpanded:]
+ -[SISchemaClientEvent setUeiAsyncInvocationInfoCollected:]
+ -[SISchemaClientEvent setUeiBreadcrumbReturned:]
+ -[SISchemaClientEvent setUeiCanvasToAppExpanded:]
+ -[SISchemaClientEvent setUeiIslandToCanvasExpanded:]
+ -[SISchemaClientEvent setUeiLinkTapped:]
+ -[SISchemaClientEvent setUeiResponseDisplayed:]
+ -[SISchemaClientEvent setUeiSourceListExpanded:]
+ -[SISchemaClientEvent ueiAsyncInvocationInfoCollected]
+ -[SISchemaClientEvent ueiBreadcrumbReturned]
+ -[SISchemaClientEvent ueiCanvasToAppExpanded]
+ -[SISchemaClientEvent ueiIslandToCanvasExpanded]
+ -[SISchemaClientEvent ueiLinkTapped]
+ -[SISchemaClientEvent ueiResponseDisplayed]
+ -[SISchemaClientEvent ueiSourceListExpanded]
+ -[SISchemaInvocation addUserAttachmentTypes:]
+ -[SISchemaInvocation clearUserAttachmentTypes]
+ -[SISchemaInvocation deleteUserAttachmentTypes]
+ -[SISchemaInvocation setUserAttachmentTypes:]
+ -[SISchemaInvocation userAttachmentTypesAtIndex:]
+ -[SISchemaInvocation userAttachmentTypesCount]
+ -[SISchemaInvocation userAttachmentTypes]
+ -[SISchemaUEIAsyncInvocationInfoCollected deleteIsNewConversation]
+ -[SISchemaUEIAsyncInvocationInfoCollected dictionaryRepresentation]
+ -[SISchemaUEIAsyncInvocationInfoCollected hasIsNewConversation]
+ -[SISchemaUEIAsyncInvocationInfoCollected hash]
+ -[SISchemaUEIAsyncInvocationInfoCollected initWithDictionary:]
+ -[SISchemaUEIAsyncInvocationInfoCollected initWithJSON:]
+ -[SISchemaUEIAsyncInvocationInfoCollected isEqual:]
+ -[SISchemaUEIAsyncInvocationInfoCollected isNewConversation]
+ -[SISchemaUEIAsyncInvocationInfoCollected jsonData]
+ -[SISchemaUEIAsyncInvocationInfoCollected readFrom:]
+ -[SISchemaUEIAsyncInvocationInfoCollected setHasIsNewConversation:]
+ -[SISchemaUEIAsyncInvocationInfoCollected setIsNewConversation:]
+ -[SISchemaUEIAsyncInvocationInfoCollected writeTo:]
+ -[SISchemaUEIBreadcrumbReturned deleteExists]
+ -[SISchemaUEIBreadcrumbReturned dictionaryRepresentation]
+ -[SISchemaUEIBreadcrumbReturned exists]
+ -[SISchemaUEIBreadcrumbReturned hasExists]
+ -[SISchemaUEIBreadcrumbReturned hash]
+ -[SISchemaUEIBreadcrumbReturned initWithDictionary:]
+ -[SISchemaUEIBreadcrumbReturned initWithJSON:]
+ -[SISchemaUEIBreadcrumbReturned isEqual:]
+ -[SISchemaUEIBreadcrumbReturned jsonData]
+ -[SISchemaUEIBreadcrumbReturned readFrom:]
+ -[SISchemaUEIBreadcrumbReturned setExists:]
+ -[SISchemaUEIBreadcrumbReturned setHasExists:]
+ -[SISchemaUEIBreadcrumbReturned writeTo:]
+ -[SISchemaUEICanvasToAppExpanded deleteExists]
+ -[SISchemaUEICanvasToAppExpanded dictionaryRepresentation]
+ -[SISchemaUEICanvasToAppExpanded exists]
+ -[SISchemaUEICanvasToAppExpanded hasExists]
+ -[SISchemaUEICanvasToAppExpanded hash]
+ -[SISchemaUEICanvasToAppExpanded initWithDictionary:]
+ -[SISchemaUEICanvasToAppExpanded initWithJSON:]
+ -[SISchemaUEICanvasToAppExpanded isEqual:]
+ -[SISchemaUEICanvasToAppExpanded jsonData]
+ -[SISchemaUEICanvasToAppExpanded readFrom:]
+ -[SISchemaUEICanvasToAppExpanded setExists:]
+ -[SISchemaUEICanvasToAppExpanded setHasExists:]
+ -[SISchemaUEICanvasToAppExpanded writeTo:]
+ -[SISchemaUEIIslandToCanvasExpanded deleteExists]
+ -[SISchemaUEIIslandToCanvasExpanded dictionaryRepresentation]
+ -[SISchemaUEIIslandToCanvasExpanded exists]
+ -[SISchemaUEIIslandToCanvasExpanded hasExists]
+ -[SISchemaUEIIslandToCanvasExpanded hash]
+ -[SISchemaUEIIslandToCanvasExpanded initWithDictionary:]
+ -[SISchemaUEIIslandToCanvasExpanded initWithJSON:]
+ -[SISchemaUEIIslandToCanvasExpanded isEqual:]
+ -[SISchemaUEIIslandToCanvasExpanded jsonData]
+ -[SISchemaUEIIslandToCanvasExpanded readFrom:]
+ -[SISchemaUEIIslandToCanvasExpanded setExists:]
+ -[SISchemaUEIIslandToCanvasExpanded setHasExists:]
+ -[SISchemaUEIIslandToCanvasExpanded writeTo:]
+ -[SISchemaUEILinkTapped deleteIsPersonalEntity]
+ -[SISchemaUEILinkTapped deleteLinkType]
+ -[SISchemaUEILinkTapped dictionaryRepresentation]
+ -[SISchemaUEILinkTapped hasIsPersonalEntity]
+ -[SISchemaUEILinkTapped hasLinkType]
+ -[SISchemaUEILinkTapped hash]
+ -[SISchemaUEILinkTapped initWithDictionary:]
+ -[SISchemaUEILinkTapped initWithJSON:]
+ -[SISchemaUEILinkTapped isEqual:]
+ -[SISchemaUEILinkTapped isPersonalEntity]
+ -[SISchemaUEILinkTapped jsonData]
+ -[SISchemaUEILinkTapped linkType]
+ -[SISchemaUEILinkTapped readFrom:]
+ -[SISchemaUEILinkTapped setHasIsPersonalEntity:]
+ -[SISchemaUEILinkTapped setHasLinkType:]
+ -[SISchemaUEILinkTapped setIsPersonalEntity:]
+ -[SISchemaUEILinkTapped setLinkType:]
+ -[SISchemaUEILinkTapped writeTo:]
+ -[SISchemaUEIResponseDisplayed deleteUiSurface]
+ -[SISchemaUEIResponseDisplayed dictionaryRepresentation]
+ -[SISchemaUEIResponseDisplayed hasUiSurface]
+ -[SISchemaUEIResponseDisplayed hash]
+ -[SISchemaUEIResponseDisplayed initWithDictionary:]
+ -[SISchemaUEIResponseDisplayed initWithJSON:]
+ -[SISchemaUEIResponseDisplayed isEqual:]
+ -[SISchemaUEIResponseDisplayed jsonData]
+ -[SISchemaUEIResponseDisplayed readFrom:]
+ -[SISchemaUEIResponseDisplayed setHasUiSurface:]
+ -[SISchemaUEIResponseDisplayed setUiSurface:]
+ -[SISchemaUEIResponseDisplayed uiSurface]
+ -[SISchemaUEIResponseDisplayed writeTo:]
+ -[SISchemaUEISourceListExpanded deleteSourceCount]
+ -[SISchemaUEISourceListExpanded dictionaryRepresentation]
+ -[SISchemaUEISourceListExpanded hasSourceCount]
+ -[SISchemaUEISourceListExpanded hash]
+ -[SISchemaUEISourceListExpanded initWithDictionary:]
+ -[SISchemaUEISourceListExpanded initWithJSON:]
+ -[SISchemaUEISourceListExpanded isEqual:]
+ -[SISchemaUEISourceListExpanded jsonData]
+ -[SISchemaUEISourceListExpanded readFrom:]
+ -[SISchemaUEISourceListExpanded setHasSourceCount:]
+ -[SISchemaUEISourceListExpanded setSourceCount:]
+ -[SISchemaUEISourceListExpanded sourceCount]
+ -[SISchemaUEISourceListExpanded writeTo:]
+ -[SISchemaUUFRShown deleteIslandExpansionIndicatorShown]
+ -[SISchemaUUFRShown hasIslandExpansionIndicatorShown]
+ -[SISchemaUUFRShown islandExpansionIndicatorShown]
+ -[SISchemaUUFRShown setHasIslandExpansionIndicatorShown:]
+ -[SISchemaUUFRShown setIslandExpansionIndicatorShown:]
+ OBJC_IVAR_$_CHSchemaCHGoalCompletionInferenceMetadata._goalCompletionConfidence
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._eventMetadata
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._hasEventMetadata
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._hasTrpFinalized
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._trpFinalized
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._whichEvent_Type
+ OBJC_IVAR_$_COLSchemaCOLClientEventMetadata._colId
+ OBJC_IVAR_$_COLSchemaCOLClientEventMetadata._hasColId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._finalizedTrpId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._has
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._hasFinalizedTrpId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._hasIfUserTurnId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._ifUserTurnId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._mitigationDecision
+ OBJC_IVAR_$_GAASchemaGAARequestStarted._agentActionId
+ OBJC_IVAR_$_GAASchemaGAARequestStarted._hasAgentActionId
+ OBJC_IVAR_$_GMSSchemaGMSExtendedInferenceMetrics._requestQueueTimeInMs
+ OBJC_IVAR_$_GMSSchemaGMSExtendedInferenceMetrics._timePerOutputTokenInMs
+ OBJC_IVAR_$_ODDSiriSchemaODDAppleIntelligenceProperties._isLLMSiriAvailable
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriCounts._siriAppOpenCount
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriDigest._hasTuples
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriDigest._tuples
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriDimensions._appPartyType
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriTuples._turnIndices
+ OBJC_IVAR_$_PLANNERSchemaPLANNERBuildPlannerRequestEnded._multimediaItems
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._has
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaHeightPixels
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaSizeBytes
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaType
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaWidthPixels
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._appNotification
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._hasAppNotification
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._threadNotificationEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._attendees
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._calendar
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._hasCalendar
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._organizers
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._call
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._hasCall
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._participants
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._conversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._hasConversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._participants
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._collection
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._entities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._hasCollection
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._entityId
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._entityKind
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._hasEntityId
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._hasEntityKind
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._calendarToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._callToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._generalResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._getSystemInfoResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasCalendarToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasCallToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasGeneralResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasGetSystemInfoResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasMessageToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareCallMessageReadingListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareNotificationsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadConversationResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadMessagesListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadRemindersListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasSearchResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasSuccessResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasValidNoIdKindResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._messageToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareCallMessageReadingListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareNotificationsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadConversationResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadMessagesListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadRemindersListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._searchResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._successResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._validNoIdKindResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._whichPlannertoolsexecutionresult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._activeNavigations
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._currentTime
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._focusedApp
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._gazePoint
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasCurrentTime
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasFocusedApp
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasGazePoint
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasSalientEntity
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasSpanMatches
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._liveEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._onscreenTexts
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._openedApps
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._salientEntity
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._selectedEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._spanMatches
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._visibleAlarms
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._visibleEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._visibleTimers
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult._currentConversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult._hasCurrentConversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult._readableMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult._exists
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult._has
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult._exists
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult._has
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._author
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._hasAuthor
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._hasMessage
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._message
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._callMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._hasReadableUnit
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._readableUnit
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._conversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._hasConversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._readableMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._hasMessage
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._message
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._senders
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._hasReminderList
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._reminderList
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._reminders
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup._globalEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup._localEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._appEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._contactRelationships
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._homeDeviceEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._hasThreadNotification
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._notificationEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._threadNotification
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._has
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._hasUrlToUi
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._urlToUi
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._urlType
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._citations
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._hasStorefront
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._storefront
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSClientEvent._citationsAttributed
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSClientEvent._hasCitationsAttributed
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus._buildVersion
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus._hasBuildVersion
+ OBJC_IVAR_$_SADSchemaSADIntelligenceFeatureAvailabilityChangeStatus._timeSinceLastSoftwareUpdateInSeconds
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiAsyncInvocationInfoCollected
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiBreadcrumbReturned
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiCanvasToAppExpanded
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiIslandToCanvasExpanded
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiLinkTapped
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiResponseDisplayed
+ OBJC_IVAR_$_SISchemaClientEvent._hasUeiSourceListExpanded
+ OBJC_IVAR_$_SISchemaClientEvent._ueiAsyncInvocationInfoCollected
+ OBJC_IVAR_$_SISchemaClientEvent._ueiBreadcrumbReturned
+ OBJC_IVAR_$_SISchemaClientEvent._ueiCanvasToAppExpanded
+ OBJC_IVAR_$_SISchemaClientEvent._ueiIslandToCanvasExpanded
+ OBJC_IVAR_$_SISchemaClientEvent._ueiLinkTapped
+ OBJC_IVAR_$_SISchemaClientEvent._ueiResponseDisplayed
+ OBJC_IVAR_$_SISchemaClientEvent._ueiSourceListExpanded
+ OBJC_IVAR_$_SISchemaInvocation._userAttachmentTypes
+ OBJC_IVAR_$_SISchemaUEIAsyncInvocationInfoCollected._has
+ OBJC_IVAR_$_SISchemaUEIAsyncInvocationInfoCollected._isNewConversation
+ OBJC_IVAR_$_SISchemaUEIBreadcrumbReturned._exists
+ OBJC_IVAR_$_SISchemaUEIBreadcrumbReturned._has
+ OBJC_IVAR_$_SISchemaUEICanvasToAppExpanded._exists
+ OBJC_IVAR_$_SISchemaUEICanvasToAppExpanded._has
+ OBJC_IVAR_$_SISchemaUEIIslandToCanvasExpanded._exists
+ OBJC_IVAR_$_SISchemaUEIIslandToCanvasExpanded._has
+ OBJC_IVAR_$_SISchemaUEILinkTapped._has
+ OBJC_IVAR_$_SISchemaUEILinkTapped._isPersonalEntity
+ OBJC_IVAR_$_SISchemaUEILinkTapped._linkType
+ OBJC_IVAR_$_SISchemaUEIResponseDisplayed._has
+ OBJC_IVAR_$_SISchemaUEIResponseDisplayed._uiSurface
+ OBJC_IVAR_$_SISchemaUEISourceListExpanded._has
+ OBJC_IVAR_$_SISchemaUEISourceListExpanded._sourceCount
+ OBJC_IVAR_$_SISchemaUUFRShown._islandExpansionIndicatorShown
+ _OBJC_CLASS_$_COLSchemaCOLClientEvent
+ _OBJC_CLASS_$_COLSchemaCOLClientEventMetadata
+ _OBJC_CLASS_$_COLSchemaCOLTrpFinalized
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantLLMSiriTuples
+ _OBJC_CLASS_$_PLANNERSchemaPLANNERMediaItemInfo
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ _OBJC_CLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ _OBJC_CLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ _OBJC_CLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ _OBJC_CLASS_$_SISchemaUEIAsyncInvocationInfoCollected
+ _OBJC_CLASS_$_SISchemaUEIBreadcrumbReturned
+ _OBJC_CLASS_$_SISchemaUEICanvasToAppExpanded
+ _OBJC_CLASS_$_SISchemaUEIIslandToCanvasExpanded
+ _OBJC_CLASS_$_SISchemaUEILinkTapped
+ _OBJC_CLASS_$_SISchemaUEIResponseDisplayed
+ _OBJC_CLASS_$_SISchemaUEISourceListExpanded
+ _OBJC_METACLASS_$_COLSchemaCOLClientEvent
+ _OBJC_METACLASS_$_COLSchemaCOLClientEventMetadata
+ _OBJC_METACLASS_$_COLSchemaCOLTrpFinalized
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantLLMSiriTuples
+ _OBJC_METACLASS_$_PLANNERSchemaPLANNERMediaItemInfo
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ _OBJC_METACLASS_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ _OBJC_METACLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ _OBJC_METACLASS_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ _OBJC_METACLASS_$_SISchemaUEIAsyncInvocationInfoCollected
+ _OBJC_METACLASS_$_SISchemaUEIBreadcrumbReturned
+ _OBJC_METACLASS_$_SISchemaUEICanvasToAppExpanded
+ _OBJC_METACLASS_$_SISchemaUEIIslandToCanvasExpanded
+ _OBJC_METACLASS_$_SISchemaUEILinkTapped
+ _OBJC_METACLASS_$_SISchemaUEIResponseDisplayed
+ _OBJC_METACLASS_$_SISchemaUEISourceListExpanded
+ _OUTLINED_FUNCTION_171
+ _OUTLINED_FUNCTION_172
+ _OUTLINED_FUNCTION_173
+ _OUTLINED_FUNCTION_174
+ _OUTLINED_FUNCTION_175
+ _OUTLINED_FUNCTION_176
+ _OUTLINED_FUNCTION_177
+ _OUTLINED_FUNCTION_178
+ _OUTLINED_FUNCTION_179
+ _OUTLINED_FUNCTION_180
+ _OUTLINED_FUNCTION_181
+ _OUTLINED_FUNCTION_182
+ _OUTLINED_FUNCTION_183
+ _OUTLINED_FUNCTION_184
+ _OUTLINED_FUNCTION_185
+ __OBJC_$_CLASS_METHODS_COLSchemaCOLClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_COLSchemaCOLClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_$_INSTANCE_METHODS_COLSchemaCOLClientEventMetadata
+ __OBJC_$_INSTANCE_METHODS_COLSchemaCOLTrpFinalized
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantLLMSiriTuples
+ __OBJC_$_INSTANCE_METHODS_PLANNERSchemaPLANNERMediaItemInfo
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ __OBJC_$_INSTANCE_METHODS_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ __OBJC_$_INSTANCE_METHODS_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ __OBJC_$_INSTANCE_METHODS_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIAsyncInvocationInfoCollected
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIBreadcrumbReturned
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEICanvasToAppExpanded
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIIslandToCanvasExpanded
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEILinkTapped
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEIResponseDisplayed
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEISourceListExpanded
+ __OBJC_$_INSTANCE_VARIABLES_COLSchemaCOLClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_COLSchemaCOLClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_COLSchemaCOLTrpFinalized
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantLLMSiriTuples
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERSchemaPLANNERMediaItemInfo
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ __OBJC_$_INSTANCE_VARIABLES_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ __OBJC_$_INSTANCE_VARIABLES_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ __OBJC_$_INSTANCE_VARIABLES_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIAsyncInvocationInfoCollected
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIBreadcrumbReturned
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEICanvasToAppExpanded
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIIslandToCanvasExpanded
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEILinkTapped
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEIResponseDisplayed
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEISourceListExpanded
+ __OBJC_$_PROP_LIST_COLSchemaCOLClientEventMetadata
+ __OBJC_$_PROP_LIST_COLSchemaCOLTrpFinalized
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantLLMSiriTuples
+ __OBJC_$_PROP_LIST_PLANNERSchemaPLANNERMediaItemInfo
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ __OBJC_$_PROP_LIST_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ __OBJC_$_PROP_LIST_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ __OBJC_$_PROP_LIST_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ __OBJC_$_PROP_LIST_SISchemaUEIAsyncInvocationInfoCollected
+ __OBJC_$_PROP_LIST_SISchemaUEIBreadcrumbReturned
+ __OBJC_$_PROP_LIST_SISchemaUEICanvasToAppExpanded
+ __OBJC_$_PROP_LIST_SISchemaUEIIslandToCanvasExpanded
+ __OBJC_$_PROP_LIST_SISchemaUEILinkTapped
+ __OBJC_$_PROP_LIST_SISchemaUEIResponseDisplayed
+ __OBJC_$_PROP_LIST_SISchemaUEISourceListExpanded
+ __OBJC_CLASS_PROTOCOLS_$_COLSchemaCOLClientEvent(InstrumentationAdditions|Component|InnerEventContainer)
+ __OBJC_CLASS_RO_$_COLSchemaCOLClientEvent
+ __OBJC_CLASS_RO_$_COLSchemaCOLClientEventMetadata
+ __OBJC_CLASS_RO_$_COLSchemaCOLTrpFinalized
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantLLMSiriTuples
+ __OBJC_CLASS_RO_$_PLANNERSchemaPLANNERMediaItemInfo
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ __OBJC_CLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ __OBJC_CLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ __OBJC_CLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ __OBJC_CLASS_RO_$_SISchemaUEIAsyncInvocationInfoCollected
+ __OBJC_CLASS_RO_$_SISchemaUEIBreadcrumbReturned
+ __OBJC_CLASS_RO_$_SISchemaUEICanvasToAppExpanded
+ __OBJC_CLASS_RO_$_SISchemaUEIIslandToCanvasExpanded
+ __OBJC_CLASS_RO_$_SISchemaUEILinkTapped
+ __OBJC_CLASS_RO_$_SISchemaUEIResponseDisplayed
+ __OBJC_CLASS_RO_$_SISchemaUEISourceListExpanded
+ __OBJC_METACLASS_RO_$_COLSchemaCOLClientEvent
+ __OBJC_METACLASS_RO_$_COLSchemaCOLClientEventMetadata
+ __OBJC_METACLASS_RO_$_COLSchemaCOLTrpFinalized
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantLLMSiriTuples
+ __OBJC_METACLASS_RO_$_PLANNERSchemaPLANNERMediaItemInfo
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionMessageToolsResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareCallMessageReadingListResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareNotificationsResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadConversationResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches
+ __OBJC_METACLASS_RO_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications
+ __OBJC_METACLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation
+ __OBJC_METACLASS_RO_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed
+ __OBJC_METACLASS_RO_$_SISchemaUEIAsyncInvocationInfoCollected
+ __OBJC_METACLASS_RO_$_SISchemaUEIBreadcrumbReturned
+ __OBJC_METACLASS_RO_$_SISchemaUEICanvasToAppExpanded
+ __OBJC_METACLASS_RO_$_SISchemaUEIIslandToCanvasExpanded
+ __OBJC_METACLASS_RO_$_SISchemaUEILinkTapped
+ __OBJC_METACLASS_RO_$_SISchemaUEIResponseDisplayed
+ __OBJC_METACLASS_RO_$_SISchemaUEISourceListExpanded
+ _objc_msgSend$activeNavigations
+ _objc_msgSend$addActiveNavigation:
+ _objc_msgSend$addAppEntities:
+ _objc_msgSend$addAttendees:
+ _objc_msgSend$addCallMessages:
+ _objc_msgSend$addCitations:
+ _objc_msgSend$addContactRelationships:
+ _objc_msgSend$addGlobalEntities:
+ _objc_msgSend$addHomeDeviceEntities:
+ _objc_msgSend$addLiveEntities:
+ _objc_msgSend$addLocalEntities:
+ _objc_msgSend$addMultimediaItems:
+ _objc_msgSend$addNotificationEntities:
+ _objc_msgSend$addOnscreenText:
+ _objc_msgSend$addOpenedApps:
+ _objc_msgSend$addOrganizers:
+ _objc_msgSend$addParticipants:
+ _objc_msgSend$addReadableMessages:
+ _objc_msgSend$addReminders:
+ _objc_msgSend$addSelectedEntities:
+ _objc_msgSend$addSenders:
+ _objc_msgSend$addThreadNotificationEntities:
+ _objc_msgSend$addTurnIndices:
+ _objc_msgSend$addUserAttachmentTypes:
+ _objc_msgSend$addVisibleAlarms:
+ _objc_msgSend$addVisibleEntities:
+ _objc_msgSend$addVisibleTimers:
+ _objc_msgSend$appEntities
+ _objc_msgSend$appNotification
+ _objc_msgSend$appPartyType
+ _objc_msgSend$attendees
+ _objc_msgSend$author
+ _objc_msgSend$buildVersion
+ _objc_msgSend$calendar
+ _objc_msgSend$calendarToolsResult
+ _objc_msgSend$callMessages
+ _objc_msgSend$callToolsResult
+ _objc_msgSend$citations
+ _objc_msgSend$citationsAttributed
+ _objc_msgSend$clearActiveNavigation
+ _objc_msgSend$clearAppEntities
+ _objc_msgSend$clearAttendees
+ _objc_msgSend$clearCallMessages
+ _objc_msgSend$clearCitations
+ _objc_msgSend$clearContactRelationships
+ _objc_msgSend$clearGlobalEntities
+ _objc_msgSend$clearHomeDeviceEntities
+ _objc_msgSend$clearLiveEntities
+ _objc_msgSend$clearLocalEntities
+ _objc_msgSend$clearMultimediaItems
+ _objc_msgSend$clearNotificationEntities
+ _objc_msgSend$clearOnscreenText
+ _objc_msgSend$clearOpenedApps
+ _objc_msgSend$clearOrganizers
+ _objc_msgSend$clearParticipants
+ _objc_msgSend$clearReadableMessages
+ _objc_msgSend$clearReminders
+ _objc_msgSend$clearSelectedEntities
+ _objc_msgSend$clearSenders
+ _objc_msgSend$clearThreadNotificationEntities
+ _objc_msgSend$clearTurnIndices
+ _objc_msgSend$clearUserAttachmentTypes
+ _objc_msgSend$clearVisibleAlarms
+ _objc_msgSend$clearVisibleEntities
+ _objc_msgSend$clearVisibleTimers
+ _objc_msgSend$colId
+ _objc_msgSend$contactRelationships
+ _objc_msgSend$conversation
+ _objc_msgSend$currentConversation
+ _objc_msgSend$currentTime
+ _objc_msgSend$deleteCitationsAttributed
+ _objc_msgSend$deleteEntityKind
+ _objc_msgSend$entityKind
+ _objc_msgSend$focusedApp
+ _objc_msgSend$gazePoint
+ _objc_msgSend$generalResult
+ _objc_msgSend$getSystemInfoResult
+ _objc_msgSend$globalEntities
+ _objc_msgSend$goalCompletionConfidence
+ _objc_msgSend$homeDeviceEntities
+ _objc_msgSend$isLLMSiriAvailable
+ _objc_msgSend$isPersonalEntity
+ _objc_msgSend$islandExpansionIndicatorShown
+ _objc_msgSend$linkType
+ _objc_msgSend$liveEntities
+ _objc_msgSend$localEntities
+ _objc_msgSend$mediaHeightPixels
+ _objc_msgSend$mediaSizeBytes
+ _objc_msgSend$mediaWidthPixels
+ _objc_msgSend$messageToolsResult
+ _objc_msgSend$multimediaItems
+ _objc_msgSend$notificationEntities
+ _objc_msgSend$onscreenTexts
+ _objc_msgSend$openedApps
+ _objc_msgSend$organizers
+ _objc_msgSend$participants
+ _objc_msgSend$prepareCallMessageReadingListResult
+ _objc_msgSend$prepareNotificationsResult
+ _objc_msgSend$prepareReadConversationResult
+ _objc_msgSend$prepareReadMessagesListResult
+ _objc_msgSend$prepareReadRemindersListResult
+ _objc_msgSend$readableMessages
+ _objc_msgSend$readableUnit
+ _objc_msgSend$reminderList
+ _objc_msgSend$reminders
+ _objc_msgSend$requestQueueTimeInMs
+ _objc_msgSend$salientEntity
+ _objc_msgSend$searchResult
+ _objc_msgSend$selectedEntities
+ _objc_msgSend$senders
+ _objc_msgSend$setAppNotification:
+ _objc_msgSend$setAppPartyType:
+ _objc_msgSend$setAuthor:
+ _objc_msgSend$setBuildVersion:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setCalendarToolsResult:
+ _objc_msgSend$setCallToolsResult:
+ _objc_msgSend$setCitationsAttributed:
+ _objc_msgSend$setColId:
+ _objc_msgSend$setConversation:
+ _objc_msgSend$setCurrentConversation:
+ _objc_msgSend$setCurrentTime:
+ _objc_msgSend$setEntityKind:
+ _objc_msgSend$setFocusedApp:
+ _objc_msgSend$setGazePoint:
+ _objc_msgSend$setGeneralResult:
+ _objc_msgSend$setGetSystemInfoResult:
+ _objc_msgSend$setGoalCompletionConfidence:
+ _objc_msgSend$setIsLLMSiriAvailable:
+ _objc_msgSend$setIsPersonalEntity:
+ _objc_msgSend$setIslandExpansionIndicatorShown:
+ _objc_msgSend$setLinkType:
+ _objc_msgSend$setMediaHeightPixels:
+ _objc_msgSend$setMediaSizeBytes:
+ _objc_msgSend$setMediaWidthPixels:
+ _objc_msgSend$setMessageToolsResult:
+ _objc_msgSend$setPrepareCallMessageReadingListResult:
+ _objc_msgSend$setPrepareNotificationsResult:
+ _objc_msgSend$setPrepareReadConversationResult:
+ _objc_msgSend$setPrepareReadMessagesListResult:
+ _objc_msgSend$setPrepareReadRemindersListResult:
+ _objc_msgSend$setReadableUnit:
+ _objc_msgSend$setReminderList:
+ _objc_msgSend$setRequestQueueTimeInMs:
+ _objc_msgSend$setSalientEntity:
+ _objc_msgSend$setSearchResult:
+ _objc_msgSend$setSiriAppOpenCount:
+ _objc_msgSend$setSourceCount:
+ _objc_msgSend$setSpanMatches:
+ _objc_msgSend$setStorefront:
+ _objc_msgSend$setSuccessResult:
+ _objc_msgSend$setThreadNotification:
+ _objc_msgSend$setTimePerOutputTokenInMs:
+ _objc_msgSend$setUeiAsyncInvocationInfoCollected:
+ _objc_msgSend$setUeiBreadcrumbReturned:
+ _objc_msgSend$setUeiCanvasToAppExpanded:
+ _objc_msgSend$setUeiIslandToCanvasExpanded:
+ _objc_msgSend$setUeiLinkTapped:
+ _objc_msgSend$setUeiResponseDisplayed:
+ _objc_msgSend$setUeiSourceListExpanded:
+ _objc_msgSend$setUiSurface:
+ _objc_msgSend$setUrlToUi:
+ _objc_msgSend$setUrlType:
+ _objc_msgSend$setValidNoIdKindResult:
+ _objc_msgSend$siriAppOpenCount
+ _objc_msgSend$sourceCount
+ _objc_msgSend$storefront
+ _objc_msgSend$successResult
+ _objc_msgSend$threadNotification
+ _objc_msgSend$threadNotificationEntities
+ _objc_msgSend$timePerOutputTokenInMs
+ _objc_msgSend$turnIndices
+ _objc_msgSend$ueiAsyncInvocationInfoCollected
+ _objc_msgSend$ueiBreadcrumbReturned
+ _objc_msgSend$ueiCanvasToAppExpanded
+ _objc_msgSend$ueiIslandToCanvasExpanded
+ _objc_msgSend$ueiLinkTapped
+ _objc_msgSend$ueiResponseDisplayed
+ _objc_msgSend$ueiSourceListExpanded
+ _objc_msgSend$uiSurface
+ _objc_msgSend$urlToUi
+ _objc_msgSend$urlType
+ _objc_msgSend$userAttachmentTypes
+ _objc_msgSend$validNoIdKindResult
+ _objc_msgSend$visibleAlarms
+ _objc_msgSend$visibleEntities
+ _objc_msgSend$visibleTimers
+ _objc_msgSend$whichPlannertoolsexecutionresult
+ _symbolic _____ So19SISchemaUEILinkTypeV
+ _symbolic _____ So20SISchemaUEIUISurfaceV
+ _symbolic _____ So25ODDSiriSchemaODDTurnIndexV
+ _symbolic _____ So25SISchemaUEIAttachmentTypeV
+ _symbolic _____ So28ODDSiriSchemaODDAppPartyTypeV
+ _symbolic _____ So29PLANNERSchemaPLANNERMediaTypeV
+ _symbolic _____ So34CHSchemaCHGoalCompletionConfidenceV
+ _symbolic _____ So40COLSchemaCOLContextualMitigationDecisionV
+ _symbolic _____ So47RESPONSETOOLSSchemaRESPONSETOOLSCitationUrlTypeV
CStrings:
+ "CDMSERVICEGRAPHNAME_SHORTCUT_DETECTOR"
+ "CHGOALCOMPLETIONCONFIDENCE_HIGH"
+ "CHGOALCOMPLETIONCONFIDENCE_LOW"
+ "CHGOALCOMPLETIONCONFIDENCE_MEDIUM"
+ "CHGOALCOMPLETIONCONFIDENCE_UNKNOWN"
+ "COLCONTEXTUALMITIGATIONDECISION_MITIGATED"
+ "COLCONTEXTUALMITIGATIONDECISION_SELECTED"
+ "COLCONTEXTUALMITIGATIONDECISION_UNKNOWN"
+ "COL_CLIENT_EVENT"
+ "COMPONENTNAME_COL"
+ "NETPROTOCOL_QUIC"
+ "ODDAPPPARTYTYPE_FIRST_PARTY"
+ "ODDAPPPARTYTYPE_SECOND_PARTY"
+ "ODDAPPPARTYTYPE_THIRD_PARTY"
+ "ODDAPPPARTYTYPE_UNKNOWN"
+ "ODDTURNINDEX_1"
+ "ODDTURNINDEX_10"
+ "ODDTURNINDEX_100_OR_MORE"
+ "ODDTURNINDEX_2"
+ "ODDTURNINDEX_20"
+ "ODDTURNINDEX_3"
+ "ODDTURNINDEX_30"
+ "ODDTURNINDEX_4"
+ "ODDTURNINDEX_40"
+ "ODDTURNINDEX_5"
+ "ODDTURNINDEX_50"
+ "ODDTURNINDEX_6"
+ "ODDTURNINDEX_60"
+ "ODDTURNINDEX_7"
+ "ODDTURNINDEX_70"
+ "ODDTURNINDEX_8"
+ "ODDTURNINDEX_80"
+ "ODDTURNINDEX_9"
+ "ODDTURNINDEX_90"
+ "ODDTURNINDEX_UNKNOWN"
+ "PLANNERMEDIATYPE_HEIC"
+ "PLANNERMEDIATYPE_JPG"
+ "PLANNERMEDIATYPE_PNG"
+ "PLANNERMEDIATYPE_SURFACE"
+ "PLANNERMEDIATYPE_UNKNOWN"
+ "RESPONSETOOLSCITATIONURLTYPE_ARTICLE"
+ "RESPONSETOOLSCITATIONURLTYPE_IMAGE"
+ "RESPONSETOOLSCITATIONURLTYPE_UNKNOWN"
+ "UEIATTACHMENTTYPE_CAMERA"
+ "UEIATTACHMENTTYPE_FILE"
+ "UEIATTACHMENTTYPE_LINK"
+ "UEIATTACHMENTTYPE_PHOTO"
+ "UEIATTACHMENTTYPE_UNKNOWN"
+ "UEILINKTYPE_CITATION"
+ "UEILINKTYPE_ENTITY_GLOSSARY"
+ "UEILINKTYPE_INLINE"
+ "UEILINKTYPE_UNKNOWN"
+ "UEIUISURFACE_ASSISTANT_ISLAND"
+ "UEIUISURFACE_FULL_APP_WINDOW"
+ "UEIUISURFACE_SINGLE_CHAT_APP_WINDOW"
+ "UEIUISURFACE_TRANSIENT_CANVAS"
+ "UEIUISURFACE_UNKNOWN"
+ "activeNavigation"
+ "appEntities"
+ "appNotification"
+ "appPartyType"
+ "attendees"
+ "author"
+ "buildVersion"
+ "calendar"
+ "calendarToolsResult"
+ "callMessages"
+ "callToolsResult"
+ "citations"
+ "citationsAttributed"
+ "colId"
+ "com.apple.aiml.siri.col.COLClientEvent"
+ "com.apple.aiml.siri.col.COLClientEvent.COLTrpFinalized"
+ "com.apple.aiml.siri.responsetools.RESPONSETOOLSClientEvent.RESPONSETOOLSCitationsAttributed"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIAsyncInvocationInfoCollected"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIBreadcrumbReturned"
+ "com.apple.aiml.siri.uei.ClientEvent.UEICanvasToAppExpanded"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIIslandToCanvasExpanded"
+ "com.apple.aiml.siri.uei.ClientEvent.UEILinkTapped"
+ "com.apple.aiml.siri.uei.ClientEvent.UEIResponseDisplayed"
+ "com.apple.aiml.siri.uei.ClientEvent.UEISourceListExpanded"
+ "contactRelationships"
+ "conversation"
+ "currentConversation"
+ "currentTime"
+ "entityKind"
+ "executionContext.ended.calendarToolsResult.results.attendees.entityKind"
+ "executionContext.ended.calendarToolsResult.results.calendar.entityKind"
+ "executionContext.ended.calendarToolsResult.results.organizers.entityKind"
+ "executionContext.ended.callToolsResult.results.call.entityKind"
+ "executionContext.ended.callToolsResult.results.participants.entityKind"
+ "executionContext.ended.generalResult.results.entityKind"
+ "executionContext.ended.getSystemInfoResult.activeNavigations.entityKind"
+ "executionContext.ended.getSystemInfoResult.currentTime.entityKind"
+ "executionContext.ended.getSystemInfoResult.focusedApp.entityKind"
+ "executionContext.ended.getSystemInfoResult.gazePoint.entityKind"
+ "executionContext.ended.getSystemInfoResult.liveEntities.entityKind"
+ "executionContext.ended.getSystemInfoResult.onscreenTexts.entityKind"
+ "executionContext.ended.getSystemInfoResult.openedApps.entityKind"
+ "executionContext.ended.getSystemInfoResult.salientEntity.entityKind"
+ "executionContext.ended.getSystemInfoResult.selectedEntities.entityKind"
+ "executionContext.ended.getSystemInfoResult.spanMatches.appEntities.entityKind"
+ "executionContext.ended.getSystemInfoResult.spanMatches.contactRelationships.entityKind"
+ "executionContext.ended.getSystemInfoResult.spanMatches.homeDeviceEntities.entityKind"
+ "executionContext.ended.getSystemInfoResult.visibleAlarms.entityKind"
+ "executionContext.ended.getSystemInfoResult.visibleEntities.entityKind"
+ "executionContext.ended.getSystemInfoResult.visibleTimers.entityKind"
+ "executionContext.ended.messageToolsResult.results.author.entityKind"
+ "executionContext.ended.messageToolsResult.results.message.entityKind"
+ "executionContext.ended.prepareCallMessageReadingListResult.results.callMessages.entityKind"
+ "executionContext.ended.prepareCallMessageReadingListResult.results.readableUnit.entityKind"
+ "executionContext.ended.prepareNotificationsResult.results.appNotification.entityKind"
+ "executionContext.ended.prepareNotificationsResult.results.threadNotificationEntities.notificationEntities.entityKind"
+ "executionContext.ended.prepareNotificationsResult.results.threadNotificationEntities.threadNotification.entityKind"
+ "executionContext.ended.prepareReadConversationResult.results.conversation.entityKind"
+ "executionContext.ended.prepareReadConversationResult.results.readableMessages.message.entityKind"
+ "executionContext.ended.prepareReadConversationResult.results.readableMessages.senders.entityKind"
+ "executionContext.ended.prepareReadMessagesListResult.currentConversation.conversation.entityKind"
+ "executionContext.ended.prepareReadMessagesListResult.currentConversation.participants.entityKind"
+ "executionContext.ended.prepareReadMessagesListResult.readableMessages.author.entityKind"
+ "executionContext.ended.prepareReadMessagesListResult.readableMessages.message.entityKind"
+ "executionContext.ended.prepareReadRemindersListResult.results.reminderList.entityKind"
+ "executionContext.ended.prepareReadRemindersListResult.results.reminders.entityKind"
+ "executionContext.ended.searchResult.results.globalEntities.entityKind"
+ "executionContext.ended.searchResult.results.localEntities.collection.entityKind"
+ "executionContext.ended.searchResult.results.localEntities.entities.entityKind"
+ "focusedApp"
+ "gazePoint"
+ "generalResult"
+ "getSystemInfoResult"
+ "globalEntities"
+ "goalCompletionConfidence"
+ "homeDeviceEntities"
+ "isLLMSiriAvailable"
+ "isPersonalEntity"
+ "islandExpansionIndicatorShown"
+ "linkType"
+ "liveEntities"
+ "localEntities"
+ "mediaHeightPixels"
+ "mediaSizeBytes"
+ "mediaWidthPixels"
+ "messageToolsResult"
+ "multimediaItems"
+ "notificationEntities"
+ "onscreenText"
+ "openedApps"
+ "organizers"
+ "participants"
+ "prepareCallMessageReadingListResult"
+ "prepareNotificationsResult"
+ "prepareReadConversationResult"
+ "prepareReadMessagesListResult"
+ "prepareReadRemindersListResult"
+ "readableMessages"
+ "readableUnit"
+ "reminderList"
+ "reminders"
+ "requestQueueTimeInMs"
+ "salientEntity"
+ "searchResult"
+ "selectedEntities"
+ "senders"
+ "siriAppOpenCount"
+ "sourceCount"
+ "storefront"
+ "successResult"
+ "threadNotification"
+ "threadNotificationEntities"
+ "timePerOutputTokenInMs"
+ "turnIndices"
+ "ueiAsyncInvocationInfoCollected"
+ "ueiBreadcrumbReturned"
+ "ueiCanvasToAppExpanded"
+ "ueiIslandToCanvasExpanded"
+ "ueiLinkTapped"
+ "ueiResponseDisplayed"
+ "ueiSourceListExpanded"
+ "uiSurface"
+ "urlToUi"
+ "urlType"
+ "userAttachmentTypes"
+ "validNoIdKindResult"
+ "visibleAlarms"
+ "visibleEntities"
+ "visibleTimers"
- "\xd1"
```
