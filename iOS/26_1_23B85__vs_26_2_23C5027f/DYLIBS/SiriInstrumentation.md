## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3505.10.2.0.0
-  __TEXT.__text: 0xa252ac
+3510.3.1.0.0
+  __TEXT.__text: 0xa28e4c
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xd440c
-  __TEXT.__const: 0x1209c
-  __TEXT.__cstring: 0x7a396
-  __TEXT.__constg_swiftt: 0x64a0
-  __TEXT.__swift5_typeref: 0x18dc
-  __TEXT.__swift5_builtin: 0x3a5c
+  __TEXT.__objc_methlist: 0xd48f4
+  __TEXT.__const: 0x12150
+  __TEXT.__cstring: 0x7a70e
+  __TEXT.__swift5_typeref: 0x18e8
   __TEXT.__swift5_reflstr: 0x212
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xefc
-  __TEXT.__swift5_types: 0xbfc
+  __TEXT.__constg_swiftt: 0x64e0
+  __TEXT.__swift5_builtin: 0x3a84
+  __TEXT.__swift5_proto: 0xf04
+  __TEXT.__swift5_types: 0xc04
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2a5f8
+  __TEXT.__unwind_info: 0x2a6f0
   __TEXT.__eh_frame: 0x24a0
-  __TEXT.__objc_classname: 0x15bf8
-  __TEXT.__objc_methname: 0x126250
-  __TEXT.__objc_methtype: 0x28ec2
-  __TEXT.__objc_stubs: 0x6a7a0
-  __DATA_CONST.__got: 0x4d38
-  __DATA_CONST.__const: 0x35128
-  __DATA_CONST.__objc_classlist: 0x4c18
+  __TEXT.__objc_classname: 0x15cbd
+  __TEXT.__objc_methname: 0x126607
+  __TEXT.__objc_methtype: 0x28fbb
+  __TEXT.__objc_stubs: 0x6a880
+  __DATA_CONST.__got: 0x4d58
+  __DATA_CONST.__const: 0x35280
+  __DATA_CONST.__objc_classlist: 0x4c38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37208
+  __DATA_CONST.__objc_selrefs: 0x37280
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7658
+  __DATA_CONST.__objc_superrefs: 0x7698
   __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x21838
-  __AUTH_CONST.__cfstring: 0x6a2a0
-  __AUTH_CONST.__objc_const: 0x11f5c0
+  __AUTH_CONST.__const: 0x21878
+  __AUTH_CONST.__cfstring: 0x6a4a0
+  __AUTH_CONST.__objc_const: 0x11fc10
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11800
-  __DATA.__objc_ivar: 0xe548
-  __DATA.__data: 0x2080
-  __DATA.__bss: 0x18e00
+  __AUTH.__objc_data: 0x11940
+  __DATA.__objc_ivar: 0xe590
+  __DATA.__data: 0x2090
+  __DATA.__bss: 0x18f00
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1e340
   __DATA_DIRTY.__data: 0x568

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B5EEF844-7307-314F-AC42-070293CBE53E
-  Functions: 76823
-  Symbols:   191105
-  CStrings:  78566
+  UUID: D2F42B31-99D5-31BF-8D63-CCE09A1CD8FC
+  Functions: 76934
+  Symbols:   191367
+  CStrings:  78631
 
Symbols:
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts deleteTurnCounts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts hasTurnCounts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts hash]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts initWithJSON:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts isEqual:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts jsonData]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts readFrom:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts setHasTurnCounts:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts setTurnCounts:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts turnCounts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts writeTo:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAICounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest counts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest deleteCounts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest deleteDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest dimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest hasCounts]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest hasDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest hash]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest initWithJSON:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest isEqual:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest jsonData]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest readFrom:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest setCounts:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest setDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest setHasCounts:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest writeTo:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported addDigests:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported clearDigests]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported deleteDigests]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported digestsCount]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported digests]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported fixedDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported hash]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported initWithJSON:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported isEqual:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported jsonData]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported readFrom:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported setDigests:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported writeTo:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions assistantDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteIsExplicitGenAIRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteRequestStatus]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteRequestType]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions deleteThirdPartyGenAIAgent]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasAssistantDimensions]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasIsExplicitGenAIRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasRequestStatus]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasRequestType]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hasThirdPartyGenAIAgent]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions hash]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions initWithJSON:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions isEqual:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions isExplicitGenAIRequest]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions jsonData]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions readFrom:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions requestStatus]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions requestType]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasAssistantDimensions:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasIsExplicitGenAIRequest:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasRequestStatus:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasRequestType:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setHasThirdPartyGenAIAgent:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setIsExplicitGenAIRequest:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setRequestStatus:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setRequestType:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions setThirdPartyGenAIAgent:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions thirdPartyGenAIAgent]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions writeTo:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriClientEvent assistantThirdPartyGenAIDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssistantThirdPartyGenAIDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssistantThirdPartyGenAIDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent setAssistantThirdPartyGenAIDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssistantThirdPartyGenAIDigestReported:]
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts._turnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._assistantDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._isExplicitGenAIRequest
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._requestStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._requestType
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._thirdPartyGenAIAgent
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assistantThirdPartyGenAIDigestReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts._hasTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions._hasAssistantDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssistantThirdPartyGenAIDigestReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ _ODDSiriSchemaODDAssistantThirdPartyGenAICountsReadFrom
+ _ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReadFrom
+ _ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReportedReadFrom
+ _ODDSiriSchemaODDAssistantThirdPartyGenAIDimensionsReadFrom
+ __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantThirdPartyGenAICounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Mapping|SensitiveConditions|Tailing|Factory|Introspection)
+ __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(SensitiveConditions|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(SensitiveConditions|Tailing)
+ __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(IsolationLevel|AnyEvent|Component)
+ __OBJC_$_INSTANCE_METHODS_SISchemaUUID(Extensions|SensitiveConditions|Tailing)
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAICounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions
+ _objc_msgSend$assistantThirdPartyGenAIDigestReported
+ _objc_msgSend$deleteAssistantThirdPartyGenAIDigestReported
+ _objc_msgSend$isExplicitGenAIRequest
+ _objc_msgSend$setAssistantThirdPartyGenAIDigestReported:
+ _objc_msgSend$setIsExplicitGenAIRequest:
+ _objc_msgSend$setThirdPartyGenAIAgent:
+ _objc_msgSend$thirdPartyGenAIAgent
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assistantThirdPartyGenAIDigestReported
+ _symbolic _____ So42ODDSiriSchemaODDThirdPartyGenAIRequestTypeV
+ _symbolic _____ So44ODDSiriSchemaODDThirdPartyGenAIRequestStatusV
- __OBJC_$_CLASS_METHODS_SISchemaTopLevelUnionType(AnyEvent|IsolationLevel|Component)
- __OBJC_$_INSTANCE_METHODS_SISchemaAnyEvent(Tailing|Factory|Mapping|SensitiveConditions|Introspection)
- __OBJC_$_INSTANCE_METHODS_SISchemaClientEventMetadata(Tailing|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaConversationTrace(Tailing|SensitiveConditions)
- __OBJC_$_INSTANCE_METHODS_SISchemaTopLevelUnionType(AnyEvent|IsolationLevel|Component)
- __OBJC_$_INSTANCE_METHODS_SISchemaUUID(Extensions|Tailing|SensitiveConditions)
CStrings:
+ "@\"ODDSiriSchemaODDAssistantThirdPartyGenAICounts\""
+ "@\"ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported\""
+ "@\"ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions\""
+ "ODDSiriSchemaODDAssistantThirdPartyGenAICounts"
+ "ODDSiriSchemaODDAssistantThirdPartyGenAIDigest"
+ "ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported"
+ "ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_NON_SYSTEM_FAILURE"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_OTHER"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_SUCCESS"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_SYSTEM_FAILURE"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_UNKNOWN"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_USER_ABANDONED"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_USER_CANCELLED"
+ "ODDTHIRDPARTYGENAIREQUESTSTATUS_WEB_SEARCH"
+ "ODDTHIRDPARTYGENAIREQUESTTYPE_GENERATE_KNOWLEDGE_RESPONSE_INTENT"
+ "ODDTHIRDPARTYGENAIREQUESTTYPE_GENERATE_RICH_CONTENT_FROM_MEDIA_INTENT"
+ "ODDTHIRDPARTYGENAIREQUESTTYPE_GENERATE_RICH_CONTENT_INTENT"
+ "ODDTHIRDPARTYGENAIREQUESTTYPE_UNKNOWN"
+ "T@\"ODDSiriSchemaODDAssistantThirdPartyGenAICounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDAssistantThirdPartyGenAIDigestReported\",&,N,V_assistantThirdPartyGenAIDigestReported"
+ "T@\"ODDSiriSchemaODDAssistantThirdPartyGenAIDimensions\",&,N,V_dimensions"
+ "TB,N,V_hasAssistantThirdPartyGenAIDigestReported"
+ "TB,N,V_isExplicitGenAIRequest"
+ "Ti,N,V_thirdPartyGenAIAgent"
+ "_assistantThirdPartyGenAIDigestReported"
+ "_hasAssistantThirdPartyGenAIDigestReported"
+ "_isExplicitGenAIRequest"
+ "_thirdPartyGenAIAgent"
+ "assistantThirdPartyGenAIDigestReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssistantThirdPartyGenAIDigestReported"
+ "deleteAssistantThirdPartyGenAIDigestReported"
+ "deleteIsExplicitGenAIRequest"
+ "deleteThirdPartyGenAIAgent"
+ "hasAssistantThirdPartyGenAIDigestReported"
+ "hasIsExplicitGenAIRequest"
+ "hasThirdPartyGenAIAgent"
+ "isExplicitGenAIRequest"
+ "setAssistantThirdPartyGenAIDigestReported:"
+ "setHasAssistantThirdPartyGenAIDigestReported:"
+ "setHasIsExplicitGenAIRequest:"
+ "setHasThirdPartyGenAIAgent:"
+ "setIsExplicitGenAIRequest:"
+ "setThirdPartyGenAIAgent:"
+ "thirdPartyGenAIAgent"
+ "{?=\"thirdPartyGenAIAgent\"b1\"requestStatus\"b1\"isExplicitGenAIRequest\"b1\"requestType\"b1}"

```
