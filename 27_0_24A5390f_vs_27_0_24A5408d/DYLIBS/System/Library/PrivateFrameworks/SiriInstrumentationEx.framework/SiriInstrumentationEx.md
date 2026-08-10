## SiriInstrumentationEx

> `/System/Library/PrivateFrameworks/SiriInstrumentationEx.framework/SiriInstrumentationEx`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`

```diff

-3600.80.1.0.0
-  __TEXT.__text: 0x21930c
-  __TEXT.__objc_methlist: 0x19064
-  __TEXT.__const: 0x575c4
+3600.85.1.0.0
+  __TEXT.__text: 0x24095c
+  __TEXT.__objc_methlist: 0x1bc7c
+  __TEXT.__const: 0x588a4
   __TEXT.__constg_swiftt: 0xc
-  __TEXT.__swift5_proto: 0x334c
+  __TEXT.__swift5_proto: 0x33f0
   __TEXT.__swift5_typeref: 0xa
-  __TEXT.__cstring: 0x5efb
-  __TEXT.__unwind_info: 0x99d0
+  __TEXT.__cstring: 0x665e
+  __TEXT.__unwind_info: 0xa398
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbb0
-  __DATA_CONST.__objc_classlist: 0xd18
+  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__objc_classlist: 0xe60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf30
-  __DATA_CONST.__objc_superrefs: 0xd18
-  __DATA_CONST.__got: 0x13c8
-  __AUTH_CONST.__cfstring: 0x6800
-  __AUTH_CONST.__objc_const: 0x25d90
-  __AUTH_CONST.__auth_got: 0x258
-  __AUTH.__objc_data: 0x82f0
-  __DATA.__objc_ivar: 0x19bc
-  __DATA.__data: 0xa88
-  __DATA.__bss: 0x66980
+  __DATA_CONST.__objc_selrefs: 0x1cc68
+  __DATA_CONST.__objc_superrefs: 0xe60
+  __DATA_CONST.__got: 0x14c0
+  __AUTH_CONST.__cfstring: 0x7440
+  __AUTH_CONST.__objc_const: 0x29600
+  __AUTH_CONST.__auth_got: 0x250
+  __AUTH.__objc_data: 0x8fc0
+  __DATA.__objc_ivar: 0x1c10
+  __DATA.__data: 0xaf8
+  __DATA.__bss: 0x67e00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 15245
-  Symbols:   26370
-  CStrings:  836
+  Functions: 16254
+  Symbols:   27920
+  CStrings:  935
 
Symbols:
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
+ OBJC_IVAR_$_CHSchemaCHGoalCompletionInferenceMetadata._goalCompletionConfidence
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._eventMetadata
+ OBJC_IVAR_$_COLSchemaCOLClientEvent._trpFinalized
+ OBJC_IVAR_$_COLSchemaCOLClientEventMetadata._colId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._finalizedTrpId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._has
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._ifUserTurnId
+ OBJC_IVAR_$_COLSchemaCOLTrpFinalized._mitigationDecision
+ OBJC_IVAR_$_GAASchemaGAARequestStarted._agentActionId
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantLLMSiriTuples._turnIndices
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._has
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaHeightPixels
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaSizeBytes
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaType
+ OBJC_IVAR_$_PLANNERSchemaPLANNERMediaItemInfo._mediaWidthPixels
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._appNotification
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._threadNotificationEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._attendees
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._calendar
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._organizers
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._call
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._participants
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._conversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._participants
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._collection
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._entities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._entityId
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._entityKind
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCalendarToolsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionCallToolsResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._calendarToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._callToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._generalResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._getSystemInfoResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._messageToolsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareCallMessageReadingListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareNotificationsResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadConversationResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadMessagesListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._prepareReadRemindersListResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._searchResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._successResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._validNoIdKindResult
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGeneralResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._activeNavigations
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._currentTime
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._focusedApp
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._gazePoint
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
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult._readableMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadRemindersListResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSearchResult._results
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult._exists
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionSuccessResult._has
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult._exists
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionValidNoIdKindResult._has
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._author
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._message
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._callMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._readableUnit
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._conversation
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._readableMessages
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._message
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._senders
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._reminderList
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._reminders
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup._globalEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSearchResultGroup._localEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._appEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._contactRelationships
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSSpanMatches._homeDeviceEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._notificationEntities
+ OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._threadNotification
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._has
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._urlToUi
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._urlType
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._citations
+ OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._storefront
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
+ _OBJC_IVAR_$_COLSchemaCOLClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_COLSchemaCOLClientEvent._hasTrpFinalized
+ _OBJC_IVAR_$_COLSchemaCOLClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_COLSchemaCOLClientEventMetadata._hasColId
+ _OBJC_IVAR_$_COLSchemaCOLTrpFinalized._hasFinalizedTrpId
+ _OBJC_IVAR_$_COLSchemaCOLTrpFinalized._hasIfUserTurnId
+ _OBJC_IVAR_$_GAASchemaGAARequestStarted._hasAgentActionId
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSAppNotifications._hasAppNotification
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCalendarEventRef._hasCalendar
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSCallEntityRef._hasCall
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSConversationRef._hasConversation
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityCollection._hasCollection
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._hasEntityId
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSEntityRef._hasEntityKind
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasCalendarToolsResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasCallToolsResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasGeneralResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasGetSystemInfoResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasMessageToolsResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareCallMessageReadingListResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareNotificationsResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadConversationResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadMessagesListResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasPrepareReadRemindersListResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasSearchResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasSuccessResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._hasValidNoIdKindResult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionEnded._whichPlannertoolsexecutionresult
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasCurrentTime
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasFocusedApp
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasGazePoint
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasSalientEntity
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionGetSystemInfoResult._hasSpanMatches
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSExecutionPrepareReadMessagesListResult._hasCurrentConversation
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._hasAuthor
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSMessageEntityRef._hasMessage
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableCallMessage._hasReadableUnit
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableConversation._hasConversation
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableMessage._hasMessage
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSReadableRemindersPerList._hasReminderList
+ _OBJC_IVAR_$_PLANNERTOOLSSchemaPLANNERTOOLSThreadNotifications._hasThreadNotification
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitation._hasUrlToUi
+ _OBJC_IVAR_$_RESPONSETOOLSSchemaRESPONSETOOLSCitationsAttributed._hasStorefront
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
+ __OBJC_$_INSTANCE_METHODS_COLSchemaCOLClientEvent(InstrumentationAdditions)
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
+ __OBJC_$_PROP_LIST_COLSchemaCOLClientEvent
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
+ _objc_msgSend$addEntities:
+ _objc_msgSend$addGlobalEntities:
+ _objc_msgSend$addHomeDeviceEntities:
+ _objc_msgSend$addLiveEntities:
+ _objc_msgSend$addLocalEntities:
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
+ _objc_msgSend$clearEntities
+ _objc_msgSend$clearGlobalEntities
+ _objc_msgSend$clearHomeDeviceEntities
+ _objc_msgSend$clearLiveEntities
+ _objc_msgSend$clearLocalEntities
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
+ _objc_msgSend$clearVisibleAlarms
+ _objc_msgSend$clearVisibleEntities
+ _objc_msgSend$clearVisibleTimers
+ _objc_msgSend$colId
+ _objc_msgSend$contactRelationships
+ _objc_msgSend$conversation
+ _objc_msgSend$currentConversation
+ _objc_msgSend$currentTime
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
+ _objc_msgSend$setActiveNavigations:
+ _objc_msgSend$setAppEntities:
+ _objc_msgSend$setAppNotification:
+ _objc_msgSend$setAppPartyType:
+ _objc_msgSend$setAttendees:
+ _objc_msgSend$setAuthor:
+ _objc_msgSend$setBuildVersion:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setCalendarToolsResult:
+ _objc_msgSend$setCallMessages:
+ _objc_msgSend$setCallToolsResult:
+ _objc_msgSend$setCitations:
+ _objc_msgSend$setCitationsAttributed:
+ _objc_msgSend$setColId:
+ _objc_msgSend$setContactRelationships:
+ _objc_msgSend$setConversation:
+ _objc_msgSend$setCurrentConversation:
+ _objc_msgSend$setCurrentTime:
+ _objc_msgSend$setEntityKind:
+ _objc_msgSend$setFocusedApp:
+ _objc_msgSend$setGazePoint:
+ _objc_msgSend$setGeneralResult:
+ _objc_msgSend$setGetSystemInfoResult:
+ _objc_msgSend$setGlobalEntities:
+ _objc_msgSend$setGoalCompletionConfidence:
+ _objc_msgSend$setHomeDeviceEntities:
+ _objc_msgSend$setIsLLMSiriAvailable:
+ _objc_msgSend$setIsPersonalEntity:
+ _objc_msgSend$setIslandExpansionIndicatorShown:
+ _objc_msgSend$setLinkType:
+ _objc_msgSend$setLiveEntities:
+ _objc_msgSend$setLocalEntities:
+ _objc_msgSend$setMediaHeightPixels:
+ _objc_msgSend$setMediaSizeBytes:
+ _objc_msgSend$setMediaWidthPixels:
+ _objc_msgSend$setMessageToolsResult:
+ _objc_msgSend$setMultimediaItems:
+ _objc_msgSend$setNotificationEntities:
+ _objc_msgSend$setOnscreenTexts:
+ _objc_msgSend$setOpenedApps:
+ _objc_msgSend$setOrganizers:
+ _objc_msgSend$setParticipants:
+ _objc_msgSend$setPrepareCallMessageReadingListResult:
+ _objc_msgSend$setPrepareNotificationsResult:
+ _objc_msgSend$setPrepareReadConversationResult:
+ _objc_msgSend$setPrepareReadMessagesListResult:
+ _objc_msgSend$setPrepareReadRemindersListResult:
+ _objc_msgSend$setReadableMessages:
+ _objc_msgSend$setReadableUnit:
+ _objc_msgSend$setReminderList:
+ _objc_msgSend$setReminders:
+ _objc_msgSend$setRequestQueueTimeInMs:
+ _objc_msgSend$setSalientEntity:
+ _objc_msgSend$setSearchResult:
+ _objc_msgSend$setSelectedEntities:
+ _objc_msgSend$setSenders:
+ _objc_msgSend$setSiriAppOpenCount:
+ _objc_msgSend$setSourceCount:
+ _objc_msgSend$setStorefront:
+ _objc_msgSend$setSuccessResult:
+ _objc_msgSend$setThreadNotification:
+ _objc_msgSend$setThreadNotificationEntities:
+ _objc_msgSend$setTimePerOutputTokenInMs:
+ _objc_msgSend$setTurnIndices:
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
+ _objc_msgSend$setUserAttachmentTypes:
+ _objc_msgSend$setValidNoIdKindResult:
+ _objc_msgSend$setVisibleAlarms:
+ _objc_msgSend$setVisibleEntities:
+ _objc_msgSend$setVisibleTimers:
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
- _objc_retain_x27
CStrings:
+ "\r"
+ "CHGOALCOMPLETIONCONFIDENCE_HIGH"
+ "CHGOALCOMPLETIONCONFIDENCE_LOW"
+ "CHGOALCOMPLETIONCONFIDENCE_MEDIUM"
+ "CHGOALCOMPLETIONCONFIDENCE_UNKNOWN"
+ "COLCONTEXTUALMITIGATIONDECISION_MITIGATED"
+ "COLCONTEXTUALMITIGATIONDECISION_SELECTED"
+ "COLCONTEXTUALMITIGATIONDECISION_UNKNOWN"
+ "PLANNERMEDIATYPE_HEIC"
+ "PLANNERMEDIATYPE_JPG"
+ "PLANNERMEDIATYPE_PNG"
+ "PLANNERMEDIATYPE_SURFACE"
+ "PLANNERMEDIATYPE_UNKNOWN"
+ "RESPONSETOOLSCITATIONURLTYPE_ARTICLE"
+ "RESPONSETOOLSCITATIONURLTYPE_IMAGE"
+ "RESPONSETOOLSCITATIONURLTYPE_UNKNOWN"
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
+ "attendees"
+ "author"
+ "calendar"
+ "calendarToolsResult"
+ "call"
+ "callMessages"
+ "callToolsResult"
+ "citations"
+ "colId"
+ "collection"
+ "com.apple.aiml.siri.col.COLClientEvent"
+ "com.apple.aiml.siri.col.COLClientEvent.COLTrpFinalized"
+ "contactRelationships"
+ "conversation"
+ "currentConversation"
+ "currentTime"
+ "entities"
+ "entityKind"
+ "finalizedTrpId"
+ "focusedApp"
+ "gazePoint"
+ "generalResult"
+ "getSystemInfoResult"
+ "globalEntities"
+ "goalCompletionConfidence"
+ "homeDeviceEntities"
+ "isNewConversation"
+ "isPersonalEntity"
+ "linkType"
+ "liveEntities"
+ "localEntities"
+ "mediaHeightPixels"
+ "mediaSizeBytes"
+ "mediaType"
+ "mediaWidthPixels"
+ "message"
+ "messageToolsResult"
+ "mitigationDecision"
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
+ "salientEntity"
+ "searchResult"
+ "selectedEntities"
+ "senders"
+ "sourceCount"
+ "spanMatches"
+ "storefront"
+ "successResult"
+ "threadNotification"
+ "threadNotificationEntities"
+ "trpFinalized"
+ "turnIndices"
+ "uiSurface"
+ "urlToUi"
+ "urlType"
+ "validNoIdKindResult"
+ "visibleAlarms"
+ "visibleEntities"
+ "visibleTimers"
```
