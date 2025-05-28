## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3304.54.1.0.0
-  __TEXT.__text: 0x67aa8c
+3305.16.1.0.0
+  __TEXT.__text: 0x67dc84
   __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x8f880
+  __TEXT.__objc_methlist: 0x8fd58
   __TEXT.__const: 0xb064
   __TEXT.__constg_swiftt: 0x4870
   __TEXT.__swift5_typeref: 0x11c2

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8d0
   __TEXT.__swift5_types: 0x890
-  __TEXT.__cstring: 0x45d08
+  __TEXT.__cstring: 0x45dbc
   __TEXT.__swift5_fieldmd: 0x2e8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1d084
+  __TEXT.__unwind_info: 0x1d8f0
   __TEXT.__eh_frame: 0x6f0
-  __TEXT.__objc_classname: 0xea95
-  __TEXT.__objc_methname: 0xcec64
-  __TEXT.__objc_methtype: 0x1cfda
-  __TEXT.__objc_stubs: 0x4bb80
+  __TEXT.__objc_classname: 0xeaf7
+  __TEXT.__objc_methname: 0xcf09e
+  __TEXT.__objc_methtype: 0x1d0a6
+  __TEXT.__objc_stubs: 0x4bda0
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x26770
-  __DATA_CONST.__objc_classlist: 0x3378
+  __DATA_CONST.__const: 0x267e8
+  __DATA_CONST.__objc_classlist: 0x3390
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa3918
-  __DATA_CONST.__objc_selrefs: 0x27cc0
+  __DATA_CONST.__objc_const: 0xa3f10
+  __DATA_CONST.__objc_selrefs: 0x27d88
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x3320
-  __DATA_CONST.__objc_superrefs: 0x4e40
+  __DATA_CONST.__objc_classrefs: 0x3338
+  __DATA_CONST.__objc_superrefs: 0x4e80
   __AUTH_CONST.__const: 0xb70
-  __AUTH_CONST.__cfstring: 0x4dc40
+  __AUTH_CONST.__cfstring: 0x4dd00
   __AUTH_CONST.__auth_ptr: 0x58
-  __AUTH_CONST.__objc_const: 0x2b48
+  __AUTH_CONST.__objc_const: 0x2c20
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH.__objc_data: 0x29e0
-  __DATA.__objc_ivar: 0x9914
+  __AUTH.__objc_data: 0x2a30
+  __DATA.__objc_ivar: 0x9978
   __DATA.__data: 0x17d0
   __DATA.__bss: 0x11600
   __DATA.__common: 0x20
   __DATA_DIRTY.__const: 0x40d8
   __DATA_DIRTY.__objc_const: 0x1ba58
-  __DATA_DIRTY.__objc_data: 0x1db08
+  __DATA_DIRTY.__objc_data: 0x1dba8
   __DATA_DIRTY.__data: 0x5a8
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 51987
-  Symbols:   129507
-  CStrings:  46101
+  Functions: 52092
+  Symbols:   129774
+  CStrings:  46158
 
Symbols:
+ -[DIMSchemaDIMExperimentContext deleteExperimentalBucketId]
+ -[DIMSchemaDIMExperimentContext experimentalBucketId]
+ -[DIMSchemaDIMExperimentContext hasExperimentalBucketId]
+ -[DIMSchemaDIMExperimentContext setExperimentalBucketId:]
+ -[DIMSchemaDIMExperimentContext setHasExperimentalBucketId:]
+ -[FLOWSchemaFLOWInformationPluginContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded deleteMitigationAssetVersion]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded deleteSpeakerIDThreshold]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded hasMitigationAssetVersion]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded hasSpeakerIDThreshold]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded mitigationAssetVersion]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded setHasMitigationAssetVersion:]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded setHasSpeakerIDThreshold:]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded setMitigationAssetVersion:]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded setSpeakerIDThreshold:]
+ -[MHSchemaMHUnintendedResponseSuppressionEnded speakerIDThreshold]
+ -[PFAPFAClientEvent deleteEventMetadata]
+ -[PFAPFAClientEvent eventMetadata]
+ -[PFAPFAClientEvent hasEventMetadata]
+ -[PFAPFAClientEvent setEventMetadata:]
+ -[PFAPFAClientEvent setHasEventMetadata:]
+ -[PFAPFADeviceDimensions .cxx_destruct]
+ -[PFAPFADeviceDimensions deleteDeviceType]
+ -[PFAPFADeviceDimensions deleteProgramCode]
+ -[PFAPFADeviceDimensions deleteSystemBuild]
+ -[PFAPFADeviceDimensions deviceType]
+ -[PFAPFADeviceDimensions dictionaryRepresentation]
+ -[PFAPFADeviceDimensions hasDeviceType]
+ -[PFAPFADeviceDimensions hasProgramCode]
+ -[PFAPFADeviceDimensions hasSystemBuild]
+ -[PFAPFADeviceDimensions hash]
+ -[PFAPFADeviceDimensions initWithDictionary:]
+ -[PFAPFADeviceDimensions initWithJSON:]
+ -[PFAPFADeviceDimensions isEqual:]
+ -[PFAPFADeviceDimensions jsonData]
+ -[PFAPFADeviceDimensions programCode]
+ -[PFAPFADeviceDimensions readFrom:]
+ -[PFAPFADeviceDimensions setDeviceType:]
+ -[PFAPFADeviceDimensions setHasDeviceType:]
+ -[PFAPFADeviceDimensions setHasProgramCode:]
+ -[PFAPFADeviceDimensions setHasSystemBuild:]
+ -[PFAPFADeviceDimensions setProgramCode:]
+ -[PFAPFADeviceDimensions setSystemBuild:]
+ -[PFAPFADeviceDimensions systemBuild]
+ -[PFAPFADeviceDimensions writeTo:]
+ -[PFAPFADeviceDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[PFAPFAEventMetadata .cxx_destruct]
+ -[PFAPFAEventMetadata deleteDeviceDimensions]
+ -[PFAPFAEventMetadata deleteEventTimestampInMsSince1970]
+ -[PFAPFAEventMetadata deviceDimensions]
+ -[PFAPFAEventMetadata dictionaryRepresentation]
+ -[PFAPFAEventMetadata eventTimestampInMsSince1970]
+ -[PFAPFAEventMetadata hasDeviceDimensions]
+ -[PFAPFAEventMetadata hasEventTimestampInMsSince1970]
+ -[PFAPFAEventMetadata hash]
+ -[PFAPFAEventMetadata initWithDictionary:]
+ -[PFAPFAEventMetadata initWithJSON:]
+ -[PFAPFAEventMetadata isEqual:]
+ -[PFAPFAEventMetadata jsonData]
+ -[PFAPFAEventMetadata readFrom:]
+ -[PFAPFAEventMetadata setDeviceDimensions:]
+ -[PFAPFAEventMetadata setEventTimestampInMsSince1970:]
+ -[PFAPFAEventMetadata setHasDeviceDimensions:]
+ -[PFAPFAEventMetadata setHasEventTimestampInMsSince1970:]
+ -[PFAPFAEventMetadata writeTo:]
+ -[PFAPFAEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PFAPFAEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[POMMESSchemaPOMMESPegasusResponseServerDrivenContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent deleteEnrollmentUtteranceDetected]
+ -[SIRISETUPSchemaSIRISETUPClientEvent enrollmentUtteranceDetected]
+ -[SIRISETUPSchemaSIRISETUPClientEvent hasEnrollmentUtteranceDetected]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setEnrollmentUtteranceDetected:]
+ -[SIRISETUPSchemaSIRISETUPClientEvent setHasEnrollmentUtteranceDetected:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected .cxx_destruct]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected audioId]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected deleteAudioId]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected deletePageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected dictionaryRepresentation]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected hasAudioId]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected hasPageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected hash]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected initWithDictionary:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected initWithJSON:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected isEqual:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected jsonData]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected pageNumber]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected readFrom:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected setAudioId:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected setHasAudioId:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected setHasPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected setPageNumber:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected writeTo:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaUEIUUFRReady(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[TTMSchemaTTMNeuralCombinerRequestEnded deleteMitigationAssetVersion]
+ -[TTMSchemaTTMNeuralCombinerRequestEnded hasMitigationAssetVersion]
+ -[TTMSchemaTTMNeuralCombinerRequestEnded mitigationAssetVersion]
+ -[TTMSchemaTTMNeuralCombinerRequestEnded setHasMitigationAssetVersion:]
+ -[TTMSchemaTTMNeuralCombinerRequestEnded setMitigationAssetVersion:]
+ OBJC_IVAR_$_DIMSchemaDIMExperimentContext._experimentalBucketId
+ OBJC_IVAR_$_DIMSchemaDIMExperimentContext._has
+ OBJC_IVAR_$_MHSchemaMHUnintendedResponseSuppressionEnded._mitigationAssetVersion
+ OBJC_IVAR_$_MHSchemaMHUnintendedResponseSuppressionEnded._speakerIDThreshold
+ OBJC_IVAR_$_PFAPFAClientEvent._eventMetadata
+ OBJC_IVAR_$_PFAPFADeviceDimensions._deviceType
+ OBJC_IVAR_$_PFAPFADeviceDimensions._has
+ OBJC_IVAR_$_PFAPFADeviceDimensions._programCode
+ OBJC_IVAR_$_PFAPFADeviceDimensions._systemBuild
+ OBJC_IVAR_$_PFAPFAEventMetadata._deviceDimensions
+ OBJC_IVAR_$_PFAPFAEventMetadata._eventTimestampInMsSince1970
+ OBJC_IVAR_$_PFAPFAEventMetadata._has
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._enrollmentUtteranceDetected
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected._audioId
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected._has
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected._pageNumber
+ OBJC_IVAR_$_TTMSchemaTTMNeuralCombinerRequestEnded._mitigationAssetVersion
+ _OBJC_CLASS_$_PFAPFADeviceDimensions
+ _OBJC_CLASS_$_PFAPFAEventMetadata
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ _OBJC_IVAR_$_MHSchemaMHUnintendedResponseSuppressionEnded._hasMitigationAssetVersion
+ _OBJC_IVAR_$_PFAPFAClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_PFAPFADeviceDimensions._hasDeviceType
+ _OBJC_IVAR_$_PFAPFADeviceDimensions._hasSystemBuild
+ _OBJC_IVAR_$_PFAPFAEventMetadata._hasDeviceDimensions
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPClientEvent._hasEnrollmentUtteranceDetected
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected._hasAudioId
+ _OBJC_IVAR_$_TTMSchemaTTMNeuralCombinerRequestEnded._hasMitigationAssetVersion
+ _OBJC_METACLASS_$_PFAPFADeviceDimensions
+ _OBJC_METACLASS_$_PFAPFAEventMetadata
+ _OBJC_METACLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ _PFAPFADeviceDimensionsReadFrom
+ _PFAPFAEventMetadataReadFrom
+ _SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetectedReadFrom
+ __OBJC_$_INSTANCE_METHODS_PFAPFADeviceDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PFAPFAEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_PFAPFADeviceDimensions
+ __OBJC_$_INSTANCE_VARIABLES_PFAPFAEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ __OBJC_$_PROP_LIST_PFAPFADeviceDimensions
+ __OBJC_$_PROP_LIST_PFAPFAEventMetadata
+ __OBJC_$_PROP_LIST_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ __OBJC_CLASS_RO_$_PFAPFADeviceDimensions
+ __OBJC_CLASS_RO_$_PFAPFAEventMetadata
+ __OBJC_CLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ __OBJC_METACLASS_RO_$_PFAPFADeviceDimensions
+ __OBJC_METACLASS_RO_$_PFAPFAEventMetadata
+ __OBJC_METACLASS_RO_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected
+ _objc_msgSend$audioId
+ _objc_msgSend$deleteAudioId
+ _objc_msgSend$deleteCatId
+ _objc_msgSend$deleteDeviceDimensions
+ _objc_msgSend$deleteDialogIdentifier
+ _objc_msgSend$deleteDialogIdentifiers
+ _objc_msgSend$deleteEnrollmentUtteranceDetected
+ _objc_msgSend$deleteExecutedPegasusDomain
+ _objc_msgSend$deviceDimensions
+ _objc_msgSend$enrollmentUtteranceDetected
+ _objc_msgSend$experimentalBucketId
+ _objc_msgSend$setAudioId:
+ _objc_msgSend$setDeviceDimensions:
+ _objc_msgSend$setEnrollmentUtteranceDetected:
+ _objc_msgSend$setExperimentalBucketId:
+ _objc_msgSend$setSpeakerIDThreshold:
+ _objc_msgSend$speakerIDThreshold
+ _qname_SIRISETUPSchemaSIRISETUPClientEvent_WhichEvent_Type_enrollmentUtteranceDetected
CStrings:
+ "@\"PFAPFADeviceDimensions\""
+ "@\"PFAPFAEventMetadata\""
+ "@\"SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected\""
+ "PFAPFADeviceDimensions"
+ "PFAPFAEventMetadata"
+ "SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected"
+ "T@\"PFAPFADeviceDimensions\",&,N,V_deviceDimensions"
+ "T@\"PFAPFAEventMetadata\",&,N,V_eventMetadata"
+ "T@\"SIRISETUPSchemaSIRISETUPPHSEnrollmentUtteranceDetected\",&,N,V_enrollmentUtteranceDetected"
+ "T@\"SISchemaUUID\",&,N,V_audioId"
+ "TB,N,V_hasAudioId"
+ "TB,N,V_hasDeviceDimensions"
+ "TB,N,V_hasEnrollmentUtteranceDetected"
+ "TI,N,V_experimentalBucketId"
+ "Tf,N,V_speakerIDThreshold"
+ "_audioId"
+ "_deviceDimensions"
+ "_enrollmentUtteranceDetected"
+ "_experimentalBucketId"
+ "_hasAudioId"
+ "_hasDeviceDimensions"
+ "_hasEnrollmentUtteranceDetected"
+ "_speakerIDThreshold"
+ "audioId"
+ "com.apple.aiml.siri.setup.SIRISETUPClientEvent.SIRISETUPPHSEnrollmentUtteranceDetected"
+ "deleteAudioId"
+ "deleteDeviceDimensions"
+ "deleteEnrollmentUtteranceDetected"
+ "deleteExperimentalBucketId"
+ "deleteSpeakerIDThreshold"
+ "deviceDimensions"
+ "enrollmentUtteranceDetected"
+ "experimentalBucketId"
+ "hasAudioId"
+ "hasDeviceDimensions"
+ "hasEnrollmentUtteranceDetected"
+ "hasExperimentalBucketId"
+ "hasSpeakerIDThreshold"
+ "setAudioId:"
+ "setDeviceDimensions:"
+ "setEnrollmentUtteranceDetected:"
+ "setExperimentalBucketId:"
+ "setHasAudioId:"
+ "setHasDeviceDimensions:"
+ "setHasEnrollmentUtteranceDetected:"
+ "setHasExperimentalBucketId:"
+ "setHasSpeakerIDThreshold:"
+ "setSpeakerIDThreshold:"
+ "speakerIDThreshold"
+ "{?=\"experimentalBucketId\"b1}"
+ "{?=\"pageNumber\"b1}"
+ "{?=\"score\"b1\"threshold\"b1\"speakerIDThreshold\"b1}"

```
