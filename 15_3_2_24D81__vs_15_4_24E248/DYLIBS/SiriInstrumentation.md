## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation`

```diff

-3403.3.1.0.0
-  __TEXT.__text: 0x98a6f0
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0xc16a0
-  __TEXT.__cstring: 0x6fd2c
-  __TEXT.__const: 0x10950
-  __TEXT.__constg_swiftt: 0x5d20
-  __TEXT.__swift5_typeref: 0x1761
-  __TEXT.__swift5_builtin: 0x35ac
+3404.73.1.0.0
+  __TEXT.__text: 0xa0403c
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0xcb47c
+  __TEXT.__const: 0x113d0
+  __TEXT.__cstring: 0x75740
+  __TEXT.__constg_swiftt: 0x60e0
+  __TEXT.__swift5_typeref: 0x1815
+  __TEXT.__swift5_builtin: 0x3804
   __TEXT.__swift5_reflstr: 0x20b
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0xdf0
-  __TEXT.__swift5_types: 0xb0c
+  __TEXT.__swift5_proto: 0xe6c
+  __TEXT.__swift5_types: 0xb84
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x27ad0
-  __TEXT.__eh_frame: 0x1c68
-  __TEXT.__objc_classname: 0x13cce
-  __TEXT.__objc_methname: 0x1084f7
-  __TEXT.__objc_methtype: 0x25077
-  __TEXT.__objc_stubs: 0x60a80
-  __DATA_CONST.__got: 0x4770
-  __DATA_CONST.__const: 0x31378
-  __DATA_CONST.__objc_classlist: 0x4640
+  __TEXT.__unwind_info: 0x28fa8
+  __TEXT.__eh_frame: 0x1f98
+  __TEXT.__objc_classname: 0x14e59
+  __TEXT.__objc_methname: 0x1170ad
+  __TEXT.__objc_methtype: 0x26965
+  __TEXT.__objc_stubs: 0x65f80
+  __DATA_CONST.__got: 0x4ac8
+  __DATA_CONST.__const: 0x32d18
+  __DATA_CONST.__objc_classlist: 0x4998
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x321c8
+  __DATA_CONST.__objc_selrefs: 0x34b30
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x6c70
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x1dc20
-  __AUTH_CONST.__cfstring: 0x61560
-  __AUTH_CONST.__objc_const: 0x1069d8
-  __AUTH_CONST.__objc_intobj: 0xb40
-  __AUTH.__objc_data: 0x2a2d0
+  __DATA_CONST.__objc_superrefs: 0x71e0
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__const: 0x20780
+  __AUTH_CONST.__cfstring: 0x66140
+  __AUTH_CONST.__objc_const: 0x113820
+  __AUTH_CONST.__objc_intobj: 0xb70
+  __AUTH.__objc_data: 0x2c440
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0xd010
-  __DATA.__data: 0x20b8
-  __DATA.__bss: 0x16f80
-  __DATA.__common: 0x58
+  __DATA.__objc_ivar: 0xdafc
+  __DATA.__data: 0x21b0
+  __DATA.__bss: 0x17e80
+  __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x1e00
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 719DFDD6-141C-32DC-85C9-A0B40F06A0B8
-  Functions: 70713
-  Symbols:   109969
-  CStrings:  71833
+  UUID: 9F2FE246-E193-3F5C-810C-8989468554D7
+  Functions: 73657
+  Symbols:   115509
+  CStrings:  75375
 
Symbols:
+ -[ASRSchemaASRClientEvent contextualEntityCollectionTriggered]
+ -[ASRSchemaASRClientEvent contextualEntityRetrievalContext]
+ -[ASRSchemaASRClientEvent deleteContextualEntityCollectionTriggered]
+ -[ASRSchemaASRClientEvent deleteContextualEntityRetrievalContext]
+ -[ASRSchemaASRClientEvent deletePersonalizationUserEditNamedEntityMetrics]
+ -[ASRSchemaASRClientEvent hasContextualEntityCollectionTriggered]
+ -[ASRSchemaASRClientEvent hasContextualEntityRetrievalContext]
+ -[ASRSchemaASRClientEvent hasPersonalizationUserEditNamedEntityMetrics]
+ -[ASRSchemaASRClientEvent personalizationUserEditNamedEntityMetrics]
+ -[ASRSchemaASRClientEvent setContextualEntityCollectionTriggered:]
+ -[ASRSchemaASRClientEvent setContextualEntityRetrievalContext:]
+ -[ASRSchemaASRClientEvent setHasContextualEntityCollectionTriggered:]
+ -[ASRSchemaASRClientEvent setHasContextualEntityRetrievalContext:]
+ -[ASRSchemaASRClientEvent setHasPersonalizationUserEditNamedEntityMetrics:]
+ -[ASRSchemaASRClientEvent setPersonalizationUserEditNamedEntityMetrics:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered deleteExists]
+ -[ASRSchemaASRContextualEntityCollectionTriggered dictionaryRepresentation]
+ -[ASRSchemaASRContextualEntityCollectionTriggered exists]
+ -[ASRSchemaASRContextualEntityCollectionTriggered hasExists]
+ -[ASRSchemaASRContextualEntityCollectionTriggered hash]
+ -[ASRSchemaASRContextualEntityCollectionTriggered initWithDictionary:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered initWithJSON:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered isEqual:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered jsonData]
+ -[ASRSchemaASRContextualEntityCollectionTriggered readFrom:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered setExists:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered setHasExists:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered writeTo:]
+ -[ASRSchemaASRContextualEntityCollectionTriggered(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRContextualEntityRetrievalContext .cxx_destruct]
+ -[ASRSchemaASRContextualEntityRetrievalContext deleteEnded]
+ -[ASRSchemaASRContextualEntityRetrievalContext deleteStartedOrChanged]
+ -[ASRSchemaASRContextualEntityRetrievalContext dictionaryRepresentation]
+ -[ASRSchemaASRContextualEntityRetrievalContext ended]
+ -[ASRSchemaASRContextualEntityRetrievalContext hasEnded]
+ -[ASRSchemaASRContextualEntityRetrievalContext hasStartedOrChanged]
+ -[ASRSchemaASRContextualEntityRetrievalContext hash]
+ -[ASRSchemaASRContextualEntityRetrievalContext initWithDictionary:]
+ -[ASRSchemaASRContextualEntityRetrievalContext initWithJSON:]
+ -[ASRSchemaASRContextualEntityRetrievalContext isEqual:]
+ -[ASRSchemaASRContextualEntityRetrievalContext jsonData]
+ -[ASRSchemaASRContextualEntityRetrievalContext readFrom:]
+ -[ASRSchemaASRContextualEntityRetrievalContext setEnded:]
+ -[ASRSchemaASRContextualEntityRetrievalContext setHasEnded:]
+ -[ASRSchemaASRContextualEntityRetrievalContext setHasStartedOrChanged:]
+ -[ASRSchemaASRContextualEntityRetrievalContext setStartedOrChanged:]
+ -[ASRSchemaASRContextualEntityRetrievalContext startedOrChanged]
+ -[ASRSchemaASRContextualEntityRetrievalContext whichContextevent]
+ -[ASRSchemaASRContextualEntityRetrievalContext writeTo:]
+ -[ASRSchemaASRContextualEntityRetrievalContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRContextualEntityRetrievalContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRContextualEntityRetrievalEnded .cxx_destruct]
+ -[ASRSchemaASRContextualEntityRetrievalEnded addRetrievedEntityStates:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded clearRetrievedEntityStates]
+ -[ASRSchemaASRContextualEntityRetrievalEnded deleteRetrievedEntityStates]
+ -[ASRSchemaASRContextualEntityRetrievalEnded dictionaryRepresentation]
+ -[ASRSchemaASRContextualEntityRetrievalEnded hash]
+ -[ASRSchemaASRContextualEntityRetrievalEnded initWithDictionary:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded initWithJSON:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded isEqual:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded jsonData]
+ -[ASRSchemaASRContextualEntityRetrievalEnded readFrom:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded retrievedEntityStatesAtIndex:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded retrievedEntityStatesCount]
+ -[ASRSchemaASRContextualEntityRetrievalEnded retrievedEntityStates]
+ -[ASRSchemaASRContextualEntityRetrievalEnded setRetrievedEntityStates:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded writeTo:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRContextualEntityRetrievalEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRContextualEntityRetrievalStarted .cxx_destruct]
+ -[ASRSchemaASRContextualEntityRetrievalStarted addEnabledTasks:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted addRejectedContextTypes:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted addRejectedEntityTypes:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted clearEnabledTasks]
+ -[ASRSchemaASRContextualEntityRetrievalStarted clearRejectedContextTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted clearRejectedEntityTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteEnabledTasks]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteMaxEnrolled]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteMaxEntityChars]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteMaxEntityWords]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteRejectedContextTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteRejectedEntityTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteRequestTask]
+ -[ASRSchemaASRContextualEntityRetrievalStarted deleteRetrievalTimeout]
+ -[ASRSchemaASRContextualEntityRetrievalStarted dictionaryRepresentation]
+ -[ASRSchemaASRContextualEntityRetrievalStarted enabledTasksAtIndex:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted enabledTasksCount]
+ -[ASRSchemaASRContextualEntityRetrievalStarted enabledTasks]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hasMaxEnrolled]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hasMaxEntityChars]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hasMaxEntityWords]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hasRequestTask]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hasRetrievalTimeout]
+ -[ASRSchemaASRContextualEntityRetrievalStarted hash]
+ -[ASRSchemaASRContextualEntityRetrievalStarted initWithDictionary:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted initWithJSON:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted isEqual:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted jsonData]
+ -[ASRSchemaASRContextualEntityRetrievalStarted maxEnrolled]
+ -[ASRSchemaASRContextualEntityRetrievalStarted maxEntityChars]
+ -[ASRSchemaASRContextualEntityRetrievalStarted maxEntityWords]
+ -[ASRSchemaASRContextualEntityRetrievalStarted readFrom:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedContextTypesAtIndex:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedContextTypesCount]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedContextTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedEntityTypesAtIndex:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedEntityTypesCount]
+ -[ASRSchemaASRContextualEntityRetrievalStarted rejectedEntityTypes]
+ -[ASRSchemaASRContextualEntityRetrievalStarted requestTask]
+ -[ASRSchemaASRContextualEntityRetrievalStarted retrievalTimeout]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setEnabledTasks:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setHasMaxEnrolled:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setHasMaxEntityChars:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setHasMaxEntityWords:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setHasRequestTask:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setHasRetrievalTimeout:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setMaxEnrolled:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setMaxEntityChars:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setMaxEntityWords:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setRejectedContextTypes:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setRejectedEntityTypes:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setRequestTask:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted setRetrievalTimeout:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted writeTo:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRContextualEntityRetrievalStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRContextualEntityState .cxx_destruct]
+ -[ASRSchemaASRContextualEntityState contextType]
+ -[ASRSchemaASRContextualEntityState deleteContextType]
+ -[ASRSchemaASRContextualEntityState deleteEnrollmentResult]
+ -[ASRSchemaASRContextualEntityState deleteEntityType]
+ -[ASRSchemaASRContextualEntityState deleteRejectReason]
+ -[ASRSchemaASRContextualEntityState dictionaryRepresentation]
+ -[ASRSchemaASRContextualEntityState enrollmentResult]
+ -[ASRSchemaASRContextualEntityState entityType]
+ -[ASRSchemaASRContextualEntityState hasContextType]
+ -[ASRSchemaASRContextualEntityState hasEnrollmentResult]
+ -[ASRSchemaASRContextualEntityState hasEntityType]
+ -[ASRSchemaASRContextualEntityState hasRejectReason]
+ -[ASRSchemaASRContextualEntityState hash]
+ -[ASRSchemaASRContextualEntityState initWithDictionary:]
+ -[ASRSchemaASRContextualEntityState initWithJSON:]
+ -[ASRSchemaASRContextualEntityState isEqual:]
+ -[ASRSchemaASRContextualEntityState jsonData]
+ -[ASRSchemaASRContextualEntityState readFrom:]
+ -[ASRSchemaASRContextualEntityState rejectReason]
+ -[ASRSchemaASRContextualEntityState setContextType:]
+ -[ASRSchemaASRContextualEntityState setEnrollmentResult:]
+ -[ASRSchemaASRContextualEntityState setEntityType:]
+ -[ASRSchemaASRContextualEntityState setHasContextType:]
+ -[ASRSchemaASRContextualEntityState setHasEnrollmentResult:]
+ -[ASRSchemaASRContextualEntityState setHasEntityType:]
+ -[ASRSchemaASRContextualEntityState setHasRejectReason:]
+ -[ASRSchemaASRContextualEntityState setRejectReason:]
+ -[ASRSchemaASRContextualEntityState writeTo:]
+ -[ASRSchemaASRContextualEntityState(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRContextualEntityState(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRFullPayloadCorrectionContext .cxx_destruct]
+ -[ASRSchemaASRFullPayloadCorrectionContext deleteEnded]
+ -[ASRSchemaASRFullPayloadCorrectionContext deleteFailed]
+ -[ASRSchemaASRFullPayloadCorrectionContext deleteStartedOrChanged]
+ -[ASRSchemaASRFullPayloadCorrectionContext dictionaryRepresentation]
+ -[ASRSchemaASRFullPayloadCorrectionContext ended]
+ -[ASRSchemaASRFullPayloadCorrectionContext failed]
+ -[ASRSchemaASRFullPayloadCorrectionContext hasEnded]
+ -[ASRSchemaASRFullPayloadCorrectionContext hasFailed]
+ -[ASRSchemaASRFullPayloadCorrectionContext hasStartedOrChanged]
+ -[ASRSchemaASRFullPayloadCorrectionContext hash]
+ -[ASRSchemaASRFullPayloadCorrectionContext initWithDictionary:]
+ -[ASRSchemaASRFullPayloadCorrectionContext initWithJSON:]
+ -[ASRSchemaASRFullPayloadCorrectionContext isEqual:]
+ -[ASRSchemaASRFullPayloadCorrectionContext jsonData]
+ -[ASRSchemaASRFullPayloadCorrectionContext readFrom:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setEnded:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setFailed:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setHasEnded:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setHasFailed:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setHasStartedOrChanged:]
+ -[ASRSchemaASRFullPayloadCorrectionContext setStartedOrChanged:]
+ -[ASRSchemaASRFullPayloadCorrectionContext startedOrChanged]
+ -[ASRSchemaASRFullPayloadCorrectionContext whichContextevent]
+ -[ASRSchemaASRFullPayloadCorrectionContext writeTo:]
+ -[ASRSchemaASRFullPayloadCorrectionContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRFullPayloadCorrectionContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRFullPayloadCorrectionEnded .cxx_destruct]
+ -[ASRSchemaASRFullPayloadCorrectionEnded deleteLinkId]
+ -[ASRSchemaASRFullPayloadCorrectionEnded deleteResponseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionEnded dictionaryRepresentation]
+ -[ASRSchemaASRFullPayloadCorrectionEnded hasLinkId]
+ -[ASRSchemaASRFullPayloadCorrectionEnded hasResponseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionEnded hash]
+ -[ASRSchemaASRFullPayloadCorrectionEnded initWithDictionary:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded initWithJSON:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded isEqual:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded jsonData]
+ -[ASRSchemaASRFullPayloadCorrectionEnded linkId]
+ -[ASRSchemaASRFullPayloadCorrectionEnded readFrom:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded responseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionEnded setHasLinkId:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded setHasResponseTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded setLinkId:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded setResponseTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded writeTo:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRFullPayloadCorrectionEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRFullPayloadCorrectionFailed deleteErrorType]
+ -[ASRSchemaASRFullPayloadCorrectionFailed deleteResponseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionFailed dictionaryRepresentation]
+ -[ASRSchemaASRFullPayloadCorrectionFailed errorType]
+ -[ASRSchemaASRFullPayloadCorrectionFailed hasErrorType]
+ -[ASRSchemaASRFullPayloadCorrectionFailed hasResponseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionFailed hash]
+ -[ASRSchemaASRFullPayloadCorrectionFailed initWithDictionary:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed initWithJSON:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed isEqual:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed jsonData]
+ -[ASRSchemaASRFullPayloadCorrectionFailed readFrom:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed responseTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionFailed setErrorType:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed setHasErrorType:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed setHasResponseTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed setResponseTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed writeTo:]
+ -[ASRSchemaASRFullPayloadCorrectionFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 .cxx_destruct]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 deleteFullPayloadCorrectorInput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 deleteFullPayloadCorrectorOutput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 deleteLinkId]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 dictionaryRepresentation]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 fullPayloadCorrectorInput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 fullPayloadCorrectorOutput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 hasFullPayloadCorrectorInput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 hasFullPayloadCorrectorOutput]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 hasLinkId]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 hash]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 initWithDictionary:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 initWithJSON:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 isEqual:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 jsonData]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 linkId]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 readFrom:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setFullPayloadCorrectorInput:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setFullPayloadCorrectorOutput:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setHasFullPayloadCorrectorInput:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setHasFullPayloadCorrectorOutput:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setHasLinkId:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 setLinkId:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1 writeTo:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRFullPayloadCorrectionInfoTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRFullPayloadCorrectionStarted deleteUtteranceEndTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted deleteUtteranceStartTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted dictionaryRepresentation]
+ -[ASRSchemaASRFullPayloadCorrectionStarted hasUtteranceEndTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted hasUtteranceStartTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted hash]
+ -[ASRSchemaASRFullPayloadCorrectionStarted initWithDictionary:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted initWithJSON:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted isEqual:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted jsonData]
+ -[ASRSchemaASRFullPayloadCorrectionStarted readFrom:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted setHasUtteranceEndTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted setHasUtteranceStartTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted setUtteranceEndTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted setUtteranceStartTimeInNs:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted utteranceEndTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted utteranceStartTimeInNs]
+ -[ASRSchemaASRFullPayloadCorrectionStarted writeTo:]
+ -[ASRSchemaASRFullPayloadCorrectionStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRLMEOverActivationEdit deleteSpeechProfileCategory]
+ -[ASRSchemaASRLMEOverActivationEdit dictionaryRepresentation]
+ -[ASRSchemaASRLMEOverActivationEdit hasSpeechProfileCategory]
+ -[ASRSchemaASRLMEOverActivationEdit hash]
+ -[ASRSchemaASRLMEOverActivationEdit initWithDictionary:]
+ -[ASRSchemaASRLMEOverActivationEdit initWithJSON:]
+ -[ASRSchemaASRLMEOverActivationEdit isEqual:]
+ -[ASRSchemaASRLMEOverActivationEdit jsonData]
+ -[ASRSchemaASRLMEOverActivationEdit readFrom:]
+ -[ASRSchemaASRLMEOverActivationEdit setHasSpeechProfileCategory:]
+ -[ASRSchemaASRLMEOverActivationEdit setSpeechProfileCategory:]
+ -[ASRSchemaASRLMEOverActivationEdit speechProfileCategory]
+ -[ASRSchemaASRLMEOverActivationEdit writeTo:]
+ -[ASRSchemaASRLMEOverActivationEdit(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRNamedEntityUserEdit .cxx_destruct]
+ -[ASRSchemaASRNamedEntityUserEdit addSpeechProfileCategories:]
+ -[ASRSchemaASRNamedEntityUserEdit addVisualContextCategories:]
+ -[ASRSchemaASRNamedEntityUserEdit clearSpeechProfileCategories]
+ -[ASRSchemaASRNamedEntityUserEdit clearVisualContextCategories]
+ -[ASRSchemaASRNamedEntityUserEdit deleteEntityTaggerCategory]
+ -[ASRSchemaASRNamedEntityUserEdit deleteIsNamedEntityPresentInSpeechProfile]
+ -[ASRSchemaASRNamedEntityUserEdit deleteIsNamedEntityPresentInVisualContext]
+ -[ASRSchemaASRNamedEntityUserEdit deleteSpeechProfileCategories]
+ -[ASRSchemaASRNamedEntityUserEdit deleteVisualContextCategories]
+ -[ASRSchemaASRNamedEntityUserEdit dictionaryRepresentation]
+ -[ASRSchemaASRNamedEntityUserEdit entityTaggerCategory]
+ -[ASRSchemaASRNamedEntityUserEdit hasEntityTaggerCategory]
+ -[ASRSchemaASRNamedEntityUserEdit hasIsNamedEntityPresentInSpeechProfile]
+ -[ASRSchemaASRNamedEntityUserEdit hasIsNamedEntityPresentInVisualContext]
+ -[ASRSchemaASRNamedEntityUserEdit hash]
+ -[ASRSchemaASRNamedEntityUserEdit initWithDictionary:]
+ -[ASRSchemaASRNamedEntityUserEdit initWithJSON:]
+ -[ASRSchemaASRNamedEntityUserEdit isEqual:]
+ -[ASRSchemaASRNamedEntityUserEdit isNamedEntityPresentInSpeechProfile]
+ -[ASRSchemaASRNamedEntityUserEdit isNamedEntityPresentInVisualContext]
+ -[ASRSchemaASRNamedEntityUserEdit jsonData]
+ -[ASRSchemaASRNamedEntityUserEdit readFrom:]
+ -[ASRSchemaASRNamedEntityUserEdit setEntityTaggerCategory:]
+ -[ASRSchemaASRNamedEntityUserEdit setHasEntityTaggerCategory:]
+ -[ASRSchemaASRNamedEntityUserEdit setHasIsNamedEntityPresentInSpeechProfile:]
+ -[ASRSchemaASRNamedEntityUserEdit setHasIsNamedEntityPresentInVisualContext:]
+ -[ASRSchemaASRNamedEntityUserEdit setIsNamedEntityPresentInSpeechProfile:]
+ -[ASRSchemaASRNamedEntityUserEdit setIsNamedEntityPresentInVisualContext:]
+ -[ASRSchemaASRNamedEntityUserEdit setSpeechProfileCategories:]
+ -[ASRSchemaASRNamedEntityUserEdit setVisualContextCategories:]
+ -[ASRSchemaASRNamedEntityUserEdit speechProfileCategoriesAtIndex:]
+ -[ASRSchemaASRNamedEntityUserEdit speechProfileCategoriesCount]
+ -[ASRSchemaASRNamedEntityUserEdit speechProfileCategories]
+ -[ASRSchemaASRNamedEntityUserEdit visualContextCategoriesAtIndex:]
+ -[ASRSchemaASRNamedEntityUserEdit visualContextCategoriesCount]
+ -[ASRSchemaASRNamedEntityUserEdit visualContextCategories]
+ -[ASRSchemaASRNamedEntityUserEdit writeTo:]
+ -[ASRSchemaASRNamedEntityUserEdit(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASROneBestTranscriptTier1 .cxx_destruct]
+ -[ASRSchemaASROneBestTranscriptTier1 deletePostItn]
+ -[ASRSchemaASROneBestTranscriptTier1 deleteRawRecognition]
+ -[ASRSchemaASROneBestTranscriptTier1 dictionaryRepresentation]
+ -[ASRSchemaASROneBestTranscriptTier1 hasPostItn]
+ -[ASRSchemaASROneBestTranscriptTier1 hasRawRecognition]
+ -[ASRSchemaASROneBestTranscriptTier1 hash]
+ -[ASRSchemaASROneBestTranscriptTier1 initWithDictionary:]
+ -[ASRSchemaASROneBestTranscriptTier1 initWithJSON:]
+ -[ASRSchemaASROneBestTranscriptTier1 isEqual:]
+ -[ASRSchemaASROneBestTranscriptTier1 jsonData]
+ -[ASRSchemaASROneBestTranscriptTier1 postItn]
+ -[ASRSchemaASROneBestTranscriptTier1 rawRecognition]
+ -[ASRSchemaASROneBestTranscriptTier1 readFrom:]
+ -[ASRSchemaASROneBestTranscriptTier1 setHasPostItn:]
+ -[ASRSchemaASROneBestTranscriptTier1 setHasRawRecognition:]
+ -[ASRSchemaASROneBestTranscriptTier1 setPostItn:]
+ -[ASRSchemaASROneBestTranscriptTier1 setRawRecognition:]
+ -[ASRSchemaASROneBestTranscriptTier1 writeTo:]
+ -[ASRSchemaASROneBestTranscriptTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASROneBestTranscriptTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics .cxx_destruct]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics addLmeOverActivationEdits:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics addNamedEntityUserEdits:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics clearLmeOverActivationEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics clearNamedEntityUserEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics deleteLmeOverActivationEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics deleteNamedEntityUserEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics deleteNumTotalEdit]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics dictionaryRepresentation]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics hasNumTotalEdit]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics hash]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics initWithDictionary:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics initWithJSON:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics isEqual:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics jsonData]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics lmeOverActivationEditsAtIndex:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics lmeOverActivationEditsCount]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics lmeOverActivationEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics namedEntityUserEditsAtIndex:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics namedEntityUserEditsCount]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics namedEntityUserEdits]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics numTotalEdit]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics readFrom:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics setHasNumTotalEdit:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics setLmeOverActivationEdits:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics setNamedEntityUserEdits:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics setNumTotalEdit:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics writeTo:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSchemaASRPersonalizationUserEditNamedEntityMetrics(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 addOneBestTranscripts:]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 clearOneBestTranscripts]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 deleteLinkId]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 deleteOneBestTranscripts]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 hasLinkId]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 linkId]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 oneBestTranscriptsAtIndex:]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 oneBestTranscriptsCount]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 oneBestTranscripts]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 setHasLinkId:]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 setLinkId:]
+ -[DODMLASRSchemaDODMLASRAudioFileResultTier1 setOneBestTranscripts:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated .cxx_destruct]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated deleteOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated hasOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated hash]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated initWithDictionary:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated initWithJSON:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated isEqual:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated jsonData]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated originalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated readFrom:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated setHasOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated setOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated writeTo:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted .cxx_destruct]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted deleteOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted hasOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted hash]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted initWithDictionary:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted initWithJSON:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted isEqual:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted jsonData]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted originalAsrId]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted readFrom:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted setHasOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted setOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted writeTo:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRDecodingResult addEntityScoreResults:]
+ -[DODMLASRSchemaDODMLASRDecodingResult clearEntityScoreResults]
+ -[DODMLASRSchemaDODMLASRDecodingResult deleteEntityScoreResults]
+ -[DODMLASRSchemaDODMLASRDecodingResult deleteOneBestTranscriptLinkIndex]
+ -[DODMLASRSchemaDODMLASRDecodingResult entityScoreResultsAtIndex:]
+ -[DODMLASRSchemaDODMLASRDecodingResult entityScoreResultsCount]
+ -[DODMLASRSchemaDODMLASRDecodingResult entityScoreResults]
+ -[DODMLASRSchemaDODMLASRDecodingResult hasOneBestTranscriptLinkIndex]
+ -[DODMLASRSchemaDODMLASRDecodingResult oneBestTranscriptLinkIndex]
+ -[DODMLASRSchemaDODMLASRDecodingResult setEntityScoreResults:]
+ -[DODMLASRSchemaDODMLASRDecodingResult setHasOneBestTranscriptLinkIndex:]
+ -[DODMLASRSchemaDODMLASRDecodingResult setOneBestTranscriptLinkIndex:]
+ -[DODMLASRSchemaDODMLASREntityScore deleteEntityTaggerCategory]
+ -[DODMLASRSchemaDODMLASREntityScore deleteNumEntityErrors]
+ -[DODMLASRSchemaDODMLASREntityScore deleteNumTotalEntities]
+ -[DODMLASRSchemaDODMLASREntityScore dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASREntityScore entityTaggerCategory]
+ -[DODMLASRSchemaDODMLASREntityScore hasEntityTaggerCategory]
+ -[DODMLASRSchemaDODMLASREntityScore hasNumEntityErrors]
+ -[DODMLASRSchemaDODMLASREntityScore hasNumTotalEntities]
+ -[DODMLASRSchemaDODMLASREntityScore hash]
+ -[DODMLASRSchemaDODMLASREntityScore initWithDictionary:]
+ -[DODMLASRSchemaDODMLASREntityScore initWithJSON:]
+ -[DODMLASRSchemaDODMLASREntityScore isEqual:]
+ -[DODMLASRSchemaDODMLASREntityScore jsonData]
+ -[DODMLASRSchemaDODMLASREntityScore numEntityErrors]
+ -[DODMLASRSchemaDODMLASREntityScore numTotalEntities]
+ -[DODMLASRSchemaDODMLASREntityScore readFrom:]
+ -[DODMLASRSchemaDODMLASREntityScore setEntityTaggerCategory:]
+ -[DODMLASRSchemaDODMLASREntityScore setHasEntityTaggerCategory:]
+ -[DODMLASRSchemaDODMLASREntityScore setHasNumEntityErrors:]
+ -[DODMLASRSchemaDODMLASREntityScore setHasNumTotalEntities:]
+ -[DODMLASRSchemaDODMLASREntityScore setNumEntityErrors:]
+ -[DODMLASRSchemaDODMLASREntityScore setNumTotalEntities:]
+ -[DODMLASRSchemaDODMLASREntityScore writeTo:]
+ -[DODMLASRSchemaDODMLASREntityScore(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASREntityScoringResult .cxx_destruct]
+ -[DODMLASRSchemaDODMLASREntityScoringResult addEntityScores:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult clearEntityScores]
+ -[DODMLASRSchemaDODMLASREntityScoringResult deleteEntityScores]
+ -[DODMLASRSchemaDODMLASREntityScoringResult deleteReferenceName]
+ -[DODMLASRSchemaDODMLASREntityScoringResult dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASREntityScoringResult entityScoresAtIndex:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult entityScoresCount]
+ -[DODMLASRSchemaDODMLASREntityScoringResult entityScores]
+ -[DODMLASRSchemaDODMLASREntityScoringResult hasReferenceName]
+ -[DODMLASRSchemaDODMLASREntityScoringResult hash]
+ -[DODMLASRSchemaDODMLASREntityScoringResult initWithDictionary:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult initWithJSON:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult isEqual:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult jsonData]
+ -[DODMLASRSchemaDODMLASREntityScoringResult readFrom:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult referenceName]
+ -[DODMLASRSchemaDODMLASREntityScoringResult setEntityScores:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult setHasReferenceName:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult setReferenceName:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult writeTo:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASREntityScoringResult(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext .cxx_destruct]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext deleteFullPayloadCorrectionContext]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext deleteOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext fullPayloadCorrectionContext]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext hasFullPayloadCorrectionContext]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext hasOriginalAsrId]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext hash]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext initWithDictionary:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext initWithJSON:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext isEqual:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext jsonData]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext originalAsrId]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext readFrom:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext setFullPayloadCorrectionContext:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext setHasFullPayloadCorrectionContext:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext setHasOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext setOriginalAsrId:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext writeTo:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 .cxx_destruct]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 deleteInfoTier1]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 hasInfoTier1]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 hash]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 infoTier1]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 initWithDictionary:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 initWithJSON:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 isEqual:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 jsonData]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 readFrom:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 setHasInfoTier1:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 setInfoTier1:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1 writeTo:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis .cxx_destruct]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis asrFullPayloadCorrectedToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis asrOutputToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis deleteAsrFullPayloadCorrectedToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis deleteAsrOutputToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis deleteTrueCorrections]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis deleteTrueRegressions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis dictionaryRepresentation]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis hasAsrFullPayloadCorrectedToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis hasAsrOutputToUserEdit]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis hasTrueCorrections]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis hasTrueRegressions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis hash]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis initWithDictionary:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis initWithJSON:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis isEqual:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis jsonData]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis readFrom:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setAsrFullPayloadCorrectedToUserEdit:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setAsrOutputToUserEdit:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setHasAsrFullPayloadCorrectedToUserEdit:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setHasAsrOutputToUserEdit:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setHasTrueCorrections:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setHasTrueRegressions:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setTrueCorrections:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis setTrueRegressions:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis trueCorrections]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis trueRegressions]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis writeTo:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis(SensitiveConditions) suppressMessageUnderConditions]
+ -[DODMLASRSchemaDODMLASRPersonalizationExperimentEnded audioFileResult]
+ -[DODMLASRSchemaDODMLASRPersonalizationExperimentEnded deleteAudioFileResult]
+ -[DODMLASRSchemaDODMLASRPersonalizationExperimentEnded hasAudioFileResult]
+ -[DODMLASRSchemaDODMLASRPersonalizationExperimentEnded setAudioFileResult:]
+ -[DODMLASRSchemaDODMLASRPersonalizationExperimentEnded setHasAudioFileResult:]
+ -[DODMLSchemaDODMLClientEvent contextualReplayBiomeRecordCreated]
+ -[DODMLSchemaDODMLClientEvent contextualReplayBiomeRecordDeleted]
+ -[DODMLSchemaDODMLClientEvent deleteContextualReplayBiomeRecordCreated]
+ -[DODMLSchemaDODMLClientEvent deleteContextualReplayBiomeRecordDeleted]
+ -[DODMLSchemaDODMLClientEvent deleteFullPayloadCorrectionExperimentContext]
+ -[DODMLSchemaDODMLClientEvent deleteFullPayloadCorrectionExperimentPostAnalysis]
+ -[DODMLSchemaDODMLClientEvent deleteFullPayloadCorrectionExperimentTier1]
+ -[DODMLSchemaDODMLClientEvent fullPayloadCorrectionExperimentContext]
+ -[DODMLSchemaDODMLClientEvent fullPayloadCorrectionExperimentPostAnalysis]
+ -[DODMLSchemaDODMLClientEvent fullPayloadCorrectionExperimentTier1]
+ -[DODMLSchemaDODMLClientEvent hasContextualReplayBiomeRecordCreated]
+ -[DODMLSchemaDODMLClientEvent hasContextualReplayBiomeRecordDeleted]
+ -[DODMLSchemaDODMLClientEvent hasFullPayloadCorrectionExperimentContext]
+ -[DODMLSchemaDODMLClientEvent hasFullPayloadCorrectionExperimentPostAnalysis]
+ -[DODMLSchemaDODMLClientEvent hasFullPayloadCorrectionExperimentTier1]
+ -[DODMLSchemaDODMLClientEvent setContextualReplayBiomeRecordCreated:]
+ -[DODMLSchemaDODMLClientEvent setContextualReplayBiomeRecordDeleted:]
+ -[DODMLSchemaDODMLClientEvent setFullPayloadCorrectionExperimentContext:]
+ -[DODMLSchemaDODMLClientEvent setFullPayloadCorrectionExperimentPostAnalysis:]
+ -[DODMLSchemaDODMLClientEvent setFullPayloadCorrectionExperimentTier1:]
+ -[DODMLSchemaDODMLClientEvent setHasContextualReplayBiomeRecordCreated:]
+ -[DODMLSchemaDODMLClientEvent setHasContextualReplayBiomeRecordDeleted:]
+ -[DODMLSchemaDODMLClientEvent setHasFullPayloadCorrectionExperimentContext:]
+ -[DODMLSchemaDODMLClientEvent setHasFullPayloadCorrectionExperimentPostAnalysis:]
+ -[DODMLSchemaDODMLClientEvent setHasFullPayloadCorrectionExperimentTier1:]
+ -[EXPSiriSchemaEXPSiriPegasusResponseSummary deleteIsLowConfidenceKnowledgeResult]
+ -[EXPSiriSchemaEXPSiriPegasusResponseSummary hasIsLowConfidenceKnowledgeResult]
+ -[EXPSiriSchemaEXPSiriPegasusResponseSummary isLowConfidenceKnowledgeResult]
+ -[EXPSiriSchemaEXPSiriPegasusResponseSummary setHasIsLowConfidenceKnowledgeResult:]
+ -[EXPSiriSchemaEXPSiriPegasusResponseSummary setIsLowConfidenceKnowledgeResult:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted appIntentSessionId]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted deleteAppIntentSessionId]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted hasAppIntentSessionId]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted setAppIntentSessionId:]
+ -[ExecutorSiriSchemaExecutorAppIntentCallStarted setHasAppIntentSessionId:]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorIdentifierQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorPersonQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorSearchToolQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorStringQueryEntityCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorStringQueryEntityMatcherCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent deleteExecutorStringQueryLocationCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorIdentifierQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorPersonQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorSearchToolQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorStringQueryEntityCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorStringQueryEntityMatcherCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent executorStringQueryLocationCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorIdentifierQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorPersonQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorSearchToolQueryCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorStringQueryEntityCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorStringQueryEntityMatcherCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent hasExecutorStringQueryLocationCallContext]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorIdentifierQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorPersonQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorSearchToolQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorStringQueryEntityCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorStringQueryEntityMatcherCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setExecutorStringQueryLocationCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorIdentifierQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorPersonQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorSearchToolQueryCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorStringQueryEntityCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorStringQueryEntityMatcherCallContext:]
+ -[ExecutorSiriSchemaExecutorClientEvent setHasExecutorStringQueryLocationCallContext:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext ended]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext failed]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext hash]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded exists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded hash]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed exists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed hash]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted exists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted hash]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorIdentifierQueryCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext ended]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext failed]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext hash]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded exists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded hash]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed exists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed hash]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted exists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted hash]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorPersonQueryCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext deleteTraceId]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext ended]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext failed]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext hasTraceId]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext hash]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setHasTraceId:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext setTraceId:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext traceId]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded exists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded hash]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed exists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed hash]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted deleteExecutorSearchToolQueryType]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted executorSearchToolQueryType]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted exists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted hasExecutorSearchToolQueryType]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted hash]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted setExecutorSearchToolQueryType:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted setHasExecutorSearchToolQueryType:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorSearchToolQueryCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext ended]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext failed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext ended]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext failed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted exists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted hash]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext .cxx_destruct]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext deleteEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext deleteFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext deleteStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext ended]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext failed]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext hasEnded]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext hasFailed]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext hasStartedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext hash]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setHasEnded:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setHasFailed:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setHasStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext setStartedOrChanged:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext startedOrChanged]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext whichContextevent]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded exists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded hash]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed exists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed hash]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted deleteExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted dictionaryRepresentation]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted exists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted hasExists]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted hash]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted initWithDictionary:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted initWithJSON:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted isEqual:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted jsonData]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted readFrom:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted setExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted setHasExists:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted writeTo:]
+ -[ExecutorSiriSchemaExecutorStringQueryLocationCallStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWClientEvent deleteFlowContactTier1]
+ -[FLOWSchemaFLOWClientEvent flowContactTier1]
+ -[FLOWSchemaFLOWClientEvent hasFlowContactTier1]
+ -[FLOWSchemaFLOWClientEvent setFlowContactTier1:]
+ -[FLOWSchemaFLOWClientEvent setHasFlowContactTier1:]
+ -[FLOWSchemaFLOWContact .cxx_destruct]
+ -[FLOWSchemaFLOWContact deleteIsRelationship]
+ -[FLOWSchemaFLOWContact deleteIsUnnamedPhoneNumber]
+ -[FLOWSchemaFLOWContact deleteLinkId]
+ -[FLOWSchemaFLOWContact dictionaryRepresentation]
+ -[FLOWSchemaFLOWContact hasIsRelationship]
+ -[FLOWSchemaFLOWContact hasIsUnnamedPhoneNumber]
+ -[FLOWSchemaFLOWContact hasLinkId]
+ -[FLOWSchemaFLOWContact hash]
+ -[FLOWSchemaFLOWContact initWithDictionary:]
+ -[FLOWSchemaFLOWContact initWithJSON:]
+ -[FLOWSchemaFLOWContact isEqual:]
+ -[FLOWSchemaFLOWContact isRelationship]
+ -[FLOWSchemaFLOWContact isUnnamedPhoneNumber]
+ -[FLOWSchemaFLOWContact jsonData]
+ -[FLOWSchemaFLOWContact linkId]
+ -[FLOWSchemaFLOWContact readFrom:]
+ -[FLOWSchemaFLOWContact setHasIsRelationship:]
+ -[FLOWSchemaFLOWContact setHasIsUnnamedPhoneNumber:]
+ -[FLOWSchemaFLOWContact setHasLinkId:]
+ -[FLOWSchemaFLOWContact setIsRelationship:]
+ -[FLOWSchemaFLOWContact setIsUnnamedPhoneNumber:]
+ -[FLOWSchemaFLOWContact setLinkId:]
+ -[FLOWSchemaFLOWContact writeTo:]
+ -[FLOWSchemaFLOWContact(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWContact(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWContactTier1 .cxx_destruct]
+ -[FLOWSchemaFLOWContactTier1 contactName]
+ -[FLOWSchemaFLOWContactTier1 deleteContactName]
+ -[FLOWSchemaFLOWContactTier1 deleteLinkId]
+ -[FLOWSchemaFLOWContactTier1 dictionaryRepresentation]
+ -[FLOWSchemaFLOWContactTier1 hasContactName]
+ -[FLOWSchemaFLOWContactTier1 hasLinkId]
+ -[FLOWSchemaFLOWContactTier1 hash]
+ -[FLOWSchemaFLOWContactTier1 initWithDictionary:]
+ -[FLOWSchemaFLOWContactTier1 initWithJSON:]
+ -[FLOWSchemaFLOWContactTier1 isEqual:]
+ -[FLOWSchemaFLOWContactTier1 jsonData]
+ -[FLOWSchemaFLOWContactTier1 linkId]
+ -[FLOWSchemaFLOWContactTier1 readFrom:]
+ -[FLOWSchemaFLOWContactTier1 setContactName:]
+ -[FLOWSchemaFLOWContactTier1 setHasContactName:]
+ -[FLOWSchemaFLOWContactTier1 setHasLinkId:]
+ -[FLOWSchemaFLOWContactTier1 setLinkId:]
+ -[FLOWSchemaFLOWContactTier1 writeTo:]
+ -[FLOWSchemaFLOWContactTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWContactTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWDomainExecutionMetadata .cxx_destruct]
+ -[FLOWSchemaFLOWDomainExecutionMetadata deleteDomainExecutionAppIntentBundleID]
+ -[FLOWSchemaFLOWDomainExecutionMetadata dictionaryRepresentation]
+ -[FLOWSchemaFLOWDomainExecutionMetadata domainExecutionAppIntentBundleID]
+ -[FLOWSchemaFLOWDomainExecutionMetadata hasDomainExecutionAppIntentBundleID]
+ -[FLOWSchemaFLOWDomainExecutionMetadata hash]
+ -[FLOWSchemaFLOWDomainExecutionMetadata initWithDictionary:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata initWithJSON:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata isEqual:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata jsonData]
+ -[FLOWSchemaFLOWDomainExecutionMetadata readFrom:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata setDomainExecutionAppIntentBundleID:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata setHasDomainExecutionAppIntentBundleID:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata writeTo:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWDomainExecutionMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWDomainExecutionStarted .cxx_destruct]
+ -[FLOWSchemaFLOWDomainExecutionStarted deleteDomainExecutionMetadata]
+ -[FLOWSchemaFLOWDomainExecutionStarted domainExecutionMetadata]
+ -[FLOWSchemaFLOWDomainExecutionStarted hasDomainExecutionMetadata]
+ -[FLOWSchemaFLOWDomainExecutionStarted setDomainExecutionMetadata:]
+ -[FLOWSchemaFLOWDomainExecutionStarted setHasDomainExecutionMetadata:]
+ -[FLOWSchemaFLOWDomainExecutionStarted(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWPhoneCallContext contact]
+ -[FLOWSchemaFLOWPhoneCallContext deleteContact]
+ -[FLOWSchemaFLOWPhoneCallContext hasContact]
+ -[FLOWSchemaFLOWPhoneCallContext setContact:]
+ -[FLOWSchemaFLOWPhoneCallContext setHasContact:]
+ -[FLOWSchemaFLOWSmsContext contact]
+ -[FLOWSchemaFLOWSmsContext deleteContact]
+ -[FLOWSchemaFLOWSmsContext hasContact]
+ -[FLOWSchemaFLOWSmsContext setContact:]
+ -[FLOWSchemaFLOWSmsContext setHasContact:]
+ -[FLSchemaFLActionEvaluationContext contextId]
+ -[FLSchemaFLActionEvaluationContext deleteContextId]
+ -[FLSchemaFLActionEvaluationContext hasContextId]
+ -[FLSchemaFLActionEvaluationContext setContextId:]
+ -[FLSchemaFLActionEvaluationContext setHasContextId:]
+ -[FLSchemaFLInteractionDonationContext contextId]
+ -[FLSchemaFLInteractionDonationContext deleteContextId]
+ -[FLSchemaFLInteractionDonationContext hasContextId]
+ -[FLSchemaFLInteractionDonationContext setContextId:]
+ -[FLSchemaFLInteractionDonationContext setHasContextId:]
+ -[GMSSchemaGMSModelRequestFailed .cxx_destruct]
+ -[GMSSchemaGMSModelRequestFailed deleteErrorCode]
+ -[GMSSchemaGMSModelRequestFailed deleteErrorDomainString]
+ -[GMSSchemaGMSModelRequestFailed errorCode]
+ -[GMSSchemaGMSModelRequestFailed errorDomainString]
+ -[GMSSchemaGMSModelRequestFailed hasErrorCode]
+ -[GMSSchemaGMSModelRequestFailed hasErrorDomainString]
+ -[GMSSchemaGMSModelRequestFailed setErrorCode:]
+ -[GMSSchemaGMSModelRequestFailed setErrorDomainString:]
+ -[GMSSchemaGMSModelRequestFailed setHasErrorCode:]
+ -[GMSSchemaGMSModelRequestFailed setHasErrorDomainString:]
+ -[IFTSchemaIFTAction actionParameterValuesAtIndex:]
+ -[IFTSchemaIFTAction actionParameterValuesCount]
+ -[IFTSchemaIFTAction actionParameterValues]
+ -[IFTSchemaIFTAction addActionParameterValues:]
+ -[IFTSchemaIFTAction clearActionParameterValues]
+ -[IFTSchemaIFTAction deleteActionParameterValues]
+ -[IFTSchemaIFTAction setActionParameterValues:]
+ -[IFTSchemaIFTActionConfirmation .cxx_destruct]
+ -[IFTSchemaIFTActionConfirmation deleteSystemStyle]
+ -[IFTSchemaIFTActionConfirmation hasSystemStyle]
+ -[IFTSchemaIFTActionConfirmation setHasSystemStyle:]
+ -[IFTSchemaIFTActionConfirmation setSystemStyle:]
+ -[IFTSchemaIFTActionConfirmation systemStyle]
+ -[IFTSchemaIFTActionConfirmation(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle .cxx_destruct]
+ -[IFTSchemaIFTActionConfirmationSystemStyle deleteGenerativeAIEnablement]
+ -[IFTSchemaIFTActionConfirmationSystemStyle dictionaryRepresentation]
+ -[IFTSchemaIFTActionConfirmationSystemStyle generativeAIEnablement]
+ -[IFTSchemaIFTActionConfirmationSystemStyle hasGenerativeAIEnablement]
+ -[IFTSchemaIFTActionConfirmationSystemStyle hash]
+ -[IFTSchemaIFTActionConfirmationSystemStyle initWithDictionary:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle initWithJSON:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle isEqual:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle jsonData]
+ -[IFTSchemaIFTActionConfirmationSystemStyle readFrom:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle setGenerativeAIEnablement:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle setHasGenerativeAIEnablement:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle whichOneof_Actionconfirmationsystemstyle]
+ -[IFTSchemaIFTActionConfirmationSystemStyle writeTo:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTActionConfirmationSystemStyle(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement .cxx_destruct]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement bundleId]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement deleteBundleId]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement deleteIsExplicit]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement deleteSource]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement dictionaryRepresentation]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement hasBundleId]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement hasIsExplicit]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement hasSource]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement hash]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement initWithDictionary:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement initWithJSON:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement isEqual:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement isExplicit]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement jsonData]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement readFrom:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setBundleId:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setHasBundleId:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setHasIsExplicit:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setHasSource:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setIsExplicit:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement setSource:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement source]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement writeTo:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTActionFailureFailure deleteUnableToCancel]
+ -[IFTSchemaIFTActionFailureFailure hasUnableToCancel]
+ -[IFTSchemaIFTActionFailureFailure setHasUnableToCancel:]
+ -[IFTSchemaIFTActionFailureFailure setUnableToCancel:]
+ -[IFTSchemaIFTActionFailureFailure unableToCancel]
+ -[IFTSchemaIFTActionParameterContext actionClass]
+ -[IFTSchemaIFTActionParameterContext deleteActionClass]
+ -[IFTSchemaIFTActionParameterContext hasActionClass]
+ -[IFTSchemaIFTActionParameterContext setActionClass:]
+ -[IFTSchemaIFTActionParameterContext setHasActionClass:]
+ -[IFTSchemaIFTActionParameterValue confirmed]
+ -[IFTSchemaIFTActionParameterValue deleteConfirmed]
+ -[IFTSchemaIFTActionParameterValue deleteDenied]
+ -[IFTSchemaIFTActionParameterValue deleteSelectedInDisambiguation]
+ -[IFTSchemaIFTActionParameterValue denied]
+ -[IFTSchemaIFTActionParameterValue dictionaryRepresentation]
+ -[IFTSchemaIFTActionParameterValue hasConfirmed]
+ -[IFTSchemaIFTActionParameterValue hasDenied]
+ -[IFTSchemaIFTActionParameterValue hasSelectedInDisambiguation]
+ -[IFTSchemaIFTActionParameterValue hash]
+ -[IFTSchemaIFTActionParameterValue initWithDictionary:]
+ -[IFTSchemaIFTActionParameterValue initWithJSON:]
+ -[IFTSchemaIFTActionParameterValue isEqual:]
+ -[IFTSchemaIFTActionParameterValue jsonData]
+ -[IFTSchemaIFTActionParameterValue readFrom:]
+ -[IFTSchemaIFTActionParameterValue selectedInDisambiguation]
+ -[IFTSchemaIFTActionParameterValue setConfirmed:]
+ -[IFTSchemaIFTActionParameterValue setDenied:]
+ -[IFTSchemaIFTActionParameterValue setHasConfirmed:]
+ -[IFTSchemaIFTActionParameterValue setHasDenied:]
+ -[IFTSchemaIFTActionParameterValue setHasSelectedInDisambiguation:]
+ -[IFTSchemaIFTActionParameterValue setSelectedInDisambiguation:]
+ -[IFTSchemaIFTActionParameterValue whichOneof_Promptselection]
+ -[IFTSchemaIFTActionParameterValue writeTo:]
+ -[IFTSchemaIFTActionParameterValue(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTActionSuccess deleteShouldOpen]
+ -[IFTSchemaIFTActionSuccess hasShouldOpen]
+ -[IFTSchemaIFTActionSuccess setHasShouldOpen:]
+ -[IFTSchemaIFTActionSuccess setShouldOpen:]
+ -[IFTSchemaIFTActionSuccess shouldOpen]
+ -[IFTSchemaIFTCallExpression addParameters:]
+ -[IFTSchemaIFTCallExpression clearParameters]
+ -[IFTSchemaIFTCallExpression deleteParameters]
+ -[IFTSchemaIFTCallExpression parametersAtIndex:]
+ -[IFTSchemaIFTCallExpression parametersCount]
+ -[IFTSchemaIFTCallExpression parameters]
+ -[IFTSchemaIFTCallExpression setParameters:]
+ -[IFTSchemaIFTCallExpressionParameters .cxx_destruct]
+ -[IFTSchemaIFTCallExpressionParameters callParameterName]
+ -[IFTSchemaIFTCallExpressionParameters deleteCallParameterName]
+ -[IFTSchemaIFTCallExpressionParameters deleteStatementId]
+ -[IFTSchemaIFTCallExpressionParameters dictionaryRepresentation]
+ -[IFTSchemaIFTCallExpressionParameters hasCallParameterName]
+ -[IFTSchemaIFTCallExpressionParameters hasStatementId]
+ -[IFTSchemaIFTCallExpressionParameters hash]
+ -[IFTSchemaIFTCallExpressionParameters initWithDictionary:]
+ -[IFTSchemaIFTCallExpressionParameters initWithJSON:]
+ -[IFTSchemaIFTCallExpressionParameters isEqual:]
+ -[IFTSchemaIFTCallExpressionParameters jsonData]
+ -[IFTSchemaIFTCallExpressionParameters readFrom:]
+ -[IFTSchemaIFTCallExpressionParameters setCallParameterName:]
+ -[IFTSchemaIFTCallExpressionParameters setHasCallParameterName:]
+ -[IFTSchemaIFTCallExpressionParameters setHasStatementId:]
+ -[IFTSchemaIFTCallExpressionParameters setStatementId:]
+ -[IFTSchemaIFTCallExpressionParameters statementId]
+ -[IFTSchemaIFTCallExpressionParameters writeTo:]
+ -[IFTSchemaIFTCallExpressionParameters(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTCallExpressionParameters(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTClientEvent deleteQueryDecorationPrePlannerResult]
+ -[IFTSchemaIFTClientEvent deleteSkipStatement]
+ -[IFTSchemaIFTClientEvent hasQueryDecorationPrePlannerResult]
+ -[IFTSchemaIFTClientEvent hasSkipStatement]
+ -[IFTSchemaIFTClientEvent queryDecorationPrePlannerResult]
+ -[IFTSchemaIFTClientEvent setHasQueryDecorationPrePlannerResult:]
+ -[IFTSchemaIFTClientEvent setHasSkipStatement:]
+ -[IFTSchemaIFTClientEvent setQueryDecorationPrePlannerResult:]
+ -[IFTSchemaIFTClientEvent setSkipStatement:]
+ -[IFTSchemaIFTClientEvent skipStatement]
+ -[IFTSchemaIFTExpression deleteFormat]
+ -[IFTSchemaIFTExpression deletePayload]
+ -[IFTSchemaIFTExpression deleteStructuredSearch]
+ -[IFTSchemaIFTExpression format]
+ -[IFTSchemaIFTExpression hasFormat]
+ -[IFTSchemaIFTExpression hasPayload]
+ -[IFTSchemaIFTExpression hasStructuredSearch]
+ -[IFTSchemaIFTExpression payload]
+ -[IFTSchemaIFTExpression setFormat:]
+ -[IFTSchemaIFTExpression setHasFormat:]
+ -[IFTSchemaIFTExpression setHasPayload:]
+ -[IFTSchemaIFTExpression setHasStructuredSearch:]
+ -[IFTSchemaIFTExpression setPayload:]
+ -[IFTSchemaIFTExpression setStructuredSearch:]
+ -[IFTSchemaIFTExpression structuredSearch]
+ -[IFTSchemaIFTFormatExpression .cxx_destruct]
+ -[IFTSchemaIFTFormatExpression addStatementIds:]
+ -[IFTSchemaIFTFormatExpression clearStatementIds]
+ -[IFTSchemaIFTFormatExpression deleteStatementIds]
+ -[IFTSchemaIFTFormatExpression dictionaryRepresentation]
+ -[IFTSchemaIFTFormatExpression hash]
+ -[IFTSchemaIFTFormatExpression initWithDictionary:]
+ -[IFTSchemaIFTFormatExpression initWithJSON:]
+ -[IFTSchemaIFTFormatExpression isEqual:]
+ -[IFTSchemaIFTFormatExpression jsonData]
+ -[IFTSchemaIFTFormatExpression readFrom:]
+ -[IFTSchemaIFTFormatExpression setStatementIds:]
+ -[IFTSchemaIFTFormatExpression statementIdsAtIndex:]
+ -[IFTSchemaIFTFormatExpression statementIdsCount]
+ -[IFTSchemaIFTFormatExpression statementIds]
+ -[IFTSchemaIFTFormatExpression writeTo:]
+ -[IFTSchemaIFTFormatExpression(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTFormatExpression(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTParameterNotAllowed deleteReason]
+ -[IFTSchemaIFTParameterNotAllowed hasReason]
+ -[IFTSchemaIFTParameterNotAllowed reason]
+ -[IFTSchemaIFTParameterNotAllowed setHasReason:]
+ -[IFTSchemaIFTParameterNotAllowed setReason:]
+ -[IFTSchemaIFTPayloadExpression .cxx_destruct]
+ -[IFTSchemaIFTPayloadExpression addStatementIds:]
+ -[IFTSchemaIFTPayloadExpression clearStatementIds]
+ -[IFTSchemaIFTPayloadExpression deleteStatementIds]
+ -[IFTSchemaIFTPayloadExpression dictionaryRepresentation]
+ -[IFTSchemaIFTPayloadExpression hash]
+ -[IFTSchemaIFTPayloadExpression initWithDictionary:]
+ -[IFTSchemaIFTPayloadExpression initWithJSON:]
+ -[IFTSchemaIFTPayloadExpression isEqual:]
+ -[IFTSchemaIFTPayloadExpression jsonData]
+ -[IFTSchemaIFTPayloadExpression readFrom:]
+ -[IFTSchemaIFTPayloadExpression setStatementIds:]
+ -[IFTSchemaIFTPayloadExpression statementIdsAtIndex:]
+ -[IFTSchemaIFTPayloadExpression statementIdsCount]
+ -[IFTSchemaIFTPayloadExpression statementIds]
+ -[IFTSchemaIFTPayloadExpression writeTo:]
+ -[IFTSchemaIFTPayloadExpression(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTPayloadExpression(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTPrimitive deletePrimitiveType]
+ -[IFTSchemaIFTPrimitive hasPrimitiveType]
+ -[IFTSchemaIFTPrimitive primitiveType]
+ -[IFTSchemaIFTPrimitive setHasPrimitiveType:]
+ -[IFTSchemaIFTPrimitive setPrimitiveType:]
+ -[IFTSchemaIFTProgramStatement deleteIsRoot]
+ -[IFTSchemaIFTProgramStatement hasIsRoot]
+ -[IFTSchemaIFTProgramStatement isRoot]
+ -[IFTSchemaIFTProgramStatement setHasIsRoot:]
+ -[IFTSchemaIFTProgramStatement setIsRoot:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult deleteExists]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult dictionaryRepresentation]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult exists]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult hasExists]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult hash]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult initWithDictionary:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult initWithJSON:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult isEqual:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult jsonData]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult readFrom:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult setExists:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult setHasExists:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult writeTo:]
+ -[IFTSchemaIFTQueryDecorationPrePlannerResult(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTQueryStep context]
+ -[IFTSchemaIFTQueryStep deleteContext]
+ -[IFTSchemaIFTQueryStep deletePayloadType]
+ -[IFTSchemaIFTQueryStep hasContext]
+ -[IFTSchemaIFTQueryStep hasPayloadType]
+ -[IFTSchemaIFTQueryStep payloadType]
+ -[IFTSchemaIFTQueryStep setContext:]
+ -[IFTSchemaIFTQueryStep setHasContext:]
+ -[IFTSchemaIFTQueryStep setHasPayloadType:]
+ -[IFTSchemaIFTQueryStep setPayloadType:]
+ -[IFTSchemaIFTSessionCoordinatorError deleteFailedToConvertClientEvent]
+ -[IFTSchemaIFTSessionCoordinatorError failedToConvertClientEvent]
+ -[IFTSchemaIFTSessionCoordinatorError hasFailedToConvertClientEvent]
+ -[IFTSchemaIFTSessionCoordinatorError setFailedToConvertClientEvent:]
+ -[IFTSchemaIFTSessionCoordinatorError setHasFailedToConvertClientEvent:]
+ -[IFTSchemaIFTSkipStatement .cxx_destruct]
+ -[IFTSchemaIFTSkipStatement deleteStatementId]
+ -[IFTSchemaIFTSkipStatement dictionaryRepresentation]
+ -[IFTSchemaIFTSkipStatement hasStatementId]
+ -[IFTSchemaIFTSkipStatement hash]
+ -[IFTSchemaIFTSkipStatement initWithDictionary:]
+ -[IFTSchemaIFTSkipStatement initWithJSON:]
+ -[IFTSchemaIFTSkipStatement isEqual:]
+ -[IFTSchemaIFTSkipStatement jsonData]
+ -[IFTSchemaIFTSkipStatement readFrom:]
+ -[IFTSchemaIFTSkipStatement setHasStatementId:]
+ -[IFTSchemaIFTSkipStatement setStatementId:]
+ -[IFTSchemaIFTSkipStatement statementId]
+ -[IFTSchemaIFTSkipStatement writeTo:]
+ -[IFTSchemaIFTSkipStatement(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTSkipStatement(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTStructuredSearchExpression .cxx_destruct]
+ -[IFTSchemaIFTStructuredSearchExpression addParameters:]
+ -[IFTSchemaIFTStructuredSearchExpression addProperties:]
+ -[IFTSchemaIFTStructuredSearchExpression clearParameters]
+ -[IFTSchemaIFTStructuredSearchExpression clearProperties]
+ -[IFTSchemaIFTStructuredSearchExpression deleteIsExpanded]
+ -[IFTSchemaIFTStructuredSearchExpression deleteParameters]
+ -[IFTSchemaIFTStructuredSearchExpression deleteProperties]
+ -[IFTSchemaIFTStructuredSearchExpression deleteReturnType]
+ -[IFTSchemaIFTStructuredSearchExpression dictionaryRepresentation]
+ -[IFTSchemaIFTStructuredSearchExpression hasIsExpanded]
+ -[IFTSchemaIFTStructuredSearchExpression hasReturnType]
+ -[IFTSchemaIFTStructuredSearchExpression hash]
+ -[IFTSchemaIFTStructuredSearchExpression initWithDictionary:]
+ -[IFTSchemaIFTStructuredSearchExpression initWithJSON:]
+ -[IFTSchemaIFTStructuredSearchExpression isEqual:]
+ -[IFTSchemaIFTStructuredSearchExpression isExpanded]
+ -[IFTSchemaIFTStructuredSearchExpression jsonData]
+ -[IFTSchemaIFTStructuredSearchExpression parametersAtIndex:]
+ -[IFTSchemaIFTStructuredSearchExpression parametersCount]
+ -[IFTSchemaIFTStructuredSearchExpression parameters]
+ -[IFTSchemaIFTStructuredSearchExpression propertiesAtIndex:]
+ -[IFTSchemaIFTStructuredSearchExpression propertiesCount]
+ -[IFTSchemaIFTStructuredSearchExpression properties]
+ -[IFTSchemaIFTStructuredSearchExpression readFrom:]
+ -[IFTSchemaIFTStructuredSearchExpression returnType]
+ -[IFTSchemaIFTStructuredSearchExpression setHasIsExpanded:]
+ -[IFTSchemaIFTStructuredSearchExpression setHasReturnType:]
+ -[IFTSchemaIFTStructuredSearchExpression setIsExpanded:]
+ -[IFTSchemaIFTStructuredSearchExpression setParameters:]
+ -[IFTSchemaIFTStructuredSearchExpression setProperties:]
+ -[IFTSchemaIFTStructuredSearchExpression setReturnType:]
+ -[IFTSchemaIFTStructuredSearchExpression writeTo:]
+ -[IFTSchemaIFTStructuredSearchExpression(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTStructuredSearchExpression(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters .cxx_destruct]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters deleteStatementId]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters deleteStructuredSearchParameterName]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters dictionaryRepresentation]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters hasStatementId]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters hasStructuredSearchParameterName]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters hash]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters initWithDictionary:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters initWithJSON:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters isEqual:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters jsonData]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters readFrom:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters setHasStatementId:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters setHasStructuredSearchParameterName:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters setStatementId:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters setStructuredSearchParameterName:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters statementId]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters structuredSearchParameterName]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters writeTo:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTStructuredSearchExpressionParameters(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTStructuredSearchProperty deleteExists]
+ -[IFTSchemaIFTStructuredSearchProperty dictionaryRepresentation]
+ -[IFTSchemaIFTStructuredSearchProperty exists]
+ -[IFTSchemaIFTStructuredSearchProperty hasExists]
+ -[IFTSchemaIFTStructuredSearchProperty hash]
+ -[IFTSchemaIFTStructuredSearchProperty initWithDictionary:]
+ -[IFTSchemaIFTStructuredSearchProperty initWithJSON:]
+ -[IFTSchemaIFTStructuredSearchProperty isEqual:]
+ -[IFTSchemaIFTStructuredSearchProperty jsonData]
+ -[IFTSchemaIFTStructuredSearchProperty readFrom:]
+ -[IFTSchemaIFTStructuredSearchProperty setExists:]
+ -[IFTSchemaIFTStructuredSearchProperty setHasExists:]
+ -[IFTSchemaIFTStructuredSearchProperty writeTo:]
+ -[IFTSchemaIFTStructuredSearchProperty(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTTypeInstance .cxx_destruct]
+ -[IFTSchemaIFTTypeInstance collection]
+ -[IFTSchemaIFTTypeInstance deleteCollection]
+ -[IFTSchemaIFTTypeInstance deleteTypeIdentifier]
+ -[IFTSchemaIFTTypeInstance dictionaryRepresentation]
+ -[IFTSchemaIFTTypeInstance hasCollection]
+ -[IFTSchemaIFTTypeInstance hasTypeIdentifier]
+ -[IFTSchemaIFTTypeInstance hash]
+ -[IFTSchemaIFTTypeInstance initWithDictionary:]
+ -[IFTSchemaIFTTypeInstance initWithJSON:]
+ -[IFTSchemaIFTTypeInstance isEqual:]
+ -[IFTSchemaIFTTypeInstance jsonData]
+ -[IFTSchemaIFTTypeInstance readFrom:]
+ -[IFTSchemaIFTTypeInstance setCollection:]
+ -[IFTSchemaIFTTypeInstance setHasCollection:]
+ -[IFTSchemaIFTTypeInstance setHasTypeIdentifier:]
+ -[IFTSchemaIFTTypeInstance setTypeIdentifier:]
+ -[IFTSchemaIFTTypeInstance typeIdentifier]
+ -[IFTSchemaIFTTypeInstance whichItemtype]
+ -[IFTSchemaIFTTypeInstance writeTo:]
+ -[IFTSchemaIFTTypeInstance(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTTypeInstance(SensitiveConditions) suppressMessageUnderConditions]
+ -[IFTSchemaIFTValueExpression .cxx_destruct]
+ -[IFTSchemaIFTValueExpression array]
+ -[IFTSchemaIFTValueExpression deleteArray]
+ -[IFTSchemaIFTValueExpression hasArray]
+ -[IFTSchemaIFTValueExpression setArray:]
+ -[IFTSchemaIFTValueExpression setHasArray:]
+ -[IFTSchemaIFTValueExpression(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTValueExpressionArrayVariant .cxx_destruct]
+ -[IFTSchemaIFTValueExpressionArrayVariant addStatementId:]
+ -[IFTSchemaIFTValueExpressionArrayVariant clearStatementId]
+ -[IFTSchemaIFTValueExpressionArrayVariant deleteStatementId]
+ -[IFTSchemaIFTValueExpressionArrayVariant dictionaryRepresentation]
+ -[IFTSchemaIFTValueExpressionArrayVariant hash]
+ -[IFTSchemaIFTValueExpressionArrayVariant initWithDictionary:]
+ -[IFTSchemaIFTValueExpressionArrayVariant initWithJSON:]
+ -[IFTSchemaIFTValueExpressionArrayVariant isEqual:]
+ -[IFTSchemaIFTValueExpressionArrayVariant jsonData]
+ -[IFTSchemaIFTValueExpressionArrayVariant readFrom:]
+ -[IFTSchemaIFTValueExpressionArrayVariant setStatementIds:]
+ -[IFTSchemaIFTValueExpressionArrayVariant statementIdAtIndex:]
+ -[IFTSchemaIFTValueExpressionArrayVariant statementIdCount]
+ -[IFTSchemaIFTValueExpressionArrayVariant statementIds]
+ -[IFTSchemaIFTValueExpressionArrayVariant writeTo:]
+ -[IFTSchemaIFTValueExpressionArrayVariant(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IFTSchemaIFTValueExpressionArrayVariant(SensitiveConditions) suppressMessageUnderConditions]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals deleteIsDefaultApp]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals deleteIsRequestByHandleType]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals deleteIsRequestByLabel]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals hasIsDefaultApp]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals hasIsRequestByHandleType]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals hasIsRequestByLabel]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals isDefaultApp]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals isRequestByHandleType]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals isRequestByLabel]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setHasIsDefaultApp:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setHasIsRequestByHandleType:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setHasIsRequestByLabel:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setIsDefaultApp:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setIsRequestByHandleType:]
+ -[INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals setIsRequestByLabel:]
+ -[JRSchemaHistoricalLocationContext .cxx_destruct]
+ -[JRSchemaHistoricalLocationContext anonymizedLocationNameId]
+ -[JRSchemaHistoricalLocationContext anonymizedLocationTypeId]
+ -[JRSchemaHistoricalLocationContext bucketedDistance]
+ -[JRSchemaHistoricalLocationContext deleteAnonymizedLocationNameId]
+ -[JRSchemaHistoricalLocationContext deleteAnonymizedLocationTypeId]
+ -[JRSchemaHistoricalLocationContext deleteBucketedDistance]
+ -[JRSchemaHistoricalLocationContext deleteLogOfTimeElapsedInSeconds]
+ -[JRSchemaHistoricalLocationContext dictionaryRepresentation]
+ -[JRSchemaHistoricalLocationContext hasAnonymizedLocationNameId]
+ -[JRSchemaHistoricalLocationContext hasAnonymizedLocationTypeId]
+ -[JRSchemaHistoricalLocationContext hasBucketedDistance]
+ -[JRSchemaHistoricalLocationContext hasLogOfTimeElapsedInSeconds]
+ -[JRSchemaHistoricalLocationContext hash]
+ -[JRSchemaHistoricalLocationContext initWithDictionary:]
+ -[JRSchemaHistoricalLocationContext initWithJSON:]
+ -[JRSchemaHistoricalLocationContext isEqual:]
+ -[JRSchemaHistoricalLocationContext jsonData]
+ -[JRSchemaHistoricalLocationContext logOfTimeElapsedInSeconds]
+ -[JRSchemaHistoricalLocationContext readFrom:]
+ -[JRSchemaHistoricalLocationContext setAnonymizedLocationNameId:]
+ -[JRSchemaHistoricalLocationContext setAnonymizedLocationTypeId:]
+ -[JRSchemaHistoricalLocationContext setBucketedDistance:]
+ -[JRSchemaHistoricalLocationContext setHasAnonymizedLocationNameId:]
+ -[JRSchemaHistoricalLocationContext setHasAnonymizedLocationTypeId:]
+ -[JRSchemaHistoricalLocationContext setHasBucketedDistance:]
+ -[JRSchemaHistoricalLocationContext setHasLogOfTimeElapsedInSeconds:]
+ -[JRSchemaHistoricalLocationContext setLogOfTimeElapsedInSeconds:]
+ -[JRSchemaHistoricalLocationContext writeTo:]
+ -[JRSchemaHistoricalLocationContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[JRSchemaHistoricalLocationContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaIntervalUntilStartTime .cxx_destruct]
+ -[JRSchemaIntervalUntilStartTime addCandidateBooleanMask:]
+ -[JRSchemaIntervalUntilStartTime addCandidateTimeIntervalMatrix:]
+ -[JRSchemaIntervalUntilStartTime candidateBooleanMaskAtIndex:]
+ -[JRSchemaIntervalUntilStartTime candidateBooleanMaskCount]
+ -[JRSchemaIntervalUntilStartTime candidateBooleanMasks]
+ -[JRSchemaIntervalUntilStartTime candidateTimeIntervalMatrixAtIndex:]
+ -[JRSchemaIntervalUntilStartTime candidateTimeIntervalMatrixCount]
+ -[JRSchemaIntervalUntilStartTime candidateTimeIntervalMatrixs]
+ -[JRSchemaIntervalUntilStartTime clearCandidateBooleanMask]
+ -[JRSchemaIntervalUntilStartTime clearCandidateTimeIntervalMatrix]
+ -[JRSchemaIntervalUntilStartTime deleteCandidateBooleanMask]
+ -[JRSchemaIntervalUntilStartTime deleteCandidateTimeIntervalMatrix]
+ -[JRSchemaIntervalUntilStartTime dictionaryRepresentation]
+ -[JRSchemaIntervalUntilStartTime hash]
+ -[JRSchemaIntervalUntilStartTime initWithDictionary:]
+ -[JRSchemaIntervalUntilStartTime initWithJSON:]
+ -[JRSchemaIntervalUntilStartTime isEqual:]
+ -[JRSchemaIntervalUntilStartTime jsonData]
+ -[JRSchemaIntervalUntilStartTime readFrom:]
+ -[JRSchemaIntervalUntilStartTime setCandidateBooleanMasks:]
+ -[JRSchemaIntervalUntilStartTime setCandidateTimeIntervalMatrixs:]
+ -[JRSchemaIntervalUntilStartTime writeTo:]
+ -[JRSchemaIntervalUntilStartTime(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[JRSchemaIntervalUntilStartTime(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJRCandidateBooleanMask .cxx_destruct]
+ -[JRSchemaJRCandidateBooleanMask addIsApplicableToCandidate:]
+ -[JRSchemaJRCandidateBooleanMask clearIsApplicableToCandidate]
+ -[JRSchemaJRCandidateBooleanMask deleteIsApplicableToCandidate]
+ -[JRSchemaJRCandidateBooleanMask dictionaryRepresentation]
+ -[JRSchemaJRCandidateBooleanMask hash]
+ -[JRSchemaJRCandidateBooleanMask initWithDictionary:]
+ -[JRSchemaJRCandidateBooleanMask initWithJSON:]
+ -[JRSchemaJRCandidateBooleanMask isApplicableToCandidateAtIndex:]
+ -[JRSchemaJRCandidateBooleanMask isApplicableToCandidateCount]
+ -[JRSchemaJRCandidateBooleanMask isApplicableToCandidates]
+ -[JRSchemaJRCandidateBooleanMask isEqual:]
+ -[JRSchemaJRCandidateBooleanMask jsonData]
+ -[JRSchemaJRCandidateBooleanMask readFrom:]
+ -[JRSchemaJRCandidateBooleanMask setIsApplicableToCandidates:]
+ -[JRSchemaJRCandidateBooleanMask writeTo:]
+ -[JRSchemaJRCandidateBooleanMask(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJRCandidateRiskLevel .cxx_destruct]
+ -[JRSchemaJRCandidateRiskLevel addRiskLevel:]
+ -[JRSchemaJRCandidateRiskLevel clearRiskLevel]
+ -[JRSchemaJRCandidateRiskLevel deleteRiskLevel]
+ -[JRSchemaJRCandidateRiskLevel dictionaryRepresentation]
+ -[JRSchemaJRCandidateRiskLevel hash]
+ -[JRSchemaJRCandidateRiskLevel initWithDictionary:]
+ -[JRSchemaJRCandidateRiskLevel initWithJSON:]
+ -[JRSchemaJRCandidateRiskLevel isEqual:]
+ -[JRSchemaJRCandidateRiskLevel jsonData]
+ -[JRSchemaJRCandidateRiskLevel readFrom:]
+ -[JRSchemaJRCandidateRiskLevel riskLevelAtIndex:]
+ -[JRSchemaJRCandidateRiskLevel riskLevelCount]
+ -[JRSchemaJRCandidateRiskLevel riskLevels]
+ -[JRSchemaJRCandidateRiskLevel setRiskLevels:]
+ -[JRSchemaJRCandidateRiskLevel writeTo:]
+ -[JRSchemaJRCandidateRiskLevel(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJRCandidateSearchToolRank .cxx_destruct]
+ -[JRSchemaJRCandidateSearchToolRank addSearchToolRank:]
+ -[JRSchemaJRCandidateSearchToolRank clearSearchToolRank]
+ -[JRSchemaJRCandidateSearchToolRank deleteSearchToolRank]
+ -[JRSchemaJRCandidateSearchToolRank dictionaryRepresentation]
+ -[JRSchemaJRCandidateSearchToolRank hash]
+ -[JRSchemaJRCandidateSearchToolRank initWithDictionary:]
+ -[JRSchemaJRCandidateSearchToolRank initWithJSON:]
+ -[JRSchemaJRCandidateSearchToolRank isEqual:]
+ -[JRSchemaJRCandidateSearchToolRank jsonData]
+ -[JRSchemaJRCandidateSearchToolRank readFrom:]
+ -[JRSchemaJRCandidateSearchToolRank searchToolRankAtIndex:]
+ -[JRSchemaJRCandidateSearchToolRank searchToolRankCount]
+ -[JRSchemaJRCandidateSearchToolRank searchToolRanks]
+ -[JRSchemaJRCandidateSearchToolRank setSearchToolRanks:]
+ -[JRSchemaJRCandidateSearchToolRank writeTo:]
+ -[JRSchemaJRCandidateSearchToolRank(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJRCandidateTimeIntervalMatrix .cxx_destruct]
+ -[JRSchemaJRCandidateTimeIntervalMatrix addLogOfIntervalUntilStartTimeInSeconds:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix clearLogOfIntervalUntilStartTimeInSeconds]
+ -[JRSchemaJRCandidateTimeIntervalMatrix deleteLogOfIntervalUntilStartTimeInSeconds]
+ -[JRSchemaJRCandidateTimeIntervalMatrix dictionaryRepresentation]
+ -[JRSchemaJRCandidateTimeIntervalMatrix hash]
+ -[JRSchemaJRCandidateTimeIntervalMatrix initWithDictionary:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix initWithJSON:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix isEqual:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix jsonData]
+ -[JRSchemaJRCandidateTimeIntervalMatrix logOfIntervalUntilStartTimeInSecondsAtIndex:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix logOfIntervalUntilStartTimeInSecondsCount]
+ -[JRSchemaJRCandidateTimeIntervalMatrix logOfIntervalUntilStartTimeInSeconds]
+ -[JRSchemaJRCandidateTimeIntervalMatrix readFrom:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix setLogOfIntervalUntilStartTimeInSeconds:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix writeTo:]
+ -[JRSchemaJRCandidateTimeIntervalMatrix(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJREntitySimilarityRow .cxx_destruct]
+ -[JRSchemaJREntitySimilarityRow candidateA]
+ -[JRSchemaJREntitySimilarityRow candidateB]
+ -[JRSchemaJREntitySimilarityRow deleteCandidateA]
+ -[JRSchemaJREntitySimilarityRow deleteCandidateB]
+ -[JRSchemaJREntitySimilarityRow deleteSimilarityScore]
+ -[JRSchemaJREntitySimilarityRow dictionaryRepresentation]
+ -[JRSchemaJREntitySimilarityRow hasCandidateA]
+ -[JRSchemaJREntitySimilarityRow hasCandidateB]
+ -[JRSchemaJREntitySimilarityRow hasSimilarityScore]
+ -[JRSchemaJREntitySimilarityRow hash]
+ -[JRSchemaJREntitySimilarityRow initWithDictionary:]
+ -[JRSchemaJREntitySimilarityRow initWithJSON:]
+ -[JRSchemaJREntitySimilarityRow isEqual:]
+ -[JRSchemaJREntitySimilarityRow jsonData]
+ -[JRSchemaJREntitySimilarityRow readFrom:]
+ -[JRSchemaJREntitySimilarityRow setCandidateA:]
+ -[JRSchemaJREntitySimilarityRow setCandidateB:]
+ -[JRSchemaJREntitySimilarityRow setHasCandidateA:]
+ -[JRSchemaJREntitySimilarityRow setHasCandidateB:]
+ -[JRSchemaJREntitySimilarityRow setHasSimilarityScore:]
+ -[JRSchemaJREntitySimilarityRow setSimilarityScore:]
+ -[JRSchemaJREntitySimilarityRow similarityScore]
+ -[JRSchemaJREntitySimilarityRow writeTo:]
+ -[JRSchemaJREntitySimilarityRow(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[JRSchemaJREntitySimilarityRow(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJREntitySimilarityScores .cxx_destruct]
+ -[JRSchemaJREntitySimilarityScores addRow:]
+ -[JRSchemaJREntitySimilarityScores clearRow]
+ -[JRSchemaJREntitySimilarityScores deleteRow]
+ -[JRSchemaJREntitySimilarityScores dictionaryRepresentation]
+ -[JRSchemaJREntitySimilarityScores hash]
+ -[JRSchemaJREntitySimilarityScores initWithDictionary:]
+ -[JRSchemaJREntitySimilarityScores initWithJSON:]
+ -[JRSchemaJREntitySimilarityScores isEqual:]
+ -[JRSchemaJREntitySimilarityScores jsonData]
+ -[JRSchemaJREntitySimilarityScores readFrom:]
+ -[JRSchemaJREntitySimilarityScores rowAtIndex:]
+ -[JRSchemaJREntitySimilarityScores rowCount]
+ -[JRSchemaJREntitySimilarityScores rows]
+ -[JRSchemaJREntitySimilarityScores setRows:]
+ -[JRSchemaJREntitySimilarityScores writeTo:]
+ -[JRSchemaJREntitySimilarityScores(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[JRSchemaJREntitySimilarityScores(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaJRInferenceEnded addBucketedDistance:]
+ -[JRSchemaJRInferenceEnded addCandidateRisk:]
+ -[JRSchemaJRInferenceEnded addIntervalUntilStartTime:]
+ -[JRSchemaJRInferenceEnded addJrEntitySimilarityScores:]
+ -[JRSchemaJRInferenceEnded addParameterSubType:]
+ -[JRSchemaJRInferenceEnded addScores:]
+ -[JRSchemaJRInferenceEnded addSearchToolRanks:]
+ -[JRSchemaJRInferenceEnded bucketedDistanceAtIndex:]
+ -[JRSchemaJRInferenceEnded bucketedDistanceCount]
+ -[JRSchemaJRInferenceEnded bucketedDistances]
+ -[JRSchemaJRInferenceEnded candidateRiskAtIndex:]
+ -[JRSchemaJRInferenceEnded candidateRiskCount]
+ -[JRSchemaJRInferenceEnded candidateRisks]
+ -[JRSchemaJRInferenceEnded clearBucketedDistance]
+ -[JRSchemaJRInferenceEnded clearCandidateRisk]
+ -[JRSchemaJRInferenceEnded clearIntervalUntilStartTime]
+ -[JRSchemaJRInferenceEnded clearJrEntitySimilarityScores]
+ -[JRSchemaJRInferenceEnded clearParameterSubType]
+ -[JRSchemaJRInferenceEnded clearScores]
+ -[JRSchemaJRInferenceEnded clearSearchToolRanks]
+ -[JRSchemaJRInferenceEnded deleteBucketedDistance]
+ -[JRSchemaJRInferenceEnded deleteCandidateRisk]
+ -[JRSchemaJRInferenceEnded deleteIntervalUntilStartTime]
+ -[JRSchemaJRInferenceEnded deleteJrEntitySimilarityScores]
+ -[JRSchemaJRInferenceEnded deleteLoudnessLevel]
+ -[JRSchemaJRInferenceEnded deleteParameterSubType]
+ -[JRSchemaJRInferenceEnded deleteScores]
+ -[JRSchemaJRInferenceEnded deleteSearchToolRanks]
+ -[JRSchemaJRInferenceEnded deleteSignalToNoiseRatio]
+ -[JRSchemaJRInferenceEnded hasLoudnessLevel]
+ -[JRSchemaJRInferenceEnded hasSignalToNoiseRatio]
+ -[JRSchemaJRInferenceEnded intervalUntilStartTimeAtIndex:]
+ -[JRSchemaJRInferenceEnded intervalUntilStartTimeCount]
+ -[JRSchemaJRInferenceEnded intervalUntilStartTimes]
+ -[JRSchemaJRInferenceEnded jrEntitySimilarityScoresAtIndex:]
+ -[JRSchemaJRInferenceEnded jrEntitySimilarityScoresCount]
+ -[JRSchemaJRInferenceEnded jrEntitySimilarityScores]
+ -[JRSchemaJRInferenceEnded loudnessLevel]
+ -[JRSchemaJRInferenceEnded parameterSubTypeAtIndex:]
+ -[JRSchemaJRInferenceEnded parameterSubTypeCount]
+ -[JRSchemaJRInferenceEnded parameterSubTypes]
+ -[JRSchemaJRInferenceEnded scoresAtIndex:]
+ -[JRSchemaJRInferenceEnded scoresCount]
+ -[JRSchemaJRInferenceEnded scores]
+ -[JRSchemaJRInferenceEnded searchToolRanksAtIndex:]
+ -[JRSchemaJRInferenceEnded searchToolRanksCount]
+ -[JRSchemaJRInferenceEnded searchToolRanks]
+ -[JRSchemaJRInferenceEnded setBucketedDistances:]
+ -[JRSchemaJRInferenceEnded setCandidateRisks:]
+ -[JRSchemaJRInferenceEnded setHasLoudnessLevel:]
+ -[JRSchemaJRInferenceEnded setHasSignalToNoiseRatio:]
+ -[JRSchemaJRInferenceEnded setIntervalUntilStartTimes:]
+ -[JRSchemaJRInferenceEnded setJrEntitySimilarityScores:]
+ -[JRSchemaJRInferenceEnded setLoudnessLevel:]
+ -[JRSchemaJRInferenceEnded setParameterSubTypes:]
+ -[JRSchemaJRInferenceEnded setScores:]
+ -[JRSchemaJRInferenceEnded setSearchToolRanks:]
+ -[JRSchemaJRInferenceEnded setSignalToNoiseRatio:]
+ -[JRSchemaJRInferenceEnded signalToNoiseRatio]
+ -[JRSchemaJRTokenConfidence .cxx_destruct]
+ -[JRSchemaJRTokenConfidence addAsrScores:]
+ -[JRSchemaJRTokenConfidence asrScoresAtIndex:]
+ -[JRSchemaJRTokenConfidence asrScoresCount]
+ -[JRSchemaJRTokenConfidence asrScores]
+ -[JRSchemaJRTokenConfidence clearAsrScores]
+ -[JRSchemaJRTokenConfidence deleteAsrScores]
+ -[JRSchemaJRTokenConfidence dictionaryRepresentation]
+ -[JRSchemaJRTokenConfidence hash]
+ -[JRSchemaJRTokenConfidence initWithDictionary:]
+ -[JRSchemaJRTokenConfidence initWithJSON:]
+ -[JRSchemaJRTokenConfidence isEqual:]
+ -[JRSchemaJRTokenConfidence jsonData]
+ -[JRSchemaJRTokenConfidence readFrom:]
+ -[JRSchemaJRTokenConfidence setAsrScores:]
+ -[JRSchemaJRTokenConfidence writeTo:]
+ -[JRSchemaJRTokenConfidence(SensitiveConditions) suppressMessageUnderConditions]
+ -[JRSchemaUserHistory addHistoricalLocationContext:]
+ -[JRSchemaUserHistory clearHistoricalLocationContext]
+ -[JRSchemaUserHistory deleteHistoricalLocationContext]
+ -[JRSchemaUserHistory historicalLocationContextAtIndex:]
+ -[JRSchemaUserHistory historicalLocationContextCount]
+ -[JRSchemaUserHistory historicalLocationContexts]
+ -[JRSchemaUserHistory setHistoricalLocationContexts:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried backgroundNoiseActivityLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried backgroundNoiseLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteBackgroundNoiseActivityLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteBackgroundNoiseLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteInvocationType]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteIsMediaPlaybackOn]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteIsPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteMusicLoudnessLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deletePermanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteSpeakerDistance]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteSpeakerSpeechLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried deleteTtsVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried dictionaryRepresentation]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasBackgroundNoiseActivityLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasBackgroundNoiseLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasInvocationType]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasIsMediaPlaybackOn]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasIsPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasMusicLoudnessLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasPermanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasSpeakerDistance]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasSpeakerSpeechLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hasTtsVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried hash]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried initWithDictionary:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried initWithJSON:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried invocationType]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried isEqual:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried isMediaPlaybackOn]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried isPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried jsonData]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried musicLoudnessLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried permanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried readFrom:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setBackgroundNoiseActivityLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setBackgroundNoiseLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasBackgroundNoiseActivityLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasBackgroundNoiseLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasInvocationType:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasIsMediaPlaybackOn:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasIsPermanentOffsetEnabled:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasMusicLoudnessLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasPermanentOffsetFactor:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasSpeakerDistance:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasSpeakerSpeechLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setHasTtsVolume:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setInvocationType:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setIsMediaPlaybackOn:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setIsPermanentOffsetEnabled:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setMusicLoudnessLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setPermanentOffsetFactor:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setSpeakerDistance:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setSpeakerSpeechLevel:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried setTtsVolume:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried speakerDistance]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried speakerSpeechLevel]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried ttsVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried writeTo:]
+ -[MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried(SensitiveConditions) suppressMessageUnderConditions]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected deleteIsPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected deletePermanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected deleteUserIntentType]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected deleteUserIntentVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected dictionaryRepresentation]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected hasIsPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected hasPermanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected hasUserIntentType]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected hasUserIntentVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected hash]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected initWithDictionary:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected initWithJSON:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected isEqual:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected isPermanentOffsetEnabled]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected jsonData]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected permanentOffsetFactor]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected readFrom:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setHasIsPermanentOffsetEnabled:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setHasPermanentOffsetFactor:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setHasUserIntentType:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setHasUserIntentVolume:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setIsPermanentOffsetEnabled:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setPermanentOffsetFactor:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setUserIntentType:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected setUserIntentVolume:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected userIntentType]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected userIntentVolume]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected writeTo:]
+ -[MHSchemaMHAdaptiveSiriVolumeUserIntentDetected(SensitiveConditions) suppressMessageUnderConditions]
+ -[MHSchemaMHClientEvent adaptiveSiriVolumeTTSVolumeQueried]
+ -[MHSchemaMHClientEvent adaptiveSiriVolumeUserIntentDetected]
+ -[MHSchemaMHClientEvent deleteAdaptiveSiriVolumeTTSVolumeQueried]
+ -[MHSchemaMHClientEvent deleteAdaptiveSiriVolumeUserIntentDetected]
+ -[MHSchemaMHClientEvent hasAdaptiveSiriVolumeTTSVolumeQueried]
+ -[MHSchemaMHClientEvent hasAdaptiveSiriVolumeUserIntentDetected]
+ -[MHSchemaMHClientEvent setAdaptiveSiriVolumeTTSVolumeQueried:]
+ -[MHSchemaMHClientEvent setAdaptiveSiriVolumeUserIntentDetected:]
+ -[MHSchemaMHClientEvent setHasAdaptiveSiriVolumeTTSVolumeQueried:]
+ -[MHSchemaMHClientEvent setHasAdaptiveSiriVolumeUserIntentDetected:]
+ -[NLRouterSchemaNLRouterClientEvent deleteNlRouterPromptGenerated]
+ -[NLRouterSchemaNLRouterClientEvent hasNlRouterPromptGenerated]
+ -[NLRouterSchemaNLRouterClientEvent nlRouterPromptGenerated]
+ -[NLRouterSchemaNLRouterClientEvent setHasNlRouterPromptGenerated:]
+ -[NLRouterSchemaNLRouterClientEvent setNlRouterPromptGenerated:]
+ -[NLRouterSchemaNLRouterHandleEnded deleteOverrideMetadata]
+ -[NLRouterSchemaNLRouterHandleEnded hasOverrideMetadata]
+ -[NLRouterSchemaNLRouterHandleEnded overrideMetadata]
+ -[NLRouterSchemaNLRouterHandleEnded setHasOverrideMetadata:]
+ -[NLRouterSchemaNLRouterHandleEnded setOverrideMetadata:]
+ -[NLRouterSchemaNLRouterOverrideMetadata .cxx_destruct]
+ -[NLRouterSchemaNLRouterOverrideMetadata deleteOverrideId]
+ -[NLRouterSchemaNLRouterOverrideMetadata dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterOverrideMetadata hasOverrideId]
+ -[NLRouterSchemaNLRouterOverrideMetadata hash]
+ -[NLRouterSchemaNLRouterOverrideMetadata initWithDictionary:]
+ -[NLRouterSchemaNLRouterOverrideMetadata initWithJSON:]
+ -[NLRouterSchemaNLRouterOverrideMetadata isEqual:]
+ -[NLRouterSchemaNLRouterOverrideMetadata jsonData]
+ -[NLRouterSchemaNLRouterOverrideMetadata overrideId]
+ -[NLRouterSchemaNLRouterOverrideMetadata readFrom:]
+ -[NLRouterSchemaNLRouterOverrideMetadata setHasOverrideId:]
+ -[NLRouterSchemaNLRouterOverrideMetadata setOverrideId:]
+ -[NLRouterSchemaNLRouterOverrideMetadata writeTo:]
+ -[NLRouterSchemaNLRouterOverrideMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterOverrideMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaNLRouterPromptComponent componentType]
+ -[NLRouterSchemaNLRouterPromptComponent deleteComponentType]
+ -[NLRouterSchemaNLRouterPromptComponent deleteSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptComponent dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterPromptComponent hasComponentType]
+ -[NLRouterSchemaNLRouterPromptComponent hasSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptComponent hash]
+ -[NLRouterSchemaNLRouterPromptComponent initWithDictionary:]
+ -[NLRouterSchemaNLRouterPromptComponent initWithJSON:]
+ -[NLRouterSchemaNLRouterPromptComponent isEqual:]
+ -[NLRouterSchemaNLRouterPromptComponent jsonData]
+ -[NLRouterSchemaNLRouterPromptComponent readFrom:]
+ -[NLRouterSchemaNLRouterPromptComponent setComponentType:]
+ -[NLRouterSchemaNLRouterPromptComponent setHasComponentType:]
+ -[NLRouterSchemaNLRouterPromptComponent setHasSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptComponent setSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptComponent sizeInTokens]
+ -[NLRouterSchemaNLRouterPromptComponent writeTo:]
+ -[NLRouterSchemaNLRouterPromptComponent(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaNLRouterPromptGenerated .cxx_destruct]
+ -[NLRouterSchemaNLRouterPromptGenerated addComponents:]
+ -[NLRouterSchemaNLRouterPromptGenerated addDroppedComponents:]
+ -[NLRouterSchemaNLRouterPromptGenerated clearComponents]
+ -[NLRouterSchemaNLRouterPromptGenerated clearDroppedComponents]
+ -[NLRouterSchemaNLRouterPromptGenerated componentsAtIndex:]
+ -[NLRouterSchemaNLRouterPromptGenerated componentsCount]
+ -[NLRouterSchemaNLRouterPromptGenerated components]
+ -[NLRouterSchemaNLRouterPromptGenerated deleteComponents]
+ -[NLRouterSchemaNLRouterPromptGenerated deleteDroppedComponents]
+ -[NLRouterSchemaNLRouterPromptGenerated deleteEstimatedSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated deleteTotalSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterPromptGenerated droppedComponentsAtIndex:]
+ -[NLRouterSchemaNLRouterPromptGenerated droppedComponentsCount]
+ -[NLRouterSchemaNLRouterPromptGenerated droppedComponents]
+ -[NLRouterSchemaNLRouterPromptGenerated estimatedSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated hasEstimatedSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated hasTotalSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated hash]
+ -[NLRouterSchemaNLRouterPromptGenerated initWithDictionary:]
+ -[NLRouterSchemaNLRouterPromptGenerated initWithJSON:]
+ -[NLRouterSchemaNLRouterPromptGenerated isEqual:]
+ -[NLRouterSchemaNLRouterPromptGenerated jsonData]
+ -[NLRouterSchemaNLRouterPromptGenerated readFrom:]
+ -[NLRouterSchemaNLRouterPromptGenerated setComponents:]
+ -[NLRouterSchemaNLRouterPromptGenerated setDroppedComponents:]
+ -[NLRouterSchemaNLRouterPromptGenerated setEstimatedSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptGenerated setHasEstimatedSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptGenerated setHasTotalSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptGenerated setTotalSizeInTokens:]
+ -[NLRouterSchemaNLRouterPromptGenerated totalSizeInTokens]
+ -[NLRouterSchemaNLRouterPromptGenerated writeTo:]
+ -[NLRouterSchemaNLRouterPromptGenerated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterPromptGenerated(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaNLRouterPromptGenerationSignalsCaptured deleteIsMailAppFocused]
+ -[NLRouterSchemaNLRouterPromptGenerationSignalsCaptured hasIsMailAppFocused]
+ -[NLRouterSchemaNLRouterPromptGenerationSignalsCaptured isMailAppFocused]
+ -[NLRouterSchemaNLRouterPromptGenerationSignalsCaptured setHasIsMailAppFocused:]
+ -[NLRouterSchemaNLRouterPromptGenerationSignalsCaptured setIsMailAppFocused:]
+ -[NLXSchemaCDMUserDialogAct deleteWantedToUndo]
+ -[NLXSchemaCDMUserDialogAct hasWantedToUndo]
+ -[NLXSchemaCDMUserDialogAct setHasWantedToUndo:]
+ -[NLXSchemaCDMUserDialogAct setWantedToUndo:]
+ -[NLXSchemaCDMUserDialogAct wantedToUndo]
+ -[NLXSchemaCDMUserWantedToUndo deleteExists]
+ -[NLXSchemaCDMUserWantedToUndo dictionaryRepresentation]
+ -[NLXSchemaCDMUserWantedToUndo exists]
+ -[NLXSchemaCDMUserWantedToUndo hasExists]
+ -[NLXSchemaCDMUserWantedToUndo hash]
+ -[NLXSchemaCDMUserWantedToUndo initWithDictionary:]
+ -[NLXSchemaCDMUserWantedToUndo initWithJSON:]
+ -[NLXSchemaCDMUserWantedToUndo isEqual:]
+ -[NLXSchemaCDMUserWantedToUndo jsonData]
+ -[NLXSchemaCDMUserWantedToUndo readFrom:]
+ -[NLXSchemaCDMUserWantedToUndo setExists:]
+ -[NLXSchemaCDMUserWantedToUndo setHasExists:]
+ -[NLXSchemaCDMUserWantedToUndo writeTo:]
+ -[NLXSchemaCDMUserWantedToUndo(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODBATCHSiriSchemaODBATCHTurnRestatementScore deleteIsCrossDevice]
+ -[ODBATCHSiriSchemaODBATCHTurnRestatementScore hasIsCrossDevice]
+ -[ODBATCHSiriSchemaODBATCHTurnRestatementScore isCrossDevice]
+ -[ODBATCHSiriSchemaODBATCHTurnRestatementScore setHasIsCrossDevice:]
+ -[ODBATCHSiriSchemaODBATCHTurnRestatementScore setIsCrossDevice:]
+ -[ODDSiriSchemaODDClientEventMetadata deleteEventOrigin]
+ -[ODDSiriSchemaODDClientEventMetadata deleteIsLongLivedIDUploadDisabled]
+ -[ODDSiriSchemaODDClientEventMetadata deleteUserAggregationId]
+ -[ODDSiriSchemaODDClientEventMetadata eventOrigin]
+ -[ODDSiriSchemaODDClientEventMetadata hasEventOrigin]
+ -[ODDSiriSchemaODDClientEventMetadata hasIsLongLivedIDUploadDisabled]
+ -[ODDSiriSchemaODDClientEventMetadata hasUserAggregationId]
+ -[ODDSiriSchemaODDClientEventMetadata isLongLivedIDUploadDisabled]
+ -[ODDSiriSchemaODDClientEventMetadata setEventOrigin:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasEventOrigin:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasIsLongLivedIDUploadDisabled:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasUserAggregationId:]
+ -[ODDSiriSchemaODDClientEventMetadata setIsLongLivedIDUploadDisabled:]
+ -[ODDSiriSchemaODDClientEventMetadata setUserAggregationId:]
+ -[ODDSiriSchemaODDClientEventMetadata userAggregationId]
+ -[ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported deletePostItn1Best]
+ -[ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported hasPostItn1Best]
+ -[ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported postItn1Best]
+ -[ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported setHasPostItn1Best:]
+ -[ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported setPostItn1Best:]
+ -[ORCHSchemaORCHAudioTopologyReported audioTopology]
+ -[ORCHSchemaORCHAudioTopologyReported deleteAudioTopology]
+ -[ORCHSchemaORCHAudioTopologyReported deleteIsLeader]
+ -[ORCHSchemaORCHAudioTopologyReported dictionaryRepresentation]
+ -[ORCHSchemaORCHAudioTopologyReported hasAudioTopology]
+ -[ORCHSchemaORCHAudioTopologyReported hasIsLeader]
+ -[ORCHSchemaORCHAudioTopologyReported hash]
+ -[ORCHSchemaORCHAudioTopologyReported initWithDictionary:]
+ -[ORCHSchemaORCHAudioTopologyReported initWithJSON:]
+ -[ORCHSchemaORCHAudioTopologyReported isEqual:]
+ -[ORCHSchemaORCHAudioTopologyReported isLeader]
+ -[ORCHSchemaORCHAudioTopologyReported jsonData]
+ -[ORCHSchemaORCHAudioTopologyReported readFrom:]
+ -[ORCHSchemaORCHAudioTopologyReported setAudioTopology:]
+ -[ORCHSchemaORCHAudioTopologyReported setHasAudioTopology:]
+ -[ORCHSchemaORCHAudioTopologyReported setHasIsLeader:]
+ -[ORCHSchemaORCHAudioTopologyReported setIsLeader:]
+ -[ORCHSchemaORCHAudioTopologyReported writeTo:]
+ -[ORCHSchemaORCHAudioTopologyReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHClientEvent audioTopologyReported]
+ -[ORCHSchemaORCHClientEvent deleteAudioTopologyReported]
+ -[ORCHSchemaORCHClientEvent deleteIntelligenceFlowRequestContext]
+ -[ORCHSchemaORCHClientEvent hasAudioTopologyReported]
+ -[ORCHSchemaORCHClientEvent hasIntelligenceFlowRequestContext]
+ -[ORCHSchemaORCHClientEvent intelligenceFlowRequestContext]
+ -[ORCHSchemaORCHClientEvent setAudioTopologyReported:]
+ -[ORCHSchemaORCHClientEvent setHasAudioTopologyReported:]
+ -[ORCHSchemaORCHClientEvent setHasIntelligenceFlowRequestContext:]
+ -[ORCHSchemaORCHClientEvent setIntelligenceFlowRequestContext:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext .cxx_destruct]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteEnded]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteFailed]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteStartedOrChanged]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteSubRequestId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteTraceId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext deleteTrpId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext dictionaryRepresentation]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext ended]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext failed]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasEnded]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasFailed]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasStartedOrChanged]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasSubRequestId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasTraceId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hasTrpId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext hash]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext initWithDictionary:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext initWithJSON:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext isEqual:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext jsonData]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext readFrom:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setEnded:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setFailed:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasEnded:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasFailed:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasStartedOrChanged:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasSubRequestId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasTraceId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setHasTrpId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setStartedOrChanged:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setSubRequestId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setTraceId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext setTrpId:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext startedOrChanged]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext subRequestId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext traceId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext trpId]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext whichContextevent]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext writeTo:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded deleteShimAction]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded dictionaryRepresentation]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded hasShimAction]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded hash]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded initWithDictionary:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded initWithJSON:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded isEqual:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded jsonData]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded readFrom:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded setHasShimAction:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded setShimAction:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded shimAction]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded writeTo:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed deleteIsSiriXFallback]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed deleteReason]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed dictionaryRepresentation]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed hasIsSiriXFallback]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed hasReason]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed hash]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed initWithDictionary:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed initWithJSON:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed isEqual:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed isSiriXFallback]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed jsonData]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed readFrom:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed reason]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setHasIsSiriXFallback:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setHasReason:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setIsSiriXFallback:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setReason:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed writeTo:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted deleteExists]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted dictionaryRepresentation]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted exists]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted hasExists]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted hash]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted initWithDictionary:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted initWithJSON:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted isEqual:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted jsonData]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted readFrom:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted setExists:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted setHasExists:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted writeTo:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHMUXRequestEnded addVoiceIdScores:]
+ -[ORCHSchemaORCHMUXRequestEnded clearVoiceIdScores]
+ -[ORCHSchemaORCHMUXRequestEnded deleteSelectedloggableUserIdHash]
+ -[ORCHSchemaORCHMUXRequestEnded deleteVoiceIdClassification]
+ -[ORCHSchemaORCHMUXRequestEnded deleteVoiceIdScores]
+ -[ORCHSchemaORCHMUXRequestEnded hasSelectedloggableUserIdHash]
+ -[ORCHSchemaORCHMUXRequestEnded hasVoiceIdClassification]
+ -[ORCHSchemaORCHMUXRequestEnded selectedloggableUserIdHash]
+ -[ORCHSchemaORCHMUXRequestEnded setHasSelectedloggableUserIdHash:]
+ -[ORCHSchemaORCHMUXRequestEnded setHasVoiceIdClassification:]
+ -[ORCHSchemaORCHMUXRequestEnded setSelectedloggableUserIdHash:]
+ -[ORCHSchemaORCHMUXRequestEnded setVoiceIdClassification:]
+ -[ORCHSchemaORCHMUXRequestEnded setVoiceIdScores:]
+ -[ORCHSchemaORCHMUXRequestEnded voiceIdClassification]
+ -[ORCHSchemaORCHMUXRequestEnded voiceIdScoresAtIndex:]
+ -[ORCHSchemaORCHMUXRequestEnded voiceIdScoresCount]
+ -[ORCHSchemaORCHMUXRequestEnded voiceIdScores]
+ -[ORCHSchemaORCHMultiUserScore deleteLoggableUserIdHash]
+ -[ORCHSchemaORCHMultiUserScore hasLoggableUserIdHash]
+ -[ORCHSchemaORCHMultiUserScore loggableUserIdHash]
+ -[ORCHSchemaORCHMultiUserScore setHasLoggableUserIdHash:]
+ -[ORCHSchemaORCHMultiUserScore setLoggableUserIdHash:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset deleteEndCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset deleteStartCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset endCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset hasEndCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset hasStartCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset hash]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset isEqual:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset jsonData]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset readFrom:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset setEndCharacterIdx:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset setHasEndCharacterIdx:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset setHasStartCharacterIdx:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset setStartCharacterIdx:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset startCharacterIdx]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset writeTo:]
+ -[PEGASUSSchemaPEGASUSAlignmentOffset(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 alternateQuerySuggestionType]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 deleteAlternateQuerySuggestionType]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 deleteText]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 hasAlternateQuerySuggestionType]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 hasText]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 hash]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 setAlternateQuerySuggestionType:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 setHasAlternateQuerySuggestionType:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 setHasText:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 setText:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 text]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 addAlternateQuerySuggestionCandidateTier1:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 alternateQuerySuggestionCandidateTier1AtIndex:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 alternateQuerySuggestionCandidateTier1Count]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 alternateQuerySuggestionCandidateTier1s]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 clearAlternateQuerySuggestionCandidateTier1]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 deleteAlternateQuerySuggestionCandidateTier1]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 hash]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 setAlternateQuerySuggestionCandidateTier1s:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo addAsrHypothesesInfo:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo asrHypothesesInfoAtIndex:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo asrHypothesesInfoCount]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo asrHypothesesInfos]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo clearAsrHypothesesInfo]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo deleteAsrHypothesesInfo]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo hash]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo isEqual:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo jsonData]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo readFrom:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo setAsrHypothesesInfos:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo writeTo:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSAsrCorrectionInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx deleteOriginalAsrInterpretationIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx deleteSourceAuxIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx deleteSourceAuxKey]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx hasOriginalAsrInterpretationIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx hasSourceAuxIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx hasSourceAuxKey]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx hash]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx isEqual:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx jsonData]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx originalAsrInterpretationIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx readFrom:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setHasOriginalAsrInterpretationIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setHasSourceAuxIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setHasSourceAuxKey:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setOriginalAsrInterpretationIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setSourceAuxIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx setSourceAuxKey:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx sourceAuxIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx sourceAuxKey]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx writeTo:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisIdx(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo addCorrections:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo clearCorrections]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo correctionsAtIndex:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo correctionsCount]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo corrections]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deleteCorrections]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deleteIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deletePostItnUtterance]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deleteScore]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deleteSelectedAsAlternateSuggestion]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo deleteSelectedAsPrimaryResponse]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hasIdx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hasPostItnUtterance]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hasScore]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hasSelectedAsAlternateSuggestion]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hasSelectedAsPrimaryResponse]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo hash]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo idx]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo initWithJSON:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo isEqual:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo jsonData]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo postItnUtterance]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo readFrom:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo score]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo selectedAsAlternateSuggestion]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo selectedAsPrimaryResponse]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setCorrections:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setHasIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setHasPostItnUtterance:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setHasScore:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setHasSelectedAsAlternateSuggestion:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setHasSelectedAsPrimaryResponse:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setIdx:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setPostItnUtterance:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setScore:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setSelectedAsAlternateSuggestion:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo setSelectedAsPrimaryResponse:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo writeTo:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSAsrHypothesisInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo alignmentOffset]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo correction]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo deleteAlignmentOffset]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo deleteCorrection]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo deleteOriginal]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo deleteScore]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo deleteSourceAuxKey]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hasAlignmentOffset]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hasCorrection]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hasOriginal]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hasScore]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hasSourceAuxKey]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo hash]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo initWithJSON:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo isEqual:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo jsonData]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo original]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo readFrom:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo score]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setAlignmentOffset:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setCorrection:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setHasAlignmentOffset:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setHasCorrection:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setHasOriginal:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setHasScore:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setHasSourceAuxKey:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setOriginal:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setScore:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo setSourceAuxKey:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo sourceAuxKey]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo writeTo:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSCorrectionInfo(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSRequestEnded alternateQuerySuggestionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEnded deleteAlternateQuerySuggestionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEnded hasAlternateQuerySuggestionTier1]
+ -[PEGASUSSchemaPEGASUSRequestEnded setAlternateQuerySuggestionTier1:]
+ -[PEGASUSSchemaPEGASUSRequestEnded setHasAlternateQuerySuggestionTier1:]
+ -[PEGASUSSchemaPEGASUSServerEvent deletePegasusAsrCorrectionInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent hasPegasusAsrCorrectionInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent pegasusAsrCorrectionInfo]
+ -[PEGASUSSchemaPEGASUSServerEvent setHasPegasusAsrCorrectionInfo:]
+ -[PEGASUSSchemaPEGASUSServerEvent setPegasusAsrCorrectionInfo:]
+ -[PEGASUSSchemaPEGASUSVideoExecutionTier1 deleteIsNlsResult]
+ -[PEGASUSSchemaPEGASUSVideoExecutionTier1 hasIsNlsResult]
+ -[PEGASUSSchemaPEGASUSVideoExecutionTier1 isNlsResult]
+ -[PEGASUSSchemaPEGASUSVideoExecutionTier1 setHasIsNlsResult:]
+ -[PEGASUSSchemaPEGASUSVideoExecutionTier1 setIsNlsResult:]
+ -[PGSchemaPGClientEvent deletePgGeneratePlanContext]
+ -[PGSchemaPGClientEvent hasPgGeneratePlanContext]
+ -[PGSchemaPGClientEvent pgGeneratePlanContext]
+ -[PGSchemaPGClientEvent setHasPgGeneratePlanContext:]
+ -[PGSchemaPGClientEvent setPgGeneratePlanContext:]
+ -[PGSchemaPGGeneratePlanContext .cxx_destruct]
+ -[PGSchemaPGGeneratePlanContext deleteEnded]
+ -[PGSchemaPGGeneratePlanContext deleteFailed]
+ -[PGSchemaPGGeneratePlanContext deleteStartedOrChanged]
+ -[PGSchemaPGGeneratePlanContext dictionaryRepresentation]
+ -[PGSchemaPGGeneratePlanContext ended]
+ -[PGSchemaPGGeneratePlanContext failed]
+ -[PGSchemaPGGeneratePlanContext hasEnded]
+ -[PGSchemaPGGeneratePlanContext hasFailed]
+ -[PGSchemaPGGeneratePlanContext hasStartedOrChanged]
+ -[PGSchemaPGGeneratePlanContext hash]
+ -[PGSchemaPGGeneratePlanContext initWithDictionary:]
+ -[PGSchemaPGGeneratePlanContext initWithJSON:]
+ -[PGSchemaPGGeneratePlanContext isEqual:]
+ -[PGSchemaPGGeneratePlanContext jsonData]
+ -[PGSchemaPGGeneratePlanContext readFrom:]
+ -[PGSchemaPGGeneratePlanContext setEnded:]
+ -[PGSchemaPGGeneratePlanContext setFailed:]
+ -[PGSchemaPGGeneratePlanContext setHasEnded:]
+ -[PGSchemaPGGeneratePlanContext setHasFailed:]
+ -[PGSchemaPGGeneratePlanContext setHasStartedOrChanged:]
+ -[PGSchemaPGGeneratePlanContext setStartedOrChanged:]
+ -[PGSchemaPGGeneratePlanContext startedOrChanged]
+ -[PGSchemaPGGeneratePlanContext whichContextevent]
+ -[PGSchemaPGGeneratePlanContext writeTo:]
+ -[PGSchemaPGGeneratePlanContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PGSchemaPGGeneratePlanContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[PGSchemaPGGeneratePlanEnded deleteExists]
+ -[PGSchemaPGGeneratePlanEnded dictionaryRepresentation]
+ -[PGSchemaPGGeneratePlanEnded exists]
+ -[PGSchemaPGGeneratePlanEnded hasExists]
+ -[PGSchemaPGGeneratePlanEnded hash]
+ -[PGSchemaPGGeneratePlanEnded initWithDictionary:]
+ -[PGSchemaPGGeneratePlanEnded initWithJSON:]
+ -[PGSchemaPGGeneratePlanEnded isEqual:]
+ -[PGSchemaPGGeneratePlanEnded jsonData]
+ -[PGSchemaPGGeneratePlanEnded readFrom:]
+ -[PGSchemaPGGeneratePlanEnded setExists:]
+ -[PGSchemaPGGeneratePlanEnded setHasExists:]
+ -[PGSchemaPGGeneratePlanEnded writeTo:]
+ -[PGSchemaPGGeneratePlanEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[PGSchemaPGGeneratePlanFailed .cxx_destruct]
+ -[PGSchemaPGGeneratePlanFailed criticalError]
+ -[PGSchemaPGGeneratePlanFailed deleteCriticalError]
+ -[PGSchemaPGGeneratePlanFailed dictionaryRepresentation]
+ -[PGSchemaPGGeneratePlanFailed hasCriticalError]
+ -[PGSchemaPGGeneratePlanFailed hash]
+ -[PGSchemaPGGeneratePlanFailed initWithDictionary:]
+ -[PGSchemaPGGeneratePlanFailed initWithJSON:]
+ -[PGSchemaPGGeneratePlanFailed isEqual:]
+ -[PGSchemaPGGeneratePlanFailed jsonData]
+ -[PGSchemaPGGeneratePlanFailed readFrom:]
+ -[PGSchemaPGGeneratePlanFailed setCriticalError:]
+ -[PGSchemaPGGeneratePlanFailed setHasCriticalError:]
+ -[PGSchemaPGGeneratePlanFailed writeTo:]
+ -[PGSchemaPGGeneratePlanFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PGSchemaPGGeneratePlanFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[PGSchemaPGGeneratePlanStarted deleteExists]
+ -[PGSchemaPGGeneratePlanStarted dictionaryRepresentation]
+ -[PGSchemaPGGeneratePlanStarted exists]
+ -[PGSchemaPGGeneratePlanStarted hasExists]
+ -[PGSchemaPGGeneratePlanStarted hash]
+ -[PGSchemaPGGeneratePlanStarted initWithDictionary:]
+ -[PGSchemaPGGeneratePlanStarted initWithJSON:]
+ -[PGSchemaPGGeneratePlanStarted isEqual:]
+ -[PGSchemaPGGeneratePlanStarted jsonData]
+ -[PGSchemaPGGeneratePlanStarted readFrom:]
+ -[PGSchemaPGGeneratePlanStarted setExists:]
+ -[PGSchemaPGGeneratePlanStarted setHasExists:]
+ -[PGSchemaPGGeneratePlanStarted writeTo:]
+ -[PGSchemaPGGeneratePlanStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[PGSchemaPGOverridesEnded assetVersion]
+ -[PGSchemaPGOverridesEnded deleteAssetVersion]
+ -[PGSchemaPGOverridesEnded deleteOverridesMatched]
+ -[PGSchemaPGOverridesEnded hasAssetVersion]
+ -[PGSchemaPGOverridesEnded hasOverridesMatched]
+ -[PGSchemaPGOverridesEnded overridesMatched]
+ -[PGSchemaPGOverridesEnded setAssetVersion:]
+ -[PGSchemaPGOverridesEnded setHasAssetVersion:]
+ -[PGSchemaPGOverridesEnded setHasOverridesMatched:]
+ -[PGSchemaPGOverridesEnded setOverridesMatched:]
+ -[PGSchemaPGOverridesFailed assetVersion]
+ -[PGSchemaPGOverridesFailed deleteAssetVersion]
+ -[PGSchemaPGOverridesFailed hasAssetVersion]
+ -[PGSchemaPGOverridesFailed setAssetVersion:]
+ -[PGSchemaPGOverridesFailed setHasAssetVersion:]
+ -[PGSchemaPGOverridesMatchMetadata deleteIsMatched]
+ -[PGSchemaPGOverridesMatchMetadata dictionaryRepresentation]
+ -[PGSchemaPGOverridesMatchMetadata hasIsMatched]
+ -[PGSchemaPGOverridesMatchMetadata hash]
+ -[PGSchemaPGOverridesMatchMetadata initWithDictionary:]
+ -[PGSchemaPGOverridesMatchMetadata initWithJSON:]
+ -[PGSchemaPGOverridesMatchMetadata isEqual:]
+ -[PGSchemaPGOverridesMatchMetadata isMatched]
+ -[PGSchemaPGOverridesMatchMetadata jsonData]
+ -[PGSchemaPGOverridesMatchMetadata readFrom:]
+ -[PGSchemaPGOverridesMatchMetadata setHasIsMatched:]
+ -[PGSchemaPGOverridesMatchMetadata setIsMatched:]
+ -[PGSchemaPGOverridesMatchMetadata writeTo:]
+ -[PGSchemaPGOverridesMatchMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[PGSchemaPGPromptResponseTier1 deleteGrammar]
+ -[PGSchemaPGPromptResponseTier1 grammar]
+ -[PGSchemaPGPromptResponseTier1 hasGrammar]
+ -[PGSchemaPGPromptResponseTier1 setGrammar:]
+ -[PGSchemaPGPromptResponseTier1 setHasGrammar:]
+ -[PNRODSchemaPNRError .cxx_destruct]
+ -[PNRODSchemaPNRError code]
+ -[PNRODSchemaPNRError deleteCode]
+ -[PNRODSchemaPNRError deleteDomain]
+ -[PNRODSchemaPNRError deleteSource]
+ -[PNRODSchemaPNRError dictionaryRepresentation]
+ -[PNRODSchemaPNRError domain]
+ -[PNRODSchemaPNRError hasCode]
+ -[PNRODSchemaPNRError hasDomain]
+ -[PNRODSchemaPNRError hasSource]
+ -[PNRODSchemaPNRError hash]
+ -[PNRODSchemaPNRError initWithDictionary:]
+ -[PNRODSchemaPNRError initWithJSON:]
+ -[PNRODSchemaPNRError isEqual:]
+ -[PNRODSchemaPNRError jsonData]
+ -[PNRODSchemaPNRError readFrom:]
+ -[PNRODSchemaPNRError setCode:]
+ -[PNRODSchemaPNRError setDomain:]
+ -[PNRODSchemaPNRError setHasCode:]
+ -[PNRODSchemaPNRError setHasDomain:]
+ -[PNRODSchemaPNRError setHasSource:]
+ -[PNRODSchemaPNRError setSource:]
+ -[PNRODSchemaPNRError source]
+ -[PNRODSchemaPNRError writeTo:]
+ -[PNRODSchemaPNRError(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODExecutor .cxx_destruct]
+ -[PNRODSchemaPNRODExecutor deleteExecutorAppIntentHandleTime]
+ -[PNRODSchemaPNRODExecutor deleteExecutorAppIntentQueryHandleTime]
+ -[PNRODSchemaPNRODExecutor deleteExecutorId]
+ -[PNRODSchemaPNRODExecutor deleteExecutorSearchToolQueryType]
+ -[PNRODSchemaPNRODExecutor deleteFailureInfo]
+ -[PNRODSchemaPNRODExecutor deleteIdentifierQueryTime]
+ -[PNRODSchemaPNRODExecutor deletePersonQueryTime]
+ -[PNRODSchemaPNRODExecutor deletePlanCycleId]
+ -[PNRODSchemaPNRODExecutor deleteSearchToolQueryTime]
+ -[PNRODSchemaPNRODExecutor deleteStringQueryEntityMatcherTime]
+ -[PNRODSchemaPNRODExecutor deleteStringQueryEntityTime]
+ -[PNRODSchemaPNRODExecutor deleteStringQueryLocationTime]
+ -[PNRODSchemaPNRODExecutor dictionaryRepresentation]
+ -[PNRODSchemaPNRODExecutor executorAppIntentHandleTime]
+ -[PNRODSchemaPNRODExecutor executorAppIntentQueryHandleTime]
+ -[PNRODSchemaPNRODExecutor executorId]
+ -[PNRODSchemaPNRODExecutor executorSearchToolQueryType]
+ -[PNRODSchemaPNRODExecutor failureInfo]
+ -[PNRODSchemaPNRODExecutor hasExecutorAppIntentHandleTime]
+ -[PNRODSchemaPNRODExecutor hasExecutorAppIntentQueryHandleTime]
+ -[PNRODSchemaPNRODExecutor hasExecutorId]
+ -[PNRODSchemaPNRODExecutor hasExecutorSearchToolQueryType]
+ -[PNRODSchemaPNRODExecutor hasFailureInfo]
+ -[PNRODSchemaPNRODExecutor hasIdentifierQueryTime]
+ -[PNRODSchemaPNRODExecutor hasPersonQueryTime]
+ -[PNRODSchemaPNRODExecutor hasPlanCycleId]
+ -[PNRODSchemaPNRODExecutor hasSearchToolQueryTime]
+ -[PNRODSchemaPNRODExecutor hasStringQueryEntityMatcherTime]
+ -[PNRODSchemaPNRODExecutor hasStringQueryEntityTime]
+ -[PNRODSchemaPNRODExecutor hasStringQueryLocationTime]
+ -[PNRODSchemaPNRODExecutor hash]
+ -[PNRODSchemaPNRODExecutor identifierQueryTime]
+ -[PNRODSchemaPNRODExecutor initWithDictionary:]
+ -[PNRODSchemaPNRODExecutor initWithJSON:]
+ -[PNRODSchemaPNRODExecutor isEqual:]
+ -[PNRODSchemaPNRODExecutor jsonData]
+ -[PNRODSchemaPNRODExecutor personQueryTime]
+ -[PNRODSchemaPNRODExecutor planCycleId]
+ -[PNRODSchemaPNRODExecutor readFrom:]
+ -[PNRODSchemaPNRODExecutor searchToolQueryTime]
+ -[PNRODSchemaPNRODExecutor setExecutorAppIntentHandleTime:]
+ -[PNRODSchemaPNRODExecutor setExecutorAppIntentQueryHandleTime:]
+ -[PNRODSchemaPNRODExecutor setExecutorId:]
+ -[PNRODSchemaPNRODExecutor setExecutorSearchToolQueryType:]
+ -[PNRODSchemaPNRODExecutor setFailureInfo:]
+ -[PNRODSchemaPNRODExecutor setHasExecutorAppIntentHandleTime:]
+ -[PNRODSchemaPNRODExecutor setHasExecutorAppIntentQueryHandleTime:]
+ -[PNRODSchemaPNRODExecutor setHasExecutorId:]
+ -[PNRODSchemaPNRODExecutor setHasExecutorSearchToolQueryType:]
+ -[PNRODSchemaPNRODExecutor setHasFailureInfo:]
+ -[PNRODSchemaPNRODExecutor setHasIdentifierQueryTime:]
+ -[PNRODSchemaPNRODExecutor setHasPersonQueryTime:]
+ -[PNRODSchemaPNRODExecutor setHasPlanCycleId:]
+ -[PNRODSchemaPNRODExecutor setHasSearchToolQueryTime:]
+ -[PNRODSchemaPNRODExecutor setHasStringQueryEntityMatcherTime:]
+ -[PNRODSchemaPNRODExecutor setHasStringQueryEntityTime:]
+ -[PNRODSchemaPNRODExecutor setHasStringQueryLocationTime:]
+ -[PNRODSchemaPNRODExecutor setIdentifierQueryTime:]
+ -[PNRODSchemaPNRODExecutor setPersonQueryTime:]
+ -[PNRODSchemaPNRODExecutor setPlanCycleId:]
+ -[PNRODSchemaPNRODExecutor setSearchToolQueryTime:]
+ -[PNRODSchemaPNRODExecutor setStringQueryEntityMatcherTime:]
+ -[PNRODSchemaPNRODExecutor setStringQueryEntityTime:]
+ -[PNRODSchemaPNRODExecutor setStringQueryLocationTime:]
+ -[PNRODSchemaPNRODExecutor stringQueryEntityMatcherTime]
+ -[PNRODSchemaPNRODExecutor stringQueryEntityTime]
+ -[PNRODSchemaPNRODExecutor stringQueryLocationTime]
+ -[PNRODSchemaPNRODExecutor writeTo:]
+ -[PNRODSchemaPNRODExecutor(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODExecutor(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODFailureInfo .cxx_destruct]
+ -[PNRODSchemaPNRODFailureInfo deleteError]
+ -[PNRODSchemaPNRODFailureInfo deleteUnderUnderlyingError]
+ -[PNRODSchemaPNRODFailureInfo deleteUnderlyingError]
+ -[PNRODSchemaPNRODFailureInfo error]
+ -[PNRODSchemaPNRODFailureInfo hasError]
+ -[PNRODSchemaPNRODFailureInfo hasUnderUnderlyingError]
+ -[PNRODSchemaPNRODFailureInfo hasUnderlyingError]
+ -[PNRODSchemaPNRODFailureInfo setError:]
+ -[PNRODSchemaPNRODFailureInfo setHasError:]
+ -[PNRODSchemaPNRODFailureInfo setHasUnderUnderlyingError:]
+ -[PNRODSchemaPNRODFailureInfo setHasUnderlyingError:]
+ -[PNRODSchemaPNRODFailureInfo setUnderUnderlyingError:]
+ -[PNRODSchemaPNRODFailureInfo setUnderlyingError:]
+ -[PNRODSchemaPNRODFailureInfo underUnderlyingError]
+ -[PNRODSchemaPNRODFailureInfo underlyingError]
+ -[PNRODSchemaPNRODFailureInfo(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary appEntityQueryResponseTime]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary deleteAppEntityQueryResponseTime]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary deleteNumActionsCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary deleteNumQueriesCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary deleteStatementId]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary hasAppEntityQueryResponseTime]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary hasNumActionsCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary hasNumQueriesCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary hasStatementId]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary numActionsCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary numQueriesCreated]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setAppEntityQueryResponseTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setHasAppEntityQueryResponseTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setHasNumActionsCreated:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setHasNumQueriesCreated:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setHasStatementId:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setNumActionsCreated:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setNumQueriesCreated:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary setStatementId:]
+ -[PNRODSchemaPNRODIntelligenceFlowActionGrainSummary statementId]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary addRequestFeatureTag:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary clearRequestFeatureTag]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary deletePlanGenerationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary deleteQueryDecorationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary deleteRequestFeatureTag]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary hasPlanGenerationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary hasQueryDecorationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary planGenerationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary queryDecorationTime]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary requestFeatureTagAtIndex:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary requestFeatureTagCount]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary requestFeatureTags]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary setHasPlanGenerationTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary setHasQueryDecorationTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary setPlanGenerationTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary setQueryDecorationTime:]
+ -[PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary setRequestFeatureTags:]
+ -[PNRODSchemaPNRODPlanGeneration .cxx_destruct]
+ -[PNRODSchemaPNRODPlanGeneration deleteFailureInfo]
+ -[PNRODSchemaPNRODPlanGeneration deletePgFullPlannerHandleTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgFullPlannerPostInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgFullPlannerPreInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgModelIdentifier]
+ -[PNRODSchemaPNRODPlanGeneration deletePgModelInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgModelInterface]
+ -[PNRODSchemaPNRODPlanGeneration deletePgOverridesAssetVersion]
+ -[PNRODSchemaPNRODPlanGeneration deletePgOverridesMatched]
+ -[PNRODSchemaPNRODPlanGeneration deletePgOverridesTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgPlanGenTotalTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePgPrescribedPlanTime]
+ -[PNRODSchemaPNRODPlanGeneration deletePlanCycleId]
+ -[PNRODSchemaPNRODPlanGeneration dictionaryRepresentation]
+ -[PNRODSchemaPNRODPlanGeneration failureInfo]
+ -[PNRODSchemaPNRODPlanGeneration hasFailureInfo]
+ -[PNRODSchemaPNRODPlanGeneration hasPgFullPlannerHandleTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgFullPlannerPostInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgFullPlannerPreInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgModelIdentifier]
+ -[PNRODSchemaPNRODPlanGeneration hasPgModelInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgModelInterface]
+ -[PNRODSchemaPNRODPlanGeneration hasPgOverridesAssetVersion]
+ -[PNRODSchemaPNRODPlanGeneration hasPgOverridesMatched]
+ -[PNRODSchemaPNRODPlanGeneration hasPgOverridesTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgPlanGenTotalTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPgPrescribedPlanTime]
+ -[PNRODSchemaPNRODPlanGeneration hasPlanCycleId]
+ -[PNRODSchemaPNRODPlanGeneration hash]
+ -[PNRODSchemaPNRODPlanGeneration initWithDictionary:]
+ -[PNRODSchemaPNRODPlanGeneration initWithJSON:]
+ -[PNRODSchemaPNRODPlanGeneration isEqual:]
+ -[PNRODSchemaPNRODPlanGeneration jsonData]
+ -[PNRODSchemaPNRODPlanGeneration pgFullPlannerHandleTime]
+ -[PNRODSchemaPNRODPlanGeneration pgFullPlannerPostInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration pgFullPlannerPreInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration pgModelIdentifier]
+ -[PNRODSchemaPNRODPlanGeneration pgModelInferenceTime]
+ -[PNRODSchemaPNRODPlanGeneration pgModelInterface]
+ -[PNRODSchemaPNRODPlanGeneration pgOverridesAssetVersion]
+ -[PNRODSchemaPNRODPlanGeneration pgOverridesMatched]
+ -[PNRODSchemaPNRODPlanGeneration pgOverridesTime]
+ -[PNRODSchemaPNRODPlanGeneration pgPlanGenTotalTime]
+ -[PNRODSchemaPNRODPlanGeneration pgPrescribedPlanTime]
+ -[PNRODSchemaPNRODPlanGeneration planCycleId]
+ -[PNRODSchemaPNRODPlanGeneration readFrom:]
+ -[PNRODSchemaPNRODPlanGeneration setFailureInfo:]
+ -[PNRODSchemaPNRODPlanGeneration setHasFailureInfo:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgFullPlannerHandleTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgFullPlannerPostInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgFullPlannerPreInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgModelIdentifier:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgModelInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgModelInterface:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgOverridesAssetVersion:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgOverridesMatched:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgOverridesTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgPlanGenTotalTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPgPrescribedPlanTime:]
+ -[PNRODSchemaPNRODPlanGeneration setHasPlanCycleId:]
+ -[PNRODSchemaPNRODPlanGeneration setPgFullPlannerHandleTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgFullPlannerPostInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgFullPlannerPreInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgModelIdentifier:]
+ -[PNRODSchemaPNRODPlanGeneration setPgModelInferenceTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgModelInterface:]
+ -[PNRODSchemaPNRODPlanGeneration setPgOverridesAssetVersion:]
+ -[PNRODSchemaPNRODPlanGeneration setPgOverridesMatched:]
+ -[PNRODSchemaPNRODPlanGeneration setPgOverridesTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgPlanGenTotalTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPgPrescribedPlanTime:]
+ -[PNRODSchemaPNRODPlanGeneration setPlanCycleId:]
+ -[PNRODSchemaPNRODPlanGeneration writeTo:]
+ -[PNRODSchemaPNRODPlanGeneration(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODPlanGeneration(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODPlanResolution .cxx_destruct]
+ -[PNRODSchemaPNRODPlanResolution actionStatementId]
+ -[PNRODSchemaPNRODPlanResolution deleteActionStatementId]
+ -[PNRODSchemaPNRODPlanResolution deleteFailureInfo]
+ -[PNRODSchemaPNRODPlanResolution deletePlanCycleId]
+ -[PNRODSchemaPNRODPlanResolution deletePrId]
+ -[PNRODSchemaPNRODPlanResolution deletePrTotalHandleTime]
+ -[PNRODSchemaPNRODPlanResolution deleteStatementId]
+ -[PNRODSchemaPNRODPlanResolution dictionaryRepresentation]
+ -[PNRODSchemaPNRODPlanResolution failureInfo]
+ -[PNRODSchemaPNRODPlanResolution hasActionStatementId]
+ -[PNRODSchemaPNRODPlanResolution hasFailureInfo]
+ -[PNRODSchemaPNRODPlanResolution hasPlanCycleId]
+ -[PNRODSchemaPNRODPlanResolution hasPrId]
+ -[PNRODSchemaPNRODPlanResolution hasPrTotalHandleTime]
+ -[PNRODSchemaPNRODPlanResolution hasStatementId]
+ -[PNRODSchemaPNRODPlanResolution hash]
+ -[PNRODSchemaPNRODPlanResolution initWithDictionary:]
+ -[PNRODSchemaPNRODPlanResolution initWithJSON:]
+ -[PNRODSchemaPNRODPlanResolution isEqual:]
+ -[PNRODSchemaPNRODPlanResolution jsonData]
+ -[PNRODSchemaPNRODPlanResolution planCycleId]
+ -[PNRODSchemaPNRODPlanResolution prId]
+ -[PNRODSchemaPNRODPlanResolution prTotalHandleTime]
+ -[PNRODSchemaPNRODPlanResolution readFrom:]
+ -[PNRODSchemaPNRODPlanResolution setActionStatementId:]
+ -[PNRODSchemaPNRODPlanResolution setFailureInfo:]
+ -[PNRODSchemaPNRODPlanResolution setHasActionStatementId:]
+ -[PNRODSchemaPNRODPlanResolution setHasFailureInfo:]
+ -[PNRODSchemaPNRODPlanResolution setHasPlanCycleId:]
+ -[PNRODSchemaPNRODPlanResolution setHasPrId:]
+ -[PNRODSchemaPNRODPlanResolution setHasPrTotalHandleTime:]
+ -[PNRODSchemaPNRODPlanResolution setHasStatementId:]
+ -[PNRODSchemaPNRODPlanResolution setPlanCycleId:]
+ -[PNRODSchemaPNRODPlanResolution setPrId:]
+ -[PNRODSchemaPNRODPlanResolution setPrTotalHandleTime:]
+ -[PNRODSchemaPNRODPlanResolution setStatementId:]
+ -[PNRODSchemaPNRODPlanResolution statementId]
+ -[PNRODSchemaPNRODPlanResolution writeTo:]
+ -[PNRODSchemaPNRODPlanResolution(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODPlanResolution(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODQueryDecoration .cxx_destruct]
+ -[PNRODSchemaPNRODQueryDecoration deleteFailureInfo]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationContextRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationFetchDynamicEnumerationTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationFullPlannerBlockingTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationHandleTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationID]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationInputCollectionTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationOutputBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationSource]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationSpanRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationToolRetrievalContextTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationToolRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationTupleBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration deleteQueryDecorationTupleRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration dictionaryRepresentation]
+ -[PNRODSchemaPNRODQueryDecoration failureInfo]
+ -[PNRODSchemaPNRODQueryDecoration hasFailureInfo]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationContextRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationFetchDynamicEnumerationTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationFullPlannerBlockingTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationHandleTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationID]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationInputCollectionTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationOutputBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationSource]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationSpanRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationToolRetrievalContextTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationToolRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationTupleBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration hasQueryDecorationTupleRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration hash]
+ -[PNRODSchemaPNRODQueryDecoration initWithDictionary:]
+ -[PNRODSchemaPNRODQueryDecoration initWithJSON:]
+ -[PNRODSchemaPNRODQueryDecoration isEqual:]
+ -[PNRODSchemaPNRODQueryDecoration jsonData]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationContextRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationFetchDynamicEnumerationTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationFullPlannerBlockingTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationHandleTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationID]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationInputCollectionTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationOutputBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationSource]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationSpanRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationToolRetrievalContextTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationToolRetrievalTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationTupleBuildingTime]
+ -[PNRODSchemaPNRODQueryDecoration queryDecorationTupleRankingTime]
+ -[PNRODSchemaPNRODQueryDecoration readFrom:]
+ -[PNRODSchemaPNRODQueryDecoration setFailureInfo:]
+ -[PNRODSchemaPNRODQueryDecoration setHasFailureInfo:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationContextRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationFetchDynamicEnumerationTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationFullPlannerBlockingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationHandleTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationID:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationInputCollectionTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationOutputBuildingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationRankingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationSource:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationSpanRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationToolRetrievalContextTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationToolRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationTupleBuildingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setHasQueryDecorationTupleRankingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationContextRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationFetchDynamicEnumerationTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationFullPlannerBlockingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationHandleTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationID:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationInputCollectionTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationOutputBuildingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationRankingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationSource:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationSpanRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationToolRetrievalContextTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationToolRetrievalTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationTupleBuildingTime:]
+ -[PNRODSchemaPNRODQueryDecoration setQueryDecorationTupleRankingTime:]
+ -[PNRODSchemaPNRODQueryDecoration writeTo:]
+ -[PNRODSchemaPNRODQueryDecoration(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODQueryDecoration(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODResponseGeneration .cxx_destruct]
+ -[PNRODSchemaPNRODResponseGeneration deleteFailureInfo]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationCacheManagerTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationCatalogTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationGMSCallTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationHallucinationDetectionTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationHandleTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationID]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationInferenceTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationOverrideTime]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationType]
+ -[PNRODSchemaPNRODResponseGeneration deleteResponseGenerationValidationTime]
+ -[PNRODSchemaPNRODResponseGeneration dictionaryRepresentation]
+ -[PNRODSchemaPNRODResponseGeneration failureInfo]
+ -[PNRODSchemaPNRODResponseGeneration hasFailureInfo]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationCacheManagerTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationCatalogTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationGMSCallTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationHallucinationDetectionTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationHandleTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationID]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationInferenceTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationOverrideTime]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationType]
+ -[PNRODSchemaPNRODResponseGeneration hasResponseGenerationValidationTime]
+ -[PNRODSchemaPNRODResponseGeneration hash]
+ -[PNRODSchemaPNRODResponseGeneration initWithDictionary:]
+ -[PNRODSchemaPNRODResponseGeneration initWithJSON:]
+ -[PNRODSchemaPNRODResponseGeneration isEqual:]
+ -[PNRODSchemaPNRODResponseGeneration jsonData]
+ -[PNRODSchemaPNRODResponseGeneration readFrom:]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationCacheManagerTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationCatalogTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationGMSCallTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationHallucinationDetectionTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationHandleTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationID]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationInferenceTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationOverrideTime]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationType]
+ -[PNRODSchemaPNRODResponseGeneration responseGenerationValidationTime]
+ -[PNRODSchemaPNRODResponseGeneration setFailureInfo:]
+ -[PNRODSchemaPNRODResponseGeneration setHasFailureInfo:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationCacheManagerTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationCatalogTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationGMSCallTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationHallucinationDetectionTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationHandleTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationID:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationInferenceTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationOverrideTime:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationType:]
+ -[PNRODSchemaPNRODResponseGeneration setHasResponseGenerationValidationTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationCacheManagerTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationCatalogTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationGMSCallTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationHallucinationDetectionTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationHandleTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationID:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationInferenceTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationOverrideTime:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationType:]
+ -[PNRODSchemaPNRODResponseGeneration setResponseGenerationValidationTime:]
+ -[PNRODSchemaPNRODResponseGeneration writeTo:]
+ -[PNRODSchemaPNRODResponseGeneration(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODResponseGeneration(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODSearch .cxx_destruct]
+ -[PNRODSchemaPNRODSearch answerSynthesisTime]
+ -[PNRODSchemaPNRODSearch deleteAnswerSynthesisTime]
+ -[PNRODSchemaPNRODSearch deleteFailureInfo]
+ -[PNRODSchemaPNRODSearch deletePostSearchTime]
+ -[PNRODSchemaPNRODSearch deletePreSearchTime]
+ -[PNRODSchemaPNRODSearch deleteSearchGlobalSearchTime]
+ -[PNRODSchemaPNRODSearch deleteSearchHallucinationTime]
+ -[PNRODSchemaPNRODSearch deleteSearchStartToGlobalSearchEnd]
+ -[PNRODSchemaPNRODSearch deleteSearchStartToSpotlightEnd]
+ -[PNRODSchemaPNRODSearch deleteSearchToolId]
+ -[PNRODSchemaPNRODSearch deleteSearchTotalHandleTime]
+ -[PNRODSchemaPNRODSearch deleteSpotlightTotalTime]
+ -[PNRODSchemaPNRODSearch dictionaryRepresentation]
+ -[PNRODSchemaPNRODSearch failureInfo]
+ -[PNRODSchemaPNRODSearch hasAnswerSynthesisTime]
+ -[PNRODSchemaPNRODSearch hasFailureInfo]
+ -[PNRODSchemaPNRODSearch hasPostSearchTime]
+ -[PNRODSchemaPNRODSearch hasPreSearchTime]
+ -[PNRODSchemaPNRODSearch hasSearchGlobalSearchTime]
+ -[PNRODSchemaPNRODSearch hasSearchHallucinationTime]
+ -[PNRODSchemaPNRODSearch hasSearchStartToGlobalSearchEnd]
+ -[PNRODSchemaPNRODSearch hasSearchStartToSpotlightEnd]
+ -[PNRODSchemaPNRODSearch hasSearchToolId]
+ -[PNRODSchemaPNRODSearch hasSearchTotalHandleTime]
+ -[PNRODSchemaPNRODSearch hasSpotlightTotalTime]
+ -[PNRODSchemaPNRODSearch hash]
+ -[PNRODSchemaPNRODSearch initWithDictionary:]
+ -[PNRODSchemaPNRODSearch initWithJSON:]
+ -[PNRODSchemaPNRODSearch isEqual:]
+ -[PNRODSchemaPNRODSearch jsonData]
+ -[PNRODSchemaPNRODSearch postSearchTime]
+ -[PNRODSchemaPNRODSearch preSearchTime]
+ -[PNRODSchemaPNRODSearch readFrom:]
+ -[PNRODSchemaPNRODSearch searchGlobalSearchTime]
+ -[PNRODSchemaPNRODSearch searchHallucinationTime]
+ -[PNRODSchemaPNRODSearch searchStartToGlobalSearchEnd]
+ -[PNRODSchemaPNRODSearch searchStartToSpotlightEnd]
+ -[PNRODSchemaPNRODSearch searchToolId]
+ -[PNRODSchemaPNRODSearch searchTotalHandleTime]
+ -[PNRODSchemaPNRODSearch setAnswerSynthesisTime:]
+ -[PNRODSchemaPNRODSearch setFailureInfo:]
+ -[PNRODSchemaPNRODSearch setHasAnswerSynthesisTime:]
+ -[PNRODSchemaPNRODSearch setHasFailureInfo:]
+ -[PNRODSchemaPNRODSearch setHasPostSearchTime:]
+ -[PNRODSchemaPNRODSearch setHasPreSearchTime:]
+ -[PNRODSchemaPNRODSearch setHasSearchGlobalSearchTime:]
+ -[PNRODSchemaPNRODSearch setHasSearchHallucinationTime:]
+ -[PNRODSchemaPNRODSearch setHasSearchStartToGlobalSearchEnd:]
+ -[PNRODSchemaPNRODSearch setHasSearchStartToSpotlightEnd:]
+ -[PNRODSchemaPNRODSearch setHasSearchToolId:]
+ -[PNRODSchemaPNRODSearch setHasSearchTotalHandleTime:]
+ -[PNRODSchemaPNRODSearch setHasSpotlightTotalTime:]
+ -[PNRODSchemaPNRODSearch setPostSearchTime:]
+ -[PNRODSchemaPNRODSearch setPreSearchTime:]
+ -[PNRODSchemaPNRODSearch setSearchGlobalSearchTime:]
+ -[PNRODSchemaPNRODSearch setSearchHallucinationTime:]
+ -[PNRODSchemaPNRODSearch setSearchStartToGlobalSearchEnd:]
+ -[PNRODSchemaPNRODSearch setSearchStartToSpotlightEnd:]
+ -[PNRODSchemaPNRODSearch setSearchToolId:]
+ -[PNRODSchemaPNRODSearch setSearchTotalHandleTime:]
+ -[PNRODSchemaPNRODSearch setSpotlightTotalTime:]
+ -[PNRODSchemaPNRODSearch spotlightTotalTime]
+ -[PNRODSchemaPNRODSearch writeTo:]
+ -[PNRODSchemaPNRODSearch(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PNRODSchemaPNRODSearch(SensitiveConditions) suppressMessageUnderConditions]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addExecutor:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addPlanGeneration:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addPlanResolution:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addQueryDecoration:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addResponseGeneration:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary addSearch:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearExecutor]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearPlanGeneration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearPlanResolution]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearQueryDecoration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearResponseGeneration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary clearSearch]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deleteExecutor]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deletePlanGeneration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deletePlanResolution]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deleteQueryDecoration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deleteResponseGeneration]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deleteSearch]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary deleteTtaie]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary executorAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary executorCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary executors]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary hasTtaie]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planGenerationAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planGenerationCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planGenerations]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planResolutionAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planResolutionCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary planResolutions]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary queryDecorationAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary queryDecorationCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary queryDecorations]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary responseGenerationAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary responseGenerationCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary responseGenerations]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary searchAtIndex:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary searchCount]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary searchs]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setExecutors:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setHasTtaie:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setPlanGenerations:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setPlanResolutions:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setQueryDecorations:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setResponseGenerations:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setSearchs:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary setTtaie:]
+ -[PNRODSchemaPNRODSiriTurnGrainSummary ttaie]
+ -[QDSchemaQDAppPreLaunchTriggered deleteIsPreLaunchExecuted]
+ -[QDSchemaQDAppPreLaunchTriggered deleteIsPredictionCorrect]
+ -[QDSchemaQDAppPreLaunchTriggered dictionaryRepresentation]
+ -[QDSchemaQDAppPreLaunchTriggered hasIsPreLaunchExecuted]
+ -[QDSchemaQDAppPreLaunchTriggered hasIsPredictionCorrect]
+ -[QDSchemaQDAppPreLaunchTriggered hash]
+ -[QDSchemaQDAppPreLaunchTriggered initWithDictionary:]
+ -[QDSchemaQDAppPreLaunchTriggered initWithJSON:]
+ -[QDSchemaQDAppPreLaunchTriggered isEqual:]
+ -[QDSchemaQDAppPreLaunchTriggered isPreLaunchExecuted]
+ -[QDSchemaQDAppPreLaunchTriggered isPredictionCorrect]
+ -[QDSchemaQDAppPreLaunchTriggered jsonData]
+ -[QDSchemaQDAppPreLaunchTriggered readFrom:]
+ -[QDSchemaQDAppPreLaunchTriggered setHasIsPreLaunchExecuted:]
+ -[QDSchemaQDAppPreLaunchTriggered setHasIsPredictionCorrect:]
+ -[QDSchemaQDAppPreLaunchTriggered setIsPreLaunchExecuted:]
+ -[QDSchemaQDAppPreLaunchTriggered setIsPredictionCorrect:]
+ -[QDSchemaQDAppPreLaunchTriggered writeTo:]
+ -[QDSchemaQDAppPreLaunchTriggered(SensitiveConditions) suppressMessageUnderConditions]
+ -[QDSchemaQDClientEvent appPreLaunchTriggered]
+ -[QDSchemaQDClientEvent contextStatementIdsReported]
+ -[QDSchemaQDClientEvent deleteAppPreLaunchTriggered]
+ -[QDSchemaQDClientEvent deleteContextStatementIdsReported]
+ -[QDSchemaQDClientEvent deleteToolboxSizeReported]
+ -[QDSchemaQDClientEvent hasAppPreLaunchTriggered]
+ -[QDSchemaQDClientEvent hasContextStatementIdsReported]
+ -[QDSchemaQDClientEvent hasToolboxSizeReported]
+ -[QDSchemaQDClientEvent setAppPreLaunchTriggered:]
+ -[QDSchemaQDClientEvent setContextStatementIdsReported:]
+ -[QDSchemaQDClientEvent setHasAppPreLaunchTriggered:]
+ -[QDSchemaQDClientEvent setHasContextStatementIdsReported:]
+ -[QDSchemaQDClientEvent setHasToolboxSizeReported:]
+ -[QDSchemaQDClientEvent setToolboxSizeReported:]
+ -[QDSchemaQDClientEvent toolboxSizeReported]
+ -[QDSchemaQDCollectionStarted .cxx_destruct]
+ -[QDSchemaQDCollectionStarted addCallers:]
+ -[QDSchemaQDCollectionStarted callersAtIndex:]
+ -[QDSchemaQDCollectionStarted callersCount]
+ -[QDSchemaQDCollectionStarted callers]
+ -[QDSchemaQDCollectionStarted clearCallers]
+ -[QDSchemaQDCollectionStarted deleteCallers]
+ -[QDSchemaQDCollectionStarted setCallers:]
+ -[QDSchemaQDContextStatementIdsReported .cxx_destruct]
+ -[QDSchemaQDContextStatementIdsReported addContextStatementIds:]
+ -[QDSchemaQDContextStatementIdsReported addContextualEntityStatementIds:]
+ -[QDSchemaQDContextStatementIdsReported clearContextStatementIds]
+ -[QDSchemaQDContextStatementIdsReported clearContextualEntityStatementIds]
+ -[QDSchemaQDContextStatementIdsReported contextStatementIdsAtIndex:]
+ -[QDSchemaQDContextStatementIdsReported contextStatementIdsCount]
+ -[QDSchemaQDContextStatementIdsReported contextStatementIds]
+ -[QDSchemaQDContextStatementIdsReported contextualEntityStatementIdsAtIndex:]
+ -[QDSchemaQDContextStatementIdsReported contextualEntityStatementIdsCount]
+ -[QDSchemaQDContextStatementIdsReported contextualEntityStatementIds]
+ -[QDSchemaQDContextStatementIdsReported deleteContextStatementIds]
+ -[QDSchemaQDContextStatementIdsReported deleteContextualEntityStatementIds]
+ -[QDSchemaQDContextStatementIdsReported dictionaryRepresentation]
+ -[QDSchemaQDContextStatementIdsReported hash]
+ -[QDSchemaQDContextStatementIdsReported initWithDictionary:]
+ -[QDSchemaQDContextStatementIdsReported initWithJSON:]
+ -[QDSchemaQDContextStatementIdsReported isEqual:]
+ -[QDSchemaQDContextStatementIdsReported jsonData]
+ -[QDSchemaQDContextStatementIdsReported readFrom:]
+ -[QDSchemaQDContextStatementIdsReported setContextStatementIds:]
+ -[QDSchemaQDContextStatementIdsReported setContextualEntityStatementIds:]
+ -[QDSchemaQDContextStatementIdsReported writeTo:]
+ -[QDSchemaQDContextStatementIdsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[QDSchemaQDContextStatementIdsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[QDSchemaQDEntitiesCollected addContext:]
+ -[QDSchemaQDEntitiesCollected clearContext]
+ -[QDSchemaQDEntitiesCollected contextAtIndex:]
+ -[QDSchemaQDEntitiesCollected contextCount]
+ -[QDSchemaQDEntitiesCollected contexts]
+ -[QDSchemaQDEntitiesCollected deleteContext]
+ -[QDSchemaQDEntitiesCollected setContexts:]
+ -[QDSchemaQDToolboxSizeReported deleteTotalToolCount]
+ -[QDSchemaQDToolboxSizeReported dictionaryRepresentation]
+ -[QDSchemaQDToolboxSizeReported hasTotalToolCount]
+ -[QDSchemaQDToolboxSizeReported hash]
+ -[QDSchemaQDToolboxSizeReported initWithDictionary:]
+ -[QDSchemaQDToolboxSizeReported initWithJSON:]
+ -[QDSchemaQDToolboxSizeReported isEqual:]
+ -[QDSchemaQDToolboxSizeReported jsonData]
+ -[QDSchemaQDToolboxSizeReported readFrom:]
+ -[QDSchemaQDToolboxSizeReported setHasTotalToolCount:]
+ -[QDSchemaQDToolboxSizeReported setTotalToolCount:]
+ -[QDSchemaQDToolboxSizeReported totalToolCount]
+ -[QDSchemaQDToolboxSizeReported writeTo:]
+ -[QDSchemaQDToolboxSizeReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[SIRISETUPSchemaSIRISETUPClientEvent deleteSessionSummary]
+ -[SIRISETUPSchemaSIRISETUPClientEvent hasSessionSummary]
+ -[SIRISETUPSchemaSIRISETUPClientEvent sessionSummary]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setHasSessionSummary:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setSessionSummary:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteDidTriggerFirstPass]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteSpeechStartPointDetected]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteTwoPassRecognizerUsed]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted didTriggerFirstPass]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasDidTriggerFirstPass]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasSpeechStartPointDetected]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasTwoPassRecognizerUsed]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setDidTriggerFirstPass:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasDidTriggerFirstPass:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasSpeechStartPointDetected:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasTwoPassRecognizerUsed:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setSpeechStartPointDetected:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setTwoPassRecognizerUsed:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted speechStartPointDetected]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted twoPassRecognizerUsed]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts deleteNumAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts deletePageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts dictionaryRepresentation]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts hasNumAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts hasPageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts hash]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts initWithDictionary:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts initWithJSON:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts isEqual:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts jsonData]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts numAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts pageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts readFrom:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts setHasNumAttempts:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts setHasPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts setNumAttempts:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts setPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts writeTo:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts(SensitiveConditions) suppressMessageUnderConditions]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary .cxx_destruct]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary addPageAttempts:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary clearPageAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary deleteLastCompletedPage]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary deleteLastOpenedPageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary deletePageAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary dictionaryRepresentation]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary hasLastCompletedPage]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary hasLastOpenedPageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary hash]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary initWithDictionary:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary initWithJSON:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary isEqual:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary jsonData]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary lastCompletedPage]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary lastOpenedPageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary pageAttemptsAtIndex:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary pageAttemptsCount]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary pageAttempts]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary readFrom:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary setHasLastCompletedPage:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary setHasLastOpenedPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary setLastCompletedPage:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary setLastOpenedPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary setPageAttempts:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary writeTo:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaClientEvent deleteTranscriptShown]
+ -[SISchemaClientEvent deleteTranscriptTapped]
+ -[SISchemaClientEvent hasTranscriptShown]
+ -[SISchemaClientEvent hasTranscriptTapped]
+ -[SISchemaClientEvent setHasTranscriptShown:]
+ -[SISchemaClientEvent setHasTranscriptTapped:]
+ -[SISchemaClientEvent setTranscriptShown:]
+ -[SISchemaClientEvent setTranscriptTapped:]
+ -[SISchemaClientEvent transcriptShown]
+ -[SISchemaClientEvent transcriptTapped]
+ -[SISchemaUEITranscriptShown deleteTranscriptShownReason]
+ -[SISchemaUEITranscriptShown dictionaryRepresentation]
+ -[SISchemaUEITranscriptShown hasTranscriptShownReason]
+ -[SISchemaUEITranscriptShown hash]
+ -[SISchemaUEITranscriptShown initWithDictionary:]
+ -[SISchemaUEITranscriptShown initWithJSON:]
+ -[SISchemaUEITranscriptShown isEqual:]
+ -[SISchemaUEITranscriptShown jsonData]
+ -[SISchemaUEITranscriptShown readFrom:]
+ -[SISchemaUEITranscriptShown setHasTranscriptShownReason:]
+ -[SISchemaUEITranscriptShown setTranscriptShownReason:]
+ -[SISchemaUEITranscriptShown transcriptShownReason]
+ -[SISchemaUEITranscriptShown writeTo:]
+ -[SISchemaUEITranscriptShown(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaUEITranscriptTapped deleteExists]
+ -[SISchemaUEITranscriptTapped dictionaryRepresentation]
+ -[SISchemaUEITranscriptTapped exists]
+ -[SISchemaUEITranscriptTapped hasExists]
+ -[SISchemaUEITranscriptTapped hash]
+ -[SISchemaUEITranscriptTapped initWithDictionary:]
+ -[SISchemaUEITranscriptTapped initWithJSON:]
+ -[SISchemaUEITranscriptTapped isEqual:]
+ -[SISchemaUEITranscriptTapped jsonData]
+ -[SISchemaUEITranscriptTapped readFrom:]
+ -[SISchemaUEITranscriptTapped setExists:]
+ -[SISchemaUEITranscriptTapped setHasExists:]
+ -[SISchemaUEITranscriptTapped writeTo:]
+ -[SISchemaUEITranscriptTapped(SensitiveConditions) suppressMessageUnderConditions]
+ -[STSchemaSTAnswerSynthesisRequestFailed .cxx_destruct]
+ -[STSchemaSTAnswerSynthesisRequestFailed deleteStError]
+ -[STSchemaSTAnswerSynthesisRequestFailed hasStError]
+ -[STSchemaSTAnswerSynthesisRequestFailed setHasStError:]
+ -[STSchemaSTAnswerSynthesisRequestFailed setStError:]
+ -[STSchemaSTAnswerSynthesisRequestFailed stError]
+ -[STSchemaSTAnswerSynthesisRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTDisambiguationFailed .cxx_destruct]
+ -[STSchemaSTDisambiguationFailed deleteStError]
+ -[STSchemaSTDisambiguationFailed hasStError]
+ -[STSchemaSTDisambiguationFailed setHasStError:]
+ -[STSchemaSTDisambiguationFailed setStError:]
+ -[STSchemaSTDisambiguationFailed stError]
+ -[STSchemaSTDisambiguationFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTFailureError .cxx_destruct]
+ -[STSchemaSTFailureError code]
+ -[STSchemaSTFailureError deleteCode]
+ -[STSchemaSTFailureError deleteDomain]
+ -[STSchemaSTFailureError dictionaryRepresentation]
+ -[STSchemaSTFailureError domain]
+ -[STSchemaSTFailureError hasCode]
+ -[STSchemaSTFailureError hasDomain]
+ -[STSchemaSTFailureError hash]
+ -[STSchemaSTFailureError initWithDictionary:]
+ -[STSchemaSTFailureError initWithJSON:]
+ -[STSchemaSTFailureError isEqual:]
+ -[STSchemaSTFailureError jsonData]
+ -[STSchemaSTFailureError readFrom:]
+ -[STSchemaSTFailureError setCode:]
+ -[STSchemaSTFailureError setDomain:]
+ -[STSchemaSTFailureError setHasCode:]
+ -[STSchemaSTFailureError setHasDomain:]
+ -[STSchemaSTFailureError writeTo:]
+ -[STSchemaSTFailureError(SensitiveConditions) suppressMessageUnderConditions]
+ -[STSchemaSTGeneralSearchFailed .cxx_destruct]
+ -[STSchemaSTGeneralSearchFailed deleteStError]
+ -[STSchemaSTGeneralSearchFailed hasStError]
+ -[STSchemaSTGeneralSearchFailed setHasStError:]
+ -[STSchemaSTGeneralSearchFailed setStError:]
+ -[STSchemaSTGeneralSearchFailed stError]
+ -[STSchemaSTGeneralSearchFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTGlobalSearchRequestFailed .cxx_destruct]
+ -[STSchemaSTGlobalSearchRequestFailed deleteStError]
+ -[STSchemaSTGlobalSearchRequestFailed hasStError]
+ -[STSchemaSTGlobalSearchRequestFailed setHasStError:]
+ -[STSchemaSTGlobalSearchRequestFailed setStError:]
+ -[STSchemaSTGlobalSearchRequestFailed stError]
+ -[STSchemaSTGlobalSearchRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTHallucinationDetectionFailed .cxx_destruct]
+ -[STSchemaSTHallucinationDetectionFailed deleteStError]
+ -[STSchemaSTHallucinationDetectionFailed hasStError]
+ -[STSchemaSTHallucinationDetectionFailed setHasStError:]
+ -[STSchemaSTHallucinationDetectionFailed setStError:]
+ -[STSchemaSTHallucinationDetectionFailed stError]
+ -[STSchemaSTHallucinationDetectionFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTLLMQURequestFailed .cxx_destruct]
+ -[STSchemaSTLLMQURequestFailed deleteStError]
+ -[STSchemaSTLLMQURequestFailed hasStError]
+ -[STSchemaSTLLMQURequestFailed setHasStError:]
+ -[STSchemaSTLLMQURequestFailed setStError:]
+ -[STSchemaSTLLMQURequestFailed stError]
+ -[STSchemaSTLLMQURequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[STSchemaSTSpotlightRequestFailed .cxx_destruct]
+ -[STSchemaSTSpotlightRequestFailed deleteStError]
+ -[STSchemaSTSpotlightRequestFailed hasStError]
+ -[STSchemaSTSpotlightRequestFailed setHasStError:]
+ -[STSchemaSTSpotlightRequestFailed setStError:]
+ -[STSchemaSTSpotlightRequestFailed stError]
+ -[STSchemaSTSpotlightRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SessionSchemaSession creationTimestampInMsSince1970]
+ -[SessionSchemaSession deleteCreationTimestampInMsSince1970]
+ -[SessionSchemaSession hasCreationTimestampInMsSince1970]
+ -[SessionSchemaSession setCreationTimestampInMsSince1970:]
+ -[SessionSchemaSession setHasCreationTimestampInMsSince1970:]
+ -[TTSSchemaTTSSpeechStarted audioQueueLatencyInSecond]
+ -[TTSSchemaTTSSpeechStarted deleteAudioQueueLatencyInSecond]
+ -[TTSSchemaTTSSpeechStarted deleteIsWarmStart]
+ -[TTSSchemaTTSSpeechStarted hasAudioQueueLatencyInSecond]
+ -[TTSSchemaTTSSpeechStarted hasIsWarmStart]
+ -[TTSSchemaTTSSpeechStarted isWarmStart]
+ -[TTSSchemaTTSSpeechStarted setAudioQueueLatencyInSecond:]
+ -[TTSSchemaTTSSpeechStarted setHasAudioQueueLatencyInSecond:]
+ -[TTSSchemaTTSSpeechStarted setHasIsWarmStart:]
+ -[TTSSchemaTTSSpeechStarted setIsWarmStart:]
+ -[UAFSchemaUAFAssetSet deleteExpensiveCellularDownloadRequested]
+ -[UAFSchemaUAFAssetSet deleteFromPreSoftwareUpdateStaging]
+ -[UAFSchemaUAFAssetSet expensiveCellularDownloadRequested]
+ -[UAFSchemaUAFAssetSet fromPreSoftwareUpdateStaging]
+ -[UAFSchemaUAFAssetSet hasExpensiveCellularDownloadRequested]
+ -[UAFSchemaUAFAssetSet hasFromPreSoftwareUpdateStaging]
+ -[UAFSchemaUAFAssetSet setExpensiveCellularDownloadRequested:]
+ -[UAFSchemaUAFAssetSet setFromPreSoftwareUpdateStaging:]
+ -[UAFSchemaUAFAssetSet setHasExpensiveCellularDownloadRequested:]
+ -[UAFSchemaUAFAssetSet setHasFromPreSoftwareUpdateStaging:]
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._contextualEntityCollectionTriggered
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._contextualEntityRetrievalContext
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._hasContextualEntityCollectionTriggered
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._hasContextualEntityRetrievalContext
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._hasPersonalizationUserEditNamedEntityMetrics
+ OBJC_IVAR_$_ASRSchemaASRClientEvent._personalizationUserEditNamedEntityMetrics
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityCollectionTriggered._exists
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityCollectionTriggered._has
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalContext._ended
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalContext._hasEnded
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalContext._hasStartedOrChanged
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalContext._startedOrChanged
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalContext._whichContextevent
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalEnded._retrievedEntityStates
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._enabledTasks
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._has
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._maxEnrolled
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._maxEntityChars
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._maxEntityWords
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._rejectedContextTypes
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._rejectedEntityTypes
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._requestTask
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityRetrievalStarted._retrievalTimeout
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._contextType
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._enrollmentResult
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._entityType
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._has
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._hasEntityType
+ OBJC_IVAR_$_ASRSchemaASRContextualEntityState._rejectReason
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._ended
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._failed
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._hasEnded
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._hasFailed
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._hasStartedOrChanged
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._startedOrChanged
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionContext._whichContextevent
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionEnded._has
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionEnded._hasLinkId
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionEnded._linkId
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionEnded._responseTimeInNs
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionFailed._errorType
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionFailed._has
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionFailed._responseTimeInNs
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._fullPayloadCorrectorInput
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._fullPayloadCorrectorOutput
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._hasFullPayloadCorrectorInput
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._hasFullPayloadCorrectorOutput
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._hasLinkId
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionInfoTier1._linkId
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionStarted._has
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionStarted._utteranceEndTimeInNs
+ OBJC_IVAR_$_ASRSchemaASRFullPayloadCorrectionStarted._utteranceStartTimeInNs
+ OBJC_IVAR_$_ASRSchemaASRLMEOverActivationEdit._has
+ OBJC_IVAR_$_ASRSchemaASRLMEOverActivationEdit._speechProfileCategory
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._entityTaggerCategory
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._has
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._isNamedEntityPresentInSpeechProfile
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._isNamedEntityPresentInVisualContext
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._speechProfileCategories
+ OBJC_IVAR_$_ASRSchemaASRNamedEntityUserEdit._visualContextCategories
+ OBJC_IVAR_$_ASRSchemaASROneBestTranscriptTier1._hasPostItn
+ OBJC_IVAR_$_ASRSchemaASROneBestTranscriptTier1._hasRawRecognition
+ OBJC_IVAR_$_ASRSchemaASROneBestTranscriptTier1._postItn
+ OBJC_IVAR_$_ASRSchemaASROneBestTranscriptTier1._rawRecognition
+ OBJC_IVAR_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics._has
+ OBJC_IVAR_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics._lmeOverActivationEdits
+ OBJC_IVAR_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics._namedEntityUserEdits
+ OBJC_IVAR_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics._numTotalEdit
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRAudioFileResultTier1._hasLinkId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRAudioFileResultTier1._linkId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRAudioFileResultTier1._oneBestTranscripts
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated._hasOriginalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated._originalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted._hasOriginalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted._originalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRDecodingResult._entityScoreResults
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRDecodingResult._oneBestTranscriptLinkIndex
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScore._entityTaggerCategory
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScore._has
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScore._numEntityErrors
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScore._numTotalEntities
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScoringResult._entityScores
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScoringResult._hasReferenceName
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASREntityScoringResult._referenceName
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext._fullPayloadCorrectionContext
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext._hasFullPayloadCorrectionContext
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext._hasOriginalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext._originalAsrId
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1._hasInfoTier1
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1._infoTier1
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._asrFullPayloadCorrectedToUserEdit
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._asrOutputToUserEdit
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._has
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._hasAsrFullPayloadCorrectedToUserEdit
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._hasAsrOutputToUserEdit
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._trueCorrections
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis._trueRegressions
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRPersonalizationExperimentEnded._audioFileResult
+ OBJC_IVAR_$_DODMLASRSchemaDODMLASRPersonalizationExperimentEnded._hasAudioFileResult
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._contextualReplayBiomeRecordCreated
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._contextualReplayBiomeRecordDeleted
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._fullPayloadCorrectionExperimentContext
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._fullPayloadCorrectionExperimentPostAnalysis
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._fullPayloadCorrectionExperimentTier1
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._hasContextualReplayBiomeRecordCreated
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._hasContextualReplayBiomeRecordDeleted
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._hasFullPayloadCorrectionExperimentContext
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._hasFullPayloadCorrectionExperimentPostAnalysis
+ OBJC_IVAR_$_DODMLSchemaDODMLClientEvent._hasFullPayloadCorrectionExperimentTier1
+ OBJC_IVAR_$_EXPSiriSchemaEXPSiriPegasusResponseSummary._isLowConfidenceKnowledgeResult
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorAppIntentCallStarted._appIntentSessionId
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorIdentifierQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorPersonQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorSearchToolQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorStringQueryEntityCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorStringQueryEntityMatcherCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._executorStringQueryLocationCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorIdentifierQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorPersonQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorSearchToolQueryCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorStringQueryEntityCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorStringQueryEntityMatcherCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorClientEvent._hasExecutorStringQueryLocationCallContext
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._hasTraceId
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._traceId
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted._executorSearchToolQueryType
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._ended
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._failed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._hasEnded
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._hasFailed
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._hasStartedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._startedOrChanged
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext._whichContextevent
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed._has
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted._exists
+ OBJC_IVAR_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted._has
+ OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._flowContactTier1
+ OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._hasFlowContactTier1
+ OBJC_IVAR_$_FLOWSchemaFLOWContact._has
+ OBJC_IVAR_$_FLOWSchemaFLOWContact._hasLinkId
+ OBJC_IVAR_$_FLOWSchemaFLOWContact._isRelationship
+ OBJC_IVAR_$_FLOWSchemaFLOWContact._isUnnamedPhoneNumber
+ OBJC_IVAR_$_FLOWSchemaFLOWContact._linkId
+ OBJC_IVAR_$_FLOWSchemaFLOWContactTier1._contactName
+ OBJC_IVAR_$_FLOWSchemaFLOWContactTier1._hasContactName
+ OBJC_IVAR_$_FLOWSchemaFLOWContactTier1._hasLinkId
+ OBJC_IVAR_$_FLOWSchemaFLOWContactTier1._linkId
+ OBJC_IVAR_$_FLOWSchemaFLOWDomainExecutionMetadata._domainExecutionAppIntentBundleID
+ OBJC_IVAR_$_FLOWSchemaFLOWDomainExecutionMetadata._hasDomainExecutionAppIntentBundleID
+ OBJC_IVAR_$_FLOWSchemaFLOWDomainExecutionStarted._domainExecutionMetadata
+ OBJC_IVAR_$_FLOWSchemaFLOWDomainExecutionStarted._hasDomainExecutionMetadata
+ OBJC_IVAR_$_FLOWSchemaFLOWPhoneCallContext._contact
+ OBJC_IVAR_$_FLOWSchemaFLOWPhoneCallContext._hasContact
+ OBJC_IVAR_$_FLOWSchemaFLOWSmsContext._contact
+ OBJC_IVAR_$_FLOWSchemaFLOWSmsContext._hasContact
+ OBJC_IVAR_$_FLSchemaFLActionEvaluationContext._contextId
+ OBJC_IVAR_$_FLSchemaFLActionEvaluationContext._hasContextId
+ OBJC_IVAR_$_FLSchemaFLInteractionDonationContext._contextId
+ OBJC_IVAR_$_FLSchemaFLInteractionDonationContext._hasContextId
+ OBJC_IVAR_$_GMSSchemaGMSModelRequestFailed._errorCode
+ OBJC_IVAR_$_GMSSchemaGMSModelRequestFailed._errorDomainString
+ OBJC_IVAR_$_GMSSchemaGMSModelRequestFailed._hasErrorDomainString
+ OBJC_IVAR_$_IFTSchemaIFTAction._actionParameterValues
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmation._hasSystemStyle
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmation._systemStyle
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyle._generativeAIEnablement
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyle._hasGenerativeAIEnablement
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyle._whichOneof_Actionconfirmationsystemstyle
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement._bundleId
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement._has
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement._hasBundleId
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement._isExplicit
+ OBJC_IVAR_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement._source
+ OBJC_IVAR_$_IFTSchemaIFTActionFailureFailure._hasUnableToCancel
+ OBJC_IVAR_$_IFTSchemaIFTActionFailureFailure._unableToCancel
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterContext._actionClass
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterContext._has
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._confirmed
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._denied
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._hasConfirmed
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._hasDenied
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._hasSelectedInDisambiguation
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._selectedInDisambiguation
+ OBJC_IVAR_$_IFTSchemaIFTActionParameterValue._whichOneof_Promptselection
+ OBJC_IVAR_$_IFTSchemaIFTActionSuccess._shouldOpen
+ OBJC_IVAR_$_IFTSchemaIFTCallExpression._parameters
+ OBJC_IVAR_$_IFTSchemaIFTCallExpressionParameters._callParameterName
+ OBJC_IVAR_$_IFTSchemaIFTCallExpressionParameters._hasCallParameterName
+ OBJC_IVAR_$_IFTSchemaIFTCallExpressionParameters._hasStatementId
+ OBJC_IVAR_$_IFTSchemaIFTCallExpressionParameters._statementId
+ OBJC_IVAR_$_IFTSchemaIFTClientEvent._hasQueryDecorationPrePlannerResult
+ OBJC_IVAR_$_IFTSchemaIFTClientEvent._hasSkipStatement
+ OBJC_IVAR_$_IFTSchemaIFTClientEvent._queryDecorationPrePlannerResult
+ OBJC_IVAR_$_IFTSchemaIFTClientEvent._skipStatement
+ OBJC_IVAR_$_IFTSchemaIFTExpression._format
+ OBJC_IVAR_$_IFTSchemaIFTExpression._hasFormat
+ OBJC_IVAR_$_IFTSchemaIFTExpression._hasPayload
+ OBJC_IVAR_$_IFTSchemaIFTExpression._hasStructuredSearch
+ OBJC_IVAR_$_IFTSchemaIFTExpression._payload
+ OBJC_IVAR_$_IFTSchemaIFTExpression._structuredSearch
+ OBJC_IVAR_$_IFTSchemaIFTFormatExpression._statementIds
+ OBJC_IVAR_$_IFTSchemaIFTParameterNotAllowed._reason
+ OBJC_IVAR_$_IFTSchemaIFTPayloadExpression._statementIds
+ OBJC_IVAR_$_IFTSchemaIFTPrimitive._primitiveType
+ OBJC_IVAR_$_IFTSchemaIFTProgramStatement._has
+ OBJC_IVAR_$_IFTSchemaIFTProgramStatement._isRoot
+ OBJC_IVAR_$_IFTSchemaIFTQueryDecorationPrePlannerResult._exists
+ OBJC_IVAR_$_IFTSchemaIFTQueryDecorationPrePlannerResult._has
+ OBJC_IVAR_$_IFTSchemaIFTQueryStep._context
+ OBJC_IVAR_$_IFTSchemaIFTQueryStep._hasContext
+ OBJC_IVAR_$_IFTSchemaIFTQueryStep._payloadType
+ OBJC_IVAR_$_IFTSchemaIFTSessionCoordinatorError._failedToConvertClientEvent
+ OBJC_IVAR_$_IFTSchemaIFTSessionCoordinatorError._hasFailedToConvertClientEvent
+ OBJC_IVAR_$_IFTSchemaIFTSkipStatement._hasStatementId
+ OBJC_IVAR_$_IFTSchemaIFTSkipStatement._statementId
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._has
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._hasReturnType
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._isExpanded
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._parameters
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._properties
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpression._returnType
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpressionParameters._hasStatementId
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpressionParameters._hasStructuredSearchParameterName
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpressionParameters._statementId
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchExpressionParameters._structuredSearchParameterName
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchProperty._exists
+ OBJC_IVAR_$_IFTSchemaIFTStructuredSearchProperty._has
+ OBJC_IVAR_$_IFTSchemaIFTTypeInstance._collection
+ OBJC_IVAR_$_IFTSchemaIFTTypeInstance._hasCollection
+ OBJC_IVAR_$_IFTSchemaIFTTypeInstance._hasTypeIdentifier
+ OBJC_IVAR_$_IFTSchemaIFTTypeInstance._typeIdentifier
+ OBJC_IVAR_$_IFTSchemaIFTTypeInstance._whichItemtype
+ OBJC_IVAR_$_IFTSchemaIFTValueExpression._array
+ OBJC_IVAR_$_IFTSchemaIFTValueExpression._hasArray
+ OBJC_IVAR_$_IFTSchemaIFTValueExpressionArrayVariant._statementIds
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals._isDefaultApp
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals._isRequestByHandleType
+ OBJC_IVAR_$_INFERENCESchemaINFERENCECommsAppSelectionTrainingAppDependentSignals._isRequestByLabel
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._anonymizedLocationNameId
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._anonymizedLocationTypeId
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._bucketedDistance
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._has
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._hasAnonymizedLocationNameId
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._hasAnonymizedLocationTypeId
+ OBJC_IVAR_$_JRSchemaHistoricalLocationContext._logOfTimeElapsedInSeconds
+ OBJC_IVAR_$_JRSchemaIntervalUntilStartTime._candidateBooleanMasks
+ OBJC_IVAR_$_JRSchemaIntervalUntilStartTime._candidateTimeIntervalMatrixs
+ OBJC_IVAR_$_JRSchemaJRCandidateBooleanMask._isApplicableToCandidates
+ OBJC_IVAR_$_JRSchemaJRCandidateRiskLevel._riskLevels
+ OBJC_IVAR_$_JRSchemaJRCandidateSearchToolRank._searchToolRanks
+ OBJC_IVAR_$_JRSchemaJRCandidateTimeIntervalMatrix._logOfIntervalUntilStartTimeInSeconds
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._candidateA
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._candidateB
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._has
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._hasCandidateA
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._hasCandidateB
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityRow._similarityScore
+ OBJC_IVAR_$_JRSchemaJREntitySimilarityScores._rows
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._bucketedDistances
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._candidateRisks
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._intervalUntilStartTimes
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._jrEntitySimilarityScores
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._loudnessLevel
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._parameterSubTypes
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._scores
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._searchToolRanks
+ OBJC_IVAR_$_JRSchemaJRInferenceEnded._signalToNoiseRatio
+ OBJC_IVAR_$_JRSchemaJRTokenConfidence._asrScores
+ OBJC_IVAR_$_JRSchemaUserHistory._historicalLocationContexts
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._backgroundNoiseActivityLevel
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._backgroundNoiseLevel
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._has
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._invocationType
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._isMediaPlaybackOn
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._isPermanentOffsetEnabled
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._musicLoudnessLevel
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._permanentOffsetFactor
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._speakerDistance
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._speakerSpeechLevel
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried._ttsVolume
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected._has
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected._isPermanentOffsetEnabled
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected._permanentOffsetFactor
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected._userIntentType
+ OBJC_IVAR_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected._userIntentVolume
+ OBJC_IVAR_$_MHSchemaMHClientEvent._adaptiveSiriVolumeTTSVolumeQueried
+ OBJC_IVAR_$_MHSchemaMHClientEvent._adaptiveSiriVolumeUserIntentDetected
+ OBJC_IVAR_$_MHSchemaMHClientEvent._hasAdaptiveSiriVolumeTTSVolumeQueried
+ OBJC_IVAR_$_MHSchemaMHClientEvent._hasAdaptiveSiriVolumeUserIntentDetected
+ OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._hasNlRouterPromptGenerated
+ OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._nlRouterPromptGenerated
+ OBJC_IVAR_$_NLRouterSchemaNLRouterHandleEnded._hasOverrideMetadata
+ OBJC_IVAR_$_NLRouterSchemaNLRouterHandleEnded._overrideMetadata
+ OBJC_IVAR_$_NLRouterSchemaNLRouterOverrideMetadata._hasOverrideId
+ OBJC_IVAR_$_NLRouterSchemaNLRouterOverrideMetadata._overrideId
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptComponent._componentType
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptComponent._has
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptComponent._sizeInTokens
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerated._components
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerated._droppedComponents
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerated._estimatedSizeInTokens
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerated._has
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerated._totalSizeInTokens
+ OBJC_IVAR_$_NLRouterSchemaNLRouterPromptGenerationSignalsCaptured._isMailAppFocused
+ OBJC_IVAR_$_NLXSchemaCDMUserDialogAct._hasWantedToUndo
+ OBJC_IVAR_$_NLXSchemaCDMUserDialogAct._wantedToUndo
+ OBJC_IVAR_$_NLXSchemaCDMUserWantedToUndo._exists
+ OBJC_IVAR_$_NLXSchemaCDMUserWantedToUndo._has
+ OBJC_IVAR_$_ODBATCHSiriSchemaODBATCHTurnRestatementScore._isCrossDevice
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._eventOrigin
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._hasUserAggregationId
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._isLongLivedIDUploadDisabled
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._userAggregationId
+ OBJC_IVAR_$_ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported._hasPostItn1Best
+ OBJC_IVAR_$_ODSAMPLESiriSchemaODSAMPLESpeakerIdModelSampleReported._postItn1Best
+ OBJC_IVAR_$_ORCHSchemaORCHAudioTopologyReported._audioTopology
+ OBJC_IVAR_$_ORCHSchemaORCHAudioTopologyReported._has
+ OBJC_IVAR_$_ORCHSchemaORCHAudioTopologyReported._isLeader
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._audioTopologyReported
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._hasAudioTopologyReported
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._hasIntelligenceFlowRequestContext
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._intelligenceFlowRequestContext
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._ended
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._failed
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasEnded
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasFailed
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasStartedOrChanged
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasSubRequestId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasTraceId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._hasTrpId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._startedOrChanged
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._subRequestId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._traceId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._trpId
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestContext._whichContextevent
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestEnded._has
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestEnded._shimAction
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestFailed._has
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestFailed._isSiriXFallback
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestFailed._reason
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestStarted._exists
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestStarted._has
+ OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._hasSelectedloggableUserIdHash
+ OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._selectedloggableUserIdHash
+ OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._voiceIdClassification
+ OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._voiceIdScores
+ OBJC_IVAR_$_ORCHSchemaORCHMultiUserScore._hasLoggableUserIdHash
+ OBJC_IVAR_$_ORCHSchemaORCHMultiUserScore._loggableUserIdHash
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlignmentOffset._endCharacterIdx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlignmentOffset._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlignmentOffset._startCharacterIdx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1._alternateQuerySuggestionType
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1._hasText
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1._text
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1._alternateQuerySuggestionCandidateTier1s
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrCorrectionInfo._asrHypothesesInfos
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx._hasSourceAuxKey
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx._originalAsrInterpretationIdx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx._sourceAuxIdx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx._sourceAuxKey
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._corrections
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._hasIdx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._hasPostItnUtterance
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._idx
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._postItnUtterance
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._score
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._selectedAsAlternateSuggestion
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo._selectedAsPrimaryResponse
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._alignmentOffset
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._correction
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._hasAlignmentOffset
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._hasCorrection
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._hasOriginal
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._hasSourceAuxKey
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._original
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._score
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSCorrectionInfo._sourceAuxKey
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSRequestEnded._alternateQuerySuggestionTier1
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSRequestEnded._hasAlternateQuerySuggestionTier1
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSServerEvent._hasPegasusAsrCorrectionInfo
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSServerEvent._pegasusAsrCorrectionInfo
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSVideoExecutionTier1._has
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSVideoExecutionTier1._isNlsResult
+ OBJC_IVAR_$_PGSchemaPGClientEvent._hasPgGeneratePlanContext
+ OBJC_IVAR_$_PGSchemaPGClientEvent._pgGeneratePlanContext
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._ended
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._failed
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._hasEnded
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._hasFailed
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._hasStartedOrChanged
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._startedOrChanged
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanContext._whichContextevent
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanEnded._exists
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanEnded._has
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanFailed._criticalError
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanFailed._hasCriticalError
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanStarted._exists
+ OBJC_IVAR_$_PGSchemaPGGeneratePlanStarted._has
+ OBJC_IVAR_$_PGSchemaPGOverridesEnded._assetVersion
+ OBJC_IVAR_$_PGSchemaPGOverridesEnded._hasAssetVersion
+ OBJC_IVAR_$_PGSchemaPGOverridesEnded._hasOverridesMatched
+ OBJC_IVAR_$_PGSchemaPGOverridesEnded._overridesMatched
+ OBJC_IVAR_$_PGSchemaPGOverridesFailed._assetVersion
+ OBJC_IVAR_$_PGSchemaPGOverridesFailed._hasAssetVersion
+ OBJC_IVAR_$_PGSchemaPGOverridesMatchMetadata._has
+ OBJC_IVAR_$_PGSchemaPGOverridesMatchMetadata._isMatched
+ OBJC_IVAR_$_PGSchemaPGPromptResponseTier1._grammar
+ OBJC_IVAR_$_PGSchemaPGPromptResponseTier1._hasGrammar
+ OBJC_IVAR_$_PNRODSchemaPNRError._code
+ OBJC_IVAR_$_PNRODSchemaPNRError._domain
+ OBJC_IVAR_$_PNRODSchemaPNRError._has
+ OBJC_IVAR_$_PNRODSchemaPNRError._hasDomain
+ OBJC_IVAR_$_PNRODSchemaPNRError._source
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._executorAppIntentHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._executorAppIntentQueryHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._executorId
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._executorSearchToolQueryType
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._has
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasExecutorAppIntentHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasExecutorAppIntentQueryHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasExecutorId
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasIdentifierQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasPersonQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasPlanCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasSearchToolQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasStringQueryEntityMatcherTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasStringQueryEntityTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._hasStringQueryLocationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._identifierQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._personQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._planCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._searchToolQueryTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._stringQueryEntityMatcherTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._stringQueryEntityTime
+ OBJC_IVAR_$_PNRODSchemaPNRODExecutor._stringQueryLocationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._error
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._hasError
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._hasUnderUnderlyingError
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._hasUnderlyingError
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._underUnderlyingError
+ OBJC_IVAR_$_PNRODSchemaPNRODFailureInfo._underlyingError
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary._appEntityQueryResponseTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary._hasAppEntityQueryResponseTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary._numActionsCreated
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary._numQueriesCreated
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowActionGrainSummary._statementId
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary._hasPlanGenerationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary._hasQueryDecorationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary._planGenerationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary._queryDecorationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODIntelligenceFlowRequestGrainSummary._requestFeatureTags
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._has
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgFullPlannerHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgFullPlannerPostInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgFullPlannerPreInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgModelIdentifier
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgModelInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgOverridesAssetVersion
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgOverridesTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgPlanGenTotalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPgPrescribedPlanTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._hasPlanCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgFullPlannerHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgFullPlannerPostInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgFullPlannerPreInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgModelIdentifier
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgModelInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgModelInterface
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgOverridesAssetVersion
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgOverridesMatched
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgOverridesTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgPlanGenTotalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._pgPrescribedPlanTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanGeneration._planCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._actionStatementId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._has
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._hasPlanCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._hasPrId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._hasPrTotalHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._planCycleId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._prId
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._prTotalHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODPlanResolution._statementId
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._has
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationContextRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationFetchDynamicEnumerationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationFullPlannerBlockingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationID
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationInputCollectionTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationOutputBuildingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationRankingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationSpanRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationToolRetrievalContextTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationToolRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationTupleBuildingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._hasQueryDecorationTupleRankingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationContextRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationFetchDynamicEnumerationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationFullPlannerBlockingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationID
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationInputCollectionTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationOutputBuildingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationRankingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationSource
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationSpanRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationToolRetrievalContextTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationToolRetrievalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationTupleBuildingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODQueryDecoration._queryDecorationTupleRankingTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._has
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationCacheManagerTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationCatalogTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationGMSCallTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationHallucinationDetectionTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationID
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationOverrideTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._hasResponseGenerationValidationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationCacheManagerTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationCatalogTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationGMSCallTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationHallucinationDetectionTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationID
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationInferenceTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationOverrideTime
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationType
+ OBJC_IVAR_$_PNRODSchemaPNRODResponseGeneration._responseGenerationValidationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._answerSynthesisTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._failureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasAnswerSynthesisTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasFailureInfo
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasPostSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasPreSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchGlobalSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchHallucinationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchStartToGlobalSearchEnd
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchStartToSpotlightEnd
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchToolId
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSearchTotalHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._hasSpotlightTotalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._postSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._preSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchGlobalSearchTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchHallucinationTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchStartToGlobalSearchEnd
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchStartToSpotlightEnd
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchToolId
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._searchTotalHandleTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSearch._spotlightTotalTime
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._executors
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._hasTtaie
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._planGenerations
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._planResolutions
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._queryDecorations
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._responseGenerations
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._searchs
+ OBJC_IVAR_$_PNRODSchemaPNRODSiriTurnGrainSummary._ttaie
+ OBJC_IVAR_$_QDSchemaQDAppPreLaunchTriggered._has
+ OBJC_IVAR_$_QDSchemaQDAppPreLaunchTriggered._isPreLaunchExecuted
+ OBJC_IVAR_$_QDSchemaQDAppPreLaunchTriggered._isPredictionCorrect
+ OBJC_IVAR_$_QDSchemaQDClientEvent._appPreLaunchTriggered
+ OBJC_IVAR_$_QDSchemaQDClientEvent._contextStatementIdsReported
+ OBJC_IVAR_$_QDSchemaQDClientEvent._hasAppPreLaunchTriggered
+ OBJC_IVAR_$_QDSchemaQDClientEvent._hasContextStatementIdsReported
+ OBJC_IVAR_$_QDSchemaQDClientEvent._hasToolboxSizeReported
+ OBJC_IVAR_$_QDSchemaQDClientEvent._toolboxSizeReported
+ OBJC_IVAR_$_QDSchemaQDCollectionStarted._callers
+ OBJC_IVAR_$_QDSchemaQDContextStatementIdsReported._contextStatementIds
+ OBJC_IVAR_$_QDSchemaQDContextStatementIdsReported._contextualEntityStatementIds
+ OBJC_IVAR_$_QDSchemaQDEntitiesCollected._contexts
+ OBJC_IVAR_$_QDSchemaQDToolboxSizeReported._has
+ OBJC_IVAR_$_QDSchemaQDToolboxSizeReported._totalToolCount
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._hasSessionSummary
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._sessionSummary
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._didTriggerFirstPass
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._speechStartPointDetected
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._twoPassRecognizerUsed
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts._has
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts._numAttempts
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts._pageNumber
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary._has
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary._lastCompletedPage
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary._lastOpenedPageNumber
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary._pageAttempts
+ OBJC_IVAR_$_SISchemaClientEvent._hasTranscriptShown
+ OBJC_IVAR_$_SISchemaClientEvent._hasTranscriptTapped
+ OBJC_IVAR_$_SISchemaClientEvent._transcriptShown
+ OBJC_IVAR_$_SISchemaClientEvent._transcriptTapped
+ OBJC_IVAR_$_SISchemaUEITranscriptShown._has
+ OBJC_IVAR_$_SISchemaUEITranscriptShown._transcriptShownReason
+ OBJC_IVAR_$_SISchemaUEITranscriptTapped._exists
+ OBJC_IVAR_$_SISchemaUEITranscriptTapped._has
+ OBJC_IVAR_$_STSchemaSTAnswerSynthesisRequestFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTAnswerSynthesisRequestFailed._stError
+ OBJC_IVAR_$_STSchemaSTDisambiguationFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTDisambiguationFailed._stError
+ OBJC_IVAR_$_STSchemaSTFailureError._code
+ OBJC_IVAR_$_STSchemaSTFailureError._domain
+ OBJC_IVAR_$_STSchemaSTFailureError._has
+ OBJC_IVAR_$_STSchemaSTFailureError._hasDomain
+ OBJC_IVAR_$_STSchemaSTGeneralSearchFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTGeneralSearchFailed._stError
+ OBJC_IVAR_$_STSchemaSTGlobalSearchRequestFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTGlobalSearchRequestFailed._stError
+ OBJC_IVAR_$_STSchemaSTHallucinationDetectionFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTHallucinationDetectionFailed._stError
+ OBJC_IVAR_$_STSchemaSTLLMQURequestFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTLLMQURequestFailed._stError
+ OBJC_IVAR_$_STSchemaSTSpotlightRequestFailed._hasStError
+ OBJC_IVAR_$_STSchemaSTSpotlightRequestFailed._stError
+ OBJC_IVAR_$_SessionSchemaSession._creationTimestampInMsSince1970
+ OBJC_IVAR_$_SessionSchemaSession._has
+ OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._audioQueueLatencyInSecond
+ OBJC_IVAR_$_TTSSchemaTTSSpeechStarted._isWarmStart
+ OBJC_IVAR_$_UAFSchemaUAFAssetSet._expensiveCellularDownloadRequested
+ OBJC_IVAR_$_UAFSchemaUAFAssetSet._fromPreSoftwareUpdateStaging
+ OBJC_IVAR_$_UAFSchemaUAFAssetSet._has
+ _ASRSchemaASRContextualEntityCollectionTriggeredReadFrom
+ _ASRSchemaASRContextualEntityRetrievalContextReadFrom
+ _ASRSchemaASRContextualEntityRetrievalEndedReadFrom
+ _ASRSchemaASRContextualEntityRetrievalStartedReadFrom
+ _ASRSchemaASRContextualEntityStateReadFrom
+ _ASRSchemaASRFullPayloadCorrectionContextReadFrom
+ _ASRSchemaASRFullPayloadCorrectionEndedReadFrom
+ _ASRSchemaASRFullPayloadCorrectionFailedReadFrom
+ _ASRSchemaASRFullPayloadCorrectionInfoTier1ReadFrom
+ _ASRSchemaASRFullPayloadCorrectionStartedReadFrom
+ _ASRSchemaASRLMEOverActivationEditReadFrom
+ _ASRSchemaASRNamedEntityUserEditReadFrom
+ _ASRSchemaASROneBestTranscriptTier1ReadFrom
+ _ASRSchemaASRPersonalizationUserEditNamedEntityMetricsReadFrom
+ _DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreatedReadFrom
+ _DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeletedReadFrom
+ _DODMLASRSchemaDODMLASREntityScoreReadFrom
+ _DODMLASRSchemaDODMLASREntityScoringResultReadFrom
+ _DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContextReadFrom
+ _DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1ReadFrom
+ _DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysisReadFrom
+ _ExecutorSiriSchemaExecutorIdentifierQueryCallContextReadFrom
+ _ExecutorSiriSchemaExecutorIdentifierQueryCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorIdentifierQueryCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorIdentifierQueryCallStartedReadFrom
+ _ExecutorSiriSchemaExecutorPersonQueryCallContextReadFrom
+ _ExecutorSiriSchemaExecutorPersonQueryCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorPersonQueryCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorPersonQueryCallStartedReadFrom
+ _ExecutorSiriSchemaExecutorSearchToolQueryCallContextReadFrom
+ _ExecutorSiriSchemaExecutorSearchToolQueryCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorSearchToolQueryCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorSearchToolQueryCallStartedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityCallContextReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityCallStartedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContextReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStartedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryLocationCallContextReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryLocationCallEndedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryLocationCallFailedReadFrom
+ _ExecutorSiriSchemaExecutorStringQueryLocationCallStartedReadFrom
+ _FLOWSchemaFLOWContactReadFrom
+ _FLOWSchemaFLOWContactTier1ReadFrom
+ _FLOWSchemaFLOWDomainExecutionMetadataReadFrom
+ _IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablementReadFrom
+ _IFTSchemaIFTActionConfirmationSystemStyleReadFrom
+ _IFTSchemaIFTActionParameterValueReadFrom
+ _IFTSchemaIFTCallExpressionParametersReadFrom
+ _IFTSchemaIFTFormatExpressionReadFrom
+ _IFTSchemaIFTPayloadExpressionReadFrom
+ _IFTSchemaIFTQueryDecorationPrePlannerResultReadFrom
+ _IFTSchemaIFTSkipStatementReadFrom
+ _IFTSchemaIFTStructuredSearchExpressionParametersReadFrom
+ _IFTSchemaIFTStructuredSearchExpressionReadFrom
+ _IFTSchemaIFTStructuredSearchPropertyReadFrom
+ _IFTSchemaIFTTypeInstanceReadFrom
+ _IFTSchemaIFTValueExpressionArrayVariantReadFrom
+ _JRSchemaHistoricalLocationContextReadFrom
+ _JRSchemaIntervalUntilStartTimeReadFrom
+ _JRSchemaJRCandidateBooleanMaskReadFrom
+ _JRSchemaJRCandidateRiskLevelReadFrom
+ _JRSchemaJRCandidateSearchToolRankReadFrom
+ _JRSchemaJRCandidateTimeIntervalMatrixReadFrom
+ _JRSchemaJREntitySimilarityRowReadFrom
+ _JRSchemaJREntitySimilarityScoresReadFrom
+ _JRSchemaJRTokenConfidenceReadFrom
+ _MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueriedReadFrom
+ _MHSchemaMHAdaptiveSiriVolumeUserIntentDetectedReadFrom
+ _NLRouterSchemaNLRouterOverrideMetadataReadFrom
+ _NLRouterSchemaNLRouterPromptComponentReadFrom
+ _NLRouterSchemaNLRouterPromptGeneratedReadFrom
+ _NLXSchemaCDMUserWantedToUndoReadFrom
+ _OBJC_CLASS_$_ASRSchemaASRContextualEntityCollectionTriggered
+ _OBJC_CLASS_$_ASRSchemaASRContextualEntityRetrievalContext
+ _OBJC_CLASS_$_ASRSchemaASRContextualEntityRetrievalEnded
+ _OBJC_CLASS_$_ASRSchemaASRContextualEntityRetrievalStarted
+ _OBJC_CLASS_$_ASRSchemaASRContextualEntityState
+ _OBJC_CLASS_$_ASRSchemaASRFullPayloadCorrectionContext
+ _OBJC_CLASS_$_ASRSchemaASRFullPayloadCorrectionEnded
+ _OBJC_CLASS_$_ASRSchemaASRFullPayloadCorrectionFailed
+ _OBJC_CLASS_$_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ _OBJC_CLASS_$_ASRSchemaASRFullPayloadCorrectionStarted
+ _OBJC_CLASS_$_ASRSchemaASRLMEOverActivationEdit
+ _OBJC_CLASS_$_ASRSchemaASRNamedEntityUserEdit
+ _OBJC_CLASS_$_ASRSchemaASROneBestTranscriptTier1
+ _OBJC_CLASS_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASREntityScore
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASREntityScoringResult
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ _OBJC_CLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ _OBJC_CLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ _OBJC_CLASS_$_FLOWSchemaFLOWContact
+ _OBJC_CLASS_$_FLOWSchemaFLOWContactTier1
+ _OBJC_CLASS_$_FLOWSchemaFLOWDomainExecutionMetadata
+ _OBJC_CLASS_$_IFTSchemaIFTActionConfirmationSystemStyle
+ _OBJC_CLASS_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ _OBJC_CLASS_$_IFTSchemaIFTActionParameterValue
+ _OBJC_CLASS_$_IFTSchemaIFTCallExpressionParameters
+ _OBJC_CLASS_$_IFTSchemaIFTFormatExpression
+ _OBJC_CLASS_$_IFTSchemaIFTPayloadExpression
+ _OBJC_CLASS_$_IFTSchemaIFTQueryDecorationPrePlannerResult
+ _OBJC_CLASS_$_IFTSchemaIFTSkipStatement
+ _OBJC_CLASS_$_IFTSchemaIFTStructuredSearchExpression
+ _OBJC_CLASS_$_IFTSchemaIFTStructuredSearchExpressionParameters
+ _OBJC_CLASS_$_IFTSchemaIFTStructuredSearchProperty
+ _OBJC_CLASS_$_IFTSchemaIFTTypeInstance
+ _OBJC_CLASS_$_IFTSchemaIFTValueExpressionArrayVariant
+ _OBJC_CLASS_$_JRSchemaHistoricalLocationContext
+ _OBJC_CLASS_$_JRSchemaIntervalUntilStartTime
+ _OBJC_CLASS_$_JRSchemaJRCandidateBooleanMask
+ _OBJC_CLASS_$_JRSchemaJRCandidateRiskLevel
+ _OBJC_CLASS_$_JRSchemaJRCandidateSearchToolRank
+ _OBJC_CLASS_$_JRSchemaJRCandidateTimeIntervalMatrix
+ _OBJC_CLASS_$_JRSchemaJREntitySimilarityRow
+ _OBJC_CLASS_$_JRSchemaJREntitySimilarityScores
+ _OBJC_CLASS_$_JRSchemaJRTokenConfidence
+ _OBJC_CLASS_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ _OBJC_CLASS_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterOverrideMetadata
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterPromptComponent
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterPromptGenerated
+ _OBJC_CLASS_$_NLXSchemaCDMUserWantedToUndo
+ _OBJC_CLASS_$_ORCHSchemaORCHAudioTopologyReported
+ _OBJC_CLASS_$_ORCHSchemaORCHIntelligenceFlowRequestContext
+ _OBJC_CLASS_$_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ _OBJC_CLASS_$_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ _OBJC_CLASS_$_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAlignmentOffset
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSCorrectionInfo
+ _OBJC_CLASS_$_PGSchemaPGGeneratePlanContext
+ _OBJC_CLASS_$_PGSchemaPGGeneratePlanEnded
+ _OBJC_CLASS_$_PGSchemaPGGeneratePlanFailed
+ _OBJC_CLASS_$_PGSchemaPGGeneratePlanStarted
+ _OBJC_CLASS_$_PGSchemaPGOverridesMatchMetadata
+ _OBJC_CLASS_$_PNRODSchemaPNRError
+ _OBJC_CLASS_$_PNRODSchemaPNRODExecutor
+ _OBJC_CLASS_$_PNRODSchemaPNRODPlanGeneration
+ _OBJC_CLASS_$_PNRODSchemaPNRODPlanResolution
+ _OBJC_CLASS_$_PNRODSchemaPNRODQueryDecoration
+ _OBJC_CLASS_$_PNRODSchemaPNRODResponseGeneration
+ _OBJC_CLASS_$_PNRODSchemaPNRODSearch
+ _OBJC_CLASS_$_QDSchemaQDAppPreLaunchTriggered
+ _OBJC_CLASS_$_QDSchemaQDContextStatementIdsReported
+ _OBJC_CLASS_$_QDSchemaQDToolboxSizeReported
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ _OBJC_CLASS_$_SISchemaUEITranscriptShown
+ _OBJC_CLASS_$_SISchemaUEITranscriptTapped
+ _OBJC_CLASS_$_STSchemaSTFailureError
+ _OBJC_METACLASS_$_ASRSchemaASRContextualEntityCollectionTriggered
+ _OBJC_METACLASS_$_ASRSchemaASRContextualEntityRetrievalContext
+ _OBJC_METACLASS_$_ASRSchemaASRContextualEntityRetrievalEnded
+ _OBJC_METACLASS_$_ASRSchemaASRContextualEntityRetrievalStarted
+ _OBJC_METACLASS_$_ASRSchemaASRContextualEntityState
+ _OBJC_METACLASS_$_ASRSchemaASRFullPayloadCorrectionContext
+ _OBJC_METACLASS_$_ASRSchemaASRFullPayloadCorrectionEnded
+ _OBJC_METACLASS_$_ASRSchemaASRFullPayloadCorrectionFailed
+ _OBJC_METACLASS_$_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ _OBJC_METACLASS_$_ASRSchemaASRFullPayloadCorrectionStarted
+ _OBJC_METACLASS_$_ASRSchemaASRLMEOverActivationEdit
+ _OBJC_METACLASS_$_ASRSchemaASRNamedEntityUserEdit
+ _OBJC_METACLASS_$_ASRSchemaASROneBestTranscriptTier1
+ _OBJC_METACLASS_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASREntityScore
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASREntityScoringResult
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ _OBJC_METACLASS_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ _OBJC_METACLASS_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ _OBJC_METACLASS_$_FLOWSchemaFLOWContact
+ _OBJC_METACLASS_$_FLOWSchemaFLOWContactTier1
+ _OBJC_METACLASS_$_FLOWSchemaFLOWDomainExecutionMetadata
+ _OBJC_METACLASS_$_IFTSchemaIFTActionConfirmationSystemStyle
+ _OBJC_METACLASS_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ _OBJC_METACLASS_$_IFTSchemaIFTActionParameterValue
+ _OBJC_METACLASS_$_IFTSchemaIFTCallExpressionParameters
+ _OBJC_METACLASS_$_IFTSchemaIFTFormatExpression
+ _OBJC_METACLASS_$_IFTSchemaIFTPayloadExpression
+ _OBJC_METACLASS_$_IFTSchemaIFTQueryDecorationPrePlannerResult
+ _OBJC_METACLASS_$_IFTSchemaIFTSkipStatement
+ _OBJC_METACLASS_$_IFTSchemaIFTStructuredSearchExpression
+ _OBJC_METACLASS_$_IFTSchemaIFTStructuredSearchExpressionParameters
+ _OBJC_METACLASS_$_IFTSchemaIFTStructuredSearchProperty
+ _OBJC_METACLASS_$_IFTSchemaIFTTypeInstance
+ _OBJC_METACLASS_$_IFTSchemaIFTValueExpressionArrayVariant
+ _OBJC_METACLASS_$_JRSchemaHistoricalLocationContext
+ _OBJC_METACLASS_$_JRSchemaIntervalUntilStartTime
+ _OBJC_METACLASS_$_JRSchemaJRCandidateBooleanMask
+ _OBJC_METACLASS_$_JRSchemaJRCandidateRiskLevel
+ _OBJC_METACLASS_$_JRSchemaJRCandidateSearchToolRank
+ _OBJC_METACLASS_$_JRSchemaJRCandidateTimeIntervalMatrix
+ _OBJC_METACLASS_$_JRSchemaJREntitySimilarityRow
+ _OBJC_METACLASS_$_JRSchemaJREntitySimilarityScores
+ _OBJC_METACLASS_$_JRSchemaJRTokenConfidence
+ _OBJC_METACLASS_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ _OBJC_METACLASS_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterOverrideMetadata
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterPromptComponent
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterPromptGenerated
+ _OBJC_METACLASS_$_NLXSchemaCDMUserWantedToUndo
+ _OBJC_METACLASS_$_ORCHSchemaORCHAudioTopologyReported
+ _OBJC_METACLASS_$_ORCHSchemaORCHIntelligenceFlowRequestContext
+ _OBJC_METACLASS_$_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ _OBJC_METACLASS_$_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ _OBJC_METACLASS_$_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAlignmentOffset
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSCorrectionInfo
+ _OBJC_METACLASS_$_PGSchemaPGGeneratePlanContext
+ _OBJC_METACLASS_$_PGSchemaPGGeneratePlanEnded
+ _OBJC_METACLASS_$_PGSchemaPGGeneratePlanFailed
+ _OBJC_METACLASS_$_PGSchemaPGGeneratePlanStarted
+ _OBJC_METACLASS_$_PGSchemaPGOverridesMatchMetadata
+ _OBJC_METACLASS_$_PNRODSchemaPNRError
+ _OBJC_METACLASS_$_PNRODSchemaPNRODExecutor
+ _OBJC_METACLASS_$_PNRODSchemaPNRODPlanGeneration
+ _OBJC_METACLASS_$_PNRODSchemaPNRODPlanResolution
+ _OBJC_METACLASS_$_PNRODSchemaPNRODQueryDecoration
+ _OBJC_METACLASS_$_PNRODSchemaPNRODResponseGeneration
+ _OBJC_METACLASS_$_PNRODSchemaPNRODSearch
+ _OBJC_METACLASS_$_QDSchemaQDAppPreLaunchTriggered
+ _OBJC_METACLASS_$_QDSchemaQDContextStatementIdsReported
+ _OBJC_METACLASS_$_QDSchemaQDToolboxSizeReported
+ _OBJC_METACLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ _OBJC_METACLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ _OBJC_METACLASS_$_SISchemaUEITranscriptShown
+ _OBJC_METACLASS_$_SISchemaUEITranscriptTapped
+ _OBJC_METACLASS_$_STSchemaSTFailureError
+ _ORCHSchemaORCHAudioTopologyReportedReadFrom
+ _ORCHSchemaORCHIntelligenceFlowRequestContextReadFrom
+ _ORCHSchemaORCHIntelligenceFlowRequestEndedReadFrom
+ _ORCHSchemaORCHIntelligenceFlowRequestFailedReadFrom
+ _ORCHSchemaORCHIntelligenceFlowRequestStartedReadFrom
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_136
+ _OUTLINED_FUNCTION_137
+ _OUTLINED_FUNCTION_138
+ _OUTLINED_FUNCTION_139
+ _OUTLINED_FUNCTION_140
+ _OUTLINED_FUNCTION_141
+ _OUTLINED_FUNCTION_142
+ _OUTLINED_FUNCTION_143
+ _OUTLINED_FUNCTION_144
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_146
+ _OUTLINED_FUNCTION_147
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_149
+ _PEGASUSSchemaPEGASUSAlignmentOffsetReadFrom
+ _PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1ReadFrom
+ _PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1ReadFrom
+ _PEGASUSSchemaPEGASUSAsrCorrectionInfoReadFrom
+ _PEGASUSSchemaPEGASUSAsrHypothesisIdxReadFrom
+ _PEGASUSSchemaPEGASUSAsrHypothesisInfoReadFrom
+ _PEGASUSSchemaPEGASUSCorrectionInfoReadFrom
+ _PGSchemaPGGeneratePlanContextReadFrom
+ _PGSchemaPGGeneratePlanEndedReadFrom
+ _PGSchemaPGGeneratePlanFailedReadFrom
+ _PGSchemaPGGeneratePlanStartedReadFrom
+ _PGSchemaPGOverridesMatchMetadataReadFrom
+ _PNRODSchemaPNRErrorReadFrom
+ _PNRODSchemaPNRODExecutorReadFrom
+ _PNRODSchemaPNRODPlanGenerationReadFrom
+ _PNRODSchemaPNRODPlanResolutionReadFrom
+ _PNRODSchemaPNRODQueryDecorationReadFrom
+ _PNRODSchemaPNRODResponseGenerationReadFrom
+ _PNRODSchemaPNRODSearchReadFrom
+ _QDSchemaQDAppPreLaunchTriggeredReadFrom
+ _QDSchemaQDContextStatementIdsReportedReadFrom
+ _QDSchemaQDToolboxSizeReportedReadFrom
+ _SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttemptsReadFrom
+ _SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummaryReadFrom
+ _SISchemaUEITranscriptShownReadFrom
+ _SISchemaUEITranscriptTappedReadFrom
+ _STSchemaSTFailureErrorReadFrom
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRContextualEntityCollectionTriggered(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRContextualEntityRetrievalContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRContextualEntityRetrievalEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRContextualEntityRetrievalStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRContextualEntityState(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRFullPayloadCorrectionContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRFullPayloadCorrectionEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRFullPayloadCorrectionFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRFullPayloadCorrectionInfoTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRFullPayloadCorrectionStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRLMEOverActivationEdit(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRNamedEntityUserEdit(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASROneBestTranscriptTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASREntityScore(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASREntityScoringResult(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorIdentifierQueryCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorPersonQueryCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorPersonQueryCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorPersonQueryCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorPersonQueryCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorSearchToolQueryCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryLocationCallContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWContact(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWContactTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWDomainExecutionMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTActionConfirmationSystemStyle(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTActionParameterValue(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTCallExpressionParameters(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTFormatExpression(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTPayloadExpression(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTQueryDecorationPrePlannerResult(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTSkipStatement(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTStructuredSearchExpression(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTStructuredSearchExpressionParameters(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTStructuredSearchProperty(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTTypeInstance(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_IFTSchemaIFTValueExpressionArrayVariant(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaHistoricalLocationContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaIntervalUntilStartTime(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJRCandidateBooleanMask(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJRCandidateRiskLevel(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJRCandidateSearchToolRank(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJRCandidateTimeIntervalMatrix(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJREntitySimilarityRow(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJREntitySimilarityScores(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_JRSchemaJRTokenConfidence(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterOverrideMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterPromptComponent(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterPromptGenerated(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLXSchemaCDMUserWantedToUndo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHAudioTopologyReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHIntelligenceFlowRequestContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHIntelligenceFlowRequestEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHIntelligenceFlowRequestFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHIntelligenceFlowRequestStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAlignmentOffset(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAsrCorrectionInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAsrHypothesisIdx(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSAsrHypothesisInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSCorrectionInfo(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PGSchemaPGGeneratePlanContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PGSchemaPGGeneratePlanEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PGSchemaPGGeneratePlanFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PGSchemaPGGeneratePlanStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PGSchemaPGOverridesMatchMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODExecutor(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODPlanGeneration(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODPlanResolution(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODQueryDecoration(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODResponseGeneration(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PNRODSchemaPNRODSearch(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_QDSchemaQDAppPreLaunchTriggered(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_QDSchemaQDContextStatementIdsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_QDSchemaQDToolboxSizeReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEITranscriptShown(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SISchemaUEITranscriptTapped(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_STSchemaSTFailureError(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRContextualEntityCollectionTriggered
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRContextualEntityRetrievalContext
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRContextualEntityRetrievalEnded
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRContextualEntityRetrievalStarted
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRContextualEntityState
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRFullPayloadCorrectionContext
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRFullPayloadCorrectionEnded
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRFullPayloadCorrectionFailed
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRFullPayloadCorrectionStarted
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRLMEOverActivationEdit
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRNamedEntityUserEdit
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASROneBestTranscriptTier1
+ __OBJC_$_INSTANCE_VARIABLES_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASREntityScore
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASREntityScoringResult
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ __OBJC_$_INSTANCE_VARIABLES_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ __OBJC_$_INSTANCE_VARIABLES_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWContact
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWContactTier1
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWDomainExecutionMetadata
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTActionConfirmationSystemStyle
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTActionParameterValue
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTCallExpressionParameters
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTFormatExpression
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTPayloadExpression
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTQueryDecorationPrePlannerResult
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTSkipStatement
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTStructuredSearchExpression
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTStructuredSearchExpressionParameters
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTStructuredSearchProperty
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTTypeInstance
+ __OBJC_$_INSTANCE_VARIABLES_IFTSchemaIFTValueExpressionArrayVariant
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaHistoricalLocationContext
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaIntervalUntilStartTime
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJRCandidateBooleanMask
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJRCandidateRiskLevel
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJRCandidateSearchToolRank
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJRCandidateTimeIntervalMatrix
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJREntitySimilarityRow
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJREntitySimilarityScores
+ __OBJC_$_INSTANCE_VARIABLES_JRSchemaJRTokenConfidence
+ __OBJC_$_INSTANCE_VARIABLES_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ __OBJC_$_INSTANCE_VARIABLES_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterOverrideMetadata
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterPromptComponent
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterPromptGenerated
+ __OBJC_$_INSTANCE_VARIABLES_NLXSchemaCDMUserWantedToUndo
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHAudioTopologyReported
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHIntelligenceFlowRequestContext
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAlignmentOffset
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSCorrectionInfo
+ __OBJC_$_INSTANCE_VARIABLES_PGSchemaPGGeneratePlanContext
+ __OBJC_$_INSTANCE_VARIABLES_PGSchemaPGGeneratePlanEnded
+ __OBJC_$_INSTANCE_VARIABLES_PGSchemaPGGeneratePlanFailed
+ __OBJC_$_INSTANCE_VARIABLES_PGSchemaPGGeneratePlanStarted
+ __OBJC_$_INSTANCE_VARIABLES_PGSchemaPGOverridesMatchMetadata
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRError
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODExecutor
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODPlanGeneration
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODPlanResolution
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODQueryDecoration
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODResponseGeneration
+ __OBJC_$_INSTANCE_VARIABLES_PNRODSchemaPNRODSearch
+ __OBJC_$_INSTANCE_VARIABLES_QDSchemaQDAppPreLaunchTriggered
+ __OBJC_$_INSTANCE_VARIABLES_QDSchemaQDContextStatementIdsReported
+ __OBJC_$_INSTANCE_VARIABLES_QDSchemaQDToolboxSizeReported
+ __OBJC_$_INSTANCE_VARIABLES_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ __OBJC_$_INSTANCE_VARIABLES_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEITranscriptShown
+ __OBJC_$_INSTANCE_VARIABLES_SISchemaUEITranscriptTapped
+ __OBJC_$_INSTANCE_VARIABLES_STSchemaSTFailureError
+ __OBJC_$_PROP_LIST_ASRSchemaASRContextualEntityCollectionTriggered
+ __OBJC_$_PROP_LIST_ASRSchemaASRContextualEntityRetrievalContext
+ __OBJC_$_PROP_LIST_ASRSchemaASRContextualEntityRetrievalEnded
+ __OBJC_$_PROP_LIST_ASRSchemaASRContextualEntityRetrievalStarted
+ __OBJC_$_PROP_LIST_ASRSchemaASRContextualEntityState
+ __OBJC_$_PROP_LIST_ASRSchemaASRFullPayloadCorrectionContext
+ __OBJC_$_PROP_LIST_ASRSchemaASRFullPayloadCorrectionEnded
+ __OBJC_$_PROP_LIST_ASRSchemaASRFullPayloadCorrectionFailed
+ __OBJC_$_PROP_LIST_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ __OBJC_$_PROP_LIST_ASRSchemaASRFullPayloadCorrectionStarted
+ __OBJC_$_PROP_LIST_ASRSchemaASRLMEOverActivationEdit
+ __OBJC_$_PROP_LIST_ASRSchemaASRNamedEntityUserEdit
+ __OBJC_$_PROP_LIST_ASRSchemaASROneBestTranscriptTier1
+ __OBJC_$_PROP_LIST_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASREntityScore
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASREntityScoringResult
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ __OBJC_$_PROP_LIST_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ __OBJC_$_PROP_LIST_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWContact
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWContactTier1
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWDomainExecutionMetadata
+ __OBJC_$_PROP_LIST_IFTSchemaIFTActionConfirmationSystemStyle
+ __OBJC_$_PROP_LIST_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ __OBJC_$_PROP_LIST_IFTSchemaIFTActionParameterValue
+ __OBJC_$_PROP_LIST_IFTSchemaIFTCallExpressionParameters
+ __OBJC_$_PROP_LIST_IFTSchemaIFTFormatExpression
+ __OBJC_$_PROP_LIST_IFTSchemaIFTPayloadExpression
+ __OBJC_$_PROP_LIST_IFTSchemaIFTQueryDecorationPrePlannerResult
+ __OBJC_$_PROP_LIST_IFTSchemaIFTSkipStatement
+ __OBJC_$_PROP_LIST_IFTSchemaIFTStructuredSearchExpression
+ __OBJC_$_PROP_LIST_IFTSchemaIFTStructuredSearchExpressionParameters
+ __OBJC_$_PROP_LIST_IFTSchemaIFTStructuredSearchProperty
+ __OBJC_$_PROP_LIST_IFTSchemaIFTTypeInstance
+ __OBJC_$_PROP_LIST_IFTSchemaIFTValueExpressionArrayVariant
+ __OBJC_$_PROP_LIST_JRSchemaHistoricalLocationContext
+ __OBJC_$_PROP_LIST_JRSchemaIntervalUntilStartTime
+ __OBJC_$_PROP_LIST_JRSchemaJRCandidateBooleanMask
+ __OBJC_$_PROP_LIST_JRSchemaJRCandidateRiskLevel
+ __OBJC_$_PROP_LIST_JRSchemaJRCandidateSearchToolRank
+ __OBJC_$_PROP_LIST_JRSchemaJRCandidateTimeIntervalMatrix
+ __OBJC_$_PROP_LIST_JRSchemaJREntitySimilarityRow
+ __OBJC_$_PROP_LIST_JRSchemaJREntitySimilarityScores
+ __OBJC_$_PROP_LIST_JRSchemaJRTokenConfidence
+ __OBJC_$_PROP_LIST_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ __OBJC_$_PROP_LIST_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterOverrideMetadata
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterPromptComponent
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterPromptGenerated
+ __OBJC_$_PROP_LIST_NLXSchemaCDMUserWantedToUndo
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHAudioTopologyReported
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHIntelligenceFlowRequestContext
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAlignmentOffset
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSCorrectionInfo
+ __OBJC_$_PROP_LIST_PGSchemaPGGeneratePlanContext
+ __OBJC_$_PROP_LIST_PGSchemaPGGeneratePlanEnded
+ __OBJC_$_PROP_LIST_PGSchemaPGGeneratePlanFailed
+ __OBJC_$_PROP_LIST_PGSchemaPGGeneratePlanStarted
+ __OBJC_$_PROP_LIST_PGSchemaPGOverridesMatchMetadata
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRError
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODExecutor
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODPlanGeneration
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODPlanResolution
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODQueryDecoration
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODResponseGeneration
+ __OBJC_$_PROP_LIST_PNRODSchemaPNRODSearch
+ __OBJC_$_PROP_LIST_QDSchemaQDAppPreLaunchTriggered
+ __OBJC_$_PROP_LIST_QDSchemaQDContextStatementIdsReported
+ __OBJC_$_PROP_LIST_QDSchemaQDToolboxSizeReported
+ __OBJC_$_PROP_LIST_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ __OBJC_$_PROP_LIST_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ __OBJC_$_PROP_LIST_SISchemaUEITranscriptShown
+ __OBJC_$_PROP_LIST_SISchemaUEITranscriptTapped
+ __OBJC_$_PROP_LIST_STSchemaSTFailureError
+ __OBJC_CLASS_RO_$_ASRSchemaASRContextualEntityCollectionTriggered
+ __OBJC_CLASS_RO_$_ASRSchemaASRContextualEntityRetrievalContext
+ __OBJC_CLASS_RO_$_ASRSchemaASRContextualEntityRetrievalEnded
+ __OBJC_CLASS_RO_$_ASRSchemaASRContextualEntityRetrievalStarted
+ __OBJC_CLASS_RO_$_ASRSchemaASRContextualEntityState
+ __OBJC_CLASS_RO_$_ASRSchemaASRFullPayloadCorrectionContext
+ __OBJC_CLASS_RO_$_ASRSchemaASRFullPayloadCorrectionEnded
+ __OBJC_CLASS_RO_$_ASRSchemaASRFullPayloadCorrectionFailed
+ __OBJC_CLASS_RO_$_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ __OBJC_CLASS_RO_$_ASRSchemaASRFullPayloadCorrectionStarted
+ __OBJC_CLASS_RO_$_ASRSchemaASRLMEOverActivationEdit
+ __OBJC_CLASS_RO_$_ASRSchemaASRNamedEntityUserEdit
+ __OBJC_CLASS_RO_$_ASRSchemaASROneBestTranscriptTier1
+ __OBJC_CLASS_RO_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASREntityScore
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASREntityScoringResult
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ __OBJC_CLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ __OBJC_CLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWContact
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWContactTier1
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWDomainExecutionMetadata
+ __OBJC_CLASS_RO_$_IFTSchemaIFTActionConfirmationSystemStyle
+ __OBJC_CLASS_RO_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ __OBJC_CLASS_RO_$_IFTSchemaIFTActionParameterValue
+ __OBJC_CLASS_RO_$_IFTSchemaIFTCallExpressionParameters
+ __OBJC_CLASS_RO_$_IFTSchemaIFTFormatExpression
+ __OBJC_CLASS_RO_$_IFTSchemaIFTPayloadExpression
+ __OBJC_CLASS_RO_$_IFTSchemaIFTQueryDecorationPrePlannerResult
+ __OBJC_CLASS_RO_$_IFTSchemaIFTSkipStatement
+ __OBJC_CLASS_RO_$_IFTSchemaIFTStructuredSearchExpression
+ __OBJC_CLASS_RO_$_IFTSchemaIFTStructuredSearchExpressionParameters
+ __OBJC_CLASS_RO_$_IFTSchemaIFTStructuredSearchProperty
+ __OBJC_CLASS_RO_$_IFTSchemaIFTTypeInstance
+ __OBJC_CLASS_RO_$_IFTSchemaIFTValueExpressionArrayVariant
+ __OBJC_CLASS_RO_$_JRSchemaHistoricalLocationContext
+ __OBJC_CLASS_RO_$_JRSchemaIntervalUntilStartTime
+ __OBJC_CLASS_RO_$_JRSchemaJRCandidateBooleanMask
+ __OBJC_CLASS_RO_$_JRSchemaJRCandidateRiskLevel
+ __OBJC_CLASS_RO_$_JRSchemaJRCandidateSearchToolRank
+ __OBJC_CLASS_RO_$_JRSchemaJRCandidateTimeIntervalMatrix
+ __OBJC_CLASS_RO_$_JRSchemaJREntitySimilarityRow
+ __OBJC_CLASS_RO_$_JRSchemaJREntitySimilarityScores
+ __OBJC_CLASS_RO_$_JRSchemaJRTokenConfidence
+ __OBJC_CLASS_RO_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ __OBJC_CLASS_RO_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterOverrideMetadata
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterPromptComponent
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterPromptGenerated
+ __OBJC_CLASS_RO_$_NLXSchemaCDMUserWantedToUndo
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHAudioTopologyReported
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestContext
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAlignmentOffset
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSCorrectionInfo
+ __OBJC_CLASS_RO_$_PGSchemaPGGeneratePlanContext
+ __OBJC_CLASS_RO_$_PGSchemaPGGeneratePlanEnded
+ __OBJC_CLASS_RO_$_PGSchemaPGGeneratePlanFailed
+ __OBJC_CLASS_RO_$_PGSchemaPGGeneratePlanStarted
+ __OBJC_CLASS_RO_$_PGSchemaPGOverridesMatchMetadata
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRError
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODExecutor
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODPlanGeneration
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODPlanResolution
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODQueryDecoration
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODResponseGeneration
+ __OBJC_CLASS_RO_$_PNRODSchemaPNRODSearch
+ __OBJC_CLASS_RO_$_QDSchemaQDAppPreLaunchTriggered
+ __OBJC_CLASS_RO_$_QDSchemaQDContextStatementIdsReported
+ __OBJC_CLASS_RO_$_QDSchemaQDToolboxSizeReported
+ __OBJC_CLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ __OBJC_CLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ __OBJC_CLASS_RO_$_SISchemaUEITranscriptShown
+ __OBJC_CLASS_RO_$_SISchemaUEITranscriptTapped
+ __OBJC_CLASS_RO_$_STSchemaSTFailureError
+ __OBJC_METACLASS_RO_$_ASRSchemaASRContextualEntityCollectionTriggered
+ __OBJC_METACLASS_RO_$_ASRSchemaASRContextualEntityRetrievalContext
+ __OBJC_METACLASS_RO_$_ASRSchemaASRContextualEntityRetrievalEnded
+ __OBJC_METACLASS_RO_$_ASRSchemaASRContextualEntityRetrievalStarted
+ __OBJC_METACLASS_RO_$_ASRSchemaASRContextualEntityState
+ __OBJC_METACLASS_RO_$_ASRSchemaASRFullPayloadCorrectionContext
+ __OBJC_METACLASS_RO_$_ASRSchemaASRFullPayloadCorrectionEnded
+ __OBJC_METACLASS_RO_$_ASRSchemaASRFullPayloadCorrectionFailed
+ __OBJC_METACLASS_RO_$_ASRSchemaASRFullPayloadCorrectionInfoTier1
+ __OBJC_METACLASS_RO_$_ASRSchemaASRFullPayloadCorrectionStarted
+ __OBJC_METACLASS_RO_$_ASRSchemaASRLMEOverActivationEdit
+ __OBJC_METACLASS_RO_$_ASRSchemaASRNamedEntityUserEdit
+ __OBJC_METACLASS_RO_$_ASRSchemaASROneBestTranscriptTier1
+ __OBJC_METACLASS_RO_$_ASRSchemaASRPersonalizationUserEditNamedEntityMetrics
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASREntityScore
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASREntityScoringResult
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1
+ __OBJC_METACLASS_RO_$_DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorIdentifierQueryCallStarted
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorPersonQueryCallStarted
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorSearchToolQueryCallStarted
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityCallStarted
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallContext
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallEnded
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallFailed
+ __OBJC_METACLASS_RO_$_ExecutorSiriSchemaExecutorStringQueryLocationCallStarted
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWContact
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWContactTier1
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWDomainExecutionMetadata
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTActionConfirmationSystemStyle
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTActionParameterValue
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTCallExpressionParameters
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTFormatExpression
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTPayloadExpression
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTQueryDecorationPrePlannerResult
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTSkipStatement
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTStructuredSearchExpression
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTStructuredSearchExpressionParameters
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTStructuredSearchProperty
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTTypeInstance
+ __OBJC_METACLASS_RO_$_IFTSchemaIFTValueExpressionArrayVariant
+ __OBJC_METACLASS_RO_$_JRSchemaHistoricalLocationContext
+ __OBJC_METACLASS_RO_$_JRSchemaIntervalUntilStartTime
+ __OBJC_METACLASS_RO_$_JRSchemaJRCandidateBooleanMask
+ __OBJC_METACLASS_RO_$_JRSchemaJRCandidateRiskLevel
+ __OBJC_METACLASS_RO_$_JRSchemaJRCandidateSearchToolRank
+ __OBJC_METACLASS_RO_$_JRSchemaJRCandidateTimeIntervalMatrix
+ __OBJC_METACLASS_RO_$_JRSchemaJREntitySimilarityRow
+ __OBJC_METACLASS_RO_$_JRSchemaJREntitySimilarityScores
+ __OBJC_METACLASS_RO_$_JRSchemaJRTokenConfidence
+ __OBJC_METACLASS_RO_$_MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried
+ __OBJC_METACLASS_RO_$_MHSchemaMHAdaptiveSiriVolumeUserIntentDetected
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterOverrideMetadata
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterPromptComponent
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterPromptGenerated
+ __OBJC_METACLASS_RO_$_NLXSchemaCDMUserWantedToUndo
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHAudioTopologyReported
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestContext
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestEnded
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestFailed
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHIntelligenceFlowRequestStarted
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAlignmentOffset
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAsrCorrectionInfo
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAsrHypothesisIdx
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSAsrHypothesisInfo
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSCorrectionInfo
+ __OBJC_METACLASS_RO_$_PGSchemaPGGeneratePlanContext
+ __OBJC_METACLASS_RO_$_PGSchemaPGGeneratePlanEnded
+ __OBJC_METACLASS_RO_$_PGSchemaPGGeneratePlanFailed
+ __OBJC_METACLASS_RO_$_PGSchemaPGGeneratePlanStarted
+ __OBJC_METACLASS_RO_$_PGSchemaPGOverridesMatchMetadata
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRError
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODExecutor
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODPlanGeneration
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODPlanResolution
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODQueryDecoration
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODResponseGeneration
+ __OBJC_METACLASS_RO_$_PNRODSchemaPNRODSearch
+ __OBJC_METACLASS_RO_$_QDSchemaQDAppPreLaunchTriggered
+ __OBJC_METACLASS_RO_$_QDSchemaQDContextStatementIdsReported
+ __OBJC_METACLASS_RO_$_QDSchemaQDToolboxSizeReported
+ __OBJC_METACLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ __OBJC_METACLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ __OBJC_METACLASS_RO_$_SISchemaUEITranscriptShown
+ __OBJC_METACLASS_RO_$_SISchemaUEITranscriptTapped
+ __OBJC_METACLASS_RO_$_STSchemaSTFailureError
+ _objc_msgSend$actionClass
+ _objc_msgSend$actionParameterValues
+ _objc_msgSend$adaptiveSiriVolumeTTSVolumeQueried
+ _objc_msgSend$adaptiveSiriVolumeUserIntentDetected
+ _objc_msgSend$addActionParameterValues:
+ _objc_msgSend$addAlternateQuerySuggestionCandidateTier1:
+ _objc_msgSend$addAsrHypothesesInfo:
+ _objc_msgSend$addAsrScores:
+ _objc_msgSend$addBucketedDistance:
+ _objc_msgSend$addCallers:
+ _objc_msgSend$addCandidateBooleanMask:
+ _objc_msgSend$addCandidateRisk:
+ _objc_msgSend$addCandidateTimeIntervalMatrix:
+ _objc_msgSend$addComponents:
+ _objc_msgSend$addContext:
+ _objc_msgSend$addContextStatementIds:
+ _objc_msgSend$addContextualEntityStatementIds:
+ _objc_msgSend$addCorrections:
+ _objc_msgSend$addDroppedComponents:
+ _objc_msgSend$addEnabledTasks:
+ _objc_msgSend$addEntityScoreResults:
+ _objc_msgSend$addEntityScores:
+ _objc_msgSend$addExecutor:
+ _objc_msgSend$addHistoricalLocationContext:
+ _objc_msgSend$addIntervalUntilStartTime:
+ _objc_msgSend$addIsApplicableToCandidate:
+ _objc_msgSend$addJrEntitySimilarityScores:
+ _objc_msgSend$addLmeOverActivationEdits:
+ _objc_msgSend$addLogOfIntervalUntilStartTimeInSeconds:
+ _objc_msgSend$addNamedEntityUserEdits:
+ _objc_msgSend$addOneBestTranscripts:
+ _objc_msgSend$addPageAttempts:
+ _objc_msgSend$addParameterSubType:
+ _objc_msgSend$addPlanGeneration:
+ _objc_msgSend$addPlanResolution:
+ _objc_msgSend$addQueryDecoration:
+ _objc_msgSend$addRejectedContextTypes:
+ _objc_msgSend$addRejectedEntityTypes:
+ _objc_msgSend$addRequestFeatureTag:
+ _objc_msgSend$addResponseGeneration:
+ _objc_msgSend$addRetrievedEntityStates:
+ _objc_msgSend$addRiskLevel:
+ _objc_msgSend$addRow:
+ _objc_msgSend$addSearch:
+ _objc_msgSend$addSearchToolRank:
+ _objc_msgSend$addSearchToolRanks:
+ _objc_msgSend$addSpeechProfileCategories:
+ _objc_msgSend$addStatementId:
+ _objc_msgSend$addVisualContextCategories:
+ _objc_msgSend$addVoiceIdScores:
+ _objc_msgSend$alignmentOffset
+ _objc_msgSend$alternateQuerySuggestionCandidateTier1s
+ _objc_msgSend$alternateQuerySuggestionTier1
+ _objc_msgSend$alternateQuerySuggestionType
+ _objc_msgSend$anonymizedLocationNameId
+ _objc_msgSend$anonymizedLocationTypeId
+ _objc_msgSend$appEntityQueryResponseTime
+ _objc_msgSend$appIntentSessionId
+ _objc_msgSend$appPreLaunchTriggered
+ _objc_msgSend$asrFullPayloadCorrectedToUserEdit
+ _objc_msgSend$asrHypothesesInfos
+ _objc_msgSend$asrOutputToUserEdit
+ _objc_msgSend$asrScores
+ _objc_msgSend$audioFileResult
+ _objc_msgSend$audioQueueLatencyInSecond
+ _objc_msgSend$backgroundNoiseActivityLevel
+ _objc_msgSend$backgroundNoiseLevel
+ _objc_msgSend$bucketedDistance
+ _objc_msgSend$bucketedDistances
+ _objc_msgSend$callParameterName
+ _objc_msgSend$callers
+ _objc_msgSend$candidateA
+ _objc_msgSend$candidateB
+ _objc_msgSend$candidateBooleanMasks
+ _objc_msgSend$candidateRisks
+ _objc_msgSend$candidateTimeIntervalMatrixs
+ _objc_msgSend$clearActionParameterValues
+ _objc_msgSend$clearAlternateQuerySuggestionCandidateTier1
+ _objc_msgSend$clearAsrHypothesesInfo
+ _objc_msgSend$clearAsrScores
+ _objc_msgSend$clearBucketedDistance
+ _objc_msgSend$clearCallers
+ _objc_msgSend$clearCandidateBooleanMask
+ _objc_msgSend$clearCandidateRisk
+ _objc_msgSend$clearCandidateTimeIntervalMatrix
+ _objc_msgSend$clearComponents
+ _objc_msgSend$clearContext
+ _objc_msgSend$clearContextStatementIds
+ _objc_msgSend$clearContextualEntityStatementIds
+ _objc_msgSend$clearCorrections
+ _objc_msgSend$clearDroppedComponents
+ _objc_msgSend$clearEnabledTasks
+ _objc_msgSend$clearEntityScoreResults
+ _objc_msgSend$clearEntityScores
+ _objc_msgSend$clearExecutor
+ _objc_msgSend$clearHistoricalLocationContext
+ _objc_msgSend$clearIntervalUntilStartTime
+ _objc_msgSend$clearIsApplicableToCandidate
+ _objc_msgSend$clearJrEntitySimilarityScores
+ _objc_msgSend$clearLmeOverActivationEdits
+ _objc_msgSend$clearLogOfIntervalUntilStartTimeInSeconds
+ _objc_msgSend$clearNamedEntityUserEdits
+ _objc_msgSend$clearOneBestTranscripts
+ _objc_msgSend$clearPageAttempts
+ _objc_msgSend$clearParameterSubType
+ _objc_msgSend$clearPlanGeneration
+ _objc_msgSend$clearPlanResolution
+ _objc_msgSend$clearQueryDecoration
+ _objc_msgSend$clearRejectedContextTypes
+ _objc_msgSend$clearRejectedEntityTypes
+ _objc_msgSend$clearRequestFeatureTag
+ _objc_msgSend$clearResponseGeneration
+ _objc_msgSend$clearRetrievedEntityStates
+ _objc_msgSend$clearRiskLevel
+ _objc_msgSend$clearRow
+ _objc_msgSend$clearSearch
+ _objc_msgSend$clearSearchToolRank
+ _objc_msgSend$clearSearchToolRanks
+ _objc_msgSend$clearSpeechProfileCategories
+ _objc_msgSend$clearStatementId
+ _objc_msgSend$clearVisualContextCategories
+ _objc_msgSend$clearVoiceIdScores
+ _objc_msgSend$componentType
+ _objc_msgSend$components
+ _objc_msgSend$contact
+ _objc_msgSend$contactName
+ _objc_msgSend$contextStatementIds
+ _objc_msgSend$contextStatementIdsReported
+ _objc_msgSend$contexts
+ _objc_msgSend$contextualEntityCollectionTriggered
+ _objc_msgSend$contextualEntityRetrievalContext
+ _objc_msgSend$contextualEntityStatementIds
+ _objc_msgSend$contextualReplayBiomeRecordCreated
+ _objc_msgSend$contextualReplayBiomeRecordDeleted
+ _objc_msgSend$correction
+ _objc_msgSend$corrections
+ _objc_msgSend$creationTimestampInMsSince1970
+ _objc_msgSend$deleteAdaptiveSiriVolumeTTSVolumeQueried
+ _objc_msgSend$deleteAdaptiveSiriVolumeUserIntentDetected
+ _objc_msgSend$deleteAlignmentOffset
+ _objc_msgSend$deleteAlternateQuerySuggestionCandidateTier1
+ _objc_msgSend$deleteAlternateQuerySuggestionTier1
+ _objc_msgSend$deleteAnonymizedLocationNameId
+ _objc_msgSend$deleteAnonymizedLocationTypeId
+ _objc_msgSend$deleteAppEntityQueryResponseTime
+ _objc_msgSend$deleteAppPreLaunchTriggered
+ _objc_msgSend$deleteArray
+ _objc_msgSend$deleteAsrFullPayloadCorrectedToUserEdit
+ _objc_msgSend$deleteAsrOutputToUserEdit
+ _objc_msgSend$deleteAudioFileResult
+ _objc_msgSend$deleteCandidateA
+ _objc_msgSend$deleteCandidateB
+ _objc_msgSend$deleteContact
+ _objc_msgSend$deleteContactName
+ _objc_msgSend$deleteContextStatementIdsReported
+ _objc_msgSend$deleteContextualEntityCollectionTriggered
+ _objc_msgSend$deleteContextualEntityRetrievalContext
+ _objc_msgSend$deleteContextualReplayBiomeRecordCreated
+ _objc_msgSend$deleteContextualReplayBiomeRecordDeleted
+ _objc_msgSend$deleteCorrection
+ _objc_msgSend$deleteDomainExecutionAppIntentBundleID
+ _objc_msgSend$deleteDomainExecutionMetadata
+ _objc_msgSend$deleteExecutorAppIntentHandleTime
+ _objc_msgSend$deleteExecutorAppIntentQueryHandleTime
+ _objc_msgSend$deleteExecutorIdentifierQueryCallContext
+ _objc_msgSend$deleteExecutorPersonQueryCallContext
+ _objc_msgSend$deleteExecutorSearchToolQueryCallContext
+ _objc_msgSend$deleteExecutorStringQueryEntityCallContext
+ _objc_msgSend$deleteExecutorStringQueryEntityMatcherCallContext
+ _objc_msgSend$deleteExecutorStringQueryLocationCallContext
+ _objc_msgSend$deleteFailedToConvertClientEvent
+ _objc_msgSend$deleteFlowContactTier1
+ _objc_msgSend$deleteFormat
+ _objc_msgSend$deleteFullPayloadCorrectionContext
+ _objc_msgSend$deleteFullPayloadCorrectionExperimentContext
+ _objc_msgSend$deleteFullPayloadCorrectionExperimentPostAnalysis
+ _objc_msgSend$deleteFullPayloadCorrectionExperimentTier1
+ _objc_msgSend$deleteFullPayloadCorrectorInput
+ _objc_msgSend$deleteFullPayloadCorrectorOutput
+ _objc_msgSend$deleteGenerativeAIEnablement
+ _objc_msgSend$deleteGrammar
+ _objc_msgSend$deleteIdentifierQueryTime
+ _objc_msgSend$deleteIdx
+ _objc_msgSend$deleteInfoTier1
+ _objc_msgSend$deleteIntelligenceFlowRequestContext
+ _objc_msgSend$deleteIsNlsResult
+ _objc_msgSend$deleteNlRouterPromptGenerated
+ _objc_msgSend$deleteOriginal
+ _objc_msgSend$deleteOverrideId
+ _objc_msgSend$deleteOverrideMetadata
+ _objc_msgSend$deleteOverridesMatched
+ _objc_msgSend$deletePegasusAsrCorrectionInfo
+ _objc_msgSend$deletePersonQueryTime
+ _objc_msgSend$deletePersonalizationUserEditNamedEntityMetrics
+ _objc_msgSend$deletePgFullPlannerHandleTime
+ _objc_msgSend$deletePgFullPlannerPostInferenceTime
+ _objc_msgSend$deletePgFullPlannerPreInferenceTime
+ _objc_msgSend$deletePgGeneratePlanContext
+ _objc_msgSend$deletePgModelInferenceTime
+ _objc_msgSend$deletePgOverridesTime
+ _objc_msgSend$deletePgPlanGenTotalTime
+ _objc_msgSend$deletePgPrescribedPlanTime
+ _objc_msgSend$deletePlanGenerationTime
+ _objc_msgSend$deletePostItnUtterance
+ _objc_msgSend$deletePostSearchTime
+ _objc_msgSend$deletePrTotalHandleTime
+ _objc_msgSend$deletePreSearchTime
+ _objc_msgSend$deleteQueryDecorationContextRetrievalTime
+ _objc_msgSend$deleteQueryDecorationFetchDynamicEnumerationTime
+ _objc_msgSend$deleteQueryDecorationFullPlannerBlockingTime
+ _objc_msgSend$deleteQueryDecorationHandleTime
+ _objc_msgSend$deleteQueryDecorationID
+ _objc_msgSend$deleteQueryDecorationInputCollectionTime
+ _objc_msgSend$deleteQueryDecorationOutputBuildingTime
+ _objc_msgSend$deleteQueryDecorationPrePlannerResult
+ _objc_msgSend$deleteQueryDecorationRankingTime
+ _objc_msgSend$deleteQueryDecorationSpanRetrievalTime
+ _objc_msgSend$deleteQueryDecorationTime
+ _objc_msgSend$deleteQueryDecorationToolRetrievalContextTime
+ _objc_msgSend$deleteQueryDecorationToolRetrievalTime
+ _objc_msgSend$deleteQueryDecorationTupleBuildingTime
+ _objc_msgSend$deleteQueryDecorationTupleRankingTime
+ _objc_msgSend$deleteResponseGenerationCacheManagerTime
+ _objc_msgSend$deleteResponseGenerationCatalogTime
+ _objc_msgSend$deleteResponseGenerationGMSCallTime
+ _objc_msgSend$deleteResponseGenerationHallucinationDetectionTime
+ _objc_msgSend$deleteResponseGenerationHandleTime
+ _objc_msgSend$deleteResponseGenerationID
+ _objc_msgSend$deleteResponseGenerationInferenceTime
+ _objc_msgSend$deleteResponseGenerationOverrideTime
+ _objc_msgSend$deleteResponseGenerationValidationTime
+ _objc_msgSend$deleteReturnType
+ _objc_msgSend$deleteSearchGlobalSearchTime
+ _objc_msgSend$deleteSearchHallucinationTime
+ _objc_msgSend$deleteSearchStartToGlobalSearchEnd
+ _objc_msgSend$deleteSearchStartToSpotlightEnd
+ _objc_msgSend$deleteSearchToolQueryTime
+ _objc_msgSend$deleteSearchTotalHandleTime
+ _objc_msgSend$deleteSessionSummary
+ _objc_msgSend$deleteSkipStatement
+ _objc_msgSend$deleteStError
+ _objc_msgSend$deleteStringQueryEntityMatcherTime
+ _objc_msgSend$deleteStringQueryEntityTime
+ _objc_msgSend$deleteStringQueryLocationTime
+ _objc_msgSend$deleteStructuredSearch
+ _objc_msgSend$deleteSystemStyle
+ _objc_msgSend$deleteToolboxSizeReported
+ _objc_msgSend$deleteTranscriptShown
+ _objc_msgSend$deleteTranscriptTapped
+ _objc_msgSend$deleteTtaie
+ _objc_msgSend$deleteWantedToUndo
+ _objc_msgSend$didTriggerFirstPass
+ _objc_msgSend$domainExecutionAppIntentBundleID
+ _objc_msgSend$domainExecutionMetadata
+ _objc_msgSend$droppedComponents
+ _objc_msgSend$enabledTasks
+ _objc_msgSend$endCharacterIdx
+ _objc_msgSend$enrollmentResult
+ _objc_msgSend$entityScoreResults
+ _objc_msgSend$entityScores
+ _objc_msgSend$entityTaggerCategory
+ _objc_msgSend$errorDomainString
+ _objc_msgSend$estimatedSizeInTokens
+ _objc_msgSend$eventOrigin
+ _objc_msgSend$executorAppIntentHandleTime
+ _objc_msgSend$executorAppIntentQueryHandleTime
+ _objc_msgSend$executorIdentifierQueryCallContext
+ _objc_msgSend$executorPersonQueryCallContext
+ _objc_msgSend$executorSearchToolQueryCallContext
+ _objc_msgSend$executorSearchToolQueryType
+ _objc_msgSend$executorStringQueryEntityCallContext
+ _objc_msgSend$executorStringQueryEntityMatcherCallContext
+ _objc_msgSend$executorStringQueryLocationCallContext
+ _objc_msgSend$executors
+ _objc_msgSend$expensiveCellularDownloadRequested
+ _objc_msgSend$failedToConvertClientEvent
+ _objc_msgSend$flowContactTier1
+ _objc_msgSend$format
+ _objc_msgSend$fromPreSoftwareUpdateStaging
+ _objc_msgSend$fullPayloadCorrectionContext
+ _objc_msgSend$fullPayloadCorrectionExperimentContext
+ _objc_msgSend$fullPayloadCorrectionExperimentPostAnalysis
+ _objc_msgSend$fullPayloadCorrectionExperimentTier1
+ _objc_msgSend$fullPayloadCorrectorInput
+ _objc_msgSend$fullPayloadCorrectorOutput
+ _objc_msgSend$generativeAIEnablement
+ _objc_msgSend$grammar
+ _objc_msgSend$historicalLocationContexts
+ _objc_msgSend$identifierQueryTime
+ _objc_msgSend$idx
+ _objc_msgSend$infoTier1
+ _objc_msgSend$intelligenceFlowRequestContext
+ _objc_msgSend$intervalUntilStartTimes
+ _objc_msgSend$isApplicableToCandidates
+ _objc_msgSend$isCrossDevice
+ _objc_msgSend$isDefaultApp
+ _objc_msgSend$isExpanded
+ _objc_msgSend$isLongLivedIDUploadDisabled
+ _objc_msgSend$isMailAppFocused
+ _objc_msgSend$isMediaPlaybackOn
+ _objc_msgSend$isNamedEntityPresentInSpeechProfile
+ _objc_msgSend$isNamedEntityPresentInVisualContext
+ _objc_msgSend$isPreLaunchExecuted
+ _objc_msgSend$isPredictionCorrect
+ _objc_msgSend$isRelationship
+ _objc_msgSend$isRequestByHandleType
+ _objc_msgSend$isRequestByLabel
+ _objc_msgSend$isRoot
+ _objc_msgSend$isSiriXFallback
+ _objc_msgSend$isUnnamedPhoneNumber
+ _objc_msgSend$jrEntitySimilarityScores
+ _objc_msgSend$lastCompletedPage
+ _objc_msgSend$lastOpenedPageNumber
+ _objc_msgSend$lmeOverActivationEdits
+ _objc_msgSend$logOfIntervalUntilStartTimeInSeconds
+ _objc_msgSend$logOfTimeElapsedInSeconds
+ _objc_msgSend$loggableUserIdHash
+ _objc_msgSend$loudnessLevel
+ _objc_msgSend$maxEnrolled
+ _objc_msgSend$maxEntityChars
+ _objc_msgSend$maxEntityWords
+ _objc_msgSend$musicLoudnessLevel
+ _objc_msgSend$namedEntityUserEdits
+ _objc_msgSend$nlRouterPromptGenerated
+ _objc_msgSend$numAttempts
+ _objc_msgSend$numEntityErrors
+ _objc_msgSend$numTotalEdit
+ _objc_msgSend$numTotalEntities
+ _objc_msgSend$oneBestTranscriptLinkIndex
+ _objc_msgSend$oneBestTranscripts
+ _objc_msgSend$original
+ _objc_msgSend$originalAsrInterpretationIdx
+ _objc_msgSend$overrideMetadata
+ _objc_msgSend$overridesMatched
+ _objc_msgSend$pageAttempts
+ _objc_msgSend$parameterSubTypes
+ _objc_msgSend$payloadType
+ _objc_msgSend$pegasusAsrCorrectionInfo
+ _objc_msgSend$personQueryTime
+ _objc_msgSend$personalizationUserEditNamedEntityMetrics
+ _objc_msgSend$pgFullPlannerHandleTime
+ _objc_msgSend$pgFullPlannerPostInferenceTime
+ _objc_msgSend$pgFullPlannerPreInferenceTime
+ _objc_msgSend$pgGeneratePlanContext
+ _objc_msgSend$pgModelIdentifier
+ _objc_msgSend$pgModelInferenceTime
+ _objc_msgSend$pgModelInterface
+ _objc_msgSend$pgOverridesAssetVersion
+ _objc_msgSend$pgOverridesMatched
+ _objc_msgSend$pgOverridesTime
+ _objc_msgSend$pgPlanGenTotalTime
+ _objc_msgSend$pgPrescribedPlanTime
+ _objc_msgSend$planGenerationTime
+ _objc_msgSend$planGenerations
+ _objc_msgSend$planResolutions
+ _objc_msgSend$postItn1Best
+ _objc_msgSend$postItnUtterance
+ _objc_msgSend$postSearchTime
+ _objc_msgSend$prTotalHandleTime
+ _objc_msgSend$preSearchTime
+ _objc_msgSend$primitiveType
+ _objc_msgSend$queryDecorationContextRetrievalTime
+ _objc_msgSend$queryDecorationFetchDynamicEnumerationTime
+ _objc_msgSend$queryDecorationFullPlannerBlockingTime
+ _objc_msgSend$queryDecorationHandleTime
+ _objc_msgSend$queryDecorationID
+ _objc_msgSend$queryDecorationInputCollectionTime
+ _objc_msgSend$queryDecorationOutputBuildingTime
+ _objc_msgSend$queryDecorationPrePlannerResult
+ _objc_msgSend$queryDecorationRankingTime
+ _objc_msgSend$queryDecorationSource
+ _objc_msgSend$queryDecorationSpanRetrievalTime
+ _objc_msgSend$queryDecorationTime
+ _objc_msgSend$queryDecorationToolRetrievalContextTime
+ _objc_msgSend$queryDecorationToolRetrievalTime
+ _objc_msgSend$queryDecorationTupleBuildingTime
+ _objc_msgSend$queryDecorationTupleRankingTime
+ _objc_msgSend$queryDecorations
+ _objc_msgSend$rejectReason
+ _objc_msgSend$rejectedContextTypes
+ _objc_msgSend$rejectedEntityTypes
+ _objc_msgSend$requestFeatureTags
+ _objc_msgSend$requestTask
+ _objc_msgSend$responseGenerationCacheManagerTime
+ _objc_msgSend$responseGenerationCatalogTime
+ _objc_msgSend$responseGenerationGMSCallTime
+ _objc_msgSend$responseGenerationHallucinationDetectionTime
+ _objc_msgSend$responseGenerationHandleTime
+ _objc_msgSend$responseGenerationID
+ _objc_msgSend$responseGenerationInferenceTime
+ _objc_msgSend$responseGenerationOverrideTime
+ _objc_msgSend$responseGenerationType
+ _objc_msgSend$responseGenerationValidationTime
+ _objc_msgSend$responseGenerations
+ _objc_msgSend$responseTimeInNs
+ _objc_msgSend$retrievalTimeout
+ _objc_msgSend$retrievedEntityStates
+ _objc_msgSend$returnType
+ _objc_msgSend$riskLevels
+ _objc_msgSend$rows
+ _objc_msgSend$searchGlobalSearchTime
+ _objc_msgSend$searchHallucinationTime
+ _objc_msgSend$searchStartToGlobalSearchEnd
+ _objc_msgSend$searchStartToSpotlightEnd
+ _objc_msgSend$searchToolQueryTime
+ _objc_msgSend$searchToolRanks
+ _objc_msgSend$searchTotalHandleTime
+ _objc_msgSend$searchs
+ _objc_msgSend$selectedAsAlternateSuggestion
+ _objc_msgSend$selectedAsPrimaryResponse
+ _objc_msgSend$selectedloggableUserIdHash
+ _objc_msgSend$sessionSummary
+ _objc_msgSend$setActionClass:
+ _objc_msgSend$setActionParameterValues:
+ _objc_msgSend$setAdaptiveSiriVolumeTTSVolumeQueried:
+ _objc_msgSend$setAdaptiveSiriVolumeUserIntentDetected:
+ _objc_msgSend$setAlignmentOffset:
+ _objc_msgSend$setAlternateQuerySuggestionCandidateTier1s:
+ _objc_msgSend$setAlternateQuerySuggestionTier1:
+ _objc_msgSend$setAlternateQuerySuggestionType:
+ _objc_msgSend$setAnonymizedLocationNameId:
+ _objc_msgSend$setAnonymizedLocationTypeId:
+ _objc_msgSend$setAppEntityQueryResponseTime:
+ _objc_msgSend$setAppIntentSessionId:
+ _objc_msgSend$setAppPreLaunchTriggered:
+ _objc_msgSend$setArray:
+ _objc_msgSend$setAsrFullPayloadCorrectedToUserEdit:
+ _objc_msgSend$setAsrHypothesesInfos:
+ _objc_msgSend$setAsrOutputToUserEdit:
+ _objc_msgSend$setAudioFileResult:
+ _objc_msgSend$setAudioQueueLatencyInSecond:
+ _objc_msgSend$setBackgroundNoiseActivityLevel:
+ _objc_msgSend$setBackgroundNoiseLevel:
+ _objc_msgSend$setBucketedDistance:
+ _objc_msgSend$setCallParameterName:
+ _objc_msgSend$setCandidateA:
+ _objc_msgSend$setCandidateB:
+ _objc_msgSend$setCandidateBooleanMasks:
+ _objc_msgSend$setCandidateRisks:
+ _objc_msgSend$setCandidateTimeIntervalMatrixs:
+ _objc_msgSend$setComponentType:
+ _objc_msgSend$setComponents:
+ _objc_msgSend$setContact:
+ _objc_msgSend$setContactName:
+ _objc_msgSend$setContextStatementIds:
+ _objc_msgSend$setContextStatementIdsReported:
+ _objc_msgSend$setContexts:
+ _objc_msgSend$setContextualEntityCollectionTriggered:
+ _objc_msgSend$setContextualEntityRetrievalContext:
+ _objc_msgSend$setContextualReplayBiomeRecordCreated:
+ _objc_msgSend$setContextualReplayBiomeRecordDeleted:
+ _objc_msgSend$setCorrection:
+ _objc_msgSend$setCorrections:
+ _objc_msgSend$setCreationTimestampInMsSince1970:
+ _objc_msgSend$setDidTriggerFirstPass:
+ _objc_msgSend$setDomainExecutionAppIntentBundleID:
+ _objc_msgSend$setDomainExecutionMetadata:
+ _objc_msgSend$setDroppedComponents:
+ _objc_msgSend$setEndCharacterIdx:
+ _objc_msgSend$setEnrollmentResult:
+ _objc_msgSend$setEntityScoreResults:
+ _objc_msgSend$setEntityScores:
+ _objc_msgSend$setEntityTaggerCategory:
+ _objc_msgSend$setErrorDomainString:
+ _objc_msgSend$setEstimatedSizeInTokens:
+ _objc_msgSend$setEventOrigin:
+ _objc_msgSend$setExecutorAppIntentHandleTime:
+ _objc_msgSend$setExecutorAppIntentQueryHandleTime:
+ _objc_msgSend$setExecutorIdentifierQueryCallContext:
+ _objc_msgSend$setExecutorPersonQueryCallContext:
+ _objc_msgSend$setExecutorSearchToolQueryCallContext:
+ _objc_msgSend$setExecutorSearchToolQueryType:
+ _objc_msgSend$setExecutorStringQueryEntityCallContext:
+ _objc_msgSend$setExecutorStringQueryEntityMatcherCallContext:
+ _objc_msgSend$setExecutorStringQueryLocationCallContext:
+ _objc_msgSend$setExecutors:
+ _objc_msgSend$setExpensiveCellularDownloadRequested:
+ _objc_msgSend$setFailedToConvertClientEvent:
+ _objc_msgSend$setFlowContactTier1:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setFromPreSoftwareUpdateStaging:
+ _objc_msgSend$setFullPayloadCorrectionContext:
+ _objc_msgSend$setFullPayloadCorrectionExperimentContext:
+ _objc_msgSend$setFullPayloadCorrectionExperimentPostAnalysis:
+ _objc_msgSend$setFullPayloadCorrectionExperimentTier1:
+ _objc_msgSend$setFullPayloadCorrectorInput:
+ _objc_msgSend$setFullPayloadCorrectorOutput:
+ _objc_msgSend$setGenerativeAIEnablement:
+ _objc_msgSend$setGrammar:
+ _objc_msgSend$setHistoricalLocationContexts:
+ _objc_msgSend$setIdentifierQueryTime:
+ _objc_msgSend$setIdx:
+ _objc_msgSend$setInfoTier1:
+ _objc_msgSend$setIntelligenceFlowRequestContext:
+ _objc_msgSend$setIntervalUntilStartTimes:
+ _objc_msgSend$setIsCrossDevice:
+ _objc_msgSend$setIsDefaultApp:
+ _objc_msgSend$setIsExpanded:
+ _objc_msgSend$setIsLongLivedIDUploadDisabled:
+ _objc_msgSend$setIsMailAppFocused:
+ _objc_msgSend$setIsMediaPlaybackOn:
+ _objc_msgSend$setIsNamedEntityPresentInSpeechProfile:
+ _objc_msgSend$setIsNamedEntityPresentInVisualContext:
+ _objc_msgSend$setIsPreLaunchExecuted:
+ _objc_msgSend$setIsPredictionCorrect:
+ _objc_msgSend$setIsRelationship:
+ _objc_msgSend$setIsRequestByHandleType:
+ _objc_msgSend$setIsRequestByLabel:
+ _objc_msgSend$setIsRoot:
+ _objc_msgSend$setIsSiriXFallback:
+ _objc_msgSend$setIsUnnamedPhoneNumber:
+ _objc_msgSend$setJrEntitySimilarityScores:
+ _objc_msgSend$setLastCompletedPage:
+ _objc_msgSend$setLastOpenedPageNumber:
+ _objc_msgSend$setLmeOverActivationEdits:
+ _objc_msgSend$setLogOfTimeElapsedInSeconds:
+ _objc_msgSend$setLoggableUserIdHash:
+ _objc_msgSend$setLoudnessLevel:
+ _objc_msgSend$setMaxEnrolled:
+ _objc_msgSend$setMaxEntityChars:
+ _objc_msgSend$setMaxEntityWords:
+ _objc_msgSend$setMusicLoudnessLevel:
+ _objc_msgSend$setNamedEntityUserEdits:
+ _objc_msgSend$setNlRouterPromptGenerated:
+ _objc_msgSend$setNumAttempts:
+ _objc_msgSend$setNumEntityErrors:
+ _objc_msgSend$setNumTotalEdit:
+ _objc_msgSend$setNumTotalEntities:
+ _objc_msgSend$setOneBestTranscriptLinkIndex:
+ _objc_msgSend$setOneBestTranscripts:
+ _objc_msgSend$setOriginal:
+ _objc_msgSend$setOriginalAsrInterpretationIdx:
+ _objc_msgSend$setOverrideMetadata:
+ _objc_msgSend$setOverridesMatched:
+ _objc_msgSend$setPageAttempts:
+ _objc_msgSend$setPayloadType:
+ _objc_msgSend$setPegasusAsrCorrectionInfo:
+ _objc_msgSend$setPersonQueryTime:
+ _objc_msgSend$setPersonalizationUserEditNamedEntityMetrics:
+ _objc_msgSend$setPgFullPlannerHandleTime:
+ _objc_msgSend$setPgFullPlannerPostInferenceTime:
+ _objc_msgSend$setPgFullPlannerPreInferenceTime:
+ _objc_msgSend$setPgGeneratePlanContext:
+ _objc_msgSend$setPgModelIdentifier:
+ _objc_msgSend$setPgModelInferenceTime:
+ _objc_msgSend$setPgModelInterface:
+ _objc_msgSend$setPgOverridesAssetVersion:
+ _objc_msgSend$setPgOverridesMatched:
+ _objc_msgSend$setPgOverridesTime:
+ _objc_msgSend$setPgPlanGenTotalTime:
+ _objc_msgSend$setPgPrescribedPlanTime:
+ _objc_msgSend$setPlanGenerationTime:
+ _objc_msgSend$setPlanGenerations:
+ _objc_msgSend$setPlanResolutions:
+ _objc_msgSend$setPostItn1Best:
+ _objc_msgSend$setPostItnUtterance:
+ _objc_msgSend$setPostSearchTime:
+ _objc_msgSend$setPrTotalHandleTime:
+ _objc_msgSend$setPreSearchTime:
+ _objc_msgSend$setPrimitiveType:
+ _objc_msgSend$setQueryDecorationContextRetrievalTime:
+ _objc_msgSend$setQueryDecorationFetchDynamicEnumerationTime:
+ _objc_msgSend$setQueryDecorationFullPlannerBlockingTime:
+ _objc_msgSend$setQueryDecorationHandleTime:
+ _objc_msgSend$setQueryDecorationID:
+ _objc_msgSend$setQueryDecorationInputCollectionTime:
+ _objc_msgSend$setQueryDecorationOutputBuildingTime:
+ _objc_msgSend$setQueryDecorationPrePlannerResult:
+ _objc_msgSend$setQueryDecorationRankingTime:
+ _objc_msgSend$setQueryDecorationSource:
+ _objc_msgSend$setQueryDecorationSpanRetrievalTime:
+ _objc_msgSend$setQueryDecorationTime:
+ _objc_msgSend$setQueryDecorationToolRetrievalContextTime:
+ _objc_msgSend$setQueryDecorationToolRetrievalTime:
+ _objc_msgSend$setQueryDecorationTupleBuildingTime:
+ _objc_msgSend$setQueryDecorationTupleRankingTime:
+ _objc_msgSend$setQueryDecorations:
+ _objc_msgSend$setRejectReason:
+ _objc_msgSend$setRejectedEntityTypes:
+ _objc_msgSend$setRequestTask:
+ _objc_msgSend$setResponseGenerationCacheManagerTime:
+ _objc_msgSend$setResponseGenerationCatalogTime:
+ _objc_msgSend$setResponseGenerationGMSCallTime:
+ _objc_msgSend$setResponseGenerationHallucinationDetectionTime:
+ _objc_msgSend$setResponseGenerationHandleTime:
+ _objc_msgSend$setResponseGenerationID:
+ _objc_msgSend$setResponseGenerationInferenceTime:
+ _objc_msgSend$setResponseGenerationOverrideTime:
+ _objc_msgSend$setResponseGenerationType:
+ _objc_msgSend$setResponseGenerationValidationTime:
+ _objc_msgSend$setResponseGenerations:
+ _objc_msgSend$setResponseTimeInNs:
+ _objc_msgSend$setRetrievalTimeout:
+ _objc_msgSend$setRetrievedEntityStates:
+ _objc_msgSend$setReturnType:
+ _objc_msgSend$setRows:
+ _objc_msgSend$setScores:
+ _objc_msgSend$setSearchGlobalSearchTime:
+ _objc_msgSend$setSearchHallucinationTime:
+ _objc_msgSend$setSearchStartToGlobalSearchEnd:
+ _objc_msgSend$setSearchStartToSpotlightEnd:
+ _objc_msgSend$setSearchToolQueryTime:
+ _objc_msgSend$setSearchToolRanks:
+ _objc_msgSend$setSearchTotalHandleTime:
+ _objc_msgSend$setSearchs:
+ _objc_msgSend$setSelectedAsAlternateSuggestion:
+ _objc_msgSend$setSelectedAsPrimaryResponse:
+ _objc_msgSend$setSelectedloggableUserIdHash:
+ _objc_msgSend$setSessionSummary:
+ _objc_msgSend$setShimAction:
+ _objc_msgSend$setShouldOpen:
+ _objc_msgSend$setSignalToNoiseRatio:
+ _objc_msgSend$setSizeInTokens:
+ _objc_msgSend$setSkipStatement:
+ _objc_msgSend$setSourceAuxIdx:
+ _objc_msgSend$setSourceAuxKey:
+ _objc_msgSend$setSpeakerDistance:
+ _objc_msgSend$setSpeakerSpeechLevel:
+ _objc_msgSend$setSpeechProfileCategory:
+ _objc_msgSend$setSpeechStartPointDetected:
+ _objc_msgSend$setStError:
+ _objc_msgSend$setStartCharacterIdx:
+ _objc_msgSend$setStringQueryEntityMatcherTime:
+ _objc_msgSend$setStringQueryEntityTime:
+ _objc_msgSend$setStringQueryLocationTime:
+ _objc_msgSend$setStructuredSearch:
+ _objc_msgSend$setStructuredSearchParameterName:
+ _objc_msgSend$setSystemStyle:
+ _objc_msgSend$setToolboxSizeReported:
+ _objc_msgSend$setTotalSizeInTokens:
+ _objc_msgSend$setTotalToolCount:
+ _objc_msgSend$setTranscriptShown:
+ _objc_msgSend$setTranscriptShownReason:
+ _objc_msgSend$setTranscriptTapped:
+ _objc_msgSend$setTrueCorrections:
+ _objc_msgSend$setTrueRegressions:
+ _objc_msgSend$setTtaie:
+ _objc_msgSend$setTtsVolume:
+ _objc_msgSend$setTwoPassRecognizerUsed:
+ _objc_msgSend$setUnableToCancel:
+ _objc_msgSend$setUserIntentType:
+ _objc_msgSend$setUserIntentVolume:
+ _objc_msgSend$setVoiceIdClassification:
+ _objc_msgSend$setVoiceIdScores:
+ _objc_msgSend$setWantedToUndo:
+ _objc_msgSend$shimAction
+ _objc_msgSend$shouldOpen
+ _objc_msgSend$signalToNoiseRatio
+ _objc_msgSend$sizeInTokens
+ _objc_msgSend$skipStatement
+ _objc_msgSend$sourceAuxIdx
+ _objc_msgSend$sourceAuxKey
+ _objc_msgSend$speakerDistance
+ _objc_msgSend$speakerSpeechLevel
+ _objc_msgSend$speechProfileCategories
+ _objc_msgSend$speechProfileCategory
+ _objc_msgSend$speechStartPointDetected
+ _objc_msgSend$stError
+ _objc_msgSend$startCharacterIdx
+ _objc_msgSend$stringQueryEntityMatcherTime
+ _objc_msgSend$stringQueryEntityTime
+ _objc_msgSend$stringQueryLocationTime
+ _objc_msgSend$structuredSearch
+ _objc_msgSend$structuredSearchParameterName
+ _objc_msgSend$systemStyle
+ _objc_msgSend$toolboxSizeReported
+ _objc_msgSend$totalSizeInTokens
+ _objc_msgSend$totalToolCount
+ _objc_msgSend$transcriptShown
+ _objc_msgSend$transcriptShownReason
+ _objc_msgSend$transcriptTapped
+ _objc_msgSend$trueCorrections
+ _objc_msgSend$trueRegressions
+ _objc_msgSend$ttaie
+ _objc_msgSend$ttsVolume
+ _objc_msgSend$twoPassRecognizerUsed
+ _objc_msgSend$unableToCancel
+ _objc_msgSend$userIntentType
+ _objc_msgSend$userIntentVolume
+ _objc_msgSend$visualContextCategories
+ _objc_msgSend$voiceIdClassification
+ _objc_msgSend$voiceIdScores
+ _objc_msgSend$wantedToUndo
+ _objc_msgSend$whichItemtype
+ _objc_msgSend$whichOneof_Actionconfirmationsystemstyle
+ _qname_ASRSchemaASRClientEvent_WhichEvent_Type_contextualEntityCollectionTriggered
+ _qname_ASRSchemaASRClientEvent_WhichEvent_Type_contextualEntityRetrievalContext
+ _qname_ASRSchemaASRClientEvent_WhichEvent_Type_personalizationUserEditNamedEntityMetrics
+ _qname_DODMLSchemaDODMLClientEvent_WhichEvent_Type_contextualReplayBiomeRecordCreated
+ _qname_DODMLSchemaDODMLClientEvent_WhichEvent_Type_contextualReplayBiomeRecordDeleted
+ _qname_DODMLSchemaDODMLClientEvent_WhichEvent_Type_fullPayloadCorrectionExperimentContext
+ _qname_DODMLSchemaDODMLClientEvent_WhichEvent_Type_fullPayloadCorrectionExperimentPostAnalysis
+ _qname_DODMLSchemaDODMLClientEvent_WhichEvent_Type_fullPayloadCorrectionExperimentTier1
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorIdentifierQueryCallContext
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorPersonQueryCallContext
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorSearchToolQueryCallContext
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorStringQueryEntityCallContext
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorStringQueryEntityMatcherCallContext
+ _qname_ExecutorSiriSchemaExecutorClientEvent_WhichEvent_Type_executorStringQueryLocationCallContext
+ _qname_FLOWSchemaFLOWClientEvent_WhichEvent_Type_flowContactTier1
+ _qname_IFTSchemaIFTClientEvent_WhichEvent_Type_queryDecorationPrePlannerResult
+ _qname_IFTSchemaIFTClientEvent_WhichEvent_Type_skipStatement
+ _qname_MHSchemaMHClientEvent_WhichEvent_Type_adaptiveSiriVolumeTTSVolumeQueried
+ _qname_MHSchemaMHClientEvent_WhichEvent_Type_adaptiveSiriVolumeUserIntentDetected
+ _qname_NLRouterSchemaNLRouterClientEvent_WhichEvent_Type_nlRouterPromptGenerated
+ _qname_ORCHSchemaORCHClientEvent_WhichEvent_Type_audioTopologyReported
+ _qname_ORCHSchemaORCHClientEvent_WhichEvent_Type_intelligenceFlowRequestContext
+ _qname_PEGASUSSchemaPEGASUSServerEvent_WhichEvent_Type_pegasusAsrCorrectionInfo
+ _qname_PGSchemaPGClientEvent_WhichEvent_Type_pgGeneratePlanContext
+ _qname_QDSchemaQDClientEvent_WhichEvent_Type_appPreLaunchTriggered
+ _qname_QDSchemaQDClientEvent_WhichEvent_Type_contextStatementIdsReported
+ _qname_QDSchemaQDClientEvent_WhichEvent_Type_toolboxSizeReported
+ _qname_SIRISETUPSchemaSIRISETUPClientEvent_WhichEvent_Type_sessionSummary
+ _qname_SISchemaClientEvent_WhichEvent_Type_transcriptShown
+ _qname_SISchemaClientEvent_WhichEvent_Type_transcriptTapped
+ _swift_bridgeObjectRetain_n
+ _symbolic _____ So014NLRouterSchemaA19PromptComponentTypeV
+ _symbolic _____ So018ExecutorSiriSchemaA19SearchToolQueryTypeV
+ _symbolic _____ So16QDSchemaQDCallerV
+ _symbolic _____ So20ASRSchemaASRTaskHintV
+ _symbolic _____ So23IFTSchemaIFTActionClassV
+ _symbolic _____ So24ORCHSchemaORCHShimActionV
+ _symbolic _____ So25IFTSchemaIFTPrimitiveTypeV
+ _symbolic _____ So26JRSchemaJRBucketedDistanceV
+ _symbolic _____ So26JRSchemaJRParameterSubTypeV
+ _symbolic _____ So27MHSchemaMHASVInvocationTypeV
+ _symbolic _____ So27MHSchemaMHASVUserIntentTypeV
+ _symbolic _____ So27ODDSiriSchemaODDEventOriginV
+ _symbolic _____ So28IFTSchemaIFTQueryPayloadTypeV
+ _symbolic _____ So29SISchemaTranscriptShownReasonV
+ _symbolic _____ So32ASRSchemaASREntityTaggerCategoryV
+ _symbolic _____ So32MHSchemaMHASVSpeakerDistanceTypeV
+ _symbolic _____ So32PNRODSchemaPNRODPGModelInterfaceV
+ _symbolic _____ So32PNRODSchemaPNRODRGResponseSourceV
+ _symbolic _____ So33ASRSchemaASRSpeechProfileCategoryV
+ _symbolic _____ So33ASRSchemaASRVisualContextCategoryV
+ _symbolic _____ So33PNRODSchemaPNRODRequestFeatureTagV
+ _symbolic _____ So34ASRSchemaASREntityEnrollmentReasonV
+ _symbolic _____ So34ASRSchemaASREntityEnrollmentResultV
+ _symbolic _____ So34ORCHSchemaORCHDevicesAudioTopologyV
+ _symbolic _____ So37IFTSchemaIFTParameterNotAllowedReasonV
+ _symbolic _____ So37PNRODSchemaPNRODQueryDecorationSourceV
+ _symbolic _____ So41MHSchemaMHASVBackgroundNoiseActivityLevelV
+ _symbolic _____ So42ASRSchemaASRFullPayloadCorrectionErrorTypeV
+ _symbolic _____ So43ORCHSchemaORCHIntelligenceFlowFailureReasonV
+ _symbolic _____ So57PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTypeV
+ _symbolic _____ So69IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablementSourceV
- -[MHSchemaMHClientEvent deleteSensorControlStatusReported]
- -[MHSchemaMHClientEvent hasSensorControlStatusReported]
- -[MHSchemaMHClientEvent sensorControlStatusReported]
- -[MHSchemaMHClientEvent setHasSensorControlStatusReported:]
- -[MHSchemaMHClientEvent setSensorControlStatusReported:]
- -[MHSchemaMHSensorControlStatusReported deleteSensorControlStatus]
- -[MHSchemaMHSensorControlStatusReported dictionaryRepresentation]
- -[MHSchemaMHSensorControlStatusReported hasSensorControlStatus]
- -[MHSchemaMHSensorControlStatusReported hash]
- -[MHSchemaMHSensorControlStatusReported initWithDictionary:]
- -[MHSchemaMHSensorControlStatusReported initWithJSON:]
- -[MHSchemaMHSensorControlStatusReported isEqual:]
- -[MHSchemaMHSensorControlStatusReported jsonData]
- -[MHSchemaMHSensorControlStatusReported readFrom:]
- -[MHSchemaMHSensorControlStatusReported sensorControlStatus]
- -[MHSchemaMHSensorControlStatusReported setHasSensorControlStatus:]
- -[MHSchemaMHSensorControlStatusReported setSensorControlStatus:]
- -[MHSchemaMHSensorControlStatusReported writeTo:]
- -[MHSchemaMHSensorControlStatusReported(SensitiveConditions) suppressMessageUnderConditions]
- OBJC_IVAR_$_MHSchemaMHClientEvent._hasSensorControlStatusReported
- OBJC_IVAR_$_MHSchemaMHClientEvent._sensorControlStatusReported
- OBJC_IVAR_$_MHSchemaMHSensorControlStatusReported._has
- OBJC_IVAR_$_MHSchemaMHSensorControlStatusReported._sensorControlStatus
- _MHSchemaMHSensorControlStatusReportedReadFrom
- _OBJC_CLASS_$_MHSchemaMHSensorControlStatusReported
- _OBJC_METACLASS_$_MHSchemaMHSensorControlStatusReported
- __OBJC_$_INSTANCE_METHODS_MHSchemaMHSensorControlStatusReported(SensitiveConditions)
- __OBJC_$_INSTANCE_VARIABLES_MHSchemaMHSensorControlStatusReported
- __OBJC_$_PROP_LIST_MHSchemaMHSensorControlStatusReported
- __OBJC_CLASS_RO_$_MHSchemaMHSensorControlStatusReported
- __OBJC_METACLASS_RO_$_MHSchemaMHSensorControlStatusReported
- _fmod
- _objc_msgSend$deleteSensorControlStatusReported
- _objc_msgSend$sensorControlStatus
- _objc_msgSend$sensorControlStatusReported
- _objc_msgSend$setSensorControlStatus:
- _objc_msgSend$setSensorControlStatusReported:
- _qname_MHSchemaMHClientEvent_WhichEvent_Type_sensorControlStatusReported
- _symbolic _____ So29MHSchemaMHSensorControlStatusV
CStrings:
+ "@\"ASRSchemaASRContextualEntityCollectionTriggered\""
+ "@\"ASRSchemaASRContextualEntityRetrievalContext\""
+ "@\"ASRSchemaASRContextualEntityRetrievalEnded\""
+ "@\"ASRSchemaASRContextualEntityRetrievalStarted\""
+ "@\"ASRSchemaASRFullPayloadCorrectionContext\""
+ "@\"ASRSchemaASRFullPayloadCorrectionEnded\""
+ "@\"ASRSchemaASRFullPayloadCorrectionFailed\""
+ "@\"ASRSchemaASRFullPayloadCorrectionInfoTier1\""
+ "@\"ASRSchemaASRFullPayloadCorrectionStarted\""
+ "@\"ASRSchemaASRPersonalizationUserEditNamedEntityMetrics\""
+ "@\"DODMLASRSchemaDODMLASRAlignmentInfo\""
+ "@\"DODMLASRSchemaDODMLASRAudioFileResult\""
+ "@\"DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated\""
+ "@\"DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted\""
+ "@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext\""
+ "@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1\""
+ "@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis\""
+ "@\"ExecutorSiriSchemaExecutorIdentifierQueryCallContext\""
+ "@\"ExecutorSiriSchemaExecutorIdentifierQueryCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorIdentifierQueryCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorIdentifierQueryCallStarted\""
+ "@\"ExecutorSiriSchemaExecutorPersonQueryCallContext\""
+ "@\"ExecutorSiriSchemaExecutorPersonQueryCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorPersonQueryCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorPersonQueryCallStarted\""
+ "@\"ExecutorSiriSchemaExecutorSearchToolQueryCallContext\""
+ "@\"ExecutorSiriSchemaExecutorSearchToolQueryCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorSearchToolQueryCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorSearchToolQueryCallStarted\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityCallContext\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityCallStarted\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryLocationCallContext\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryLocationCallEnded\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryLocationCallFailed\""
+ "@\"ExecutorSiriSchemaExecutorStringQueryLocationCallStarted\""
+ "@\"FLOWSchemaFLOWContact\""
+ "@\"FLOWSchemaFLOWContactTier1\""
+ "@\"FLOWSchemaFLOWDomainExecutionMetadata\""
+ "@\"IFTSchemaIFTActionConfirmationSystemStyle\""
+ "@\"IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement\""
+ "@\"IFTSchemaIFTFormatExpression\""
+ "@\"IFTSchemaIFTPayloadExpression\""
+ "@\"IFTSchemaIFTQueryDecorationPrePlannerResult\""
+ "@\"IFTSchemaIFTSkipStatement\""
+ "@\"IFTSchemaIFTStructuredSearchExpression\""
+ "@\"IFTSchemaIFTTypeInstance\""
+ "@\"IFTSchemaIFTValueExpressionArrayVariant\""
+ "@\"MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried\""
+ "@\"MHSchemaMHAdaptiveSiriVolumeUserIntentDetected\""
+ "@\"NLRouterSchemaNLRouterOverrideMetadata\""
+ "@\"NLRouterSchemaNLRouterPromptGenerated\""
+ "@\"NLXSchemaCDMUserWantedToUndo\""
+ "@\"ORCHSchemaORCHAudioTopologyReported\""
+ "@\"ORCHSchemaORCHIntelligenceFlowRequestContext\""
+ "@\"ORCHSchemaORCHIntelligenceFlowRequestEnded\""
+ "@\"ORCHSchemaORCHIntelligenceFlowRequestFailed\""
+ "@\"ORCHSchemaORCHIntelligenceFlowRequestStarted\""
+ "@\"PEGASUSSchemaPEGASUSAlignmentOffset\""
+ "@\"PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1\""
+ "@\"PEGASUSSchemaPEGASUSAsrCorrectionInfo\""
+ "@\"PEGASUSSchemaPEGASUSAsrHypothesisIdx\""
+ "@\"PGSchemaPGGeneratePlanContext\""
+ "@\"PGSchemaPGGeneratePlanEnded\""
+ "@\"PGSchemaPGGeneratePlanFailed\""
+ "@\"PGSchemaPGGeneratePlanStarted\""
+ "@\"PGSchemaPGOverridesMatchMetadata\""
+ "@\"PNRODSchemaPNRError\""
+ "@\"QDSchemaQDAppPreLaunchTriggered\""
+ "@\"QDSchemaQDContextStatementIdsReported\""
+ "@\"QDSchemaQDToolboxSizeReported\""
+ "@\"SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary\""
+ "@\"SISchemaUEITranscriptShown\""
+ "@\"SISchemaUEITranscriptTapped\""
+ "@\"STSchemaSTFailureError\""
+ "ASRENTITYENROLLMENTREASON_ENTITY_LENGTH"
+ "ASRENTITYENROLLMENTREASON_NO_DISPLAY_REPRESENTATION"
+ "ASRENTITYENROLLMENTREASON_TYPE_FILTER"
+ "ASRENTITYENROLLMENTREASON_UNKNOWN"
+ "ASRENTITYENROLLMENTRESULT_ENROLL"
+ "ASRENTITYENROLLMENTRESULT_REJECT"
+ "ASRENTITYENROLLMENTRESULT_UNKNOWN"
+ "ASRENTITYTAGGERCATEGORY_ORGANIZATION_NAME"
+ "ASRENTITYTAGGERCATEGORY_PERSON_NAME"
+ "ASRENTITYTAGGERCATEGORY_PLACE_NAME"
+ "ASRENTITYTAGGERCATEGORY_UNKNOWN"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_BLOCKED_USER_PAYLOAD"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_CANCELLATION"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_EXCESSIVE"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_INCOMPLETE_EXECUTION"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_INSUFFICIENT_TEXT"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_MALFORMED_OUTPUT"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_MODEL_EXECUTION"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_MODEL_OUTPUT_LENGTH"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_OUTPUT_RANGE"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_RANGE"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_UNKNOWN"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_UNSUPPORTED_LANGUAGE"
+ "ASRFULLPAYLOADCORRECTIONERRORTYPE_UNSUPPORTED_LANGUAGE_OUTPUT"
+ "ASRSPEECHPROFILECATEGORY_NT_ACTION"
+ "ASRSPEECHPROFILECATEGORY_NT_APPCONTACT"
+ "ASRSPEECHPROFILECATEGORY_NT_APPNAME"
+ "ASRSPEECHPROFILECATEGORY_NT_APPUNKNOWN"
+ "ASRSPEECHPROFILECATEGORY_NT_APPVOCAB"
+ "ASRSPEECHPROFILECATEGORY_NT_ARTIST"
+ "ASRSPEECHPROFILECATEGORY_NT_CALEVENT"
+ "ASRSPEECHPROFILECATEGORY_NT_CONTACT"
+ "ASRSPEECHPROFILECATEGORY_NT_CORRECTION"
+ "ASRSPEECHPROFILECATEGORY_NT_DEVICE"
+ "ASRSPEECHPROFILECATEGORY_NT_EFFECT"
+ "ASRSPEECHPROFILECATEGORY_NT_ENTITY"
+ "ASRSPEECHPROFILECATEGORY_NT_GROUP"
+ "ASRSPEECHPROFILECATEGORY_NT_HOUSE"
+ "ASRSPEECHPROFILECATEGORY_NT_LOCATION"
+ "ASRSPEECHPROFILECATEGORY_NT_NOTEFOLDER"
+ "ASRSPEECHPROFILECATEGORY_NT_NOTETITLE"
+ "ASRSPEECHPROFILECATEGORY_NT_PAYACCOUNT"
+ "ASRSPEECHPROFILECATEGORY_NT_PHOTOALBUM"
+ "ASRSPEECHPROFILECATEGORY_NT_PHOTOTAG"
+ "ASRSPEECHPROFILECATEGORY_NT_PLAYLIST"
+ "ASRSPEECHPROFILECATEGORY_NT_ROOM"
+ "ASRSPEECHPROFILECATEGORY_NT_SAVEDACTIVITY"
+ "ASRSPEECHPROFILECATEGORY_NT_SCENE"
+ "ASRSPEECHPROFILECATEGORY_NT_SEARCHTERM"
+ "ASRSPEECHPROFILECATEGORY_NT_UNKNOWN"
+ "ASRSPEECHPROFILECATEGORY_NT_WIDGET"
+ "ASRSPEECHPROFILECATEGORY_NT_ZONE"
+ "ASRSPEECHPROFILECATEGORY_UNKNOWN"
+ "ASRSchemaASRContextualEntityCollectionTriggered"
+ "ASRSchemaASRContextualEntityRetrievalContext"
+ "ASRSchemaASRContextualEntityRetrievalEnded"
+ "ASRSchemaASRContextualEntityRetrievalStarted"
+ "ASRSchemaASRContextualEntityState"
+ "ASRSchemaASRFullPayloadCorrectionContext"
+ "ASRSchemaASRFullPayloadCorrectionEnded"
+ "ASRSchemaASRFullPayloadCorrectionFailed"
+ "ASRSchemaASRFullPayloadCorrectionInfoTier1"
+ "ASRSchemaASRFullPayloadCorrectionStarted"
+ "ASRSchemaASRLMEOverActivationEdit"
+ "ASRSchemaASRNamedEntityUserEdit"
+ "ASRSchemaASROneBestTranscriptTier1"
+ "ASRSchemaASRPersonalizationUserEditNamedEntityMetrics"
+ "ASRTASKHINT_ASSISTANT"
+ "ASRTASKHINT_ASSISTANT_DICTATION"
+ "ASRTASKHINT_CAPTIONING"
+ "ASRTASKHINT_CONFIRMATION"
+ "ASRTASKHINT_DICTATION"
+ "ASRTASKHINT_DICTATION_CC"
+ "ASRTASKHINT_FOUND_IN_CALLS"
+ "ASRTASKHINT_KEYBOARD_DICTATION"
+ "ASRTASKHINT_LIVE_TRANSCRIPTION"
+ "ASRTASKHINT_OFFLINE_TRANSCRIPTION"
+ "ASRTASKHINT_SEARCH"
+ "ASRTASKHINT_SPELLING"
+ "ASRTASKHINT_SPELL_CC"
+ "ASRTASKHINT_TSHOT"
+ "ASRTASKHINT_UNKNOWN"
+ "ASRTASKHINT_VOICEMAIL"
+ "ASRTASKHINT_WATCH_DICTATION"
+ "ASRVISUALCONTEXTCATEGORY_SENDER"
+ "ASRVISUALCONTEXTCATEGORY_THREAD"
+ "ASRVISUALCONTEXTCATEGORY_UNKNOWN"
+ "CNVPLUGIN_READER"
+ "COMPONENTNAME_RI"
+ "DEVICE_SENSITIVITY_STATE_SIRI_DATA_SHARING_OPT_OUT_NON_GMS"
+ "DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated"
+ "DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted"
+ "DODMLASRSchemaDODMLASREntityScore"
+ "DODMLASRSchemaDODMLASREntityScoringResult"
+ "DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext"
+ "DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1"
+ "DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis"
+ "EXECUTORSEARCHTOOLQUERYTYPE_APP_ENTITY"
+ "EXECUTORSEARCHTOOLQUERYTYPE_ENTITY_SEARCHABLE_ITEM"
+ "EXECUTORSEARCHTOOLQUERYTYPE_STANDARD"
+ "EXECUTORSEARCHTOOLQUERYTYPE_UNKNOWN"
+ "ExecutorSiriSchemaExecutorIdentifierQueryCallContext"
+ "ExecutorSiriSchemaExecutorIdentifierQueryCallEnded"
+ "ExecutorSiriSchemaExecutorIdentifierQueryCallFailed"
+ "ExecutorSiriSchemaExecutorIdentifierQueryCallStarted"
+ "ExecutorSiriSchemaExecutorPersonQueryCallContext"
+ "ExecutorSiriSchemaExecutorPersonQueryCallEnded"
+ "ExecutorSiriSchemaExecutorPersonQueryCallFailed"
+ "ExecutorSiriSchemaExecutorPersonQueryCallStarted"
+ "ExecutorSiriSchemaExecutorSearchToolQueryCallContext"
+ "ExecutorSiriSchemaExecutorSearchToolQueryCallEnded"
+ "ExecutorSiriSchemaExecutorSearchToolQueryCallFailed"
+ "ExecutorSiriSchemaExecutorSearchToolQueryCallStarted"
+ "ExecutorSiriSchemaExecutorStringQueryEntityCallContext"
+ "ExecutorSiriSchemaExecutorStringQueryEntityCallEnded"
+ "ExecutorSiriSchemaExecutorStringQueryEntityCallFailed"
+ "ExecutorSiriSchemaExecutorStringQueryEntityCallStarted"
+ "ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext"
+ "ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded"
+ "ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed"
+ "ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted"
+ "ExecutorSiriSchemaExecutorStringQueryLocationCallContext"
+ "ExecutorSiriSchemaExecutorStringQueryLocationCallEnded"
+ "ExecutorSiriSchemaExecutorStringQueryLocationCallFailed"
+ "ExecutorSiriSchemaExecutorStringQueryLocationCallStarted"
+ "FLOWDOMAINEXECUTIONTYPE_APPINTENT"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_AUTO_SEND_MODEL_INFERENCE"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_CONTACT_RESOLUTION_CRR"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_CORE_EMOJI_IMAGE_CAPTION"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_RESOLVE_SRR_ENTITY"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_SIRI_REMEMBERS_READ"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_SIRI_REMEMBERS_WRITE"
+ "FLOWDOMAINEXECUTIONTYPE_MESSAGE_SMART_APP_SELECTION"
+ "FLOWSchemaFLOWContact"
+ "FLOWSchemaFLOWContactTier1"
+ "FLOWSchemaFLOWDomainExecutionMetadata"
+ "FLTASKSTATUS_DID_NOT_EXECUTE"
+ "IFTACTIONCLASS_APP_INTENT"
+ "IFTACTIONCLASS_CLIENT_ACTION"
+ "IFTACTIONCLASS_SCHEMA"
+ "IFTACTIONCLASS_UNKNOWN"
+ "IFTACTIONCONFIRMATIONSYSTEMSTYLEGENERATIVEAIENABLEMENTSOURCE_COMPOSE_VIA_SIRI"
+ "IFTACTIONCONFIRMATIONSYSTEMSTYLEGENERATIVEAIENABLEMENTSOURCE_KNOWLEDGE_FALLBACK"
+ "IFTACTIONCONFIRMATIONSYSTEMSTYLEGENERATIVEAIENABLEMENTSOURCE_MEDIA_QA"
+ "IFTACTIONCONFIRMATIONSYSTEMSTYLEGENERATIVEAIENABLEMENTSOURCE_TEXT_ASSISTANT"
+ "IFTACTIONCONFIRMATIONSYSTEMSTYLEGENERATIVEAIENABLEMENTSOURCE_UNKNOWN"
+ "IFTPARAMETERNOTALLOWEDREASON_MISSING_REQUIRED_EMAIL_ADDRESS"
+ "IFTPARAMETERNOTALLOWEDREASON_MISSING_REQUIRED_PHONE_NUMBER"
+ "IFTPARAMETERNOTALLOWEDREASON_UNKNOWN"
+ "IFTPRIMITIVETYPE_APP"
+ "IFTPRIMITIVETYPE_ATTRIBUTED_STRING"
+ "IFTPRIMITIVETYPE_BOOL"
+ "IFTPRIMITIVETYPE_CURRENCY_AMOUNT"
+ "IFTPRIMITIVETYPE_DATE"
+ "IFTPRIMITIVETYPE_DATE_COMPONENTS"
+ "IFTPRIMITIVETYPE_DECIMAL"
+ "IFTPRIMITIVETYPE_DICTIONARY"
+ "IFTPRIMITIVETYPE_FILE"
+ "IFTPRIMITIVETYPE_INT"
+ "IFTPRIMITIVETYPE_MEASUREMENT"
+ "IFTPRIMITIVETYPE_NONE"
+ "IFTPRIMITIVETYPE_NUMBER"
+ "IFTPRIMITIVETYPE_PAYMENT_METHOD"
+ "IFTPRIMITIVETYPE_PERSON"
+ "IFTPRIMITIVETYPE_PLACEMARK"
+ "IFTPRIMITIVETYPE_SEARCHABLE_ITEM"
+ "IFTPRIMITIVETYPE_STRING"
+ "IFTPRIMITIVETYPE_UNKNOWN"
+ "IFTPRIMITIVETYPE_URL"
+ "IFTQUERYPAYLOADTYPE_IDENTIFER_QUERY"
+ "IFTQUERYPAYLOADTYPE_PERSON_QUERY"
+ "IFTQUERYPAYLOADTYPE_SEARCH_TOOL_QUERY"
+ "IFTQUERYPAYLOADTYPE_STRING_QUERY"
+ "IFTQUERYPAYLOADTYPE_UNKNOWN"
+ "IFTSchemaIFTActionConfirmationSystemStyle"
+ "IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement"
+ "IFTSchemaIFTActionParameterValue"
+ "IFTSchemaIFTCallExpressionParameters"
+ "IFTSchemaIFTFormatExpression"
+ "IFTSchemaIFTPayloadExpression"
+ "IFTSchemaIFTQueryDecorationPrePlannerResult"
+ "IFTSchemaIFTSkipStatement"
+ "IFTSchemaIFTStructuredSearchExpression"
+ "IFTSchemaIFTStructuredSearchExpressionParameters"
+ "IFTSchemaIFTStructuredSearchProperty"
+ "IFTSchemaIFTTypeInstance"
+ "IFTSchemaIFTValueExpressionArrayVariant"
+ "INVOCATIONSOURCE_QUICK_TYPE_TO_SIRI_KEYBOARD_SHORTCUT"
+ "INVOCATIONSOURCE_QUICK_TYPE_TO_SIRI_MENU_BAR"
+ "JRBUCKETEDDISTANCE_LEVEL_1"
+ "JRBUCKETEDDISTANCE_LEVEL_2"
+ "JRBUCKETEDDISTANCE_LEVEL_3"
+ "JRBUCKETEDDISTANCE_LEVEL_4"
+ "JRBUCKETEDDISTANCE_LEVEL_5"
+ "JRBUCKETEDDISTANCE_LEVEL_6"
+ "JRBUCKETEDDISTANCE_LEVEL_7"
+ "JRBUCKETEDDISTANCE_UNKNOWN"
+ "JRPARAMETERSUBTYPE_DEFERRED_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_DEFERRED_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_DEFERRED_CONTACT"
+ "JRPARAMETERSUBTYPE_DEFERRED_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_DEFERRED_FILE_URL"
+ "JRPARAMETERSUBTYPE_DEFERRED_IMAGE"
+ "JRPARAMETERSUBTYPE_DEFERRED_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_DEFERRED_MESSAGE"
+ "JRPARAMETERSUBTYPE_DEFERRED_UNKNOWN"
+ "JRPARAMETERSUBTYPE_DEFERRED_VIDEO"
+ "JRPARAMETERSUBTYPE_ENTITY_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_ENTITY_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_ENTITY_CONTACT"
+ "JRPARAMETERSUBTYPE_ENTITY_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_FILE_URL"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_CONTACT"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_FILE_URL"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_IMAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_UNKNOWN"
+ "JRPARAMETERSUBTYPE_ENTITY_IDENTIFIER_VIDEO"
+ "JRPARAMETERSUBTYPE_ENTITY_IMAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_ENTITY_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENTITY_UNKNOWN"
+ "JRPARAMETERSUBTYPE_ENTITY_VIDEO"
+ "JRPARAMETERSUBTYPE_ENUMERATION_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_ENUMERATION_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_ENUMERATION_CONTACT"
+ "JRPARAMETERSUBTYPE_ENUMERATION_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENUMERATION_FILE_URL"
+ "JRPARAMETERSUBTYPE_ENUMERATION_IMAGE"
+ "JRPARAMETERSUBTYPE_ENUMERATION_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_ENUMERATION_MESSAGE"
+ "JRPARAMETERSUBTYPE_ENUMERATION_UNKNOWN"
+ "JRPARAMETERSUBTYPE_ENUMERATION_VIDEO"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_APP"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_ATTRIBUTED_STRING"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_BOOL"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_CURRENCY_AMOUNT"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_DATE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_DATE_COMPONENTS"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_DECIMAL"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_FILE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_INT"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_INTENTS_FILE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_MEASUREMENT"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_NUMBER"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_PAYMENT_METHOD"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_PERSON"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_PLACEMARK"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_CONTACT"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_FILEURL"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_IMAGE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_MESSAGE"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_UNKNOWN"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_SEARCHABLE_ITEM_VIDEO"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_STRING"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_UNKNOWN"
+ "JRPARAMETERSUBTYPE_PRIMITIVE_URL"
+ "JRPARAMETERSUBTYPE_QUERY_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_QUERY_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_QUERY_CONTACT"
+ "JRPARAMETERSUBTYPE_QUERY_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_QUERY_FILE_URL"
+ "JRPARAMETERSUBTYPE_QUERY_IMAGE"
+ "JRPARAMETERSUBTYPE_QUERY_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_QUERY_MESSAGE"
+ "JRPARAMETERSUBTYPE_QUERY_UNKNOWN"
+ "JRPARAMETERSUBTYPE_QUERY_VIDEO"
+ "JRPARAMETERSUBTYPE_REFERENCE_ALIAS_FILE"
+ "JRPARAMETERSUBTYPE_REFERENCE_CALENDAR_EVENT"
+ "JRPARAMETERSUBTYPE_REFERENCE_CONTACT"
+ "JRPARAMETERSUBTYPE_REFERENCE_EMAIL_MESSAGE"
+ "JRPARAMETERSUBTYPE_REFERENCE_FILE_URL"
+ "JRPARAMETERSUBTYPE_REFERENCE_IMAGE"
+ "JRPARAMETERSUBTYPE_REFERENCE_LIVE_PHOTO"
+ "JRPARAMETERSUBTYPE_REFERENCE_MESSAGE"
+ "JRPARAMETERSUBTYPE_REFERENCE_UNKNOWN"
+ "JRPARAMETERSUBTYPE_REFERENCE_VIDEO"
+ "JRPARAMETERSUBTYPE_UNKNOWN"
+ "JRSchemaHistoricalLocationContext"
+ "JRSchemaIntervalUntilStartTime"
+ "JRSchemaJRCandidateBooleanMask"
+ "JRSchemaJRCandidateRiskLevel"
+ "JRSchemaJRCandidateSearchToolRank"
+ "JRSchemaJRCandidateTimeIntervalMatrix"
+ "JRSchemaJREntitySimilarityRow"
+ "JRSchemaJREntitySimilarityScores"
+ "JRSchemaJRTokenConfidence"
+ "MHASVBACKGROUNDNOISEACTIVITYLEVEL_HIGH"
+ "MHASVBACKGROUNDNOISEACTIVITYLEVEL_LOW"
+ "MHASVBACKGROUNDNOISEACTIVITYLEVEL_UNKNOWN"
+ "MHASVINVOCATIONTYPE_BUTTON_PRESS"
+ "MHASVINVOCATIONTYPE_UNKNOWN"
+ "MHASVINVOCATIONTYPE_VOICE_TRIGGER"
+ "MHASVSPEAKERDISTANCETYPE_ESTIMATION_INCOMPLETE"
+ "MHASVSPEAKERDISTANCETYPE_FAR"
+ "MHASVSPEAKERDISTANCETYPE_MID"
+ "MHASVSPEAKERDISTANCETYPE_NEAR"
+ "MHASVSPEAKERDISTANCETYPE_UNKNOWN"
+ "MHASVUSERINTENTTYPE_DECREASE_SIRI_VOLUME"
+ "MHASVUSERINTENTTYPE_DEFAULT"
+ "MHASVUSERINTENTTYPE_INCREASE_SIRI_VOLUME"
+ "MHASVUSERINTENTTYPE_SET_VOLUME"
+ "MHASVUSERINTENTTYPE_UNKNOWN"
+ "MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried"
+ "MHSchemaMHAdaptiveSiriVolumeUserIntentDetected"
+ "NLROUTERDECISIONSOURCE_MAGIC_WORD_OVERRIDE"
+ "NLROUTERDECISIONSOURCE_USER_DEFAULT_OVERRIDE"
+ "NLROUTERPROMPTCOMPONENTTYPE_CONVERSATION_HISTORY"
+ "NLROUTERPROMPTCOMPONENTTYPE_CORRECTIONS"
+ "NLROUTERPROMPTCOMPONENTTYPE_CURRENT_QUERY"
+ "NLROUTERPROMPTCOMPONENTTYPE_ON_SCREEN_CONTEXT"
+ "NLROUTERPROMPTCOMPONENTTYPE_SPANS"
+ "NLROUTERPROMPTCOMPONENTTYPE_UNKNOWN"
+ "NLRouterSchemaNLRouterOverrideMetadata"
+ "NLRouterSchemaNLRouterPromptComponent"
+ "NLRouterSchemaNLRouterPromptGenerated"
+ "NLXSchemaCDMUserWantedToUndo"
+ "ODDEVENTORIGIN_ODDI"
+ "ODDEVENTORIGIN_POIROT"
+ "ODDEVENTORIGIN_UDI"
+ "ODDEVENTORIGIN_UNKNOWN"
+ "ORCHDEVICESAUDIOTOPOLOGY_ATV_PLUS_SINGLE"
+ "ORCHDEVICESAUDIOTOPOLOGY_ATV_PLUS_STEREO_PAIR"
+ "ORCHDEVICESAUDIOTOPOLOGY_SINGLE"
+ "ORCHDEVICESAUDIOTOPOLOGY_STEREO_PAIR"
+ "ORCHDEVICESAUDIOTOPOLOGY_UNKNOWN"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_ACTION_CANCELED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_ACTION_NOT_ALLOWED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_BLUETOOTH_DISABLED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_DEVELOPER_DEFINED_ERROR"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_ENTITY_NOT_FOUND"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_FEATURE_CURRENTLY_RESTRICTED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_LOCATION_DISABLED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_NETWORK_FAILURE"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_NO_MATCHING_TOOL"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_PARTIAL_FAILURE"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_PRECISE_LOCATION_DISABLED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_PRE_FLIGHT_CHECK_FAILURE"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_UNABLE_TO_CANCEL"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_UNABLE_TO_UNDO"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_UNKNOWN"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_UNSUPPORTED_ON_DEVICE"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_VALUE_DISAMBIGUATION_REJECTED"
+ "ORCHINTELLIGENCEFLOWFAILUREREASON_WIFI_DISABLED"
+ "ORCHSHIMACTION_CREATE_ALARM"
+ "ORCHSHIMACTION_CREATE_NOTE"
+ "ORCHSHIMACTION_CREATE_REMINDER"
+ "ORCHSHIMACTION_NAVIGATE_TO"
+ "ORCHSHIMACTION_PLAY_MEDIA"
+ "ORCHSHIMACTION_SEND_MESSAGE"
+ "ORCHSHIMACTION_START_CALL"
+ "ORCHSHIMACTION_UNKNOWN"
+ "ORCHSchemaORCHAudioTopologyReported"
+ "ORCHSchemaORCHIntelligenceFlowRequestContext"
+ "ORCHSchemaORCHIntelligenceFlowRequestEnded"
+ "ORCHSchemaORCHIntelligenceFlowRequestFailed"
+ "ORCHSchemaORCHIntelligenceFlowRequestStarted"
+ "PEGASUSALTERNATEQUERYSUGGESTIONCANDIDATETYPE_ASR"
+ "PEGASUSALTERNATEQUERYSUGGESTIONCANDIDATETYPE_UNSPECIFIED"
+ "PEGASUSSchemaPEGASUSAlignmentOffset"
+ "PEGASUSSchemaPEGASUSAlternateQuerySuggestionCandidateTier1"
+ "PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1"
+ "PEGASUSSchemaPEGASUSAsrCorrectionInfo"
+ "PEGASUSSchemaPEGASUSAsrHypothesisIdx"
+ "PEGASUSSchemaPEGASUSAsrHypothesisInfo"
+ "PEGASUSSchemaPEGASUSCorrectionInfo"
+ "PGSchemaPGGeneratePlanContext"
+ "PGSchemaPGGeneratePlanEnded"
+ "PGSchemaPGGeneratePlanFailed"
+ "PGSchemaPGGeneratePlanStarted"
+ "PGSchemaPGOverridesMatchMetadata"
+ "PNRODSchemaPNRError"
+ "PNRODSchemaPNRODExecutor"
+ "PNRODSchemaPNRODPlanGeneration"
+ "PNRODSchemaPNRODPlanResolution"
+ "PNRODSchemaPNRODQueryDecoration"
+ "PNRODSchemaPNRODResponseGeneration"
+ "PNRODSchemaPNRODSearch"
+ "PNROD_PGMODELINTERFACE_FULLPLANNER_HTTPCLIENT"
+ "PNROD_PGMODELINTERFACE_FULLPLANNER_TOKENGENERATIONCLIENT"
+ "PNROD_PGMODELINTERFACE_FULLPLANNER_TOKENGENERATIONCLIENT_CONSTRAINEDDECODING"
+ "PNROD_PGMODELINTERFACE_UNKNOWN"
+ "PNROD_QDSOURCE_CROSS_DEVICE_ORCHESTRATION"
+ "PNROD_QDSOURCE_FULL_PLANNER"
+ "PNROD_QDSOURCE_PREWARM"
+ "PNROD_QDSOURCE_PRE_PLANNER"
+ "PNROD_QDSOURCE_UNKNOWN"
+ "PNROD_REQUESTFEATURETAG_APP_ENTITY_RESOLUTION"
+ "PNROD_REQUESTFEATURETAG_NLG"
+ "PNROD_REQUESTFEATURETAG_ON_SCREEN_REFERENCE"
+ "PNROD_REQUESTFEATURETAG_PCS"
+ "PNROD_REQUESTFEATURETAG_PQA"
+ "PNROD_REQUESTFEATURETAG_SEARCH_ACT"
+ "PNROD_REQUESTFEATURETAG_SHIMS"
+ "PNROD_REQUESTFEATURETAG_SIMPLE_APP_INTENT"
+ "PNROD_REQUESTFEATURETAG_UNKNOWN"
+ "PNROD_RGRESPONSESOURCE_CLIENT_CACHE"
+ "PNROD_RGRESPONSESOURCE_CONTINUE_ON_DEVICE"
+ "PNROD_RGRESPONSESOURCE_FALLBACK"
+ "PNROD_RGRESPONSESOURCE_IN_APP"
+ "PNROD_RGRESPONSESOURCE_NLG_MODEL"
+ "PNROD_RGRESPONSESOURCE_OVERRIDE"
+ "PNROD_RGRESPONSESOURCE_RESPONSE_CATALOG"
+ "PNROD_RGRESPONSESOURCE_TOOL"
+ "PNROD_RGRESPONSESOURCE_UNKNOWN"
+ "POMMESREQUESTFAILEDREASON_REQUEST_CONSTRUCTION_ERROR"
+ "POMMESREQUESTFAILEDREASON_RESOLUTION_REQUEST_FAILURE"
+ "QDCALLER_CROSS_DEVICE_ORCHESTRATION"
+ "QDCALLER_FULL_PLANNER"
+ "QDCALLER_PREWARM"
+ "QDCALLER_PRE_PLANNER"
+ "QDCALLER_UNKNOWN"
+ "QDENTITYCONTEXTTYPE_HAS_FOCUSED_ON_SCREEN_DOCUMENT"
+ "QDENTITYCONTEXTTYPE_HAS_FOCUSED_ON_SCREEN_IMAGE"
+ "QDENTITYCONTEXTTYPE_INTELLIGENCE_COMMAND"
+ "QDENTITYCONTEXTTYPE_ON_SCREEN_APP"
+ "QDENTITYCONTEXTTYPE_ON_SCREEN_UI_TEXT"
+ "QDSUBCOMPONENT_FETCH_DYNAMIC_ENUMERATION_ENTITIES"
+ "QDSUBCOMPONENT_TOOL_CONTEXT_RETRIEVAL"
+ "QDSchemaQDAppPreLaunchTriggered"
+ "QDSchemaQDContextStatementIdsReported"
+ "QDSchemaQDToolboxSizeReported"
+ "RFCOMPONENT_SF_DETAILED"
+ "RFCOMPONENT_SF_LINK_PRESENTATION"
+ "SIRISETUPENROLLMENTUIMODE_HOME_ONBOARDING"
+ "SIRISETUPENROLLMENTUIMODE_HOME_VOICE_ENROLL"
+ "SIRISETUPENROLLMENTUISESSIONOUTCOME_SKIPPED"
+ "SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts"
+ "SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary"
+ "SISchemaUEITranscriptShown"
+ "SISchemaUEITranscriptTapped"
+ "STSchemaSTFailureError"
+ "T@\"ASRSchemaASRContextualEntityCollectionTriggered\",&,N,V_contextualEntityCollectionTriggered"
+ "T@\"ASRSchemaASRContextualEntityRetrievalContext\",&,N,V_contextualEntityRetrievalContext"
+ "T@\"ASRSchemaASRContextualEntityRetrievalEnded\",&,N,V_ended"
+ "T@\"ASRSchemaASRContextualEntityRetrievalStarted\",&,N,V_startedOrChanged"
+ "T@\"ASRSchemaASRFullPayloadCorrectionContext\",&,N,V_fullPayloadCorrectionContext"
+ "T@\"ASRSchemaASRFullPayloadCorrectionEnded\",&,N,V_ended"
+ "T@\"ASRSchemaASRFullPayloadCorrectionFailed\",&,N,V_failed"
+ "T@\"ASRSchemaASRFullPayloadCorrectionInfoTier1\",&,N,V_infoTier1"
+ "T@\"ASRSchemaASRFullPayloadCorrectionStarted\",&,N,V_startedOrChanged"
+ "T@\"ASRSchemaASRPersonalizationUserEditNamedEntityMetrics\",&,N,V_personalizationUserEditNamedEntityMetrics"
+ "T@\"DODMLASRSchemaDODMLASRAlignmentInfo\",&,N,V_asrFullPayloadCorrectedToUserEdit"
+ "T@\"DODMLASRSchemaDODMLASRAlignmentInfo\",&,N,V_asrOutputToUserEdit"
+ "T@\"DODMLASRSchemaDODMLASRAudioFileResult\",&,N,V_audioFileResult"
+ "T@\"DODMLASRSchemaDODMLASRContextualReplayBiomeRecordCreated\",&,N,V_contextualReplayBiomeRecordCreated"
+ "T@\"DODMLASRSchemaDODMLASRContextualReplayBiomeRecordDeleted\",&,N,V_contextualReplayBiomeRecordDeleted"
+ "T@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentContext\",&,N,V_fullPayloadCorrectionExperimentContext"
+ "T@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentInfoTier1\",&,N,V_fullPayloadCorrectionExperimentTier1"
+ "T@\"DODMLASRSchemaDODMLASRFullPayloadCorrectionExperimentPostAnalysis\",&,N,V_fullPayloadCorrectionExperimentPostAnalysis"
+ "T@\"ExecutorSiriSchemaExecutorIdentifierQueryCallContext\",&,N,V_executorIdentifierQueryCallContext"
+ "T@\"ExecutorSiriSchemaExecutorIdentifierQueryCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorIdentifierQueryCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorIdentifierQueryCallStarted\",&,N,V_startedOrChanged"
+ "T@\"ExecutorSiriSchemaExecutorPersonQueryCallContext\",&,N,V_executorPersonQueryCallContext"
+ "T@\"ExecutorSiriSchemaExecutorPersonQueryCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorPersonQueryCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorPersonQueryCallStarted\",&,N,V_startedOrChanged"
+ "T@\"ExecutorSiriSchemaExecutorSearchToolQueryCallContext\",&,N,V_executorSearchToolQueryCallContext"
+ "T@\"ExecutorSiriSchemaExecutorSearchToolQueryCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorSearchToolQueryCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorSearchToolQueryCallStarted\",&,N,V_startedOrChanged"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityCallContext\",&,N,V_executorStringQueryEntityCallContext"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityCallStarted\",&,N,V_startedOrChanged"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallContext\",&,N,V_executorStringQueryEntityMatcherCallContext"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryEntityMatcherCallStarted\",&,N,V_startedOrChanged"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryLocationCallContext\",&,N,V_executorStringQueryLocationCallContext"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryLocationCallEnded\",&,N,V_ended"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryLocationCallFailed\",&,N,V_failed"
+ "T@\"ExecutorSiriSchemaExecutorStringQueryLocationCallStarted\",&,N,V_startedOrChanged"
+ "T@\"FLOWSchemaFLOWContact\",&,N,V_contact"
+ "T@\"FLOWSchemaFLOWContactTier1\",&,N,V_flowContactTier1"
+ "T@\"FLOWSchemaFLOWDomainExecutionMetadata\",&,N,V_domainExecutionMetadata"
+ "T@\"IFTSchemaIFTActionConfirmationSystemStyle\",&,N,V_systemStyle"
+ "T@\"IFTSchemaIFTActionConfirmationSystemStyleGenerativeAIEnablement\",&,N,V_generativeAIEnablement"
+ "T@\"IFTSchemaIFTFormatExpression\",&,N,V_format"
+ "T@\"IFTSchemaIFTIntelligenceFlowError\",&,N,V_failedToConvertClientEvent"
+ "T@\"IFTSchemaIFTPayloadExpression\",&,N,V_payload"
+ "T@\"IFTSchemaIFTQueryDecorationPrePlannerResult\",&,N,V_queryDecorationPrePlannerResult"
+ "T@\"IFTSchemaIFTSkipStatement\",&,N,V_skipStatement"
+ "T@\"IFTSchemaIFTStructuredSearchExpression\",&,N,V_structuredSearch"
+ "T@\"IFTSchemaIFTTypeInstance\",&,N,V_returnType"
+ "T@\"IFTSchemaIFTValueExpressionArrayVariant\",&,N,V_array"
+ "T@\"MHSchemaMHAdaptiveSiriVolumeTTSVolumeQueried\",&,N,V_adaptiveSiriVolumeTTSVolumeQueried"
+ "T@\"MHSchemaMHAdaptiveSiriVolumeUserIntentDetected\",&,N,V_adaptiveSiriVolumeUserIntentDetected"
+ "T@\"NLRouterSchemaNLRouterOverrideMetadata\",&,N,V_overrideMetadata"
+ "T@\"NLRouterSchemaNLRouterPromptGenerated\",&,N,V_nlRouterPromptGenerated"
+ "T@\"NLXSchemaCDMUserWantedToUndo\",&,N,V_wantedToUndo"
+ "T@\"NSArray\",C,N,V_actionParameterValues"
+ "T@\"NSArray\",C,N,V_alternateQuerySuggestionCandidateTier1s"
+ "T@\"NSArray\",C,N,V_asrHypothesesInfos"
+ "T@\"NSArray\",C,N,V_asrScores"
+ "T@\"NSArray\",C,N,V_bucketedDistances"
+ "T@\"NSArray\",C,N,V_callers"
+ "T@\"NSArray\",C,N,V_candidateBooleanMasks"
+ "T@\"NSArray\",C,N,V_candidateRisks"
+ "T@\"NSArray\",C,N,V_candidateTimeIntervalMatrixs"
+ "T@\"NSArray\",C,N,V_components"
+ "T@\"NSArray\",C,N,V_contextStatementIds"
+ "T@\"NSArray\",C,N,V_contexts"
+ "T@\"NSArray\",C,N,V_contextualEntityStatementIds"
+ "T@\"NSArray\",C,N,V_corrections"
+ "T@\"NSArray\",C,N,V_droppedComponents"
+ "T@\"NSArray\",C,N,V_enabledTasks"
+ "T@\"NSArray\",C,N,V_entityScoreResults"
+ "T@\"NSArray\",C,N,V_entityScores"
+ "T@\"NSArray\",C,N,V_executors"
+ "T@\"NSArray\",C,N,V_historicalLocationContexts"
+ "T@\"NSArray\",C,N,V_intervalUntilStartTimes"
+ "T@\"NSArray\",C,N,V_isApplicableToCandidates"
+ "T@\"NSArray\",C,N,V_jrEntitySimilarityScores"
+ "T@\"NSArray\",C,N,V_lmeOverActivationEdits"
+ "T@\"NSArray\",C,N,V_logOfIntervalUntilStartTimeInSeconds"
+ "T@\"NSArray\",C,N,V_namedEntityUserEdits"
+ "T@\"NSArray\",C,N,V_oneBestTranscripts"
+ "T@\"NSArray\",C,N,V_pageAttempts"
+ "T@\"NSArray\",C,N,V_parameterSubTypes"
+ "T@\"NSArray\",C,N,V_planGenerations"
+ "T@\"NSArray\",C,N,V_planResolutions"
+ "T@\"NSArray\",C,N,V_queryDecorations"
+ "T@\"NSArray\",C,N,V_rejectedContextTypes"
+ "T@\"NSArray\",C,N,V_rejectedEntityTypes"
+ "T@\"NSArray\",C,N,V_requestFeatureTags"
+ "T@\"NSArray\",C,N,V_responseGenerations"
+ "T@\"NSArray\",C,N,V_retrievedEntityStates"
+ "T@\"NSArray\",C,N,V_riskLevels"
+ "T@\"NSArray\",C,N,V_rows"
+ "T@\"NSArray\",C,N,V_searchToolRanks"
+ "T@\"NSArray\",C,N,V_searchs"
+ "T@\"NSArray\",C,N,V_speechProfileCategories"
+ "T@\"NSArray\",C,N,V_visualContextCategories"
+ "T@\"NSArray\",C,N,V_voiceIdScores"
+ "T@\"NSString\",C,N,V_callParameterName"
+ "T@\"NSString\",C,N,V_contactName"
+ "T@\"NSString\",C,N,V_correction"
+ "T@\"NSString\",C,N,V_domainExecutionAppIntentBundleID"
+ "T@\"NSString\",C,N,V_errorDomainString"
+ "T@\"NSString\",C,N,V_fullPayloadCorrectorInput"
+ "T@\"NSString\",C,N,V_fullPayloadCorrectorOutput"
+ "T@\"NSString\",C,N,V_grammar"
+ "T@\"NSString\",C,N,V_loggableUserIdHash"
+ "T@\"NSString\",C,N,V_original"
+ "T@\"NSString\",C,N,V_pgModelIdentifier"
+ "T@\"NSString\",C,N,V_pgOverridesAssetVersion"
+ "T@\"NSString\",C,N,V_postItn"
+ "T@\"NSString\",C,N,V_postItn1Best"
+ "T@\"NSString\",C,N,V_postItnUtterance"
+ "T@\"NSString\",C,N,V_rawRecognition"
+ "T@\"NSString\",C,N,V_selectedloggableUserIdHash"
+ "T@\"NSString\",C,N,V_sourceAuxKey"
+ "T@\"NSString\",C,N,V_structuredSearchParameterName"
+ "T@\"ORCHSchemaORCHAudioTopologyReported\",&,N,V_audioTopologyReported"
+ "T@\"ORCHSchemaORCHIntelligenceFlowRequestContext\",&,N,V_intelligenceFlowRequestContext"
+ "T@\"ORCHSchemaORCHIntelligenceFlowRequestEnded\",&,N,V_ended"
+ "T@\"ORCHSchemaORCHIntelligenceFlowRequestFailed\",&,N,V_failed"
+ "T@\"ORCHSchemaORCHIntelligenceFlowRequestStarted\",&,N,V_startedOrChanged"
+ "T@\"PEGASUSSchemaPEGASUSAlignmentOffset\",&,N,V_alignmentOffset"
+ "T@\"PEGASUSSchemaPEGASUSAlternateQuerySuggestionTier1\",&,N,V_alternateQuerySuggestionTier1"
+ "T@\"PEGASUSSchemaPEGASUSAsrCorrectionInfo\",&,N,V_pegasusAsrCorrectionInfo"
+ "T@\"PEGASUSSchemaPEGASUSAsrHypothesisIdx\",&,N,V_idx"
+ "T@\"PGSchemaPGGeneratePlanContext\",&,N,V_pgGeneratePlanContext"
+ "T@\"PGSchemaPGGeneratePlanEnded\",&,N,V_ended"
+ "T@\"PGSchemaPGGeneratePlanFailed\",&,N,V_failed"
+ "T@\"PGSchemaPGGeneratePlanStarted\",&,N,V_startedOrChanged"
+ "T@\"PGSchemaPGOverridesMatchMetadata\",&,N,V_overridesMatched"
+ "T@\"PNRODSchemaPNRError\",&,N,V_error"
+ "T@\"PNRODSchemaPNRError\",&,N,V_underUnderlyingError"
+ "T@\"PNRODSchemaPNRError\",&,N,V_underlyingError"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_appEntityQueryResponseTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_executorAppIntentHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_executorAppIntentQueryHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_identifierQueryTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_personQueryTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgFullPlannerHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgFullPlannerPostInferenceTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgFullPlannerPreInferenceTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgModelInferenceTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgOverridesTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgPlanGenTotalTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_pgPrescribedPlanTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_planGenerationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_postSearchTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_prTotalHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_preSearchTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationContextRetrievalTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationFetchDynamicEnumerationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationFullPlannerBlockingTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationInputCollectionTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationOutputBuildingTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationRankingTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationSpanRetrievalTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationToolRetrievalContextTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationToolRetrievalTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationTupleBuildingTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_queryDecorationTupleRankingTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationCacheManagerTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationCatalogTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationGMSCallTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationHallucinationDetectionTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationInferenceTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationOverrideTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_responseGenerationValidationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchGlobalSearchTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchHallucinationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchStartToGlobalSearchEnd"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchStartToSpotlightEnd"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchToolQueryTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_searchTotalHandleTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_stringQueryEntityMatcherTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_stringQueryEntityTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_stringQueryLocationTime"
+ "T@\"PNRODSchemaPNRODMetricDuration\",&,N,V_ttaie"
+ "T@\"QDSchemaQDAppPreLaunchTriggered\",&,N,V_appPreLaunchTriggered"
+ "T@\"QDSchemaQDContextStatementIdsReported\",&,N,V_contextStatementIdsReported"
+ "T@\"QDSchemaQDToolboxSizeReported\",&,N,V_toolboxSizeReported"
+ "T@\"SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary\",&,N,V_sessionSummary"
+ "T@\"SISchemaUEITranscriptShown\",&,N,V_transcriptShown"
+ "T@\"SISchemaUEITranscriptTapped\",&,N,V_transcriptTapped"
+ "T@\"SISchemaUUID\",&,N,V_anonymizedLocationNameId"
+ "T@\"SISchemaUUID\",&,N,V_anonymizedLocationTypeId"
+ "T@\"SISchemaUUID\",&,N,V_candidateA"
+ "T@\"SISchemaUUID\",&,N,V_candidateB"
+ "T@\"SISchemaUUID\",&,N,V_overrideId"
+ "T@\"SISchemaUUID\",&,N,V_queryDecorationID"
+ "T@\"SISchemaUUID\",&,N,V_responseGenerationID"
+ "T@\"STSchemaSTFailureError\",&,N,V_stError"
+ "TB,N,V_didTriggerFirstPass"
+ "TB,N,V_expensiveCellularDownloadRequested"
+ "TB,N,V_fromPreSoftwareUpdateStaging"
+ "TB,N,V_hasAdaptiveSiriVolumeTTSVolumeQueried"
+ "TB,N,V_hasAdaptiveSiriVolumeUserIntentDetected"
+ "TB,N,V_hasAlignmentOffset"
+ "TB,N,V_hasAlternateQuerySuggestionTier1"
+ "TB,N,V_hasAnonymizedLocationNameId"
+ "TB,N,V_hasAnonymizedLocationTypeId"
+ "TB,N,V_hasAppEntityQueryResponseTime"
+ "TB,N,V_hasAppPreLaunchTriggered"
+ "TB,N,V_hasArray"
+ "TB,N,V_hasAsrFullPayloadCorrectedToUserEdit"
+ "TB,N,V_hasAsrOutputToUserEdit"
+ "TB,N,V_hasAudioFileResult"
+ "TB,N,V_hasCallParameterName"
+ "TB,N,V_hasCandidateA"
+ "TB,N,V_hasCandidateB"
+ "TB,N,V_hasContact"
+ "TB,N,V_hasContactName"
+ "TB,N,V_hasContextStatementIdsReported"
+ "TB,N,V_hasContextualEntityCollectionTriggered"
+ "TB,N,V_hasContextualEntityRetrievalContext"
+ "TB,N,V_hasContextualReplayBiomeRecordCreated"
+ "TB,N,V_hasContextualReplayBiomeRecordDeleted"
+ "TB,N,V_hasCorrection"
+ "TB,N,V_hasDomainExecutionAppIntentBundleID"
+ "TB,N,V_hasDomainExecutionMetadata"
+ "TB,N,V_hasErrorDomainString"
+ "TB,N,V_hasExecutorAppIntentHandleTime"
+ "TB,N,V_hasExecutorAppIntentQueryHandleTime"
+ "TB,N,V_hasExecutorIdentifierQueryCallContext"
+ "TB,N,V_hasExecutorPersonQueryCallContext"
+ "TB,N,V_hasExecutorSearchToolQueryCallContext"
+ "TB,N,V_hasExecutorStringQueryEntityCallContext"
+ "TB,N,V_hasExecutorStringQueryEntityMatcherCallContext"
+ "TB,N,V_hasExecutorStringQueryLocationCallContext"
+ "TB,N,V_hasFailedToConvertClientEvent"
+ "TB,N,V_hasFlowContactTier1"
+ "TB,N,V_hasFormat"
+ "TB,N,V_hasFullPayloadCorrectionContext"
+ "TB,N,V_hasFullPayloadCorrectionExperimentContext"
+ "TB,N,V_hasFullPayloadCorrectionExperimentPostAnalysis"
+ "TB,N,V_hasFullPayloadCorrectionExperimentTier1"
+ "TB,N,V_hasFullPayloadCorrectorInput"
+ "TB,N,V_hasFullPayloadCorrectorOutput"
+ "TB,N,V_hasGenerativeAIEnablement"
+ "TB,N,V_hasGrammar"
+ "TB,N,V_hasIdentifierQueryTime"
+ "TB,N,V_hasIdx"
+ "TB,N,V_hasInfoTier1"
+ "TB,N,V_hasIntelligenceFlowRequestContext"
+ "TB,N,V_hasLoggableUserIdHash"
+ "TB,N,V_hasNlRouterPromptGenerated"
+ "TB,N,V_hasOriginal"
+ "TB,N,V_hasOverrideMetadata"
+ "TB,N,V_hasOverridesMatched"
+ "TB,N,V_hasPegasusAsrCorrectionInfo"
+ "TB,N,V_hasPersonQueryTime"
+ "TB,N,V_hasPersonalizationUserEditNamedEntityMetrics"
+ "TB,N,V_hasPgFullPlannerHandleTime"
+ "TB,N,V_hasPgFullPlannerPostInferenceTime"
+ "TB,N,V_hasPgFullPlannerPreInferenceTime"
+ "TB,N,V_hasPgGeneratePlanContext"
+ "TB,N,V_hasPgModelIdentifier"
+ "TB,N,V_hasPgModelInferenceTime"
+ "TB,N,V_hasPgOverridesAssetVersion"
+ "TB,N,V_hasPgOverridesTime"
+ "TB,N,V_hasPgPlanGenTotalTime"
+ "TB,N,V_hasPgPrescribedPlanTime"
+ "TB,N,V_hasPlanGenerationTime"
+ "TB,N,V_hasPostItn1Best"
+ "TB,N,V_hasPostItnUtterance"
+ "TB,N,V_hasPostSearchTime"
+ "TB,N,V_hasPrTotalHandleTime"
+ "TB,N,V_hasPreSearchTime"
+ "TB,N,V_hasQueryDecorationContextRetrievalTime"
+ "TB,N,V_hasQueryDecorationFetchDynamicEnumerationTime"
+ "TB,N,V_hasQueryDecorationFullPlannerBlockingTime"
+ "TB,N,V_hasQueryDecorationHandleTime"
+ "TB,N,V_hasQueryDecorationID"
+ "TB,N,V_hasQueryDecorationInputCollectionTime"
+ "TB,N,V_hasQueryDecorationOutputBuildingTime"
+ "TB,N,V_hasQueryDecorationPrePlannerResult"
+ "TB,N,V_hasQueryDecorationRankingTime"
+ "TB,N,V_hasQueryDecorationSpanRetrievalTime"
+ "TB,N,V_hasQueryDecorationTime"
+ "TB,N,V_hasQueryDecorationToolRetrievalContextTime"
+ "TB,N,V_hasQueryDecorationToolRetrievalTime"
+ "TB,N,V_hasQueryDecorationTupleBuildingTime"
+ "TB,N,V_hasQueryDecorationTupleRankingTime"
+ "TB,N,V_hasResponseGenerationCacheManagerTime"
+ "TB,N,V_hasResponseGenerationCatalogTime"
+ "TB,N,V_hasResponseGenerationGMSCallTime"
+ "TB,N,V_hasResponseGenerationHallucinationDetectionTime"
+ "TB,N,V_hasResponseGenerationHandleTime"
+ "TB,N,V_hasResponseGenerationID"
+ "TB,N,V_hasResponseGenerationInferenceTime"
+ "TB,N,V_hasResponseGenerationOverrideTime"
+ "TB,N,V_hasResponseGenerationValidationTime"
+ "TB,N,V_hasReturnType"
+ "TB,N,V_hasSearchGlobalSearchTime"
+ "TB,N,V_hasSearchHallucinationTime"
+ "TB,N,V_hasSearchStartToGlobalSearchEnd"
+ "TB,N,V_hasSearchStartToSpotlightEnd"
+ "TB,N,V_hasSearchToolQueryTime"
+ "TB,N,V_hasSearchTotalHandleTime"
+ "TB,N,V_hasSelectedloggableUserIdHash"
+ "TB,N,V_hasSessionSummary"
+ "TB,N,V_hasSkipStatement"
+ "TB,N,V_hasSourceAuxKey"
+ "TB,N,V_hasStError"
+ "TB,N,V_hasStringQueryEntityMatcherTime"
+ "TB,N,V_hasStringQueryEntityTime"
+ "TB,N,V_hasStringQueryLocationTime"
+ "TB,N,V_hasStructuredSearch"
+ "TB,N,V_hasStructuredSearchParameterName"
+ "TB,N,V_hasSystemStyle"
+ "TB,N,V_hasToolboxSizeReported"
+ "TB,N,V_hasTranscriptShown"
+ "TB,N,V_hasTranscriptTapped"
+ "TB,N,V_hasTtaie"
+ "TB,N,V_hasUnableToCancel"
+ "TB,N,V_hasWantedToUndo"
+ "TB,N,V_isCrossDevice"
+ "TB,N,V_isDefaultApp"
+ "TB,N,V_isExpanded"
+ "TB,N,V_isLongLivedIDUploadDisabled"
+ "TB,N,V_isMailAppFocused"
+ "TB,N,V_isMediaPlaybackOn"
+ "TB,N,V_isNamedEntityPresentInSpeechProfile"
+ "TB,N,V_isNamedEntityPresentInVisualContext"
+ "TB,N,V_isPreLaunchExecuted"
+ "TB,N,V_isPredictionCorrect"
+ "TB,N,V_isRelationship"
+ "TB,N,V_isRequestByHandleType"
+ "TB,N,V_isRequestByLabel"
+ "TB,N,V_isRoot"
+ "TB,N,V_isSiriXFallback"
+ "TB,N,V_isUnnamedPhoneNumber"
+ "TB,N,V_pgOverridesMatched"
+ "TB,N,V_selectedAsAlternateSuggestion"
+ "TB,N,V_selectedAsPrimaryResponse"
+ "TB,N,V_shouldOpen"
+ "TB,N,V_speechStartPointDetected"
+ "TB,N,V_twoPassRecognizerUsed"
+ "TB,N,V_unableToCancel"
+ "TI,N,V_estimatedSizeInTokens"
+ "TI,N,V_lastCompletedPage"
+ "TI,N,V_lastOpenedPageNumber"
+ "TI,N,V_numAttempts"
+ "TI,N,V_numEntityErrors"
+ "TI,N,V_numTotalEdit"
+ "TI,N,V_numTotalEntities"
+ "TI,N,V_oneBestTranscriptLinkIndex"
+ "TI,N,V_originalAsrInterpretationIdx"
+ "TI,N,V_sizeInTokens"
+ "TI,N,V_sourceAuxIdx"
+ "TI,N,V_totalSizeInTokens"
+ "TI,N,V_totalToolCount"
+ "TI,N,V_trueCorrections"
+ "TI,N,V_trueRegressions"
+ "TQ,N,V_appIntentSessionId"
+ "TQ,N,V_creationTimestampInMsSince1970"
+ "TQ,N,V_responseTimeInNs"
+ "TQ,R,N,V_whichItemtype"
+ "TQ,R,N,V_whichOneof_Actionconfirmationsystemstyle"
+ "TRANSCRIPTSHOWNREASON_ALWAYS_SHOW"
+ "TRANSCRIPTSHOWNREASON_RECEIVED_SHOW_TRANSCRIPT_COMMAND"
+ "TRANSCRIPTSHOWNREASON_UNKNOWN"
+ "Td,N,V_retrievalTimeout"
+ "Tf,N,V_audioQueueLatencyInSecond"
+ "Tf,N,V_backgroundNoiseLevel"
+ "Tf,N,V_logOfTimeElapsedInSeconds"
+ "Tf,N,V_loudnessLevel"
+ "Tf,N,V_musicLoudnessLevel"
+ "Tf,N,V_signalToNoiseRatio"
+ "Tf,N,V_speakerSpeechLevel"
+ "Tf,N,V_ttsVolume"
+ "Tf,N,V_userIntentVolume"
+ "Ti,N,V_actionClass"
+ "Ti,N,V_alternateQuerySuggestionType"
+ "Ti,N,V_backgroundNoiseActivityLevel"
+ "Ti,N,V_bucketedDistance"
+ "Ti,N,V_componentType"
+ "Ti,N,V_endCharacterIdx"
+ "Ti,N,V_enrollmentResult"
+ "Ti,N,V_entityTaggerCategory"
+ "Ti,N,V_eventOrigin"
+ "Ti,N,V_executorSearchToolQueryType"
+ "Ti,N,V_maxEnrolled"
+ "Ti,N,V_maxEntityChars"
+ "Ti,N,V_maxEntityWords"
+ "Ti,N,V_payloadType"
+ "Ti,N,V_pgModelInterface"
+ "Ti,N,V_primitiveType"
+ "Ti,N,V_queryDecorationSource"
+ "Ti,N,V_rejectReason"
+ "Ti,N,V_requestTask"
+ "Ti,N,V_responseGenerationType"
+ "Ti,N,V_shimAction"
+ "Ti,N,V_speakerDistance"
+ "Ti,N,V_speechProfileCategory"
+ "Ti,N,V_startCharacterIdx"
+ "Ti,N,V_transcriptShownReason"
+ "Ti,N,V_userIntentType"
+ "Ti,N,V_voiceIdClassification"
+ "VOICENAME_ENAUC"
+ "VOICENAME_ENAUD"
+ "VOICENAME_FRFRC"
+ "VOICENAME_FRFRD"
+ "VOICENAME_ITITC"
+ "VOICENAME_ITITD"
+ "_actionClass"
+ "_actionParameterValues"
+ "_adaptiveSiriVolumeTTSVolumeQueried"
+ "_adaptiveSiriVolumeUserIntentDetected"
+ "_alignmentOffset"
+ "_alternateQuerySuggestionCandidateTier1s"
+ "_alternateQuerySuggestionTier1"
+ "_alternateQuerySuggestionType"
+ "_anonymizedLocationNameId"
+ "_anonymizedLocationTypeId"
+ "_appEntityQueryResponseTime"
+ "_appIntentSessionId"
+ "_appPreLaunchTriggered"
+ "_array"
+ "_asrFullPayloadCorrectedToUserEdit"
+ "_asrHypothesesInfos"
+ "_asrOutputToUserEdit"
+ "_asrScores"
+ "_audioFileResult"
+ "_audioQueueLatencyInSecond"
+ "_backgroundNoiseActivityLevel"
+ "_backgroundNoiseLevel"
+ "_bucketedDistance"
+ "_bucketedDistances"
+ "_callParameterName"
+ "_callers"
+ "_candidateA"
+ "_candidateB"
+ "_candidateBooleanMasks"
+ "_candidateRisks"
+ "_candidateTimeIntervalMatrixs"
+ "_componentType"
+ "_components"
+ "_contact"
+ "_contactName"
+ "_contextStatementIds"
+ "_contextStatementIdsReported"
+ "_contexts"
+ "_contextualEntityCollectionTriggered"
+ "_contextualEntityRetrievalContext"
+ "_contextualEntityStatementIds"
+ "_contextualReplayBiomeRecordCreated"
+ "_contextualReplayBiomeRecordDeleted"
+ "_correction"
+ "_corrections"
+ "_creationTimestampInMsSince1970"
+ "_didTriggerFirstPass"
+ "_domainExecutionAppIntentBundleID"
+ "_domainExecutionMetadata"
+ "_droppedComponents"
+ "_enabledTasks"
+ "_endCharacterIdx"
+ "_enrollmentResult"
+ "_entityScoreResults"
+ "_entityScores"
+ "_entityTaggerCategory"
+ "_errorDomainString"
+ "_estimatedSizeInTokens"
+ "_eventOrigin"
+ "_executorAppIntentHandleTime"
+ "_executorAppIntentQueryHandleTime"
+ "_executorIdentifierQueryCallContext"
+ "_executorPersonQueryCallContext"
+ "_executorSearchToolQueryCallContext"
+ "_executorSearchToolQueryType"
+ "_executorStringQueryEntityCallContext"
+ "_executorStringQueryEntityMatcherCallContext"
+ "_executorStringQueryLocationCallContext"
+ "_executors"
+ "_expensiveCellularDownloadRequested"
+ "_failedToConvertClientEvent"
+ "_flowContactTier1"
+ "_format"
+ "_fromPreSoftwareUpdateStaging"
+ "_fullPayloadCorrectionContext"
+ "_fullPayloadCorrectionExperimentContext"
+ "_fullPayloadCorrectionExperimentPostAnalysis"
+ "_fullPayloadCorrectionExperimentTier1"
+ "_fullPayloadCorrectorInput"
+ "_fullPayloadCorrectorOutput"
+ "_generativeAIEnablement"
+ "_grammar"
+ "_hasAdaptiveSiriVolumeTTSVolumeQueried"
+ "_hasAdaptiveSiriVolumeUserIntentDetected"
+ "_hasAlignmentOffset"
+ "_hasAlternateQuerySuggestionTier1"
+ "_hasAnonymizedLocationNameId"
+ "_hasAnonymizedLocationTypeId"
+ "_hasAppEntityQueryResponseTime"
+ "_hasAppPreLaunchTriggered"
+ "_hasArray"
+ "_hasAsrFullPayloadCorrectedToUserEdit"
+ "_hasAsrOutputToUserEdit"
+ "_hasAudioFileResult"
+ "_hasCallParameterName"
+ "_hasCandidateA"
+ "_hasCandidateB"
+ "_hasContact"
+ "_hasContactName"
+ "_hasContextStatementIdsReported"
+ "_hasContextualEntityCollectionTriggered"
+ "_hasContextualEntityRetrievalContext"
+ "_hasContextualReplayBiomeRecordCreated"
+ "_hasContextualReplayBiomeRecordDeleted"
+ "_hasCorrection"
+ "_hasDomainExecutionAppIntentBundleID"
+ "_hasDomainExecutionMetadata"
+ "_hasErrorDomainString"
+ "_hasExecutorAppIntentHandleTime"
+ "_hasExecutorAppIntentQueryHandleTime"
+ "_hasExecutorIdentifierQueryCallContext"
+ "_hasExecutorPersonQueryCallContext"
+ "_hasExecutorSearchToolQueryCallContext"
+ "_hasExecutorStringQueryEntityCallContext"
+ "_hasExecutorStringQueryEntityMatcherCallContext"
+ "_hasExecutorStringQueryLocationCallContext"
+ "_hasFailedToConvertClientEvent"
+ "_hasFlowContactTier1"
+ "_hasFormat"
+ "_hasFullPayloadCorrectionContext"
+ "_hasFullPayloadCorrectionExperimentContext"
+ "_hasFullPayloadCorrectionExperimentPostAnalysis"
+ "_hasFullPayloadCorrectionExperimentTier1"
+ "_hasFullPayloadCorrectorInput"
+ "_hasFullPayloadCorrectorOutput"
+ "_hasGenerativeAIEnablement"
+ "_hasGrammar"
+ "_hasIdentifierQueryTime"
+ "_hasIdx"
+ "_hasInfoTier1"
+ "_hasIntelligenceFlowRequestContext"
+ "_hasLoggableUserIdHash"
+ "_hasNlRouterPromptGenerated"
+ "_hasOriginal"
+ "_hasOverrideMetadata"
+ "_hasOverridesMatched"
+ "_hasPegasusAsrCorrectionInfo"
+ "_hasPersonQueryTime"
+ "_hasPersonalizationUserEditNamedEntityMetrics"
+ "_hasPgFullPlannerHandleTime"
+ "_hasPgFullPlannerPostInferenceTime"
+ "_hasPgFullPlannerPreInferenceTime"
+ "_hasPgGeneratePlanContext"
+ "_hasPgModelIdentifier"
+ "_hasPgModelInferenceTime"
+ "_hasPgOverridesAssetVersion"
+ "_hasPgOverridesTime"
+ "_hasPgPlanGenTotalTime"
+ "_hasPgPrescribedPlanTime"
+ "_hasPlanGenerationTime"
+ "_hasPostItn1Best"
+ "_hasPostItnUtterance"
+ "_hasPostSearchTime"
+ "_hasPrTotalHandleTime"
+ "_hasPreSearchTime"
+ "_hasQueryDecorationContextRetrievalTime"
+ "_hasQueryDecorationFetchDynamicEnumerationTime"
+ "_hasQueryDecorationFullPlannerBlockingTime"
+ "_hasQueryDecorationHandleTime"
+ "_hasQueryDecorationID"
+ "_hasQueryDecorationInputCollectionTime"
+ "_hasQueryDecorationOutputBuildingTime"
+ "_hasQueryDecorationPrePlannerResult"
+ "_hasQueryDecorationRankingTime"
+ "_hasQueryDecorationSpanRetrievalTime"
+ "_hasQueryDecorationTime"
+ "_hasQueryDecorationToolRetrievalContextTime"
+ "_hasQueryDecorationToolRetrievalTime"
+ "_hasQueryDecorationTupleBuildingTime"
+ "_hasQueryDecorationTupleRankingTime"
+ "_hasResponseGenerationCacheManagerTime"
+ "_hasResponseGenerationCatalogTime"
+ "_hasResponseGenerationGMSCallTime"
+ "_hasResponseGenerationHallucinationDetectionTime"
+ "_hasResponseGenerationHandleTime"
+ "_hasResponseGenerationID"
+ "_hasResponseGenerationInferenceTime"
+ "_hasResponseGenerationOverrideTime"
+ "_hasResponseGenerationValidationTime"
+ "_hasReturnType"
+ "_hasSearchGlobalSearchTime"
+ "_hasSearchHallucinationTime"
+ "_hasSearchStartToGlobalSearchEnd"
+ "_hasSearchStartToSpotlightEnd"
+ "_hasSearchToolQueryTime"
+ "_hasSearchTotalHandleTime"
+ "_hasSelectedloggableUserIdHash"
+ "_hasSessionSummary"
+ "_hasSkipStatement"
+ "_hasSourceAuxKey"
+ "_hasStError"
+ "_hasStringQueryEntityMatcherTime"
+ "_hasStringQueryEntityTime"
+ "_hasStringQueryLocationTime"
+ "_hasStructuredSearch"
+ "_hasStructuredSearchParameterName"
+ "_hasSystemStyle"
+ "_hasToolboxSizeReported"
+ "_hasTranscriptShown"
+ "_hasTranscriptTapped"
+ "_hasTtaie"
+ "_hasUnableToCancel"
+ "_hasWantedToUndo"
+ "_historicalLocationContexts"
+ "_identifierQueryTime"
+ "_idx"
+ "_infoTier1"
+ "_intelligenceFlowRequestContext"
+ "_intervalUntilStartTimes"
+ "_isApplicableToCandidates"
+ "_isCrossDevice"
+ "_isDefaultApp"
+ "_isExpanded"
+ "_isLongLivedIDUploadDisabled"
+ "_isMailAppFocused"
+ "_isMediaPlaybackOn"
+ "_isNamedEntityPresentInSpeechProfile"
+ "_isNamedEntityPresentInVisualContext"
+ "_isPreLaunchExecuted"
+ "_isPredictionCorrect"
+ "_isRelationship"
+ "_isRequestByHandleType"
+ "_isRequestByLabel"
+ "_isRoot"
+ "_isSiriXFallback"
+ "_isUnnamedPhoneNumber"
+ "_jrEntitySimilarityScores"
+ "_lastCompletedPage"
+ "_lastOpenedPageNumber"
+ "_lmeOverActivationEdits"
+ "_logOfIntervalUntilStartTimeInSeconds"
+ "_logOfTimeElapsedInSeconds"
+ "_loggableUserIdHash"
+ "_loudnessLevel"
+ "_maxEnrolled"
+ "_maxEntityChars"
+ "_maxEntityWords"
+ "_musicLoudnessLevel"
+ "_namedEntityUserEdits"
+ "_nlRouterPromptGenerated"
+ "_numAttempts"
+ "_numEntityErrors"
+ "_numTotalEdit"
+ "_numTotalEntities"
+ "_oneBestTranscriptLinkIndex"
+ "_oneBestTranscripts"
+ "_original"
+ "_originalAsrInterpretationIdx"
+ "_overrideMetadata"
+ "_overridesMatched"
+ "_pageAttempts"
+ "_parameterSubTypes"
+ "_payloadType"
+ "_pegasusAsrCorrectionInfo"
+ "_personQueryTime"
+ "_personalizationUserEditNamedEntityMetrics"
+ "_pgFullPlannerHandleTime"
+ "_pgFullPlannerPostInferenceTime"
+ "_pgFullPlannerPreInferenceTime"
+ "_pgGeneratePlanContext"
+ "_pgModelIdentifier"
+ "_pgModelInferenceTime"
+ "_pgModelInterface"
+ "_pgOverridesAssetVersion"
+ "_pgOverridesMatched"
+ "_pgOverridesTime"
+ "_pgPlanGenTotalTime"
+ "_pgPrescribedPlanTime"
+ "_planGenerationTime"
+ "_planGenerations"
+ "_planResolutions"
+ "_postItn1Best"
+ "_postItnUtterance"
+ "_postSearchTime"
+ "_prTotalHandleTime"
+ "_preSearchTime"
+ "_primitiveType"
+ "_queryDecorationContextRetrievalTime"
+ "_queryDecorationFetchDynamicEnumerationTime"
+ "_queryDecorationFullPlannerBlockingTime"
+ "_queryDecorationHandleTime"
+ "_queryDecorationID"
+ "_queryDecorationInputCollectionTime"
+ "_queryDecorationOutputBuildingTime"
+ "_queryDecorationPrePlannerResult"
+ "_queryDecorationRankingTime"
+ "_queryDecorationSource"
+ "_queryDecorationSpanRetrievalTime"
+ "_queryDecorationTime"
+ "_queryDecorationToolRetrievalContextTime"
+ "_queryDecorationToolRetrievalTime"
+ "_queryDecorationTupleBuildingTime"
+ "_queryDecorationTupleRankingTime"
+ "_queryDecorations"
+ "_rejectReason"
+ "_rejectedContextTypes"
+ "_rejectedEntityTypes"
+ "_requestFeatureTags"
+ "_requestTask"
+ "_responseGenerationCacheManagerTime"
+ "_responseGenerationCatalogTime"
+ "_responseGenerationGMSCallTime"
+ "_responseGenerationHallucinationDetectionTime"
+ "_responseGenerationHandleTime"
+ "_responseGenerationID"
+ "_responseGenerationInferenceTime"
+ "_responseGenerationOverrideTime"
+ "_responseGenerationType"
+ "_responseGenerationValidationTime"
+ "_responseGenerations"
+ "_responseTimeInNs"
+ "_retrievalTimeout"
+ "_retrievedEntityStates"
+ "_returnType"
+ "_riskLevels"
+ "_rows"
+ "_searchGlobalSearchTime"
+ "_searchHallucinationTime"
+ "_searchStartToGlobalSearchEnd"
+ "_searchStartToSpotlightEnd"
+ "_searchToolQueryTime"
+ "_searchToolRanks"
+ "_searchTotalHandleTime"
+ "_searchs"
+ "_selectedAsAlternateSuggestion"
+ "_selectedAsPrimaryResponse"
+ "_selectedloggableUserIdHash"
+ "_sessionSummary"
+ "_shimAction"
+ "_shouldOpen"
+ "_signalToNoiseRatio"
+ "_sizeInTokens"
+ "_skipStatement"
+ "_sourceAuxIdx"
+ "_sourceAuxKey"
+ "_speakerDistance"
+ "_speakerSpeechLevel"
+ "_speechProfileCategories"
+ "_speechProfileCategory"
+ "_speechStartPointDetected"
+ "_stError"
+ "_startCharacterIdx"
+ "_stringQueryEntityMatcherTime"
+ "_stringQueryEntityTime"
+ "_stringQueryLocationTime"
+ "_structuredSearch"
+ "_structuredSearchParameterName"
+ "_systemStyle"
+ "_toolboxSizeReported"
+ "_totalSizeInTokens"
+ "_totalToolCount"
+ "_transcriptShown"
+ "_transcriptShownReason"
+ "_transcriptTapped"
+ "_trueCorrections"
+ "_trueRegressions"
+ "_ttaie"
+ "_ttsVolume"
+ "_twoPassRecognizerUsed"
+ "_unableToCancel"
+ "_userIntentType"
+ "_userIntentVolume"
+ "_visualContextCategories"
+ "_voiceIdClassification"
+ "_voiceIdScores"
+ "_wantedToUndo"
+ "_whichItemtype"
+ "_whichOneof_Actionconfirmationsystemstyle"
+ "actionClass"
+ "actionParameterValues"
+ "actionParameterValuesAtIndex:"
+ "actionParameterValuesCount"
+ "adaptiveSiriVolumeTTSVolumeQueried"
+ "adaptiveSiriVolumeUserIntentDetected"
+ "addActionParameterValues:"
+ "addAlternateQuerySuggestionCandidateTier1:"
+ "addAsrHypothesesInfo:"
+ "addAsrScores:"
+ "addBucketedDistance:"
+ "addCallers:"
+ "addCandidateBooleanMask:"
+ "addCandidateRisk:"
+ "addCandidateTimeIntervalMatrix:"
+ "addComponents:"
+ "addContext:"
+ "addContextStatementIds:"
+ "addContextualEntityStatementIds:"
+ "addCorrections:"
+ "addDroppedComponents:"
+ "addEnabledTasks:"
+ "addEntityScoreResults:"
+ "addEntityScores:"
+ "addExecutor:"
+ "addHistoricalLocationContext:"
+ "addIntervalUntilStartTime:"
+ "addIsApplicableToCandidate:"
+ "addJrEntitySimilarityScores:"
+ "addLmeOverActivationEdits:"
+ "addLogOfIntervalUntilStartTimeInSeconds:"
+ "addNamedEntityUserEdits:"
+ "addOneBestTranscripts:"
+ "addPageAttempts:"
+ "addParameterSubType:"
+ "addPlanGeneration:"
+ "addPlanResolution:"
+ "addQueryDecoration:"
+ "addRejectedContextTypes:"
+ "addRejectedEntityTypes:"
+ "addRequestFeatureTag:"
+ "addResponseGeneration:"
+ "addRetrievedEntityStates:"
+ "addRiskLevel:"
+ "addRow:"
+ "addSearch:"
+ "addSearchToolRank:"
+ "addSearchToolRanks:"
+ "addSpeechProfileCategories:"
+ "addStatementId:"
+ "addVisualContextCategories:"
+ "addVoiceIdScores:"
+ "alignmentOffset"
+ "alternateQuerySuggestionCandidateTier1"
+ "alternateQuerySuggestionCandidateTier1AtIndex:"
+ "alternateQuerySuggestionCandidateTier1Count"
+ "alternateQuerySuggestionCandidateTier1s"
+ "alternateQuerySuggestionTier1"
+ "alternateQuerySuggestionType"
+ "anonymizedLocationNameId"
+ "anonymizedLocationTypeId"
+ "appEntityQueryResponseTime"
+ "appIntentSessionId"
+ "appPreLaunchTriggered"
+ "asrFullPayloadCorrectedToUserEdit"
+ "asrHypothesesInfo"
+ "asrHypothesesInfoAtIndex:"
+ "asrHypothesesInfoCount"
+ "asrHypothesesInfos"
+ "asrOutputToUserEdit"
+ "asrScores"
+ "asrScoresAtIndex:"
+ "asrScoresCount"
+ "audioFileResult"
+ "audioFileResultTier1.oneBestTranscripts.postItn"
+ "audioFileResultTier1.oneBestTranscripts.rawRecognition"
+ "audioQueueLatencyInSecond"
+ "backgroundNoiseActivityLevel"
+ "backgroundNoiseLevel"
+ "bucketedDistance"
+ "bucketedDistanceAtIndex:"
+ "bucketedDistanceCount"
+ "bucketedDistances"
+ "callParameterName"
+ "callers"
+ "callersAtIndex:"
+ "callersCount"
+ "candidateA"
+ "candidateB"
+ "candidateBooleanMask"
+ "candidateBooleanMaskAtIndex:"
+ "candidateBooleanMaskCount"
+ "candidateBooleanMasks"
+ "candidateRisk"
+ "candidateRiskAtIndex:"
+ "candidateRiskCount"
+ "candidateRisks"
+ "candidateTimeIntervalMatrix"
+ "candidateTimeIntervalMatrixAtIndex:"
+ "candidateTimeIntervalMatrixCount"
+ "candidateTimeIntervalMatrixs"
+ "clearActionParameterValues"
+ "clearAlternateQuerySuggestionCandidateTier1"
+ "clearAsrHypothesesInfo"
+ "clearAsrScores"
+ "clearBucketedDistance"
+ "clearCallers"
+ "clearCandidateBooleanMask"
+ "clearCandidateRisk"
+ "clearCandidateTimeIntervalMatrix"
+ "clearComponents"
+ "clearContext"
+ "clearContextStatementIds"
+ "clearContextualEntityStatementIds"
+ "clearCorrections"
+ "clearDroppedComponents"
+ "clearEnabledTasks"
+ "clearEntityScoreResults"
+ "clearEntityScores"
+ "clearExecutor"
+ "clearHistoricalLocationContext"
+ "clearIntervalUntilStartTime"
+ "clearIsApplicableToCandidate"
+ "clearJrEntitySimilarityScores"
+ "clearLmeOverActivationEdits"
+ "clearLogOfIntervalUntilStartTimeInSeconds"
+ "clearNamedEntityUserEdits"
+ "clearOneBestTranscripts"
+ "clearPageAttempts"
+ "clearParameterSubType"
+ "clearPlanGeneration"
+ "clearPlanResolution"
+ "clearQueryDecoration"
+ "clearRejectedContextTypes"
+ "clearRejectedEntityTypes"
+ "clearRequestFeatureTag"
+ "clearResponseGeneration"
+ "clearRetrievedEntityStates"
+ "clearRiskLevel"
+ "clearRow"
+ "clearSearch"
+ "clearSearchToolRank"
+ "clearSearchToolRanks"
+ "clearSpeechProfileCategories"
+ "clearStatementId"
+ "clearVisualContextCategories"
+ "clearVoiceIdScores"
+ "com.apple.aiml.siri.asr.ASRClientEvent.ASRContextualEntityCollectionTriggered"
+ "com.apple.aiml.siri.asr.ASRClientEvent.ASRContextualEntityRetrievalContext"
+ "com.apple.aiml.siri.asr.ASRClientEvent.ASRPersonalizationUserEditNamedEntityMetrics"
+ "com.apple.aiml.siri.dodml.DODMLClientEvent.DODMLASRContextualReplayBiomeRecordCreated"
+ "com.apple.aiml.siri.dodml.DODMLClientEvent.DODMLASRContextualReplayBiomeRecordDeleted"
+ "com.apple.aiml.siri.dodml.DODMLClientEvent.DODMLASRFullPayloadCorrectionExperimentContext"
+ "com.apple.aiml.siri.dodml.DODMLClientEvent.DODMLASRFullPayloadCorrectionExperimentInfoTier1"
+ "com.apple.aiml.siri.dodml.DODMLClientEvent.DODMLASRFullPayloadCorrectionExperimentPostAnalysis"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorIdentifierQueryCallContext"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorPersonQueryCallContext"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorSearchToolQueryCallContext"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorStringQueryEntityCallContext"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorStringQueryEntityMatcherCallContext"
+ "com.apple.aiml.siri.executor.ExecutorClientEvent.ExecutorStringQueryLocationCallContext"
+ "com.apple.aiml.siri.flow.FLOWClientEvent.FLOWContactTier1"
+ "com.apple.aiml.siri.ift.IFTClientEvent.IFTQueryDecorationPrePlannerResult"
+ "com.apple.aiml.siri.ift.IFTClientEvent.IFTSkipStatement"
+ "com.apple.aiml.siri.mh.MHClientEvent.MHAdaptiveSiriVolumeTTSVolumeQueried"
+ "com.apple.aiml.siri.mh.MHClientEvent.MHAdaptiveSiriVolumeUserIntentDetected"
+ "com.apple.aiml.siri.nlrouter.NLRouterClientEvent.NLRouterPromptGenerated"
+ "com.apple.aiml.siri.orch.ORCHClientEvent.ORCHAudioTopologyReported"
+ "com.apple.aiml.siri.orch.ORCHClientEvent.ORCHIntelligenceFlowRequestContext"
+ "com.apple.aiml.siri.pegasus.PEGASUSServerEvent.PEGASUSAsrCorrectionInfo"
+ "com.apple.aiml.siri.pg.PGClientEvent.PGGeneratePlanContext"
+ "com.apple.aiml.siri.qd.QDClientEvent.QDAppPreLaunchTriggered"
+ "com.apple.aiml.siri.qd.QDClientEvent.QDContextStatementIdsReported"
+ "com.apple.aiml.siri.qd.QDClientEvent.QDToolboxSizeReported"
+ "com.apple.aiml.siri.setup.SIRISETUPClientEvent.SIRISETUPPHSEnrollmentSessionSummary"
+ "com.apple.aiml.siri.uei.ClientEvent.UEITranscriptShown"
+ "com.apple.aiml.siri.uei.ClientEvent.UEITranscriptTapped"
+ "componentType"
+ "components"
+ "componentsAtIndex:"
+ "componentsCount"
+ "contact"
+ "contactName"
+ "contextAtIndex:"
+ "contextCount"
+ "contextStatementIds"
+ "contextStatementIdsAtIndex:"
+ "contextStatementIdsCount"
+ "contextStatementIdsReported"
+ "contexts"
+ "contextualEntityCollectionTriggered"
+ "contextualEntityRetrievalContext"
+ "contextualEntityRetrievalContext.ended.retrievedEntityStates.entityType.bundleId"
+ "contextualEntityRetrievalContext.startedOrChanged.rejectedEntityTypes.bundleId"
+ "contextualEntityStatementIds"
+ "contextualEntityStatementIdsAtIndex:"
+ "contextualEntityStatementIdsCount"
+ "contextualReplayBiomeRecordCreated"
+ "contextualReplayBiomeRecordDeleted"
+ "correction"
+ "corrections"
+ "correctionsAtIndex:"
+ "correctionsCount"
+ "creationTimestampInMsSince1970"
+ "deleteActionClass"
+ "deleteActionParameterValues"
+ "deleteAdaptiveSiriVolumeTTSVolumeQueried"
+ "deleteAdaptiveSiriVolumeUserIntentDetected"
+ "deleteAlignmentOffset"
+ "deleteAlternateQuerySuggestionCandidateTier1"
+ "deleteAlternateQuerySuggestionTier1"
+ "deleteAlternateQuerySuggestionType"
+ "deleteAnonymizedLocationNameId"
+ "deleteAnonymizedLocationTypeId"
+ "deleteAppEntityQueryResponseTime"
+ "deleteAppIntentSessionId"
+ "deleteAppPreLaunchTriggered"
+ "deleteArray"
+ "deleteAsrFullPayloadCorrectedToUserEdit"
+ "deleteAsrHypothesesInfo"
+ "deleteAsrOutputToUserEdit"
+ "deleteAsrScores"
+ "deleteAudioFileResult"
+ "deleteAudioQueueLatencyInSecond"
+ "deleteBackgroundNoiseActivityLevel"
+ "deleteBackgroundNoiseLevel"
+ "deleteBucketedDistance"
+ "deleteCallParameterName"
+ "deleteCallers"
+ "deleteCandidateA"
+ "deleteCandidateB"
+ "deleteCandidateBooleanMask"
+ "deleteCandidateRisk"
+ "deleteCandidateTimeIntervalMatrix"
+ "deleteComponentType"
+ "deleteComponents"
+ "deleteContact"
+ "deleteContactName"
+ "deleteContextStatementIds"
+ "deleteContextStatementIdsReported"
+ "deleteContextualEntityCollectionTriggered"
+ "deleteContextualEntityRetrievalContext"
+ "deleteContextualEntityStatementIds"
+ "deleteContextualReplayBiomeRecordCreated"
+ "deleteContextualReplayBiomeRecordDeleted"
+ "deleteCorrection"
+ "deleteCorrections"
+ "deleteCreationTimestampInMsSince1970"
+ "deleteDidTriggerFirstPass"
+ "deleteDomainExecutionAppIntentBundleID"
+ "deleteDomainExecutionMetadata"
+ "deleteDroppedComponents"
+ "deleteEnabledTasks"
+ "deleteEndCharacterIdx"
+ "deleteEnrollmentResult"
+ "deleteEntityScoreResults"
+ "deleteEntityScores"
+ "deleteEntityTaggerCategory"
+ "deleteErrorDomainString"
+ "deleteEstimatedSizeInTokens"
+ "deleteEventOrigin"
+ "deleteExecutor"
+ "deleteExecutorAppIntentHandleTime"
+ "deleteExecutorAppIntentQueryHandleTime"
+ "deleteExecutorIdentifierQueryCallContext"
+ "deleteExecutorPersonQueryCallContext"
+ "deleteExecutorSearchToolQueryCallContext"
+ "deleteExecutorSearchToolQueryType"
+ "deleteExecutorStringQueryEntityCallContext"
+ "deleteExecutorStringQueryEntityMatcherCallContext"
+ "deleteExecutorStringQueryLocationCallContext"
+ "deleteExpensiveCellularDownloadRequested"
+ "deleteFailedToConvertClientEvent"
+ "deleteFlowContactTier1"
+ "deleteFormat"
+ "deleteFromPreSoftwareUpdateStaging"
+ "deleteFullPayloadCorrectionContext"
+ "deleteFullPayloadCorrectionExperimentContext"
+ "deleteFullPayloadCorrectionExperimentPostAnalysis"
+ "deleteFullPayloadCorrectionExperimentTier1"
+ "deleteFullPayloadCorrectorInput"
+ "deleteFullPayloadCorrectorOutput"
+ "deleteGenerativeAIEnablement"
+ "deleteGrammar"
+ "deleteHistoricalLocationContext"
+ "deleteIdentifierQueryTime"
+ "deleteIdx"
+ "deleteInfoTier1"
+ "deleteIntelligenceFlowRequestContext"
+ "deleteIntervalUntilStartTime"
+ "deleteIsApplicableToCandidate"
+ "deleteIsCrossDevice"
+ "deleteIsDefaultApp"
+ "deleteIsExpanded"
+ "deleteIsLongLivedIDUploadDisabled"
+ "deleteIsMailAppFocused"
+ "deleteIsMediaPlaybackOn"
+ "deleteIsNamedEntityPresentInSpeechProfile"
+ "deleteIsNamedEntityPresentInVisualContext"
+ "deleteIsPreLaunchExecuted"
+ "deleteIsPredictionCorrect"
+ "deleteIsRelationship"
+ "deleteIsRequestByHandleType"
+ "deleteIsRequestByLabel"
+ "deleteIsRoot"
+ "deleteIsSiriXFallback"
+ "deleteIsUnnamedPhoneNumber"
+ "deleteJrEntitySimilarityScores"
+ "deleteLastCompletedPage"
+ "deleteLastOpenedPageNumber"
+ "deleteLmeOverActivationEdits"
+ "deleteLogOfIntervalUntilStartTimeInSeconds"
+ "deleteLogOfTimeElapsedInSeconds"
+ "deleteLoggableUserIdHash"
+ "deleteLoudnessLevel"
+ "deleteMaxEnrolled"
+ "deleteMaxEntityChars"
+ "deleteMaxEntityWords"
+ "deleteMusicLoudnessLevel"
+ "deleteNamedEntityUserEdits"
+ "deleteNlRouterPromptGenerated"
+ "deleteNumAttempts"
+ "deleteNumEntityErrors"
+ "deleteNumTotalEdit"
+ "deleteNumTotalEntities"
+ "deleteOneBestTranscriptLinkIndex"
+ "deleteOneBestTranscripts"
+ "deleteOriginal"
+ "deleteOriginalAsrInterpretationIdx"
+ "deleteOverrideMetadata"
+ "deleteOverridesMatched"
+ "deletePageAttempts"
+ "deleteParameterSubType"
+ "deletePayloadType"
+ "deletePegasusAsrCorrectionInfo"
+ "deletePersonQueryTime"
+ "deletePersonalizationUserEditNamedEntityMetrics"
+ "deletePgFullPlannerHandleTime"
+ "deletePgFullPlannerPostInferenceTime"
+ "deletePgFullPlannerPreInferenceTime"
+ "deletePgGeneratePlanContext"
+ "deletePgModelIdentifier"
+ "deletePgModelInferenceTime"
+ "deletePgModelInterface"
+ "deletePgOverridesAssetVersion"
+ "deletePgOverridesMatched"
+ "deletePgOverridesTime"
+ "deletePgPlanGenTotalTime"
+ "deletePgPrescribedPlanTime"
+ "deletePlanGeneration"
+ "deletePlanGenerationTime"
+ "deletePlanResolution"
+ "deletePostItn1Best"
+ "deletePostItnUtterance"
+ "deletePostSearchTime"
+ "deletePrTotalHandleTime"
+ "deletePreSearchTime"
+ "deletePrimitiveType"
+ "deleteQueryDecoration"
+ "deleteQueryDecorationContextRetrievalTime"
+ "deleteQueryDecorationFetchDynamicEnumerationTime"
+ "deleteQueryDecorationFullPlannerBlockingTime"
+ "deleteQueryDecorationHandleTime"
+ "deleteQueryDecorationID"
+ "deleteQueryDecorationInputCollectionTime"
+ "deleteQueryDecorationOutputBuildingTime"
+ "deleteQueryDecorationPrePlannerResult"
+ "deleteQueryDecorationRankingTime"
+ "deleteQueryDecorationSource"
+ "deleteQueryDecorationSpanRetrievalTime"
+ "deleteQueryDecorationTime"
+ "deleteQueryDecorationToolRetrievalContextTime"
+ "deleteQueryDecorationToolRetrievalTime"
+ "deleteQueryDecorationTupleBuildingTime"
+ "deleteQueryDecorationTupleRankingTime"
+ "deleteRejectReason"
+ "deleteRejectedContextTypes"
+ "deleteRejectedEntityTypes"
+ "deleteRequestFeatureTag"
+ "deleteRequestTask"
+ "deleteResponseGeneration"
+ "deleteResponseGenerationCacheManagerTime"
+ "deleteResponseGenerationCatalogTime"
+ "deleteResponseGenerationGMSCallTime"
+ "deleteResponseGenerationHallucinationDetectionTime"
+ "deleteResponseGenerationHandleTime"
+ "deleteResponseGenerationID"
+ "deleteResponseGenerationInferenceTime"
+ "deleteResponseGenerationOverrideTime"
+ "deleteResponseGenerationType"
+ "deleteResponseGenerationValidationTime"
+ "deleteResponseTimeInNs"
+ "deleteRetrievalTimeout"
+ "deleteRetrievedEntityStates"
+ "deleteReturnType"
+ "deleteRiskLevel"
+ "deleteRow"
+ "deleteSearchGlobalSearchTime"
+ "deleteSearchHallucinationTime"
+ "deleteSearchStartToGlobalSearchEnd"
+ "deleteSearchStartToSpotlightEnd"
+ "deleteSearchToolQueryTime"
+ "deleteSearchToolRank"
+ "deleteSearchToolRanks"
+ "deleteSearchTotalHandleTime"
+ "deleteSelectedAsAlternateSuggestion"
+ "deleteSelectedAsPrimaryResponse"
+ "deleteSelectedloggableUserIdHash"
+ "deleteSessionSummary"
+ "deleteShimAction"
+ "deleteShouldOpen"
+ "deleteSignalToNoiseRatio"
+ "deleteSizeInTokens"
+ "deleteSkipStatement"
+ "deleteSourceAuxIdx"
+ "deleteSourceAuxKey"
+ "deleteSpeakerDistance"
+ "deleteSpeakerSpeechLevel"
+ "deleteSpeechProfileCategories"
+ "deleteSpeechProfileCategory"
+ "deleteSpeechStartPointDetected"
+ "deleteStError"
+ "deleteStartCharacterIdx"
+ "deleteStringQueryEntityMatcherTime"
+ "deleteStringQueryEntityTime"
+ "deleteStringQueryLocationTime"
+ "deleteStructuredSearch"
+ "deleteStructuredSearchParameterName"
+ "deleteSystemStyle"
+ "deleteToolboxSizeReported"
+ "deleteTotalSizeInTokens"
+ "deleteTotalToolCount"
+ "deleteTranscriptShown"
+ "deleteTranscriptShownReason"
+ "deleteTranscriptTapped"
+ "deleteTrueCorrections"
+ "deleteTrueRegressions"
+ "deleteTtaie"
+ "deleteTtsVolume"
+ "deleteTwoPassRecognizerUsed"
+ "deleteUnableToCancel"
+ "deleteUserIntentType"
+ "deleteUserIntentVolume"
+ "deleteVisualContextCategories"
+ "deleteVoiceIdClassification"
+ "deleteVoiceIdScores"
+ "deleteWantedToUndo"
+ "didTriggerFirstPass"
+ "domainExecutionAppIntentBundleID"
+ "domainExecutionMetadata"
+ "droppedComponents"
+ "droppedComponentsAtIndex:"
+ "droppedComponentsCount"
+ "enabledTasks"
+ "enabledTasksAtIndex:"
+ "enabledTasksCount"
+ "endCharacterIdx"
+ "enrollmentResult"
+ "entitiesCollected.contexts.valueType.bundleId"
+ "entityScoreResults"
+ "entityScoreResultsAtIndex:"
+ "entityScoreResultsCount"
+ "entityScores"
+ "entityScoresAtIndex:"
+ "entityScoresCount"
+ "entityTaggerCategory"
+ "errorDomainString"
+ "estimatedSizeInTokens"
+ "eventOrigin"
+ "executor"
+ "executorAppIntentHandleTime"
+ "executorAppIntentQueryHandleTime"
+ "executorAtIndex:"
+ "executorCount"
+ "executorIdentifierQueryCallContext"
+ "executorPersonQueryCallContext"
+ "executorSearchToolQueryCallContext"
+ "executorSearchToolQueryType"
+ "executorStringQueryEntityCallContext"
+ "executorStringQueryEntityMatcherCallContext"
+ "executorStringQueryLocationCallContext"
+ "executors"
+ "expensiveCellularDownloadRequested"
+ "failedToConvertClientEvent"
+ "flowContactTier1"
+ "flowContactTier1.contactName"
+ "flowDomainExecutionContext.startedOrChanged.domainExecutionMetadata.domainExecutionAppIntentBundleID"
+ "format"
+ "fromPreSoftwareUpdateStaging"
+ "fullPayloadCorrectionContext"
+ "fullPayloadCorrectionExperimentContext"
+ "fullPayloadCorrectionExperimentPostAnalysis"
+ "fullPayloadCorrectionExperimentTier1"
+ "fullPayloadCorrectionExperimentTier1.infoTier1.fullPayloadCorrectorInput"
+ "fullPayloadCorrectionExperimentTier1.infoTier1.fullPayloadCorrectorOutput"
+ "fullPayloadCorrectorInput"
+ "fullPayloadCorrectorOutput"
+ "generativeAIEnablement"
+ "grammar"
+ "hasActionClass"
+ "hasAdaptiveSiriVolumeTTSVolumeQueried"
+ "hasAdaptiveSiriVolumeUserIntentDetected"
+ "hasAlignmentOffset"
+ "hasAlternateQuerySuggestionTier1"
+ "hasAlternateQuerySuggestionType"
+ "hasAnonymizedLocationNameId"
+ "hasAnonymizedLocationTypeId"
+ "hasAppEntityQueryResponseTime"
+ "hasAppIntentSessionId"
+ "hasAppPreLaunchTriggered"
+ "hasArray"
+ "hasAsrFullPayloadCorrectedToUserEdit"
+ "hasAsrOutputToUserEdit"
+ "hasAudioFileResult"
+ "hasAudioQueueLatencyInSecond"
+ "hasBackgroundNoiseActivityLevel"
+ "hasBackgroundNoiseLevel"
+ "hasBucketedDistance"
+ "hasCallParameterName"
+ "hasCandidateA"
+ "hasCandidateB"
+ "hasComponentType"
+ "hasContact"
+ "hasContactName"
+ "hasContextStatementIdsReported"
+ "hasContextualEntityCollectionTriggered"
+ "hasContextualEntityRetrievalContext"
+ "hasContextualReplayBiomeRecordCreated"
+ "hasContextualReplayBiomeRecordDeleted"
+ "hasCorrection"
+ "hasCreationTimestampInMsSince1970"
+ "hasDidTriggerFirstPass"
+ "hasDomainExecutionAppIntentBundleID"
+ "hasDomainExecutionMetadata"
+ "hasEndCharacterIdx"
+ "hasEnrollmentResult"
+ "hasEntityTaggerCategory"
+ "hasErrorDomainString"
+ "hasEstimatedSizeInTokens"
+ "hasEventOrigin"
+ "hasExecutorAppIntentHandleTime"
+ "hasExecutorAppIntentQueryHandleTime"
+ "hasExecutorIdentifierQueryCallContext"
+ "hasExecutorPersonQueryCallContext"
+ "hasExecutorSearchToolQueryCallContext"
+ "hasExecutorSearchToolQueryType"
+ "hasExecutorStringQueryEntityCallContext"
+ "hasExecutorStringQueryEntityMatcherCallContext"
+ "hasExecutorStringQueryLocationCallContext"
+ "hasExpensiveCellularDownloadRequested"
+ "hasFailedToConvertClientEvent"
+ "hasFlowContactTier1"
+ "hasFormat"
+ "hasFromPreSoftwareUpdateStaging"
+ "hasFullPayloadCorrectionContext"
+ "hasFullPayloadCorrectionExperimentContext"
+ "hasFullPayloadCorrectionExperimentPostAnalysis"
+ "hasFullPayloadCorrectionExperimentTier1"
+ "hasFullPayloadCorrectorInput"
+ "hasFullPayloadCorrectorOutput"
+ "hasGenerativeAIEnablement"
+ "hasGrammar"
+ "hasIdentifierQueryTime"
+ "hasIdx"
+ "hasInfoTier1"
+ "hasIntelligenceFlowRequestContext"
+ "hasIsCrossDevice"
+ "hasIsDefaultApp"
+ "hasIsExpanded"
+ "hasIsLongLivedIDUploadDisabled"
+ "hasIsMailAppFocused"
+ "hasIsMediaPlaybackOn"
+ "hasIsNamedEntityPresentInSpeechProfile"
+ "hasIsNamedEntityPresentInVisualContext"
+ "hasIsPreLaunchExecuted"
+ "hasIsPredictionCorrect"
+ "hasIsRelationship"
+ "hasIsRequestByHandleType"
+ "hasIsRequestByLabel"
+ "hasIsRoot"
+ "hasIsSiriXFallback"
+ "hasIsUnnamedPhoneNumber"
+ "hasLastCompletedPage"
+ "hasLastOpenedPageNumber"
+ "hasLogOfTimeElapsedInSeconds"
+ "hasLoggableUserIdHash"
+ "hasLoudnessLevel"
+ "hasMaxEnrolled"
+ "hasMaxEntityChars"
+ "hasMaxEntityWords"
+ "hasMusicLoudnessLevel"
+ "hasNlRouterPromptGenerated"
+ "hasNumAttempts"
+ "hasNumEntityErrors"
+ "hasNumTotalEdit"
+ "hasNumTotalEntities"
+ "hasOneBestTranscriptLinkIndex"
+ "hasOriginal"
+ "hasOriginalAsrInterpretationIdx"
+ "hasOverrideMetadata"
+ "hasOverridesMatched"
+ "hasPayloadType"
+ "hasPegasusAsrCorrectionInfo"
+ "hasPersonQueryTime"
+ "hasPersonalizationUserEditNamedEntityMetrics"
+ "hasPgFullPlannerHandleTime"
+ "hasPgFullPlannerPostInferenceTime"
+ "hasPgFullPlannerPreInferenceTime"
+ "hasPgGeneratePlanContext"
+ "hasPgModelIdentifier"
+ "hasPgModelInferenceTime"
+ "hasPgModelInterface"
+ "hasPgOverridesAssetVersion"
+ "hasPgOverridesMatched"
+ "hasPgOverridesTime"
+ "hasPgPlanGenTotalTime"
+ "hasPgPrescribedPlanTime"
+ "hasPlanGenerationTime"
+ "hasPostItn1Best"
+ "hasPostItnUtterance"
+ "hasPostSearchTime"
+ "hasPrTotalHandleTime"
+ "hasPreSearchTime"
+ "hasPrimitiveType"
+ "hasQueryDecorationContextRetrievalTime"
+ "hasQueryDecorationFetchDynamicEnumerationTime"
+ "hasQueryDecorationFullPlannerBlockingTime"
+ "hasQueryDecorationHandleTime"
+ "hasQueryDecorationID"
+ "hasQueryDecorationInputCollectionTime"
+ "hasQueryDecorationOutputBuildingTime"
+ "hasQueryDecorationPrePlannerResult"
+ "hasQueryDecorationRankingTime"
+ "hasQueryDecorationSource"
+ "hasQueryDecorationSpanRetrievalTime"
+ "hasQueryDecorationTime"
+ "hasQueryDecorationToolRetrievalContextTime"
+ "hasQueryDecorationToolRetrievalTime"
+ "hasQueryDecorationTupleBuildingTime"
+ "hasQueryDecorationTupleRankingTime"
+ "hasRejectReason"
+ "hasRequestTask"
+ "hasResponseGenerationCacheManagerTime"
+ "hasResponseGenerationCatalogTime"
+ "hasResponseGenerationGMSCallTime"
+ "hasResponseGenerationHallucinationDetectionTime"
+ "hasResponseGenerationHandleTime"
+ "hasResponseGenerationID"
+ "hasResponseGenerationInferenceTime"
+ "hasResponseGenerationOverrideTime"
+ "hasResponseGenerationType"
+ "hasResponseGenerationValidationTime"
+ "hasResponseTimeInNs"
+ "hasRetrievalTimeout"
+ "hasReturnType"
+ "hasSearchGlobalSearchTime"
+ "hasSearchHallucinationTime"
+ "hasSearchStartToGlobalSearchEnd"
+ "hasSearchStartToSpotlightEnd"
+ "hasSearchToolQueryTime"
+ "hasSearchTotalHandleTime"
+ "hasSelectedAsAlternateSuggestion"
+ "hasSelectedAsPrimaryResponse"
+ "hasSelectedloggableUserIdHash"
+ "hasSessionSummary"
+ "hasShimAction"
+ "hasShouldOpen"
+ "hasSignalToNoiseRatio"
+ "hasSizeInTokens"
+ "hasSkipStatement"
+ "hasSourceAuxIdx"
+ "hasSourceAuxKey"
+ "hasSpeakerDistance"
+ "hasSpeakerSpeechLevel"
+ "hasSpeechProfileCategory"
+ "hasSpeechStartPointDetected"
+ "hasStError"
+ "hasStartCharacterIdx"
+ "hasStringQueryEntityMatcherTime"
+ "hasStringQueryEntityTime"
+ "hasStringQueryLocationTime"
+ "hasStructuredSearch"
+ "hasStructuredSearchParameterName"
+ "hasSystemStyle"
+ "hasToolboxSizeReported"
+ "hasTotalSizeInTokens"
+ "hasTotalToolCount"
+ "hasTranscriptShown"
+ "hasTranscriptShownReason"
+ "hasTranscriptTapped"
+ "hasTrueCorrections"
+ "hasTrueRegressions"
+ "hasTtaie"
+ "hasTtsVolume"
+ "hasTwoPassRecognizerUsed"
+ "hasUnableToCancel"
+ "hasUserIntentType"
+ "hasUserIntentVolume"
+ "hasVoiceIdClassification"
+ "hasWantedToUndo"
+ "historicalLocationContext"
+ "historicalLocationContextAtIndex:"
+ "historicalLocationContextCount"
+ "historicalLocationContexts"
+ "identifierQueryTime"
+ "idx"
+ "infoTier1"
+ "intelligenceFlowRequestContext"
+ "intervalUntilStartTime"
+ "intervalUntilStartTimeAtIndex:"
+ "intervalUntilStartTimeCount"
+ "intervalUntilStartTimes"
+ "isApplicableToCandidate"
+ "isApplicableToCandidateAtIndex:"
+ "isApplicableToCandidateCount"
+ "isApplicableToCandidates"
+ "isCrossDevice"
+ "isDefaultApp"
+ "isExpanded"
+ "isLongLivedIDUploadDisabled"
+ "isMailAppFocused"
+ "isMediaPlaybackOn"
+ "isNamedEntityPresentInSpeechProfile"
+ "isNamedEntityPresentInVisualContext"
+ "isPreLaunchExecuted"
+ "isPredictionCorrect"
+ "isRelationship"
+ "isRequestByHandleType"
+ "isRequestByLabel"
+ "isRoot"
+ "isSiriXFallback"
+ "isUnnamedPhoneNumber"
+ "jrEntitySimilarityScores"
+ "jrEntitySimilarityScoresAtIndex:"
+ "jrEntitySimilarityScoresCount"
+ "lastCompletedPage"
+ "lastOpenedPageNumber"
+ "lmeOverActivationEdits"
+ "lmeOverActivationEditsAtIndex:"
+ "lmeOverActivationEditsCount"
+ "logOfIntervalUntilStartTimeInSeconds"
+ "logOfIntervalUntilStartTimeInSecondsAtIndex:"
+ "logOfIntervalUntilStartTimeInSecondsCount"
+ "logOfTimeElapsedInSeconds"
+ "loggableUserIdHash"
+ "loudnessLevel"
+ "maxEnrolled"
+ "maxEntityChars"
+ "maxEntityWords"
+ "musicLoudnessLevel"
+ "muxBridgeContext.ended.voiceIdScores.loggableSharedUserId"
+ "namedEntityUserEdits"
+ "namedEntityUserEditsAtIndex:"
+ "namedEntityUserEditsCount"
+ "nlRouterPromptGenerated"
+ "numAttempts"
+ "numEntityErrors"
+ "numTotalEdit"
+ "numTotalEntities"
+ "oneBestTranscriptLinkIndex"
+ "oneBestTranscripts"
+ "oneBestTranscriptsAtIndex:"
+ "oneBestTranscriptsCount"
+ "orderedMessages.siriEventTypeUnion.asrClientEvent.contextualEntityRetrievalContext.ended.retrievedEntityStates.entityType.bundleId"
+ "orderedMessages.siriEventTypeUnion.asrClientEvent.contextualEntityRetrievalContext.startedOrChanged.rejectedEntityTypes.bundleId"
+ "orderedMessages.siriEventTypeUnion.dodmlClientEvent.audioFileResultTier1.oneBestTranscripts.postItn"
+ "orderedMessages.siriEventTypeUnion.dodmlClientEvent.audioFileResultTier1.oneBestTranscripts.rawRecognition"
+ "orderedMessages.siriEventTypeUnion.dodmlClientEvent.fullPayloadCorrectionExperimentTier1"
+ "orderedMessages.siriEventTypeUnion.dodmlClientEvent.fullPayloadCorrectionExperimentTier1.infoTier1.fullPayloadCorrectorInput"
+ "orderedMessages.siriEventTypeUnion.dodmlClientEvent.fullPayloadCorrectionExperimentTier1.infoTier1.fullPayloadCorrectorOutput"
+ "orderedMessages.siriEventTypeUnion.flowClientEvent.flowContactTier1"
+ "orderedMessages.siriEventTypeUnion.flowClientEvent.flowContactTier1.contactName"
+ "orderedMessages.siriEventTypeUnion.flowClientEvent.flowDomainExecutionContext.startedOrChanged.domainExecutionMetadata.domainExecutionAppIntentBundleID"
+ "orderedMessages.siriEventTypeUnion.orchClientEvent.muxBridgeContext.ended.voiceIdScores.loggableSharedUserId"
+ "original"
+ "originalAsrInterpretationIdx"
+ "overrideMetadata"
+ "overridesMatched"
+ "pageAttempts"
+ "pageAttemptsAtIndex:"
+ "pageAttemptsCount"
+ "parameterSubType"
+ "parameterSubTypeAtIndex:"
+ "parameterSubTypeCount"
+ "parameterSubTypes"
+ "payloadType"
+ "pegasusAsrCorrectionInfo"
+ "pegasusAsrCorrectionInfo.asrHypothesesInfos.corrections.correction"
+ "pegasusAsrCorrectionInfo.asrHypothesesInfos.corrections.original"
+ "pegasusAsrCorrectionInfo.asrHypothesesInfos.postItnUtterance"
+ "pegasusRequestContext.ended.alternateQuerySuggestionTier1.alternateQuerySuggestionCandidateTier1s"
+ "pegasusRequestContext.ended.alternateQuerySuggestionTier1.alternateQuerySuggestionCandidateTier1s.text"
+ "pegasusRequestEndedTier1.videoExecutionTier1.isNlsResult"
+ "personQueryTime"
+ "personalizationUserEditNamedEntityMetrics"
+ "pgFullPlannerHandleTime"
+ "pgFullPlannerPostInferenceTime"
+ "pgFullPlannerPreInferenceTime"
+ "pgGeneratePlanContext"
+ "pgModelIdentifier"
+ "pgModelInferenceTime"
+ "pgModelInterface"
+ "pgOverridesAssetVersion"
+ "pgOverridesMatched"
+ "pgOverridesTime"
+ "pgPlanGenTotalTime"
+ "pgPrescribedPlanTime"
+ "pgPromptResponseTier1.grammar"
+ "planCreated.statements.expressionName.structuredSearch.returnType.collection.typeIdentifier.custom.bundleId"
+ "planCreated.statements.expressionName.structuredSearch.returnType.collection.values.entity.typeIdentifier.custom.bundleId"
+ "planCreated.statements.expressionName.structuredSearch.returnType.collection.values.enumeration.typeIdentifier.custom.bundleId"
+ "planCreated.statements.expressionName.structuredSearch.returnType.collection.values.primitive.app.bundleId"
+ "planCreated.statements.expressionName.structuredSearch.returnType.collection.values.query.typeIdentifier.custom.bundleId"
+ "planCreated.statements.expressionName.structuredSearch.returnType.typeIdentifier.custom.bundleId"
+ "planGeneration"
+ "planGenerationAtIndex:"
+ "planGenerationCount"
+ "planGenerationTime"
+ "planGenerations"
+ "planResolution"
+ "planResolutionAtIndex:"
+ "planResolutionCount"
+ "planResolutions"
+ "postItn1Best"
+ "postItnUtterance"
+ "postSearchTime"
+ "prTotalHandleTime"
+ "preSearchTime"
+ "primitiveType"
+ "queriesCreated.context.toolId"
+ "queryDecoration"
+ "queryDecorationAtIndex:"
+ "queryDecorationContextRetrievalTime"
+ "queryDecorationCount"
+ "queryDecorationFetchDynamicEnumerationTime"
+ "queryDecorationFullPlannerBlockingTime"
+ "queryDecorationHandleTime"
+ "queryDecorationID"
+ "queryDecorationInputCollectionTime"
+ "queryDecorationOutputBuildingTime"
+ "queryDecorationPrePlannerResult"
+ "queryDecorationRankingTime"
+ "queryDecorationSource"
+ "queryDecorationSpanRetrievalTime"
+ "queryDecorationTime"
+ "queryDecorationToolRetrievalContextTime"
+ "queryDecorationToolRetrievalTime"
+ "queryDecorationTupleBuildingTime"
+ "queryDecorationTupleRankingTime"
+ "queryDecorations"
+ "rejectReason"
+ "rejectedContextTypes"
+ "rejectedContextTypesAtIndex:"
+ "rejectedContextTypesCount"
+ "rejectedEntityTypes"
+ "rejectedEntityTypesAtIndex:"
+ "rejectedEntityTypesCount"
+ "requestFeatureTag"
+ "requestFeatureTagAtIndex:"
+ "requestFeatureTagCount"
+ "requestFeatureTags"
+ "requestTask"
+ "responseGeneration"
+ "responseGenerationAtIndex:"
+ "responseGenerationCacheManagerTime"
+ "responseGenerationCatalogTime"
+ "responseGenerationCount"
+ "responseGenerationGMSCallTime"
+ "responseGenerationHallucinationDetectionTime"
+ "responseGenerationHandleTime"
+ "responseGenerationID"
+ "responseGenerationInferenceTime"
+ "responseGenerationOverrideTime"
+ "responseGenerationRequest.statementResults.payload.outcome.actionConfirmation.systemStyle.generativeAIEnablement.bundleId"
+ "responseGenerationType"
+ "responseGenerationValidationTime"
+ "responseGenerations"
+ "responseTimeInNs"
+ "retrievalTimeout"
+ "retrievedEntityStates"
+ "retrievedEntityStatesAtIndex:"
+ "retrievedEntityStatesCount"
+ "returnType"
+ "riskLevel"
+ "riskLevelAtIndex:"
+ "riskLevelCount"
+ "riskLevels"
+ "row"
+ "rowAtIndex:"
+ "rowCount"
+ "rows"
+ "searchAtIndex:"
+ "searchCount"
+ "searchGlobalSearchTime"
+ "searchHallucinationTime"
+ "searchStartToGlobalSearchEnd"
+ "searchStartToSpotlightEnd"
+ "searchToolQueryTime"
+ "searchToolRank"
+ "searchToolRankAtIndex:"
+ "searchToolRankCount"
+ "searchToolRanks"
+ "searchToolRanksAtIndex:"
+ "searchToolRanksCount"
+ "searchTotalHandleTime"
+ "searchs"
+ "selectedAsAlternateSuggestion"
+ "selectedAsPrimaryResponse"
+ "selectedloggableUserIdHash"
+ "sessionSummary"
+ "setActionClass:"
+ "setActionParameterValues:"
+ "setAdaptiveSiriVolumeTTSVolumeQueried:"
+ "setAdaptiveSiriVolumeUserIntentDetected:"
+ "setAlignmentOffset:"
+ "setAlternateQuerySuggestionCandidateTier1s:"
+ "setAlternateQuerySuggestionTier1:"
+ "setAlternateQuerySuggestionType:"
+ "setAnonymizedLocationNameId:"
+ "setAnonymizedLocationTypeId:"
+ "setAppEntityQueryResponseTime:"
+ "setAppIntentSessionId:"
+ "setAppPreLaunchTriggered:"
+ "setArray:"
+ "setAsrFullPayloadCorrectedToUserEdit:"
+ "setAsrHypothesesInfos:"
+ "setAsrOutputToUserEdit:"
+ "setAsrScores:"
+ "setAudioFileResult:"
+ "setAudioQueueLatencyInSecond:"
+ "setBackgroundNoiseActivityLevel:"
+ "setBackgroundNoiseLevel:"
+ "setBucketedDistance:"
+ "setBucketedDistances:"
+ "setCallParameterName:"
+ "setCallers:"
+ "setCandidateA:"
+ "setCandidateB:"
+ "setCandidateBooleanMasks:"
+ "setCandidateRisks:"
+ "setCandidateTimeIntervalMatrixs:"
+ "setComponentType:"
+ "setComponents:"
+ "setContact:"
+ "setContactName:"
+ "setContextStatementIds:"
+ "setContextStatementIdsReported:"
+ "setContexts:"
+ "setContextualEntityCollectionTriggered:"
+ "setContextualEntityRetrievalContext:"
+ "setContextualEntityStatementIds:"
+ "setContextualReplayBiomeRecordCreated:"
+ "setContextualReplayBiomeRecordDeleted:"
+ "setCorrection:"
+ "setCorrections:"
+ "setCreationTimestampInMsSince1970:"
+ "setDidTriggerFirstPass:"
+ "setDomainExecutionAppIntentBundleID:"
+ "setDomainExecutionMetadata:"
+ "setDroppedComponents:"
+ "setEnabledTasks:"
+ "setEndCharacterIdx:"
+ "setEnrollmentResult:"
+ "setEntityScoreResults:"
+ "setEntityScores:"
+ "setEntityTaggerCategory:"
+ "setErrorDomainString:"
+ "setEstimatedSizeInTokens:"
+ "setEventOrigin:"
+ "setExecutorAppIntentHandleTime:"
+ "setExecutorAppIntentQueryHandleTime:"
+ "setExecutorIdentifierQueryCallContext:"
+ "setExecutorPersonQueryCallContext:"
+ "setExecutorSearchToolQueryCallContext:"
+ "setExecutorSearchToolQueryType:"
+ "setExecutorStringQueryEntityCallContext:"
+ "setExecutorStringQueryEntityMatcherCallContext:"
+ "setExecutorStringQueryLocationCallContext:"
+ "setExecutors:"
+ "setExpensiveCellularDownloadRequested:"
+ "setFailedToConvertClientEvent:"
+ "setFlowContactTier1:"
+ "setFormat:"
+ "setFromPreSoftwareUpdateStaging:"
+ "setFullPayloadCorrectionContext:"
+ "setFullPayloadCorrectionExperimentContext:"
+ "setFullPayloadCorrectionExperimentPostAnalysis:"
+ "setFullPayloadCorrectionExperimentTier1:"
+ "setFullPayloadCorrectorInput:"
+ "setFullPayloadCorrectorOutput:"
+ "setGenerativeAIEnablement:"
+ "setGrammar:"
+ "setHasActionClass:"
+ "setHasAdaptiveSiriVolumeTTSVolumeQueried:"
+ "setHasAdaptiveSiriVolumeUserIntentDetected:"
+ "setHasAlignmentOffset:"
+ "setHasAlternateQuerySuggestionTier1:"
+ "setHasAlternateQuerySuggestionType:"
+ "setHasAnonymizedLocationNameId:"
+ "setHasAnonymizedLocationTypeId:"
+ "setHasAppEntityQueryResponseTime:"
+ "setHasAppIntentSessionId:"
+ "setHasAppPreLaunchTriggered:"
+ "setHasArray:"
+ "setHasAsrFullPayloadCorrectedToUserEdit:"
+ "setHasAsrOutputToUserEdit:"
+ "setHasAudioFileResult:"
+ "setHasAudioQueueLatencyInSecond:"
+ "setHasBackgroundNoiseActivityLevel:"
+ "setHasBackgroundNoiseLevel:"
+ "setHasBucketedDistance:"
+ "setHasCallParameterName:"
+ "setHasCandidateA:"
+ "setHasCandidateB:"
+ "setHasComponentType:"
+ "setHasContact:"
+ "setHasContactName:"
+ "setHasContextStatementIdsReported:"
+ "setHasContextualEntityCollectionTriggered:"
+ "setHasContextualEntityRetrievalContext:"
+ "setHasContextualReplayBiomeRecordCreated:"
+ "setHasContextualReplayBiomeRecordDeleted:"
+ "setHasCorrection:"
+ "setHasCreationTimestampInMsSince1970:"
+ "setHasDidTriggerFirstPass:"
+ "setHasDomainExecutionAppIntentBundleID:"
+ "setHasDomainExecutionMetadata:"
+ "setHasEndCharacterIdx:"
+ "setHasEnrollmentResult:"
+ "setHasEntityTaggerCategory:"
+ "setHasErrorDomainString:"
+ "setHasEstimatedSizeInTokens:"
+ "setHasEventOrigin:"
+ "setHasExecutorAppIntentHandleTime:"
+ "setHasExecutorAppIntentQueryHandleTime:"
+ "setHasExecutorIdentifierQueryCallContext:"
+ "setHasExecutorPersonQueryCallContext:"
+ "setHasExecutorSearchToolQueryCallContext:"
+ "setHasExecutorSearchToolQueryType:"
+ "setHasExecutorStringQueryEntityCallContext:"
+ "setHasExecutorStringQueryEntityMatcherCallContext:"
+ "setHasExecutorStringQueryLocationCallContext:"
+ "setHasExpensiveCellularDownloadRequested:"
+ "setHasFailedToConvertClientEvent:"
+ "setHasFlowContactTier1:"
+ "setHasFormat:"
+ "setHasFromPreSoftwareUpdateStaging:"
+ "setHasFullPayloadCorrectionContext:"
+ "setHasFullPayloadCorrectionExperimentContext:"
+ "setHasFullPayloadCorrectionExperimentPostAnalysis:"
+ "setHasFullPayloadCorrectionExperimentTier1:"
+ "setHasFullPayloadCorrectorInput:"
+ "setHasFullPayloadCorrectorOutput:"
+ "setHasGenerativeAIEnablement:"
+ "setHasGrammar:"
+ "setHasIdentifierQueryTime:"
+ "setHasIdx:"
+ "setHasInfoTier1:"
+ "setHasIntelligenceFlowRequestContext:"
+ "setHasIsCrossDevice:"
+ "setHasIsDefaultApp:"
+ "setHasIsExpanded:"
+ "setHasIsLongLivedIDUploadDisabled:"
+ "setHasIsMailAppFocused:"
+ "setHasIsMediaPlaybackOn:"
+ "setHasIsNamedEntityPresentInSpeechProfile:"
+ "setHasIsNamedEntityPresentInVisualContext:"
+ "setHasIsPreLaunchExecuted:"
+ "setHasIsPredictionCorrect:"
+ "setHasIsRelationship:"
+ "setHasIsRequestByHandleType:"
+ "setHasIsRequestByLabel:"
+ "setHasIsRoot:"
+ "setHasIsSiriXFallback:"
+ "setHasIsUnnamedPhoneNumber:"
+ "setHasLastCompletedPage:"
+ "setHasLastOpenedPageNumber:"
+ "setHasLogOfTimeElapsedInSeconds:"
+ "setHasLoggableUserIdHash:"
+ "setHasLoudnessLevel:"
+ "setHasMaxEnrolled:"
+ "setHasMaxEntityChars:"
+ "setHasMaxEntityWords:"
+ "setHasMusicLoudnessLevel:"
+ "setHasNlRouterPromptGenerated:"
+ "setHasNumAttempts:"
+ "setHasNumEntityErrors:"
+ "setHasNumTotalEdit:"
+ "setHasNumTotalEntities:"
+ "setHasOneBestTranscriptLinkIndex:"
+ "setHasOriginal:"
+ "setHasOriginalAsrInterpretationIdx:"
+ "setHasOverrideMetadata:"
+ "setHasOverridesMatched:"
+ "setHasPayloadType:"
+ "setHasPegasusAsrCorrectionInfo:"
+ "setHasPersonQueryTime:"
+ "setHasPersonalizationUserEditNamedEntityMetrics:"
+ "setHasPgFullPlannerHandleTime:"
+ "setHasPgFullPlannerPostInferenceTime:"
+ "setHasPgFullPlannerPreInferenceTime:"
+ "setHasPgGeneratePlanContext:"
+ "setHasPgModelIdentifier:"
+ "setHasPgModelInferenceTime:"
+ "setHasPgModelInterface:"
+ "setHasPgOverridesAssetVersion:"
+ "setHasPgOverridesMatched:"
+ "setHasPgOverridesTime:"
+ "setHasPgPlanGenTotalTime:"
+ "setHasPgPrescribedPlanTime:"
+ "setHasPlanGenerationTime:"
+ "setHasPostItn1Best:"
+ "setHasPostItnUtterance:"
+ "setHasPostSearchTime:"
+ "setHasPrTotalHandleTime:"
+ "setHasPreSearchTime:"
+ "setHasPrimitiveType:"
+ "setHasQueryDecorationContextRetrievalTime:"
+ "setHasQueryDecorationFetchDynamicEnumerationTime:"
+ "setHasQueryDecorationFullPlannerBlockingTime:"
+ "setHasQueryDecorationHandleTime:"
+ "setHasQueryDecorationID:"
+ "setHasQueryDecorationInputCollectionTime:"
+ "setHasQueryDecorationOutputBuildingTime:"
+ "setHasQueryDecorationPrePlannerResult:"
+ "setHasQueryDecorationRankingTime:"
+ "setHasQueryDecorationSource:"
+ "setHasQueryDecorationSpanRetrievalTime:"
+ "setHasQueryDecorationTime:"
+ "setHasQueryDecorationToolRetrievalContextTime:"
+ "setHasQueryDecorationToolRetrievalTime:"
+ "setHasQueryDecorationTupleBuildingTime:"
+ "setHasQueryDecorationTupleRankingTime:"
+ "setHasRejectReason:"
+ "setHasRequestTask:"
+ "setHasResponseGenerationCacheManagerTime:"
+ "setHasResponseGenerationCatalogTime:"
+ "setHasResponseGenerationGMSCallTime:"
+ "setHasResponseGenerationHallucinationDetectionTime:"
+ "setHasResponseGenerationHandleTime:"
+ "setHasResponseGenerationID:"
+ "setHasResponseGenerationInferenceTime:"
+ "setHasResponseGenerationOverrideTime:"
+ "setHasResponseGenerationType:"
+ "setHasResponseGenerationValidationTime:"
+ "setHasResponseTimeInNs:"
+ "setHasRetrievalTimeout:"
+ "setHasReturnType:"
+ "setHasSearchGlobalSearchTime:"
+ "setHasSearchHallucinationTime:"
+ "setHasSearchStartToGlobalSearchEnd:"
+ "setHasSearchStartToSpotlightEnd:"
+ "setHasSearchToolQueryTime:"
+ "setHasSearchTotalHandleTime:"
+ "setHasSelectedAsAlternateSuggestion:"
+ "setHasSelectedAsPrimaryResponse:"
+ "setHasSelectedloggableUserIdHash:"
+ "setHasSessionSummary:"
+ "setHasShimAction:"
+ "setHasShouldOpen:"
+ "setHasSignalToNoiseRatio:"
+ "setHasSizeInTokens:"
+ "setHasSkipStatement:"
+ "setHasSourceAuxIdx:"
+ "setHasSourceAuxKey:"
+ "setHasSpeakerDistance:"
+ "setHasSpeakerSpeechLevel:"
+ "setHasSpeechProfileCategory:"
+ "setHasSpeechStartPointDetected:"
+ "setHasStError:"
+ "setHasStartCharacterIdx:"
+ "setHasStringQueryEntityMatcherTime:"
+ "setHasStringQueryEntityTime:"
+ "setHasStringQueryLocationTime:"
+ "setHasStructuredSearch:"
+ "setHasStructuredSearchParameterName:"
+ "setHasSystemStyle:"
+ "setHasToolboxSizeReported:"
+ "setHasTotalSizeInTokens:"
+ "setHasTotalToolCount:"
+ "setHasTranscriptShown:"
+ "setHasTranscriptShownReason:"
+ "setHasTranscriptTapped:"
+ "setHasTrueCorrections:"
+ "setHasTrueRegressions:"
+ "setHasTtaie:"
+ "setHasTtsVolume:"
+ "setHasTwoPassRecognizerUsed:"
+ "setHasUnableToCancel:"
+ "setHasUserIntentType:"
+ "setHasUserIntentVolume:"
+ "setHasVoiceIdClassification:"
+ "setHasWantedToUndo:"
+ "setHistoricalLocationContexts:"
+ "setIdentifierQueryTime:"
+ "setIdx:"
+ "setInfoTier1:"
+ "setIntelligenceFlowRequestContext:"
+ "setIntervalUntilStartTimes:"
+ "setIsApplicableToCandidates:"
+ "setIsCrossDevice:"
+ "setIsDefaultApp:"
+ "setIsExpanded:"
+ "setIsLongLivedIDUploadDisabled:"
+ "setIsMailAppFocused:"
+ "setIsMediaPlaybackOn:"
+ "setIsNamedEntityPresentInSpeechProfile:"
+ "setIsNamedEntityPresentInVisualContext:"
+ "setIsPreLaunchExecuted:"
+ "setIsPredictionCorrect:"
+ "setIsRelationship:"
+ "setIsRequestByHandleType:"
+ "setIsRequestByLabel:"
+ "setIsRoot:"
+ "setIsSiriXFallback:"
+ "setIsUnnamedPhoneNumber:"
+ "setJrEntitySimilarityScores:"
+ "setLastCompletedPage:"
+ "setLastOpenedPageNumber:"
+ "setLmeOverActivationEdits:"
+ "setLogOfIntervalUntilStartTimeInSeconds:"
+ "setLogOfTimeElapsedInSeconds:"
+ "setLoggableUserIdHash:"
+ "setLoudnessLevel:"
+ "setMaxEnrolled:"
+ "setMaxEntityChars:"
+ "setMaxEntityWords:"
+ "setMusicLoudnessLevel:"
+ "setNamedEntityUserEdits:"
+ "setNlRouterPromptGenerated:"
+ "setNumAttempts:"
+ "setNumEntityErrors:"
+ "setNumTotalEdit:"
+ "setNumTotalEntities:"
+ "setOneBestTranscriptLinkIndex:"
+ "setOneBestTranscripts:"
+ "setOriginal:"
+ "setOriginalAsrInterpretationIdx:"
+ "setOverrideMetadata:"
+ "setOverridesMatched:"
+ "setPageAttempts:"
+ "setParameterSubTypes:"
+ "setPayloadType:"
+ "setPegasusAsrCorrectionInfo:"
+ "setPersonQueryTime:"
+ "setPersonalizationUserEditNamedEntityMetrics:"
+ "setPgFullPlannerHandleTime:"
+ "setPgFullPlannerPostInferenceTime:"
+ "setPgFullPlannerPreInferenceTime:"
+ "setPgGeneratePlanContext:"
+ "setPgModelIdentifier:"
+ "setPgModelInferenceTime:"
+ "setPgModelInterface:"
+ "setPgOverridesAssetVersion:"
+ "setPgOverridesMatched:"
+ "setPgOverridesTime:"
+ "setPgPlanGenTotalTime:"
+ "setPgPrescribedPlanTime:"
+ "setPlanGenerationTime:"
+ "setPlanGenerations:"
+ "setPlanResolutions:"
+ "setPostItn1Best:"
+ "setPostItnUtterance:"
+ "setPostSearchTime:"
+ "setPrTotalHandleTime:"
+ "setPreSearchTime:"
+ "setPrimitiveType:"
+ "setQueryDecorationContextRetrievalTime:"
+ "setQueryDecorationFetchDynamicEnumerationTime:"
+ "setQueryDecorationFullPlannerBlockingTime:"
+ "setQueryDecorationHandleTime:"
+ "setQueryDecorationID:"
+ "setQueryDecorationInputCollectionTime:"
+ "setQueryDecorationOutputBuildingTime:"
+ "setQueryDecorationPrePlannerResult:"
+ "setQueryDecorationRankingTime:"
+ "setQueryDecorationSource:"
+ "setQueryDecorationSpanRetrievalTime:"
+ "setQueryDecorationTime:"
+ "setQueryDecorationToolRetrievalContextTime:"
+ "setQueryDecorationToolRetrievalTime:"
+ "setQueryDecorationTupleBuildingTime:"
+ "setQueryDecorationTupleRankingTime:"
+ "setQueryDecorations:"
+ "setRejectReason:"
+ "setRejectedContextTypes:"
+ "setRejectedEntityTypes:"
+ "setRequestFeatureTags:"
+ "setRequestTask:"
+ "setResponseGenerationCacheManagerTime:"
+ "setResponseGenerationCatalogTime:"
+ "setResponseGenerationGMSCallTime:"
+ "setResponseGenerationHallucinationDetectionTime:"
+ "setResponseGenerationHandleTime:"
+ "setResponseGenerationID:"
+ "setResponseGenerationInferenceTime:"
+ "setResponseGenerationOverrideTime:"
+ "setResponseGenerationType:"
+ "setResponseGenerationValidationTime:"
+ "setResponseGenerations:"
+ "setResponseTimeInNs:"
+ "setRetrievalTimeout:"
+ "setRetrievedEntityStates:"
+ "setReturnType:"
+ "setRiskLevels:"
+ "setRows:"
+ "setSearchGlobalSearchTime:"
+ "setSearchHallucinationTime:"
+ "setSearchStartToGlobalSearchEnd:"
+ "setSearchStartToSpotlightEnd:"
+ "setSearchToolQueryTime:"
+ "setSearchToolRanks:"
+ "setSearchTotalHandleTime:"
+ "setSearchs:"
+ "setSelectedAsAlternateSuggestion:"
+ "setSelectedAsPrimaryResponse:"
+ "setSelectedloggableUserIdHash:"
+ "setSessionSummary:"
+ "setShimAction:"
+ "setShouldOpen:"
+ "setSignalToNoiseRatio:"
+ "setSizeInTokens:"
+ "setSkipStatement:"
+ "setSourceAuxIdx:"
+ "setSourceAuxKey:"
+ "setSpeakerDistance:"
+ "setSpeakerSpeechLevel:"
+ "setSpeechProfileCategories:"
+ "setSpeechProfileCategory:"
+ "setSpeechStartPointDetected:"
+ "setStError:"
+ "setStartCharacterIdx:"
+ "setStringQueryEntityMatcherTime:"
+ "setStringQueryEntityTime:"
+ "setStringQueryLocationTime:"
+ "setStructuredSearch:"
+ "setStructuredSearchParameterName:"
+ "setSystemStyle:"
+ "setToolboxSizeReported:"
+ "setTotalSizeInTokens:"
+ "setTotalToolCount:"
+ "setTranscriptShown:"
+ "setTranscriptShownReason:"
+ "setTranscriptTapped:"
+ "setTrueCorrections:"
+ "setTrueRegressions:"
+ "setTtaie:"
+ "setTtsVolume:"
+ "setTwoPassRecognizerUsed:"
+ "setUnableToCancel:"
+ "setUserIntentType:"
+ "setUserIntentVolume:"
+ "setVisualContextCategories:"
+ "setVoiceIdClassification:"
+ "setVoiceIdScores:"
+ "setWantedToUndo:"
+ "shimAction"
+ "shouldOpen"
+ "signalToNoiseRatio"
+ "sizeInTokens"
+ "skipStatement"
+ "sourceAuxIdx"
+ "sourceAuxKey"
+ "speakerDistance"
+ "speakerSpeechLevel"
+ "speechProfileCategories"
+ "speechProfileCategoriesAtIndex:"
+ "speechProfileCategoriesCount"
+ "speechProfileCategory"
+ "speechStartPointDetected"
+ "stError"
+ "startCharacterIdx"
+ "statementEvaluated.payload.outcome.actionConfirmation.systemStyle.generativeAIEnablement.bundleId"
+ "statementIdAtIndex:"
+ "statementIdCount"
+ "stringQueryEntityMatcherTime"
+ "stringQueryEntityTime"
+ "stringQueryLocationTime"
+ "structuredSearch"
+ "structuredSearchParameterName"
+ "systemResponseGenerated.interpretedStatementResults.outcome.actionConfirmation.systemStyle.generativeAIEnablement.bundleId"
+ "systemResponseGenerated.outcome.actionConfirmation.systemStyle.generativeAIEnablement.bundleId"
+ "systemStyle"
+ "toolboxSizeReported"
+ "totalSizeInTokens"
+ "totalToolCount"
+ "transcriptShown"
+ "transcriptShownReason"
+ "transcriptTapped"
+ "trueCorrections"
+ "trueRegressions"
+ "ttaie"
+ "ttsVolume"
+ "twoPassRecognizerUsed"
+ "unableToCancel"
+ "userIntentType"
+ "userIntentVolume"
+ "visualContextCategories"
+ "visualContextCategoriesAtIndex:"
+ "visualContextCategoriesCount"
+ "voiceIdClassification"
+ "voiceIdScores"
+ "voiceIdScoresAtIndex:"
+ "voiceIdScoresCount"
+ "wantedToUndo"
+ "whichItemtype"
+ "whichOneof_Actionconfirmationsystemstyle"
+ "{?=\"actionClass\"b1}"
+ "{?=\"actionStatementId\"b1\"statementId\"b1}"
+ "{?=\"alternateQuerySuggestionType\"b1}"
+ "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1\"audioQueueLatencyInSecond\"b1\"isWarmStart\"b1}"
+ "{?=\"code\"b1\"source\"b1}"
+ "{?=\"componentType\"b1\"sizeInTokens\"b1}"
+ "{?=\"contextType\"b1\"enrollmentResult\"b1\"rejectReason\"b1}"
+ "{?=\"creationTimestampInMsSince1970\"b1}"
+ "{?=\"decodeDurationInNs\"b1\"oneBestTranscriptLinkIndex\"b1}"
+ "{?=\"entityTaggerCategory\"b1\"isNamedEntityPresentInVisualContext\"b1\"isNamedEntityPresentInSpeechProfile\"b1}"
+ "{?=\"entityTaggerCategory\"b1\"numTotalEntities\"b1\"numEntityErrors\"b1}"
+ "{?=\"errorDomain\"b1\"gmsErrorCode\"b1\"openAIErrorCode\"b1\"errorCode\"b1}"
+ "{?=\"errorType\"b1\"responseTimeInNs\"b1}"
+ "{?=\"eventTimestampInMsSince1970\"b1\"userAggregationIdRotationTimestampMs\"b1\"userAggregationIdExpirationTimestampMs\"b1\"eventOrigin\"b1\"isLongLivedIDUploadDisabled\"b1}"
+ "{?=\"executorSearchToolQueryType\"b1}"
+ "{?=\"exists\"b1\"appIntentSessionId\"b1}"
+ "{?=\"exists\"b1\"appLaunched\"b1\"didShowInAppResult\"b1\"shouldOpen\"b1}"
+ "{?=\"exists\"b1\"executorSearchToolQueryType\"b1}"
+ "{?=\"exists\"b1\"payloadType\"b1}"
+ "{?=\"exists\"b1\"primitiveType\"b1}"
+ "{?=\"fromPreSoftwareUpdateStaging\"b1\"expensiveCellularDownloadRequested\"b1}"
+ "{?=\"isAppFocused\"b1\"isMediaRichAppFocused\"b1\"isMediaFocused\"b1\"isMailAppFocused\"b1}"
+ "{?=\"isExpanded\"b1}"
+ "{?=\"isMatched\"b1}"
+ "{?=\"isMultiUser\"b1\"nlRerunTimeInMs\"b1\"ORCHUserIdentityClassification\"b1\"isOutsider\"b1\"isSelectedUserPartOfMultipleHomes\"b1\"nlRerunLatencyInMs\"b1\"voiceIdClassification\"b1}"
+ "{?=\"isNlsResult\"b1}"
+ "{?=\"isPredictionCorrect\"b1\"isPreLaunchExecuted\"b1}"
+ "{?=\"isRelationship\"b1\"isUnnamedPhoneNumber\"b1}"
+ "{?=\"isResolvedApp\"b1\"isResolvedContactInApp\"b1\"appTimeSpentAffinityScore\"b1\"isForegroundApp\"b1\"timeSinceAppLastLaunchedInSec\"b1\"isFirstPartyApp\"b1\"appTimeSpentInSec\"b1\"timeSinceAppContactLastLaunchedInSec\"b1\"isDefaultApp\"b1\"isRequestByLabel\"b1\"isRequestByHandleType\"b1}"
+ "{?=\"isRoot\"b1}"
+ "{?=\"lastOpenedPageNumber\"b1\"lastCompletedPage\"b1}"
+ "{?=\"logOfTimeElapsedInSeconds\"b1\"bucketedDistance\"b1}"
+ "{?=\"maxEnrolled\"b1\"retrievalTimeout\"b1\"maxEntityChars\"b1\"maxEntityWords\"b1\"requestTask\"b1}"
+ "{?=\"numTotalEdit\"b1}"
+ "{?=\"pageNumber\"b1\"maxNumContinuousZeros\"b1\"maxNumAllowedContinuousZeros\"b1\"isMaxNumContinuousZerosOverThreshold\"b1\"stageStatus\"b1\"speechStartPointDetected\"b1\"twoPassRecognizerUsed\"b1\"didTriggerFirstPass\"b1}"
+ "{?=\"pageNumber\"b1\"numAttempts\"b1}"
+ "{?=\"pgModelInterface\"b1\"pgOverridesMatched\"b1}"
+ "{?=\"queryDecorationSource\"b1}"
+ "{?=\"reason\"b1\"isSiriXFallback\"b1}"
+ "{?=\"responseGenerationType\"b1}"
+ "{?=\"responseTimeInNs\"b1}"
+ "{?=\"resultDomain\"b1\"responseStatus\"b1\"confidenceScore\"b1\"isLowConfidenceKnowledgeResult\"b1}"
+ "{?=\"score\"b1\"selectedAsPrimaryResponse\"b1\"selectedAsAlternateSuggestion\"b1}"
+ "{?=\"shimAction\"b1}"
+ "{?=\"source\"b1\"isExplicit\"b1}"
+ "{?=\"sourceAuxIdx\"b1\"originalAsrInterpretationIdx\"b1}"
+ "{?=\"speechProfileCategory\"b1}"
+ "{?=\"startCharacterIdx\"b1\"endCharacterIdx\"b1}"
+ "{?=\"status\"b1\"statementId\"b1\"numQueriesCreated\"b1\"numActionsCreated\"b1}"
+ "{?=\"totalSizeInTokens\"b1\"estimatedSizeInTokens\"b1}"
+ "{?=\"totalToolCount\"b1}"
+ "{?=\"transcriptShownReason\"b1}"
+ "{?=\"trialDisambiguationRate\"b1\"trialConfirmationRate\"b1\"signalToNoiseRatio\"b1\"loudnessLevel\"b1}"
+ "{?=\"trueCorrections\"b1\"trueRegressions\"b1}"
+ "{?=\"ttsVolume\"b1\"speakerDistance\"b1\"speakerSpeechLevel\"b1\"musicLoudnessLevel\"b1\"backgroundNoiseLevel\"b1\"backgroundNoiseActivityLevel\"b1\"isMediaPlaybackOn\"b1\"invocationType\"b1\"isPermanentOffsetEnabled\"b1\"permanentOffsetFactor\"b1}"
+ "{?=\"userIntentType\"b1\"userIntentVolume\"b1\"isPermanentOffsetEnabled\"b1\"permanentOffsetFactor\"b1}"
+ "{?=\"utteranceRestatementScore\"b1\"semanticSimilarityScore\"b1\"isCrossDevice\"b1}"
+ "{?=\"utteranceStartTimeInNs\"b1\"utteranceEndTimeInNs\"b1}"
- "@\"MHSchemaMHSensorControlStatusReported\""
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "MHSENSORCONTROLSTATUS_ALLOWED"
- "MHSENSORCONTROLSTATUS_DENIED"
- "MHSENSORCONTROLSTATUS_DENIED_BY_CONTROL_POLICY"
- "MHSENSORCONTROLSTATUS_UNKNOWN"
- "MHSchemaMHSensorControlStatusReported"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"MHSchemaMHSensorControlStatusReported\",&,N,V_sensorControlStatusReported"
- "TB,N,V_hasSensorControlStatusReported"
- "Ti,N,V_sensorControlStatus"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "_hasSensorControlStatusReported"
- "_sensorControlStatus"
- "_sensorControlStatusReported"
- "com.apple.aiml.siri.mh.MHClientEvent.MHSensorControlStatusReported"
- "deleteSensorControlStatus"
- "deleteSensorControlStatusReported"
- "hasSensorControlStatus"
- "hasSensorControlStatusReported"
- "invalid Collection: less than 'count' elements in collection"
- "sensorControlStatus"
- "sensorControlStatusReported"
- "setHasSensorControlStatus:"
- "setHasSensorControlStatusReported:"
- "setSensorControlStatus:"
- "setSensorControlStatusReported:"
- "{?=\"audioOutputRoute\"b1\"customerPerceivedLatencyInSecond\"b1\"synthesisSource\"b1\"synthesisEffect\"b1\"volume\"b1\"thermalState\"b1\"assetSelectionLatencyInSecond\"b1}"
- "{?=\"decodeDurationInNs\"b1}"
- "{?=\"errorDomain\"b1\"gmsErrorCode\"b1\"openAIErrorCode\"b1}"
- "{?=\"exists\"b1\"appLaunched\"b1\"didShowInAppResult\"b1}"
- "{?=\"isAppFocused\"b1\"isMediaRichAppFocused\"b1\"isMediaFocused\"b1}"
- "{?=\"isMultiUser\"b1\"nlRerunTimeInMs\"b1\"ORCHUserIdentityClassification\"b1\"isOutsider\"b1\"isSelectedUserPartOfMultipleHomes\"b1\"nlRerunLatencyInMs\"b1}"
- "{?=\"isResolvedApp\"b1\"isResolvedContactInApp\"b1\"appTimeSpentAffinityScore\"b1\"isForegroundApp\"b1\"timeSinceAppLastLaunchedInSec\"b1\"isFirstPartyApp\"b1\"appTimeSpentInSec\"b1\"timeSinceAppContactLastLaunchedInSec\"b1}"
- "{?=\"pageNumber\"b1\"maxNumContinuousZeros\"b1\"maxNumAllowedContinuousZeros\"b1\"isMaxNumContinuousZerosOverThreshold\"b1\"stageStatus\"b1}"
- "{?=\"resultDomain\"b1\"responseStatus\"b1\"confidenceScore\"b1}"
- "{?=\"sensorControlStatus\"b1}"
- "{?=\"trialDisambiguationRate\"b1\"trialConfirmationRate\"b1}"
- "{?=\"utteranceRestatementScore\"b1\"semanticSimilarityScore\"b1}"

```
