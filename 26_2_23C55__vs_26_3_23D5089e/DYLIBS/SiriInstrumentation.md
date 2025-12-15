## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3510.5.1.0.0
-  __TEXT.__text: 0xa29358
-  __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xd48f4
-  __TEXT.__const: 0x12290
-  __TEXT.__cstring: 0x7aaee
-  __TEXT.__swift5_typeref: 0x18e8
+3515.3.1.0.0
+  __TEXT.__text: 0xa53c40
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_methlist: 0xd52fc
+  __TEXT.__const: 0x12790
+  __TEXT.__constg_swiftt: 0x6580
+  __TEXT.__swift5_typeref: 0x190c
+  __TEXT.__swift5_builtin: 0x3ae8
   __TEXT.__swift5_reflstr: 0x212
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__constg_swiftt: 0x64e0
-  __TEXT.__swift5_builtin: 0x3a84
-  __TEXT.__swift5_proto: 0xf28
-  __TEXT.__swift5_types: 0xc04
+  __TEXT.__swift5_proto: 0xf44
+  __TEXT.__swift5_types: 0xc18
+  __TEXT.__cstring: 0x7b9c0
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2a730
+  __TEXT.__unwind_info: 0x2afb0
   __TEXT.__eh_frame: 0x24d8
-  __TEXT.__objc_classname: 0x15cbd
-  __TEXT.__objc_methname: 0x126607
-  __TEXT.__objc_methtype: 0x28fbb
-  __TEXT.__objc_stubs: 0x6a880
-  __DATA_CONST.__got: 0x4d58
-  __DATA_CONST.__const: 0x35280
-  __DATA_CONST.__objc_classlist: 0x4c38
+  __TEXT.__objc_classname: 0x15dbf
+  __TEXT.__objc_methname: 0x127715
+  __TEXT.__objc_methtype: 0x291e1
+  __TEXT.__objc_stubs: 0x6ad80
+  __DATA_CONST.__got: 0x4d90
+  __DATA_CONST.__const: 0x35870
+  __DATA_CONST.__objc_classlist: 0x4c70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37280
+  __DATA_CONST.__objc_selrefs: 0x37510
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7698
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x21fe8
-  __AUTH_CONST.__cfstring: 0x6a4a0
-  __AUTH_CONST.__objc_const: 0x11fc10
+  __DATA_CONST.__objc_superrefs: 0x7700
+  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__const: 0x1c080
+  __AUTH_CONST.__cfstring: 0x6ae80
+  __AUTH_CONST.__objc_const: 0x120930
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11940
-  __DATA.__objc_ivar: 0xe590
-  __DATA.__data: 0x2090
-  __DATA.__bss: 0x18f00
+  __AUTH.__objc_data: 0x11b70
+  __DATA.__objc_ivar: 0xe638
+  __DATA.__data: 0x2868
+  __DATA.__bss: 0x19180
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1e340
   __DATA_DIRTY.__data: 0x568

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1D072507-A12F-36A7-B035-900624C3C91B
-  Functions: 76975
-  Symbols:   191369
-  CStrings:  78646
+  UUID: F5837B18-B9B2-3530-B943-681C4958BB32
+  Functions: 77689
+  Symbols:   191931
+  CStrings:  78956
 
Symbols:
+ +[CHSchemaCHClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[CHSchemaCHClientEvent .cxx_destruct]
+ -[CHSchemaCHClientEvent conversationQualityInferenceGenerated]
+ -[CHSchemaCHClientEvent deleteConversationQualityInferenceGenerated]
+ -[CHSchemaCHClientEvent deleteEventMetadata]
+ -[CHSchemaCHClientEvent deleteUserAlignmentInferenceGenerated]
+ -[CHSchemaCHClientEvent dictionaryRepresentation]
+ -[CHSchemaCHClientEvent eventMetadata]
+ -[CHSchemaCHClientEvent hasConversationQualityInferenceGenerated]
+ -[CHSchemaCHClientEvent hasEventMetadata]
+ -[CHSchemaCHClientEvent hasUserAlignmentInferenceGenerated]
+ -[CHSchemaCHClientEvent hash]
+ -[CHSchemaCHClientEvent initWithDictionary:]
+ -[CHSchemaCHClientEvent initWithJSON:]
+ -[CHSchemaCHClientEvent isEqual:]
+ -[CHSchemaCHClientEvent jsonData]
+ -[CHSchemaCHClientEvent qualifiedMessageName]
+ -[CHSchemaCHClientEvent readFrom:]
+ -[CHSchemaCHClientEvent setConversationQualityInferenceGenerated:]
+ -[CHSchemaCHClientEvent setEventMetadata:]
+ -[CHSchemaCHClientEvent setHasConversationQualityInferenceGenerated:]
+ -[CHSchemaCHClientEvent setHasEventMetadata:]
+ -[CHSchemaCHClientEvent setHasUserAlignmentInferenceGenerated:]
+ -[CHSchemaCHClientEvent setUserAlignmentInferenceGenerated:]
+ -[CHSchemaCHClientEvent userAlignmentInferenceGenerated]
+ -[CHSchemaCHClientEvent whichEvent_Type]
+ -[CHSchemaCHClientEvent writeTo:]
+ -[CHSchemaCHClientEvent(InnerEventContainer) innerEvent]
+ -[CHSchemaCHClientEvent(InnerEventContainer) whichInnerEventType]
+ -[CHSchemaCHClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[CHSchemaCHClientEvent(IsolationLevel) clockIsolationLevel]
+ -[CHSchemaCHClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHClientEventMetadata .cxx_destruct]
+ -[CHSchemaCHClientEventMetadata chId]
+ -[CHSchemaCHClientEventMetadata deleteChId]
+ -[CHSchemaCHClientEventMetadata deleteRequestId]
+ -[CHSchemaCHClientEventMetadata deleteSessionId]
+ -[CHSchemaCHClientEventMetadata dictionaryRepresentation]
+ -[CHSchemaCHClientEventMetadata hasChId]
+ -[CHSchemaCHClientEventMetadata hasRequestId]
+ -[CHSchemaCHClientEventMetadata hasSessionId]
+ -[CHSchemaCHClientEventMetadata hash]
+ -[CHSchemaCHClientEventMetadata initWithDictionary:]
+ -[CHSchemaCHClientEventMetadata initWithJSON:]
+ -[CHSchemaCHClientEventMetadata isEqual:]
+ -[CHSchemaCHClientEventMetadata jsonData]
+ -[CHSchemaCHClientEventMetadata readFrom:]
+ -[CHSchemaCHClientEventMetadata requestId]
+ -[CHSchemaCHClientEventMetadata sessionId]
+ -[CHSchemaCHClientEventMetadata setChId:]
+ -[CHSchemaCHClientEventMetadata setHasChId:]
+ -[CHSchemaCHClientEventMetadata setHasRequestId:]
+ -[CHSchemaCHClientEventMetadata setHasSessionId:]
+ -[CHSchemaCHClientEventMetadata setRequestId:]
+ -[CHSchemaCHClientEventMetadata setSessionId:]
+ -[CHSchemaCHClientEventMetadata writeTo:]
+ -[CHSchemaCHClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHConversationQualityInferenceGenerated .cxx_destruct]
+ -[CHSchemaCHConversationQualityInferenceGenerated conversationQualityInferenceMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated deleteConversationQualityInferenceMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated deleteEvaluatorMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated dictionaryRepresentation]
+ -[CHSchemaCHConversationQualityInferenceGenerated evaluatorMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated hasConversationQualityInferenceMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated hasEvaluatorMetadata]
+ -[CHSchemaCHConversationQualityInferenceGenerated hash]
+ -[CHSchemaCHConversationQualityInferenceGenerated initWithDictionary:]
+ -[CHSchemaCHConversationQualityInferenceGenerated initWithJSON:]
+ -[CHSchemaCHConversationQualityInferenceGenerated isEqual:]
+ -[CHSchemaCHConversationQualityInferenceGenerated jsonData]
+ -[CHSchemaCHConversationQualityInferenceGenerated readFrom:]
+ -[CHSchemaCHConversationQualityInferenceGenerated setConversationQualityInferenceMetadata:]
+ -[CHSchemaCHConversationQualityInferenceGenerated setEvaluatorMetadata:]
+ -[CHSchemaCHConversationQualityInferenceGenerated setHasConversationQualityInferenceMetadata:]
+ -[CHSchemaCHConversationQualityInferenceGenerated setHasEvaluatorMetadata:]
+ -[CHSchemaCHConversationQualityInferenceGenerated writeTo:]
+ -[CHSchemaCHConversationQualityInferenceGenerated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHConversationQualityInferenceGenerated(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHConversationQualityInferenceMetadata .cxx_destruct]
+ -[CHSchemaCHConversationQualityInferenceMetadata addIssueCategory:]
+ -[CHSchemaCHConversationQualityInferenceMetadata clearIssueCategory]
+ -[CHSchemaCHConversationQualityInferenceMetadata conversationQualityComplexity]
+ -[CHSchemaCHConversationQualityInferenceMetadata deleteConversationQualityComplexity]
+ -[CHSchemaCHConversationQualityInferenceMetadata deleteIssueCategory]
+ -[CHSchemaCHConversationQualityInferenceMetadata deleteIssueDetected]
+ -[CHSchemaCHConversationQualityInferenceMetadata deleteRationale]
+ -[CHSchemaCHConversationQualityInferenceMetadata dictionaryRepresentation]
+ -[CHSchemaCHConversationQualityInferenceMetadata hasConversationQualityComplexity]
+ -[CHSchemaCHConversationQualityInferenceMetadata hasIssueDetected]
+ -[CHSchemaCHConversationQualityInferenceMetadata hasRationale]
+ -[CHSchemaCHConversationQualityInferenceMetadata hash]
+ -[CHSchemaCHConversationQualityInferenceMetadata initWithDictionary:]
+ -[CHSchemaCHConversationQualityInferenceMetadata initWithJSON:]
+ -[CHSchemaCHConversationQualityInferenceMetadata isEqual:]
+ -[CHSchemaCHConversationQualityInferenceMetadata issueCategoryAtIndex:]
+ -[CHSchemaCHConversationQualityInferenceMetadata issueCategoryCount]
+ -[CHSchemaCHConversationQualityInferenceMetadata issueCategorys]
+ -[CHSchemaCHConversationQualityInferenceMetadata issueDetected]
+ -[CHSchemaCHConversationQualityInferenceMetadata jsonData]
+ -[CHSchemaCHConversationQualityInferenceMetadata rationale]
+ -[CHSchemaCHConversationQualityInferenceMetadata readFrom:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setConversationQualityComplexity:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setHasConversationQualityComplexity:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setHasIssueDetected:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setHasRationale:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setIssueCategorys:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setIssueDetected:]
+ -[CHSchemaCHConversationQualityInferenceMetadata setRationale:]
+ -[CHSchemaCHConversationQualityInferenceMetadata writeTo:]
+ -[CHSchemaCHConversationQualityInferenceMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHConversationQualityInferenceMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHEvaluatorMetadata .cxx_destruct]
+ -[CHSchemaCHEvaluatorMetadata deleteDynamicEvaluatorTaskName]
+ -[CHSchemaCHEvaluatorMetadata deletePromptIdentifier]
+ -[CHSchemaCHEvaluatorMetadata deletePromptVersion]
+ -[CHSchemaCHEvaluatorMetadata dictionaryRepresentation]
+ -[CHSchemaCHEvaluatorMetadata dynamicEvaluatorTaskName]
+ -[CHSchemaCHEvaluatorMetadata hasDynamicEvaluatorTaskName]
+ -[CHSchemaCHEvaluatorMetadata hasPromptIdentifier]
+ -[CHSchemaCHEvaluatorMetadata hasPromptVersion]
+ -[CHSchemaCHEvaluatorMetadata hash]
+ -[CHSchemaCHEvaluatorMetadata initWithDictionary:]
+ -[CHSchemaCHEvaluatorMetadata initWithJSON:]
+ -[CHSchemaCHEvaluatorMetadata isEqual:]
+ -[CHSchemaCHEvaluatorMetadata jsonData]
+ -[CHSchemaCHEvaluatorMetadata promptIdentifier]
+ -[CHSchemaCHEvaluatorMetadata promptVersion]
+ -[CHSchemaCHEvaluatorMetadata readFrom:]
+ -[CHSchemaCHEvaluatorMetadata setDynamicEvaluatorTaskName:]
+ -[CHSchemaCHEvaluatorMetadata setHasDynamicEvaluatorTaskName:]
+ -[CHSchemaCHEvaluatorMetadata setHasPromptIdentifier:]
+ -[CHSchemaCHEvaluatorMetadata setHasPromptVersion:]
+ -[CHSchemaCHEvaluatorMetadata setPromptIdentifier:]
+ -[CHSchemaCHEvaluatorMetadata setPromptVersion:]
+ -[CHSchemaCHEvaluatorMetadata writeTo:]
+ -[CHSchemaCHEvaluatorMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHUserAlignmentInferenceGenerated .cxx_destruct]
+ -[CHSchemaCHUserAlignmentInferenceGenerated deleteEvaluatorMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated deleteUserAlignmentInferenceMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated dictionaryRepresentation]
+ -[CHSchemaCHUserAlignmentInferenceGenerated evaluatorMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated hasEvaluatorMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated hasUserAlignmentInferenceMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated hash]
+ -[CHSchemaCHUserAlignmentInferenceGenerated initWithDictionary:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated initWithJSON:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated isEqual:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated jsonData]
+ -[CHSchemaCHUserAlignmentInferenceGenerated readFrom:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated setEvaluatorMetadata:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated setHasEvaluatorMetadata:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated setHasUserAlignmentInferenceMetadata:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated setUserAlignmentInferenceMetadata:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated userAlignmentInferenceMetadata]
+ -[CHSchemaCHUserAlignmentInferenceGenerated writeTo:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHUserAlignmentInferenceGenerated(SensitiveConditions) suppressMessageUnderConditions]
+ -[CHSchemaCHUserAlignmentInferenceMetadata .cxx_destruct]
+ -[CHSchemaCHUserAlignmentInferenceMetadata addIssueCategory:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata clearIssueCategory]
+ -[CHSchemaCHUserAlignmentInferenceMetadata confidenceScore]
+ -[CHSchemaCHUserAlignmentInferenceMetadata deleteConfidenceScore]
+ -[CHSchemaCHUserAlignmentInferenceMetadata deleteIssueCategory]
+ -[CHSchemaCHUserAlignmentInferenceMetadata deleteRationale]
+ -[CHSchemaCHUserAlignmentInferenceMetadata deleteUserAlignmentResult]
+ -[CHSchemaCHUserAlignmentInferenceMetadata dictionaryRepresentation]
+ -[CHSchemaCHUserAlignmentInferenceMetadata hasConfidenceScore]
+ -[CHSchemaCHUserAlignmentInferenceMetadata hasRationale]
+ -[CHSchemaCHUserAlignmentInferenceMetadata hasUserAlignmentResult]
+ -[CHSchemaCHUserAlignmentInferenceMetadata hash]
+ -[CHSchemaCHUserAlignmentInferenceMetadata initWithDictionary:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata initWithJSON:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata isEqual:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata issueCategoryAtIndex:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata issueCategoryCount]
+ -[CHSchemaCHUserAlignmentInferenceMetadata issueCategorys]
+ -[CHSchemaCHUserAlignmentInferenceMetadata jsonData]
+ -[CHSchemaCHUserAlignmentInferenceMetadata rationale]
+ -[CHSchemaCHUserAlignmentInferenceMetadata readFrom:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setConfidenceScore:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setHasConfidenceScore:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setHasRationale:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setHasUserAlignmentResult:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setIssueCategorys:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setRationale:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata setUserAlignmentResult:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata userAlignmentResult]
+ -[CHSchemaCHUserAlignmentInferenceMetadata writeTo:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[CHSchemaCHUserAlignmentInferenceMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions deleteDurationFromBootToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions deleteDurationFromClassCUnlockToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions deleteDurationFromSoftwareUpdateToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions durationFromBootToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions durationFromClassCUnlockToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions durationFromSoftwareUpdateToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions hasDurationFromBootToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions hasDurationFromClassCUnlockToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions hasDurationFromSoftwareUpdateToFirstRequestSeconds]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setDurationFromBootToFirstRequestSeconds:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setDurationFromClassCUnlockToFirstRequestSeconds:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setDurationFromSoftwareUpdateToFirstRequestSeconds:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setHasDurationFromBootToFirstRequestSeconds:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setHasDurationFromClassCUnlockToFirstRequestSeconds:]
+ -[ODDSiriSchemaODDRequestsWithoutAssetsDimensions setHasDurationFromSoftwareUpdateToFirstRequestSeconds:]
+ OBJC_IVAR_$_CHSchemaCHClientEvent._conversationQualityInferenceGenerated
+ OBJC_IVAR_$_CHSchemaCHClientEvent._eventMetadata
+ OBJC_IVAR_$_CHSchemaCHClientEvent._userAlignmentInferenceGenerated
+ OBJC_IVAR_$_CHSchemaCHClientEventMetadata._chId
+ OBJC_IVAR_$_CHSchemaCHClientEventMetadata._requestId
+ OBJC_IVAR_$_CHSchemaCHClientEventMetadata._sessionId
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceGenerated._conversationQualityInferenceMetadata
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceGenerated._evaluatorMetadata
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._conversationQualityComplexity
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._has
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._issueCategorys
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._issueDetected
+ OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._rationale
+ OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._dynamicEvaluatorTaskName
+ OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._promptIdentifier
+ OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._promptVersion
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceGenerated._evaluatorMetadata
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceGenerated._userAlignmentInferenceMetadata
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._confidenceScore
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._has
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._issueCategorys
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._rationale
+ OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._userAlignmentResult
+ OBJC_IVAR_$_ODDSiriSchemaODDRequestsWithoutAssetsDimensions._durationFromBootToFirstRequestSeconds
+ OBJC_IVAR_$_ODDSiriSchemaODDRequestsWithoutAssetsDimensions._durationFromClassCUnlockToFirstRequestSeconds
+ OBJC_IVAR_$_ODDSiriSchemaODDRequestsWithoutAssetsDimensions._durationFromSoftwareUpdateToFirstRequestSeconds
+ _CHSchemaCHClientEventMetadataReadFrom
+ _CHSchemaCHClientEventReadFrom
+ _CHSchemaCHConversationQualityInferenceGeneratedReadFrom
+ _CHSchemaCHConversationQualityInferenceMetadataReadFrom
+ _CHSchemaCHEvaluatorMetadataReadFrom
+ _CHSchemaCHUserAlignmentInferenceGeneratedReadFrom
+ _CHSchemaCHUserAlignmentInferenceMetadataReadFrom
+ _OBJC_CLASS_$_CHSchemaCHClientEvent
+ _OBJC_CLASS_$_CHSchemaCHClientEventMetadata
+ _OBJC_CLASS_$_CHSchemaCHConversationQualityInferenceGenerated
+ _OBJC_CLASS_$_CHSchemaCHConversationQualityInferenceMetadata
+ _OBJC_CLASS_$_CHSchemaCHEvaluatorMetadata
+ _OBJC_CLASS_$_CHSchemaCHUserAlignmentInferenceGenerated
+ _OBJC_CLASS_$_CHSchemaCHUserAlignmentInferenceMetadata
+ _OBJC_IVAR_$_CHSchemaCHClientEvent._hasConversationQualityInferenceGenerated
+ _OBJC_IVAR_$_CHSchemaCHClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_CHSchemaCHClientEvent._hasUserAlignmentInferenceGenerated
+ _OBJC_IVAR_$_CHSchemaCHClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_CHSchemaCHClientEventMetadata._hasChId
+ _OBJC_IVAR_$_CHSchemaCHClientEventMetadata._hasRequestId
+ _OBJC_IVAR_$_CHSchemaCHClientEventMetadata._hasSessionId
+ _OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceGenerated._hasConversationQualityInferenceMetadata
+ _OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceGenerated._hasEvaluatorMetadata
+ _OBJC_IVAR_$_CHSchemaCHConversationQualityInferenceMetadata._hasRationale
+ _OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._hasDynamicEvaluatorTaskName
+ _OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._hasPromptIdentifier
+ _OBJC_IVAR_$_CHSchemaCHEvaluatorMetadata._hasPromptVersion
+ _OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceGenerated._hasEvaluatorMetadata
+ _OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceGenerated._hasUserAlignmentInferenceMetadata
+ _OBJC_IVAR_$_CHSchemaCHUserAlignmentInferenceMetadata._hasRationale
+ _OBJC_METACLASS_$_CHSchemaCHClientEvent
+ _OBJC_METACLASS_$_CHSchemaCHClientEventMetadata
+ _OBJC_METACLASS_$_CHSchemaCHConversationQualityInferenceGenerated
+ _OBJC_METACLASS_$_CHSchemaCHConversationQualityInferenceMetadata
+ _OBJC_METACLASS_$_CHSchemaCHEvaluatorMetadata
+ _OBJC_METACLASS_$_CHSchemaCHUserAlignmentInferenceGenerated
+ _OBJC_METACLASS_$_CHSchemaCHUserAlignmentInferenceMetadata
+ __OBJC_$_CLASS_METHODS_CHSchemaCHClientEvent(InstrumentationAdditions|SensitiveConditions|InnerEventContainer|IsolationLevel)
+ __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(AnyEvent|Component|IsolationLevel)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHClientEvent(InstrumentationAdditions|SensitiveConditions|InnerEventContainer|IsolationLevel)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHConversationQualityInferenceGenerated(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHConversationQualityInferenceMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHEvaluatorMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHUserAlignmentInferenceGenerated(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_CHSchemaCHUserAlignmentInferenceMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Tailing|Factory|Introspection|Mapping|SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(Tailing|SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(Tailing|SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaOrderedAnyEvent(Introspection|InstrumentationAdditions|SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(AnyEvent|Component|IsolationLevel)
+ __OBJC_$_INSTANCE_METHODS_SISchemaUUID(Extensions|Tailing|SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHConversationQualityInferenceGenerated
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHConversationQualityInferenceMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHEvaluatorMetadata
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHUserAlignmentInferenceGenerated
+ __OBJC_$_INSTANCE_VARIABLES_CHSchemaCHUserAlignmentInferenceMetadata
+ __OBJC_$_PROP_LIST_CHSchemaCHClientEventMetadata
+ __OBJC_$_PROP_LIST_CHSchemaCHConversationQualityInferenceGenerated
+ __OBJC_$_PROP_LIST_CHSchemaCHConversationQualityInferenceMetadata
+ __OBJC_$_PROP_LIST_CHSchemaCHEvaluatorMetadata
+ __OBJC_$_PROP_LIST_CHSchemaCHUserAlignmentInferenceGenerated
+ __OBJC_$_PROP_LIST_CHSchemaCHUserAlignmentInferenceMetadata
+ __OBJC_CLASS_PROTOCOLS_$_CHSchemaCHClientEvent(InstrumentationAdditions|SensitiveConditions|InnerEventContainer|IsolationLevel)
+ __OBJC_CLASS_RO_$_CHSchemaCHClientEvent
+ __OBJC_CLASS_RO_$_CHSchemaCHClientEventMetadata
+ __OBJC_CLASS_RO_$_CHSchemaCHConversationQualityInferenceGenerated
+ __OBJC_CLASS_RO_$_CHSchemaCHConversationQualityInferenceMetadata
+ __OBJC_CLASS_RO_$_CHSchemaCHEvaluatorMetadata
+ __OBJC_CLASS_RO_$_CHSchemaCHUserAlignmentInferenceGenerated
+ __OBJC_CLASS_RO_$_CHSchemaCHUserAlignmentInferenceMetadata
+ __OBJC_METACLASS_RO_$_CHSchemaCHClientEvent
+ __OBJC_METACLASS_RO_$_CHSchemaCHClientEventMetadata
+ __OBJC_METACLASS_RO_$_CHSchemaCHConversationQualityInferenceGenerated
+ __OBJC_METACLASS_RO_$_CHSchemaCHConversationQualityInferenceMetadata
+ __OBJC_METACLASS_RO_$_CHSchemaCHEvaluatorMetadata
+ __OBJC_METACLASS_RO_$_CHSchemaCHUserAlignmentInferenceGenerated
+ __OBJC_METACLASS_RO_$_CHSchemaCHUserAlignmentInferenceMetadata
+ _objc_msgSend$addIssueCategory:
+ _objc_msgSend$chId
+ _objc_msgSend$clearIssueCategory
+ _objc_msgSend$conversationQualityComplexity
+ _objc_msgSend$conversationQualityInferenceGenerated
+ _objc_msgSend$conversationQualityInferenceMetadata
+ _objc_msgSend$deleteChId
+ _objc_msgSend$deleteConversationQualityInferenceGenerated
+ _objc_msgSend$deleteConversationQualityInferenceMetadata
+ _objc_msgSend$deleteEvaluatorMetadata
+ _objc_msgSend$deleteRationale
+ _objc_msgSend$deleteUserAlignmentInferenceGenerated
+ _objc_msgSend$deleteUserAlignmentInferenceMetadata
+ _objc_msgSend$durationFromBootToFirstRequestSeconds
+ _objc_msgSend$durationFromClassCUnlockToFirstRequestSeconds
+ _objc_msgSend$durationFromSoftwareUpdateToFirstRequestSeconds
+ _objc_msgSend$dynamicEvaluatorTaskName
+ _objc_msgSend$evaluatorMetadata
+ _objc_msgSend$issueCategorys
+ _objc_msgSend$issueDetected
+ _objc_msgSend$promptIdentifier
+ _objc_msgSend$rationale
+ _objc_msgSend$setChId:
+ _objc_msgSend$setConversationQualityComplexity:
+ _objc_msgSend$setConversationQualityInferenceGenerated:
+ _objc_msgSend$setConversationQualityInferenceMetadata:
+ _objc_msgSend$setDurationFromBootToFirstRequestSeconds:
+ _objc_msgSend$setDurationFromClassCUnlockToFirstRequestSeconds:
+ _objc_msgSend$setDurationFromSoftwareUpdateToFirstRequestSeconds:
+ _objc_msgSend$setDynamicEvaluatorTaskName:
+ _objc_msgSend$setEvaluatorMetadata:
+ _objc_msgSend$setIssueDetected:
+ _objc_msgSend$setPromptIdentifier:
+ _objc_msgSend$setRationale:
+ _objc_msgSend$setUserAlignmentInferenceGenerated:
+ _objc_msgSend$setUserAlignmentInferenceMetadata:
+ _objc_msgSend$setUserAlignmentResult:
+ _objc_msgSend$userAlignmentInferenceGenerated
+ _objc_msgSend$userAlignmentInferenceMetadata
+ _objc_msgSend$userAlignmentResult
+ _qname_CHSchemaCHClientEvent_WhichEvent_Type_None
+ _qname_CHSchemaCHClientEvent_WhichEvent_Type_conversationQualityInferenceGenerated
+ _qname_CHSchemaCHClientEvent_WhichEvent_Type_userAlignmentInferenceGenerated
+ _symbolic _____ So29CHSchemaCHUserAlignmentResultV
+ _symbolic _____ So32CHSchemaCHConversationComplexityV
+ _symbolic _____ So36CHSchemaCHUserAlignmentIssueCategoryV
+ _symbolic _____ So38CHSchemaCHUserAlignmentConfidenceScoreV
+ _symbolic _____ So42CHSchemaCHConversationQualityIssueCategoryV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySSShy_____GG s17_NativeDictionaryV So30SISchemaDeviceSensitivityStateV
+ _symbolic _____ySay_____GShy_____GG s17_NativeDictionaryV s6UInt32V So30SISchemaDeviceSensitivityStateV
- _OUTLINED_FUNCTION_129
- _OUTLINED_FUNCTION_130
- _OUTLINED_FUNCTION_131
- _OUTLINED_FUNCTION_132
- _OUTLINED_FUNCTION_133
- _OUTLINED_FUNCTION_134
- _OUTLINED_FUNCTION_135
- _OUTLINED_FUNCTION_136
- _OUTLINED_FUNCTION_137
- __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
- __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Mapping|SensitiveConditions|Tailing|Factory|Introspection)
- __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(SensitiveConditions|Tailing)
- __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(SensitiveConditions|Tailing)
- __OBJC_$_INSTANCE_METHODS_SISchemaOrderedAnyEvent(InstrumentationAdditions|SensitiveConditions|Introspection)
- __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
- __OBJC_$_INSTANCE_METHODS_SISchemaUUID(Extensions|SensitiveConditions|Tailing)
- _symbolic _____ySS_Shy_____GtG s23_ContiguousArrayStorageC So30SISchemaDeviceSensitivityStateV
- _symbolic _____ySay_____G_Shy_____GtG s23_ContiguousArrayStorageC s6UInt32V So30SISchemaDeviceSensitivityStateV
CStrings:
+ "@\"CHSchemaCHClientEventMetadata\""
+ "@\"CHSchemaCHConversationQualityInferenceGenerated\""
+ "@\"CHSchemaCHConversationQualityInferenceMetadata\""
+ "@\"CHSchemaCHEvaluatorMetadata\""
+ "@\"CHSchemaCHUserAlignmentInferenceGenerated\""
+ "@\"CHSchemaCHUserAlignmentInferenceMetadata\""
+ "CHCONVERSATIONCOMPLEXITY_HIGH"
+ "CHCONVERSATIONCOMPLEXITY_LOW"
+ "CHCONVERSATIONCOMPLEXITY_MEDIUM"
+ "CHCONVERSATIONCOMPLEXITY_UNKNOWN"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_AMBIGUOUS_CLOSURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_ASR_TRANSCRIPTION_ERROR"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_AUDIO_VOICE_QUALITY_TTS_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_CRITICAL_ACTION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_DEVICE_ARBITRATION_MYRIAD_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_DEVICE_STATE_APP_AWARENESS_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_DICTATION_QUICKTATION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_DISAMBIGUATION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_DOMAIN_SPECIFIC_ACTION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_EVOLVING_INTENT_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_FACTUAL_INACCURACY"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_GRAMMATICAL_LINGUISTIC_ERROR"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_INCONSISTENT_BEHAVIOR"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_INTENT_MISUNDERSTANDING_WRONG_DOMAIN"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_INTERACTION_FLOW_DISRUPTION"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_INVOCATION_ACTIVATION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_LANGUAGE_LOCALE_CONFUSION"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_LOCATION_AWARENESS_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_MULTI_TURN_CONVERSATION_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_ONBOARDING_SETUP_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_ON_SCREEN_CONTEXT_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_PARTIAL_INTENT_FULFILLMENT"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_PERSONAL_CONTEXT_PROFILE_ISSUE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_PRECISION_SPECIFICITY_ISSUE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_PRIVACY_PERMISSIONS_BARRIER"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_SPATIAL_CONTEXT_FAILURE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_TECHNICAL_INFRASTRUCTURE_ISSUE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_TIMEOUT_CONNECTIVITY_ISSUE"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_UI_VISUAL_EXPERIENCE_PROBLEM"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_UNKNOWN"
+ "CHCONVERSATIONQUALITYISSUECATEGORY_UNRESOLVED_THREAD"
+ "CHSchemaCHClientEvent"
+ "CHSchemaCHClientEventMetadata"
+ "CHSchemaCHConversationQualityInferenceGenerated"
+ "CHSchemaCHConversationQualityInferenceMetadata"
+ "CHSchemaCHEvaluatorMetadata"
+ "CHSchemaCHUserAlignmentInferenceGenerated"
+ "CHSchemaCHUserAlignmentInferenceMetadata"
+ "CHUSERALIGNMENTCONFIDENCESCORE_HIGH"
+ "CHUSERALIGNMENTCONFIDENCESCORE_LOW"
+ "CHUSERALIGNMENTCONFIDENCESCORE_MEDIUM"
+ "CHUSERALIGNMENTCONFIDENCESCORE_UNKNOWN"
+ "CHUSERALIGNMENTISSUECATEGORY_ACTION_NOT_ALLOWED"
+ "CHUSERALIGNMENTISSUECATEGORY_ASR_RECOGNITION_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_CONTACT_ENTITY_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_CONTEXT_LOST"
+ "CHUSERALIGNMENTISSUECATEGORY_DATE_TIME_RESOLUTION_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_ENTITY_NOT_FOUND"
+ "CHUSERALIGNMENTISSUECATEGORY_FEATURE_CURRENTLY_RESTRICTED"
+ "CHUSERALIGNMENTISSUECATEGORY_LOCATION_ENTITY_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_MEDIA_ENTITY_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_NETWORK_FAILURE"
+ "CHUSERALIGNMENTISSUECATEGORY_NO_MATCHING_TOOL"
+ "CHUSERALIGNMENTISSUECATEGORY_NUMBER_RESOLUTION_ERROR"
+ "CHUSERALIGNMENTISSUECATEGORY_PRONOUN_RESOLUTION_FAILURE"
+ "CHUSERALIGNMENTISSUECATEGORY_UNABLE_TO_HANDLE_REQUEST"
+ "CHUSERALIGNMENTISSUECATEGORY_UNKNOWN"
+ "CHUSERALIGNMENTISSUECATEGORY_USER_INTENT_RECOGNITION_ERROR"
+ "CHUSERALIGNMENTRESULT_CANNOT_BE_DETERMINED"
+ "CHUSERALIGNMENTRESULT_SUCCESSFUL"
+ "CHUSERALIGNMENTRESULT_UNKNOWN"
+ "CHUSERALIGNMENTRESULT_UNSUCCESSFUL"
+ "CH_CLIENT_EVENT"
+ "T@\"CHSchemaCHClientEventMetadata\",&,N,V_eventMetadata"
+ "T@\"CHSchemaCHConversationQualityInferenceGenerated\",&,N,V_conversationQualityInferenceGenerated"
+ "T@\"CHSchemaCHConversationQualityInferenceMetadata\",&,N,V_conversationQualityInferenceMetadata"
+ "T@\"CHSchemaCHEvaluatorMetadata\",&,N,V_evaluatorMetadata"
+ "T@\"CHSchemaCHUserAlignmentInferenceGenerated\",&,N,V_userAlignmentInferenceGenerated"
+ "T@\"CHSchemaCHUserAlignmentInferenceMetadata\",&,N,V_userAlignmentInferenceMetadata"
+ "T@\"NSArray\",C,N,V_issueCategorys"
+ "T@\"NSString\",C,N,V_dynamicEvaluatorTaskName"
+ "T@\"NSString\",C,N,V_promptIdentifier"
+ "T@\"NSString\",C,N,V_rationale"
+ "T@\"SISchemaUUID\",&,N,V_chId"
+ "TB,N,V_hasChId"
+ "TB,N,V_hasConversationQualityInferenceGenerated"
+ "TB,N,V_hasConversationQualityInferenceMetadata"
+ "TB,N,V_hasDynamicEvaluatorTaskName"
+ "TB,N,V_hasEvaluatorMetadata"
+ "TB,N,V_hasPromptIdentifier"
+ "TB,N,V_hasRationale"
+ "TB,N,V_hasUserAlignmentInferenceGenerated"
+ "TB,N,V_hasUserAlignmentInferenceMetadata"
+ "TB,N,V_issueDetected"
+ "Td,N,V_durationFromBootToFirstRequestSeconds"
+ "Td,N,V_durationFromClassCUnlockToFirstRequestSeconds"
+ "Td,N,V_durationFromSoftwareUpdateToFirstRequestSeconds"
+ "Ti,N,V_confidenceScore"
+ "Ti,N,V_conversationQualityComplexity"
+ "Ti,N,V_userAlignmentResult"
+ "_chId"
+ "_conversationQualityComplexity"
+ "_conversationQualityInferenceGenerated"
+ "_conversationQualityInferenceMetadata"
+ "_durationFromBootToFirstRequestSeconds"
+ "_durationFromClassCUnlockToFirstRequestSeconds"
+ "_durationFromSoftwareUpdateToFirstRequestSeconds"
+ "_dynamicEvaluatorTaskName"
+ "_evaluatorMetadata"
+ "_hasChId"
+ "_hasConversationQualityInferenceGenerated"
+ "_hasConversationQualityInferenceMetadata"
+ "_hasDynamicEvaluatorTaskName"
+ "_hasEvaluatorMetadata"
+ "_hasPromptIdentifier"
+ "_hasRationale"
+ "_hasUserAlignmentInferenceGenerated"
+ "_hasUserAlignmentInferenceMetadata"
+ "_issueCategorys"
+ "_issueDetected"
+ "_promptIdentifier"
+ "_rationale"
+ "_userAlignmentInferenceGenerated"
+ "_userAlignmentInferenceMetadata"
+ "_userAlignmentResult"
+ "addIssueCategory:"
+ "chId"
+ "clearIssueCategory"
+ "com.apple.aiml.engagement.ch.CHClientEvent"
+ "com.apple.aiml.engagement.ch.CHClientEvent.CHConversationQualityInferenceGenerated"
+ "com.apple.aiml.engagement.ch.CHClientEvent.CHUserAlignmentInferenceGenerated"
+ "conversationQualityComplexity"
+ "conversationQualityInferenceGenerated"
+ "conversationQualityInferenceGenerated.conversationQualityInferenceMetadata.rationale"
+ "conversationQualityInferenceMetadata"
+ "deleteChId"
+ "deleteConversationQualityComplexity"
+ "deleteConversationQualityInferenceGenerated"
+ "deleteConversationQualityInferenceMetadata"
+ "deleteDurationFromBootToFirstRequestSeconds"
+ "deleteDurationFromClassCUnlockToFirstRequestSeconds"
+ "deleteDurationFromSoftwareUpdateToFirstRequestSeconds"
+ "deleteDynamicEvaluatorTaskName"
+ "deleteEvaluatorMetadata"
+ "deleteIssueCategory"
+ "deleteIssueDetected"
+ "deletePromptIdentifier"
+ "deleteRationale"
+ "deleteUserAlignmentInferenceGenerated"
+ "deleteUserAlignmentInferenceMetadata"
+ "deleteUserAlignmentResult"
+ "durationFromBootToFirstRequestSeconds"
+ "durationFromClassCUnlockToFirstRequestSeconds"
+ "durationFromSoftwareUpdateToFirstRequestSeconds"
+ "dynamicEvaluatorTaskName"
+ "evaluatorMetadata"
+ "hasChId"
+ "hasConversationQualityComplexity"
+ "hasConversationQualityInferenceGenerated"
+ "hasConversationQualityInferenceMetadata"
+ "hasDurationFromBootToFirstRequestSeconds"
+ "hasDurationFromClassCUnlockToFirstRequestSeconds"
+ "hasDurationFromSoftwareUpdateToFirstRequestSeconds"
+ "hasDynamicEvaluatorTaskName"
+ "hasEvaluatorMetadata"
+ "hasIssueDetected"
+ "hasPromptIdentifier"
+ "hasRationale"
+ "hasUserAlignmentInferenceGenerated"
+ "hasUserAlignmentInferenceMetadata"
+ "hasUserAlignmentResult"
+ "issueCategory"
+ "issueCategoryAtIndex:"
+ "issueCategoryCount"
+ "issueCategorys"
+ "issueDetected"
+ "promptIdentifier"
+ "rationale"
+ "setChId:"
+ "setConversationQualityComplexity:"
+ "setConversationQualityInferenceGenerated:"
+ "setConversationQualityInferenceMetadata:"
+ "setDurationFromBootToFirstRequestSeconds:"
+ "setDurationFromClassCUnlockToFirstRequestSeconds:"
+ "setDurationFromSoftwareUpdateToFirstRequestSeconds:"
+ "setDynamicEvaluatorTaskName:"
+ "setEvaluatorMetadata:"
+ "setHasChId:"
+ "setHasConversationQualityComplexity:"
+ "setHasConversationQualityInferenceGenerated:"
+ "setHasConversationQualityInferenceMetadata:"
+ "setHasDurationFromBootToFirstRequestSeconds:"
+ "setHasDurationFromClassCUnlockToFirstRequestSeconds:"
+ "setHasDurationFromSoftwareUpdateToFirstRequestSeconds:"
+ "setHasDynamicEvaluatorTaskName:"
+ "setHasEvaluatorMetadata:"
+ "setHasIssueDetected:"
+ "setHasPromptIdentifier:"
+ "setHasRationale:"
+ "setHasUserAlignmentInferenceGenerated:"
+ "setHasUserAlignmentInferenceMetadata:"
+ "setHasUserAlignmentResult:"
+ "setIssueCategorys:"
+ "setIssueDetected:"
+ "setPromptIdentifier:"
+ "setRationale:"
+ "setUserAlignmentInferenceGenerated:"
+ "setUserAlignmentInferenceMetadata:"
+ "setUserAlignmentResult:"
+ "userAlignmentInferenceGenerated"
+ "userAlignmentInferenceGenerated.userAlignmentInferenceMetadata.rationale"
+ "userAlignmentInferenceMetadata"
+ "userAlignmentResult"
+ "{?=\"buildInstallationTimestampInSecondsSince1970\"b1\"durationFromBootToFirstRequestSeconds\"b1\"durationFromSoftwareUpdateToFirstRequestSeconds\"b1\"durationFromClassCUnlockToFirstRequestSeconds\"b1}"
+ "{?=\"conversationQualityComplexity\"b1\"issueDetected\"b1}"
+ "{?=\"userAlignmentResult\"b1\"confidenceScore\"b1}"

```
