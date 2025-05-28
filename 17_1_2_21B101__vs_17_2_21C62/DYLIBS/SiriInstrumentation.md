## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3301.10.2.0.0
-  __TEXT.__text: 0x6132c4
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x86c08
-  __TEXT.__const: 0xa7fc
-  __TEXT.__constg_swiftt: 0x453c
-  __TEXT.__swift5_typeref: 0xf8f
-  __TEXT.__swift5_builtin: 0x27ec
-  __TEXT.__swift5_reflstr: 0x12f
+3302.16.1.0.0
+  __TEXT.__text: 0x63b734
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_methlist: 0x89f30
+  __TEXT.__const: 0xac3c
+  __TEXT.__constg_swiftt: 0x46b4
+  __TEXT.__swift5_typeref: 0x10db
+  __TEXT.__swift5_builtin: 0x288c
+  __TEXT.__swift5_reflstr: 0x182
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x860
-  __TEXT.__swift5_types: 0x830
-  __TEXT.__cstring: 0x4226d
-  __TEXT.__swift5_fieldmd: 0x234
+  __TEXT.__swift5_proto: 0x89c
+  __TEXT.__swift5_types: 0x858
+  __TEXT.__cstring: 0x43409
+  __TEXT.__swift5_fieldmd: 0x2c0
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1b338
-  __TEXT.__eh_frame: 0x528
-  __TEXT.__objc_classname: 0xdda3
-  __TEXT.__objc_methname: 0xc2a9b
-  __TEXT.__objc_methtype: 0x1b1d8
-  __TEXT.__objc_stubs: 0x472c0
+  __TEXT.__unwind_info: 0x1bf68
+  __TEXT.__eh_frame: 0x680
+  __TEXT.__objc_classname: 0xe238
+  __TEXT.__objc_methname: 0xc7271
+  __TEXT.__objc_methtype: 0x1bae9
+  __TEXT.__objc_stubs: 0x48f80
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x24a90
-  __DATA_CONST.__objc_classlist: 0x30b0
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x250c0
+  __DATA_CONST.__objc_classlist: 0x31c0
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x99a68
-  __DATA_CONST.__objc_selrefs: 0x256c8
-  __AUTH_CONST.__const: 0x628
-  __AUTH_CONST.__cfstring: 0x49aa0
-  __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__objc_const: 0x1128
+  __DATA_CONST.__objc_const: 0x9d500
+  __DATA_CONST.__objc_selrefs: 0x265c8
+  __AUTH_CONST.__const: 0x918
+  __AUTH_CONST.__cfstring: 0x4ae80
+  __AUTH_CONST.__auth_ptr: 0x58
+  __AUTH_CONST.__objc_const: 0x1b40
   __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__auth_got: 0x738
-  __AUTH.__objc_data: 0xf50
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x3068
-  __DATA.__objc_superrefs: 0x4968
-  __DATA.__objc_ivar: 0x8f90
-  __DATA.__data: 0x1308
-  __DATA.__bss: 0x10800
-  __DATA.__common: 0x20
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH.__objc_data: 0x19f0
+  __DATA.__objc_protorefs: 0x10
+  __DATA.__objc_classrefs: 0x3168
+  __DATA.__objc_superrefs: 0x4b50
+  __DATA.__objc_ivar: 0x9314
+  __DATA.__data: 0x13b8
+  __DATA.__bss: 0x10f80
+  __DATA.__common: 0x28
   __DATA_DIRTY.__const: 0x40d8
   __DATA_DIRTY.__objc_const: 0x1ba58
-  __DATA_DIRTY.__objc_data: 0x1d988
+  __DATA_DIRTY.__objc_data: 0x1d9c8
   __DATA_DIRTY.__data: 0x5e8
   __DATA_DIRTY.__bss: 0x300
   __DATA_DIRTY.__common: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 48750
-  Symbols:   121657
-  CStrings:  43424
+  Functions: 49985
+  Symbols:   124569
+  CStrings:  44426
 
Symbols:
+ +[ODDSiriSchemaODDSiriClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[CDASchemaCDAParticipant .cxx_destruct]
+ -[CDASchemaCDAParticipant deleteElectionParticipantId]
+ -[CDASchemaCDAParticipant deleteRotatedElectionParticipantId]
+ -[CDASchemaCDAParticipant electionParticipantId]
+ -[CDASchemaCDAParticipant hasElectionParticipantId]
+ -[CDASchemaCDAParticipant hasRotatedElectionParticipantId]
+ -[CDASchemaCDAParticipant rotatedElectionParticipantId]
+ -[CDASchemaCDAParticipant setElectionParticipantId:]
+ -[CDASchemaCDAParticipant setHasElectionParticipantId:]
+ -[CDASchemaCDAParticipant setHasRotatedElectionParticipantId:]
+ -[CDASchemaCDAParticipant setRotatedElectionParticipantId:]
+ -[CDASchemaCDAParticipant(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMClientEvent deleteEphemeralIdentifiers]
+ -[DIMSchemaDIMClientEvent deleteEphemeralToAggregationIdentifierMap]
+ -[DIMSchemaDIMClientEvent deleteOnDeviceDigest]
+ -[DIMSchemaDIMClientEvent ephemeralIdentifiers]
+ -[DIMSchemaDIMClientEvent ephemeralToAggregationIdentifierMap]
+ -[DIMSchemaDIMClientEvent hasEphemeralIdentifiers]
+ -[DIMSchemaDIMClientEvent hasEphemeralToAggregationIdentifierMap]
+ -[DIMSchemaDIMClientEvent hasOnDeviceDigest]
+ -[DIMSchemaDIMClientEvent onDeviceDigest]
+ -[DIMSchemaDIMClientEvent setEphemeralIdentifiers:]
+ -[DIMSchemaDIMClientEvent setEphemeralToAggregationIdentifierMap:]
+ -[DIMSchemaDIMClientEvent setHasEphemeralIdentifiers:]
+ -[DIMSchemaDIMClientEvent setHasEphemeralToAggregationIdentifierMap:]
+ -[DIMSchemaDIMClientEvent setHasOnDeviceDigest:]
+ -[DIMSchemaDIMClientEvent setOnDeviceDigest:]
+ -[DIMSchemaDIMDeviceFixedContext availableDictationKeyboards]
+ -[DIMSchemaDIMDeviceFixedContext deleteAvailableDictationKeyboards]
+ -[DIMSchemaDIMDeviceFixedContext hasAvailableDictationKeyboards]
+ -[DIMSchemaDIMDeviceFixedContext setAvailableDictationKeyboards:]
+ -[DIMSchemaDIMDeviceFixedContext setHasAvailableDictationKeyboards:]
+ -[DIMSchemaDIMEphemeralIdentifiers .cxx_destruct]
+ -[DIMSchemaDIMEphemeralIdentifiers deleteHomeEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers deleteSecondsSinceEphemeralIdCreation]
+ -[DIMSchemaDIMEphemeralIdentifiers deleteUserEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers dictionaryRepresentation]
+ -[DIMSchemaDIMEphemeralIdentifiers hasHomeEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers hasSecondsSinceEphemeralIdCreation]
+ -[DIMSchemaDIMEphemeralIdentifiers hasUserEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers hash]
+ -[DIMSchemaDIMEphemeralIdentifiers homeEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers initWithDictionary:]
+ -[DIMSchemaDIMEphemeralIdentifiers initWithJSON:]
+ -[DIMSchemaDIMEphemeralIdentifiers isEqual:]
+ -[DIMSchemaDIMEphemeralIdentifiers jsonData]
+ -[DIMSchemaDIMEphemeralIdentifiers readFrom:]
+ -[DIMSchemaDIMEphemeralIdentifiers secondsSinceEphemeralIdCreation]
+ -[DIMSchemaDIMEphemeralIdentifiers setHasHomeEphemeralId:]
+ -[DIMSchemaDIMEphemeralIdentifiers setHasSecondsSinceEphemeralIdCreation:]
+ -[DIMSchemaDIMEphemeralIdentifiers setHasUserEphemeralId:]
+ -[DIMSchemaDIMEphemeralIdentifiers setHomeEphemeralId:]
+ -[DIMSchemaDIMEphemeralIdentifiers setSecondsSinceEphemeralIdCreation:]
+ -[DIMSchemaDIMEphemeralIdentifiers setUserEphemeralId:]
+ -[DIMSchemaDIMEphemeralIdentifiers userEphemeralId]
+ -[DIMSchemaDIMEphemeralIdentifiers writeTo:]
+ -[DIMSchemaDIMEphemeralIdentifiers(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMEphemeralIdentifiers(SensitiveConditions) suppressMessageUnderConditions]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap .cxx_destruct]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deleteDeviceAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deleteUserAggregationIdExpirationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deleteUserAggregationIdRotationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deleteUserAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deleteUserEphemeralId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap deviceAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap dictionaryRepresentation]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hasDeviceAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hasUserAggregationIdExpirationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hasUserAggregationIdRotationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hasUserAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hasUserEphemeralId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap hash]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap initWithDictionary:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap initWithJSON:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap isEqual:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap jsonData]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap readFrom:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setDeviceAggregationId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setHasDeviceAggregationId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setHasUserAggregationId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setHasUserAggregationIdExpirationTimestampMs:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setHasUserAggregationIdRotationTimestampMs:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setHasUserEphemeralId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setUserAggregationId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setUserAggregationIdExpirationTimestampMs:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setUserAggregationIdRotationTimestampMs:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap setUserEphemeralId:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap userAggregationIdExpirationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap userAggregationIdRotationTimestampMs]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap userAggregationId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap userEphemeralId]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap writeTo:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[DIMSchemaDIMEphemeralToAggregationIdentifierMap(SensitiveConditions) suppressMessageUnderConditions]
+ -[DIMSchemaDIMOnDeviceDigest daysWithTwoAssistantSpeechRequestsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest daysWithTwoValidAssistantTurnsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest deleteDaysWithTwoAssistantSpeechRequestsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest deleteDaysWithTwoValidAssistantTurnsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest dictionaryRepresentation]
+ -[DIMSchemaDIMOnDeviceDigest hasDaysWithTwoAssistantSpeechRequestsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest hasDaysWithTwoValidAssistantTurnsPerWeek]
+ -[DIMSchemaDIMOnDeviceDigest hash]
+ -[DIMSchemaDIMOnDeviceDigest initWithDictionary:]
+ -[DIMSchemaDIMOnDeviceDigest initWithJSON:]
+ -[DIMSchemaDIMOnDeviceDigest isEqual:]
+ -[DIMSchemaDIMOnDeviceDigest jsonData]
+ -[DIMSchemaDIMOnDeviceDigest readFrom:]
+ -[DIMSchemaDIMOnDeviceDigest setDaysWithTwoAssistantSpeechRequestsPerWeek:]
+ -[DIMSchemaDIMOnDeviceDigest setDaysWithTwoValidAssistantTurnsPerWeek:]
+ -[DIMSchemaDIMOnDeviceDigest setHasDaysWithTwoAssistantSpeechRequestsPerWeek:]
+ -[DIMSchemaDIMOnDeviceDigest setHasDaysWithTwoValidAssistantTurnsPerWeek:]
+ -[DIMSchemaDIMOnDeviceDigest writeTo:]
+ -[DIMSchemaDIMOnDeviceDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[HALSchemaHALClientEvent deleteNearbyPersonalDevicesReported]
+ -[HALSchemaHALClientEvent hasNearbyPersonalDevicesReported]
+ -[HALSchemaHALClientEvent nearbyPersonalDevicesReported]
+ -[HALSchemaHALClientEvent setHasNearbyPersonalDevicesReported:]
+ -[HALSchemaHALClientEvent setNearbyPersonalDevicesReported:]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteIMacCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteIPadCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteIPhoneCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteMacBookCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteMacStudioCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported deleteWatchCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported dictionaryRepresentation]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasIMacCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasIPadCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasIPhoneCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasMacBookCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasMacStudioCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hasWatchCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported hash]
+ -[HALSchemaHALNearbyPersonalDevicesReported iMacCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported iPadCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported iPhoneCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported initWithDictionary:]
+ -[HALSchemaHALNearbyPersonalDevicesReported initWithJSON:]
+ -[HALSchemaHALNearbyPersonalDevicesReported isEqual:]
+ -[HALSchemaHALNearbyPersonalDevicesReported jsonData]
+ -[HALSchemaHALNearbyPersonalDevicesReported macBookCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported macStudioCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported readFrom:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasIMacCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasIPadCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasIPhoneCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasMacBookCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasMacStudioCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setHasWatchCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setIMacCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setIPadCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setIPhoneCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setMacBookCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setMacStudioCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported setWatchCount:]
+ -[HALSchemaHALNearbyPersonalDevicesReported watchCount]
+ -[HALSchemaHALNearbyPersonalDevicesReported writeTo:]
+ -[HALSchemaHALNearbyPersonalDevicesReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[HomeKitSchemaHKAudioTopologyReported deleteIsLeader]
+ -[HomeKitSchemaHKAudioTopologyReported hasIsLeader]
+ -[HomeKitSchemaHKAudioTopologyReported isLeader]
+ -[HomeKitSchemaHKAudioTopologyReported setHasIsLeader:]
+ -[HomeKitSchemaHKAudioTopologyReported setIsLeader:]
+ -[IDENTITYSchemaIDENTITYScoreTuple deleteUserEphemeralId]
+ -[IDENTITYSchemaIDENTITYScoreTuple hasUserEphemeralId]
+ -[IDENTITYSchemaIDENTITYScoreTuple setHasUserEphemeralId:]
+ -[IDENTITYSchemaIDENTITYScoreTuple setUserEphemeralId:]
+ -[IDENTITYSchemaIDENTITYScoreTuple userEphemeralId]
+ -[IDENTITYSchemaIDENTITYScoreTuple(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata deleteUserEphemeralId]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata hasUserEphemeralId]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata setHasUserEphemeralId:]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata setUserEphemeralId:]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata userEphemeralId]
+ -[IDENTITYSchemaIDENTITYUserPresenceMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteIsBoltEnabled]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteIsCommonForegroundApp]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals deleteIsRawLastNowPlayingBoolean]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasIsBoltEnabled]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasIsCommonForegroundApp]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals hasIsRawLastNowPlayingBoolean]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals isBoltEnabled]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals isCommonForegroundApp]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals isRawLastNowPlayingBoolean]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasIsBoltEnabled:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasIsCommonForegroundApp:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setHasIsRawLastNowPlayingBoolean:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setIsBoltEnabled:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setIsCommonForegroundApp:]
+ -[INFERENCESchemaINFERENCEMusicTrainingDependentSignals setIsRawLastNowPlayingBoolean:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteIsContentFree]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals deleteIsUserRecognized]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasIsContentFree]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals hasIsUserRecognized]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals isContentFree]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals isUserRecognized]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasIsContentFree:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setHasIsUserRecognized:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setIsContentFree:]
+ -[INFERENCESchemaINFERENCEMusicTrainingIndependentSignals setIsUserRecognized:]
+ -[ODDSiriSchemaODDAssistantCounts .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantCounts deleteReliabilityCounts]
+ -[ODDSiriSchemaODDAssistantCounts deleteTaskCounts]
+ -[ODDSiriSchemaODDAssistantCounts deleteTurnCounts]
+ -[ODDSiriSchemaODDAssistantCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantCounts hasReliabilityCounts]
+ -[ODDSiriSchemaODDAssistantCounts hasTaskCounts]
+ -[ODDSiriSchemaODDAssistantCounts hasTurnCounts]
+ -[ODDSiriSchemaODDAssistantCounts hash]
+ -[ODDSiriSchemaODDAssistantCounts initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantCounts initWithJSON:]
+ -[ODDSiriSchemaODDAssistantCounts isEqual:]
+ -[ODDSiriSchemaODDAssistantCounts jsonData]
+ -[ODDSiriSchemaODDAssistantCounts readFrom:]
+ -[ODDSiriSchemaODDAssistantCounts reliabilityCounts]
+ -[ODDSiriSchemaODDAssistantCounts setHasReliabilityCounts:]
+ -[ODDSiriSchemaODDAssistantCounts setHasTaskCounts:]
+ -[ODDSiriSchemaODDAssistantCounts setHasTurnCounts:]
+ -[ODDSiriSchemaODDAssistantCounts setReliabilityCounts:]
+ -[ODDSiriSchemaODDAssistantCounts setTaskCounts:]
+ -[ODDSiriSchemaODDAssistantCounts setTurnCounts:]
+ -[ODDSiriSchemaODDAssistantCounts taskCounts]
+ -[ODDSiriSchemaODDAssistantCounts turnCounts]
+ -[ODDSiriSchemaODDAssistantCounts writeTo:]
+ -[ODDSiriSchemaODDAssistantCounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported addDigests:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported clearDigests]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported digestsCount]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported digests]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported hash]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported isEqual:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported jsonData]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported readFrom:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported setDigests:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported writeTo:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantDeviceDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDigest .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantDigest counts]
+ -[ODDSiriSchemaODDAssistantDigest deleteCounts]
+ -[ODDSiriSchemaODDAssistantDigest deleteDimensions]
+ -[ODDSiriSchemaODDAssistantDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantDigest dimensions]
+ -[ODDSiriSchemaODDAssistantDigest hasCounts]
+ -[ODDSiriSchemaODDAssistantDigest hasDimensions]
+ -[ODDSiriSchemaODDAssistantDigest hash]
+ -[ODDSiriSchemaODDAssistantDigest initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantDigest initWithJSON:]
+ -[ODDSiriSchemaODDAssistantDigest isEqual:]
+ -[ODDSiriSchemaODDAssistantDigest jsonData]
+ -[ODDSiriSchemaODDAssistantDigest readFrom:]
+ -[ODDSiriSchemaODDAssistantDigest setCounts:]
+ -[ODDSiriSchemaODDAssistantDigest setDimensions:]
+ -[ODDSiriSchemaODDAssistantDigest setHasCounts:]
+ -[ODDSiriSchemaODDAssistantDigest setHasDimensions:]
+ -[ODDSiriSchemaODDAssistantDigest writeTo:]
+ -[ODDSiriSchemaODDAssistantDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDAssistantDimensions asrLocation]
+ -[ODDSiriSchemaODDAssistantDimensions audioInterfaceProductId]
+ -[ODDSiriSchemaODDAssistantDimensions audioInterfaceVendorId]
+ -[ODDSiriSchemaODDAssistantDimensions dataSharingOptInStatus]
+ -[ODDSiriSchemaODDAssistantDimensions deleteAsrLocation]
+ -[ODDSiriSchemaODDAssistantDimensions deleteAudioInterfaceProductId]
+ -[ODDSiriSchemaODDAssistantDimensions deleteAudioInterfaceVendorId]
+ -[ODDSiriSchemaODDAssistantDimensions deleteDataSharingOptInStatus]
+ -[ODDSiriSchemaODDAssistantDimensions deleteNlLocation]
+ -[ODDSiriSchemaODDAssistantDimensions deleteSiriInputLocale]
+ -[ODDSiriSchemaODDAssistantDimensions deleteSubDomain]
+ -[ODDSiriSchemaODDAssistantDimensions deleteSystemBuild]
+ -[ODDSiriSchemaODDAssistantDimensions deleteViewInterface]
+ -[ODDSiriSchemaODDAssistantDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDAssistantDimensions hasAsrLocation]
+ -[ODDSiriSchemaODDAssistantDimensions hasAudioInterfaceProductId]
+ -[ODDSiriSchemaODDAssistantDimensions hasAudioInterfaceVendorId]
+ -[ODDSiriSchemaODDAssistantDimensions hasDataSharingOptInStatus]
+ -[ODDSiriSchemaODDAssistantDimensions hasNlLocation]
+ -[ODDSiriSchemaODDAssistantDimensions hasSiriInputLocale]
+ -[ODDSiriSchemaODDAssistantDimensions hasSubDomain]
+ -[ODDSiriSchemaODDAssistantDimensions hasSystemBuild]
+ -[ODDSiriSchemaODDAssistantDimensions hasViewInterface]
+ -[ODDSiriSchemaODDAssistantDimensions hash]
+ -[ODDSiriSchemaODDAssistantDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDAssistantDimensions initWithJSON:]
+ -[ODDSiriSchemaODDAssistantDimensions isEqual:]
+ -[ODDSiriSchemaODDAssistantDimensions jsonData]
+ -[ODDSiriSchemaODDAssistantDimensions nlLocation]
+ -[ODDSiriSchemaODDAssistantDimensions readFrom:]
+ -[ODDSiriSchemaODDAssistantDimensions setAsrLocation:]
+ -[ODDSiriSchemaODDAssistantDimensions setAudioInterfaceProductId:]
+ -[ODDSiriSchemaODDAssistantDimensions setAudioInterfaceVendorId:]
+ -[ODDSiriSchemaODDAssistantDimensions setDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasAsrLocation:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasAudioInterfaceProductId:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasAudioInterfaceVendorId:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasNlLocation:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasSiriInputLocale:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasSubDomain:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasSystemBuild:]
+ -[ODDSiriSchemaODDAssistantDimensions setHasViewInterface:]
+ -[ODDSiriSchemaODDAssistantDimensions setNlLocation:]
+ -[ODDSiriSchemaODDAssistantDimensions setSiriInputLocale:]
+ -[ODDSiriSchemaODDAssistantDimensions setSubDomain:]
+ -[ODDSiriSchemaODDAssistantDimensions setSystemBuild:]
+ -[ODDSiriSchemaODDAssistantDimensions setViewInterface:]
+ -[ODDSiriSchemaODDAssistantDimensions siriInputLocale]
+ -[ODDSiriSchemaODDAssistantDimensions subDomain]
+ -[ODDSiriSchemaODDAssistantDimensions systemBuild]
+ -[ODDSiriSchemaODDAssistantDimensions viewInterface]
+ -[ODDSiriSchemaODDAssistantDimensions writeTo:]
+ -[ODDSiriSchemaODDAssistantDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDAssistantDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDClientEventMetadata .cxx_destruct]
+ -[ODDSiriSchemaODDClientEventMetadata aggregationInterval]
+ -[ODDSiriSchemaODDClientEventMetadata deleteAggregationInterval]
+ -[ODDSiriSchemaODDClientEventMetadata deleteDeviceAggregationId]
+ -[ODDSiriSchemaODDClientEventMetadata deleteEventTimestampInMsSince1970]
+ -[ODDSiriSchemaODDClientEventMetadata deleteOddId]
+ -[ODDSiriSchemaODDClientEventMetadata deviceAggregationId]
+ -[ODDSiriSchemaODDClientEventMetadata dictionaryRepresentation]
+ -[ODDSiriSchemaODDClientEventMetadata eventTimestampInMsSince1970]
+ -[ODDSiriSchemaODDClientEventMetadata hasAggregationInterval]
+ -[ODDSiriSchemaODDClientEventMetadata hasDeviceAggregationId]
+ -[ODDSiriSchemaODDClientEventMetadata hasEventTimestampInMsSince1970]
+ -[ODDSiriSchemaODDClientEventMetadata hasOddId]
+ -[ODDSiriSchemaODDClientEventMetadata hash]
+ -[ODDSiriSchemaODDClientEventMetadata initWithDictionary:]
+ -[ODDSiriSchemaODDClientEventMetadata initWithJSON:]
+ -[ODDSiriSchemaODDClientEventMetadata isEqual:]
+ -[ODDSiriSchemaODDClientEventMetadata jsonData]
+ -[ODDSiriSchemaODDClientEventMetadata oddId]
+ -[ODDSiriSchemaODDClientEventMetadata readFrom:]
+ -[ODDSiriSchemaODDClientEventMetadata setAggregationInterval:]
+ -[ODDSiriSchemaODDClientEventMetadata setDeviceAggregationId:]
+ -[ODDSiriSchemaODDClientEventMetadata setEventTimestampInMsSince1970:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasAggregationInterval:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasDeviceAggregationId:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasEventTimestampInMsSince1970:]
+ -[ODDSiriSchemaODDClientEventMetadata setHasOddId:]
+ -[ODDSiriSchemaODDClientEventMetadata setOddId:]
+ -[ODDSiriSchemaODDClientEventMetadata writeTo:]
+ -[ODDSiriSchemaODDClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceCohort .cxx_destruct]
+ -[ODDSiriSchemaODDDeviceCohort cohortDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceCohort cohortInterval]
+ -[ODDSiriSchemaODDDeviceCohort cohortType]
+ -[ODDSiriSchemaODDDeviceCohort deleteCohortDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceCohort deleteCohortInterval]
+ -[ODDSiriSchemaODDDeviceCohort deleteCohortType]
+ -[ODDSiriSchemaODDDeviceCohort dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceCohort hasCohortDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceCohort hasCohortInterval]
+ -[ODDSiriSchemaODDDeviceCohort hasCohortType]
+ -[ODDSiriSchemaODDDeviceCohort hash]
+ -[ODDSiriSchemaODDDeviceCohort initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceCohort initWithJSON:]
+ -[ODDSiriSchemaODDDeviceCohort isEqual:]
+ -[ODDSiriSchemaODDDeviceCohort jsonData]
+ -[ODDSiriSchemaODDDeviceCohort readFrom:]
+ -[ODDSiriSchemaODDDeviceCohort setCohortDataAvailabilityState:]
+ -[ODDSiriSchemaODDDeviceCohort setCohortInterval:]
+ -[ODDSiriSchemaODDDeviceCohort setCohortType:]
+ -[ODDSiriSchemaODDDeviceCohort setHasCohortDataAvailabilityState:]
+ -[ODDSiriSchemaODDDeviceCohort setHasCohortInterval:]
+ -[ODDSiriSchemaODDDeviceCohort setHasCohortType:]
+ -[ODDSiriSchemaODDDeviceCohort writeTo:]
+ -[ODDSiriSchemaODDDeviceCohort(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDeviceCohort(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceCohortsReported .cxx_destruct]
+ -[ODDSiriSchemaODDDeviceCohortsReported addCohorts:]
+ -[ODDSiriSchemaODDDeviceCohortsReported clearCohorts]
+ -[ODDSiriSchemaODDDeviceCohortsReported cohortsAtIndex:]
+ -[ODDSiriSchemaODDDeviceCohortsReported cohortsCount]
+ -[ODDSiriSchemaODDDeviceCohortsReported cohorts]
+ -[ODDSiriSchemaODDDeviceCohortsReported deleteCohorts]
+ -[ODDSiriSchemaODDDeviceCohortsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceCohortsReported hash]
+ -[ODDSiriSchemaODDDeviceCohortsReported initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceCohortsReported initWithJSON:]
+ -[ODDSiriSchemaODDDeviceCohortsReported isEqual:]
+ -[ODDSiriSchemaODDDeviceCohortsReported jsonData]
+ -[ODDSiriSchemaODDDeviceCohortsReported readFrom:]
+ -[ODDSiriSchemaODDDeviceCohortsReported setCohorts:]
+ -[ODDSiriSchemaODDDeviceCohortsReported writeTo:]
+ -[ODDSiriSchemaODDDeviceCohortsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDeviceCohortsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceSegment deleteSegmentDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceSegment deleteSegmentType]
+ -[ODDSiriSchemaODDDeviceSegment dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceSegment hasSegmentDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceSegment hasSegmentType]
+ -[ODDSiriSchemaODDDeviceSegment hash]
+ -[ODDSiriSchemaODDDeviceSegment initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceSegment initWithJSON:]
+ -[ODDSiriSchemaODDDeviceSegment isEqual:]
+ -[ODDSiriSchemaODDDeviceSegment jsonData]
+ -[ODDSiriSchemaODDDeviceSegment readFrom:]
+ -[ODDSiriSchemaODDDeviceSegment segmentDataAvailabilityState]
+ -[ODDSiriSchemaODDDeviceSegment segmentType]
+ -[ODDSiriSchemaODDDeviceSegment setHasSegmentDataAvailabilityState:]
+ -[ODDSiriSchemaODDDeviceSegment setHasSegmentType:]
+ -[ODDSiriSchemaODDDeviceSegment setSegmentDataAvailabilityState:]
+ -[ODDSiriSchemaODDDeviceSegment setSegmentType:]
+ -[ODDSiriSchemaODDDeviceSegment writeTo:]
+ -[ODDSiriSchemaODDDeviceSegment(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDeviceSegmentsReported .cxx_destruct]
+ -[ODDSiriSchemaODDDeviceSegmentsReported addSegments:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported clearSegments]
+ -[ODDSiriSchemaODDDeviceSegmentsReported deleteSegments]
+ -[ODDSiriSchemaODDDeviceSegmentsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDDeviceSegmentsReported hash]
+ -[ODDSiriSchemaODDDeviceSegmentsReported initWithDictionary:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported initWithJSON:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported isEqual:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported jsonData]
+ -[ODDSiriSchemaODDDeviceSegmentsReported readFrom:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported segmentsAtIndex:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported segmentsCount]
+ -[ODDSiriSchemaODDDeviceSegmentsReported segments]
+ -[ODDSiriSchemaODDDeviceSegmentsReported setSegments:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported writeTo:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDeviceSegmentsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationCounts .cxx_destruct]
+ -[ODDSiriSchemaODDDictationCounts deleteTurnCounts]
+ -[ODDSiriSchemaODDDictationCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDDictationCounts hasTurnCounts]
+ -[ODDSiriSchemaODDDictationCounts hash]
+ -[ODDSiriSchemaODDDictationCounts initWithDictionary:]
+ -[ODDSiriSchemaODDDictationCounts initWithJSON:]
+ -[ODDSiriSchemaODDDictationCounts isEqual:]
+ -[ODDSiriSchemaODDDictationCounts jsonData]
+ -[ODDSiriSchemaODDDictationCounts readFrom:]
+ -[ODDSiriSchemaODDDictationCounts setHasTurnCounts:]
+ -[ODDSiriSchemaODDDictationCounts setTurnCounts:]
+ -[ODDSiriSchemaODDDictationCounts turnCounts]
+ -[ODDSiriSchemaODDDictationCounts writeTo:]
+ -[ODDSiriSchemaODDDictationCounts(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDictationCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported .cxx_destruct]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported addDigests:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported clearDigests]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported deleteDigests]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported digestsAtIndex:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported digestsCount]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported digests]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported fixedDimensions]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported hash]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported initWithDictionary:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported initWithJSON:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported isEqual:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported jsonData]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported readFrom:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported setDigests:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported writeTo:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDictationDeviceDigestsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationDigest .cxx_destruct]
+ -[ODDSiriSchemaODDDictationDigest counts]
+ -[ODDSiriSchemaODDDictationDigest deleteCounts]
+ -[ODDSiriSchemaODDDictationDigest deleteDimensions]
+ -[ODDSiriSchemaODDDictationDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDDictationDigest dimensions]
+ -[ODDSiriSchemaODDDictationDigest hasCounts]
+ -[ODDSiriSchemaODDDictationDigest hasDimensions]
+ -[ODDSiriSchemaODDDictationDigest hash]
+ -[ODDSiriSchemaODDDictationDigest initWithDictionary:]
+ -[ODDSiriSchemaODDDictationDigest initWithJSON:]
+ -[ODDSiriSchemaODDDictationDigest isEqual:]
+ -[ODDSiriSchemaODDDictationDigest jsonData]
+ -[ODDSiriSchemaODDDictationDigest readFrom:]
+ -[ODDSiriSchemaODDDictationDigest setCounts:]
+ -[ODDSiriSchemaODDDictationDigest setDimensions:]
+ -[ODDSiriSchemaODDDictationDigest setHasCounts:]
+ -[ODDSiriSchemaODDDictationDigest setHasDimensions:]
+ -[ODDSiriSchemaODDDictationDigest writeTo:]
+ -[ODDSiriSchemaODDDictationDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDictationDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDDictationDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDDictationDimensions asrLocation]
+ -[ODDSiriSchemaODDDictationDimensions audioInterfaceProductId]
+ -[ODDSiriSchemaODDDictationDimensions audioInterfaceVendorId]
+ -[ODDSiriSchemaODDDictationDimensions dataSharingOptInStatus]
+ -[ODDSiriSchemaODDDictationDimensions deleteAsrLocation]
+ -[ODDSiriSchemaODDDictationDimensions deleteAudioInterfaceProductId]
+ -[ODDSiriSchemaODDDictationDimensions deleteAudioInterfaceVendorId]
+ -[ODDSiriSchemaODDDictationDimensions deleteDataSharingOptInStatus]
+ -[ODDSiriSchemaODDDictationDimensions deleteDictationLocale]
+ -[ODDSiriSchemaODDDictationDimensions deleteSystemBuild]
+ -[ODDSiriSchemaODDDictationDimensions deleteViewInterface]
+ -[ODDSiriSchemaODDDictationDimensions dictationLocale]
+ -[ODDSiriSchemaODDDictationDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDDictationDimensions hasAsrLocation]
+ -[ODDSiriSchemaODDDictationDimensions hasAudioInterfaceProductId]
+ -[ODDSiriSchemaODDDictationDimensions hasAudioInterfaceVendorId]
+ -[ODDSiriSchemaODDDictationDimensions hasDataSharingOptInStatus]
+ -[ODDSiriSchemaODDDictationDimensions hasDictationLocale]
+ -[ODDSiriSchemaODDDictationDimensions hasSystemBuild]
+ -[ODDSiriSchemaODDDictationDimensions hasViewInterface]
+ -[ODDSiriSchemaODDDictationDimensions hash]
+ -[ODDSiriSchemaODDDictationDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDDictationDimensions initWithJSON:]
+ -[ODDSiriSchemaODDDictationDimensions isEqual:]
+ -[ODDSiriSchemaODDDictationDimensions jsonData]
+ -[ODDSiriSchemaODDDictationDimensions readFrom:]
+ -[ODDSiriSchemaODDDictationDimensions setAsrLocation:]
+ -[ODDSiriSchemaODDDictationDimensions setAudioInterfaceProductId:]
+ -[ODDSiriSchemaODDDictationDimensions setAudioInterfaceVendorId:]
+ -[ODDSiriSchemaODDDictationDimensions setDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDDictationDimensions setDictationLocale:]
+ -[ODDSiriSchemaODDDictationDimensions setHasAsrLocation:]
+ -[ODDSiriSchemaODDDictationDimensions setHasAudioInterfaceProductId:]
+ -[ODDSiriSchemaODDDictationDimensions setHasAudioInterfaceVendorId:]
+ -[ODDSiriSchemaODDDictationDimensions setHasDataSharingOptInStatus:]
+ -[ODDSiriSchemaODDDictationDimensions setHasDictationLocale:]
+ -[ODDSiriSchemaODDDictationDimensions setHasSystemBuild:]
+ -[ODDSiriSchemaODDDictationDimensions setHasViewInterface:]
+ -[ODDSiriSchemaODDDictationDimensions setSystemBuild:]
+ -[ODDSiriSchemaODDDictationDimensions setViewInterface:]
+ -[ODDSiriSchemaODDDictationDimensions systemBuild]
+ -[ODDSiriSchemaODDDictationDimensions viewInterface]
+ -[ODDSiriSchemaODDDictationDimensions writeTo:]
+ -[ODDSiriSchemaODDDictationDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDDictationDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDFixedDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDFixedDimensions deleteDeviceType]
+ -[ODDSiriSchemaODDFixedDimensions deleteProgramCode]
+ -[ODDSiriSchemaODDFixedDimensions deviceType]
+ -[ODDSiriSchemaODDFixedDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDFixedDimensions hasDeviceType]
+ -[ODDSiriSchemaODDFixedDimensions hasProgramCode]
+ -[ODDSiriSchemaODDFixedDimensions hash]
+ -[ODDSiriSchemaODDFixedDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDFixedDimensions initWithJSON:]
+ -[ODDSiriSchemaODDFixedDimensions isEqual:]
+ -[ODDSiriSchemaODDFixedDimensions jsonData]
+ -[ODDSiriSchemaODDFixedDimensions programCode]
+ -[ODDSiriSchemaODDFixedDimensions readFrom:]
+ -[ODDSiriSchemaODDFixedDimensions setDeviceType:]
+ -[ODDSiriSchemaODDFixedDimensions setHasDeviceType:]
+ -[ODDSiriSchemaODDFixedDimensions setHasProgramCode:]
+ -[ODDSiriSchemaODDFixedDimensions setProgramCode:]
+ -[ODDSiriSchemaODDFixedDimensions writeTo:]
+ -[ODDSiriSchemaODDFixedDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDReliabilityCounts clientErrorCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteClientErrorCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteFailureResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteFatalResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteReliabilityRequestCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteReliabilityTurnCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteSiriUnavailableResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts deleteUndesiredResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDReliabilityCounts failureResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts fatalResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasClientErrorCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasFailureResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasFatalResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasReliabilityRequestCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasReliabilityTurnCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasSiriUnavailableResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts hasUndesiredResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts hash]
+ -[ODDSiriSchemaODDReliabilityCounts initWithDictionary:]
+ -[ODDSiriSchemaODDReliabilityCounts initWithJSON:]
+ -[ODDSiriSchemaODDReliabilityCounts isEqual:]
+ -[ODDSiriSchemaODDReliabilityCounts jsonData]
+ -[ODDSiriSchemaODDReliabilityCounts readFrom:]
+ -[ODDSiriSchemaODDReliabilityCounts reliabilityRequestCount]
+ -[ODDSiriSchemaODDReliabilityCounts reliabilityTurnCount]
+ -[ODDSiriSchemaODDReliabilityCounts setClientErrorCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setFailureResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setFatalResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasClientErrorCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasFailureResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasFatalResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasReliabilityRequestCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasReliabilityTurnCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasSiriUnavailableResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setHasUndesiredResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setReliabilityRequestCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setReliabilityTurnCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setSiriUnavailableResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts setUndesiredResponseCount:]
+ -[ODDSiriSchemaODDReliabilityCounts siriUnavailableResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts undesiredResponseCount]
+ -[ODDSiriSchemaODDReliabilityCounts writeTo:]
+ -[ODDSiriSchemaODDReliabilityCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriAccountInformation .cxx_destruct]
+ -[ODDSiriSchemaODDSiriAccountInformation assistantId]
+ -[ODDSiriSchemaODDSiriAccountInformation deleteAssistantId]
+ -[ODDSiriSchemaODDSiriAccountInformation dictionaryRepresentation]
+ -[ODDSiriSchemaODDSiriAccountInformation hasAssistantId]
+ -[ODDSiriSchemaODDSiriAccountInformation hash]
+ -[ODDSiriSchemaODDSiriAccountInformation initWithDictionary:]
+ -[ODDSiriSchemaODDSiriAccountInformation initWithJSON:]
+ -[ODDSiriSchemaODDSiriAccountInformation isEqual:]
+ -[ODDSiriSchemaODDSiriAccountInformation jsonData]
+ -[ODDSiriSchemaODDSiriAccountInformation readFrom:]
+ -[ODDSiriSchemaODDSiriAccountInformation setAssistantId:]
+ -[ODDSiriSchemaODDSiriAccountInformation setHasAssistantId:]
+ -[ODDSiriSchemaODDSiriAccountInformation writeTo:]
+ -[ODDSiriSchemaODDSiriAccountInformation(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriClientEvent .cxx_destruct]
+ -[ODDSiriSchemaODDSiriClientEvent assistantDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteAssistantDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteDeviceCohortsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteDeviceSegmentsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteDictationDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent deleteEventMetadata]
+ -[ODDSiriSchemaODDSiriClientEvent deleteSiriAccountInformation]
+ -[ODDSiriSchemaODDSiriClientEvent deviceCohortsReported]
+ -[ODDSiriSchemaODDSiriClientEvent deviceSegmentsReported]
+ -[ODDSiriSchemaODDSiriClientEvent dictationDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent dictionaryRepresentation]
+ -[ODDSiriSchemaODDSiriClientEvent eventMetadata]
+ -[ODDSiriSchemaODDSiriClientEvent hasAssistantDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasDeviceCohortsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasDeviceSegmentsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasDictationDeviceDigestReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasEventMetadata]
+ -[ODDSiriSchemaODDSiriClientEvent hasSiriAccountInformation]
+ -[ODDSiriSchemaODDSiriClientEvent hash]
+ -[ODDSiriSchemaODDSiriClientEvent initWithDictionary:]
+ -[ODDSiriSchemaODDSiriClientEvent initWithJSON:]
+ -[ODDSiriSchemaODDSiriClientEvent isEqual:]
+ -[ODDSiriSchemaODDSiriClientEvent jsonData]
+ -[ODDSiriSchemaODDSiriClientEvent qualifiedMessageName]
+ -[ODDSiriSchemaODDSiriClientEvent readFrom:]
+ -[ODDSiriSchemaODDSiriClientEvent setAssistantDeviceDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setDeviceCohortsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setDeviceSegmentsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setDictationDeviceDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setEventMetadata:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasAssistantDeviceDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasDeviceCohortsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasDeviceSegmentsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasDictationDeviceDigestReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasEventMetadata:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasSiriAccountInformation:]
+ -[ODDSiriSchemaODDSiriClientEvent setSiriAccountInformation:]
+ -[ODDSiriSchemaODDSiriClientEvent siriAccountInformation]
+ -[ODDSiriSchemaODDSiriClientEvent whichEvent_Type]
+ -[ODDSiriSchemaODDSiriClientEvent writeTo:]
+ -[ODDSiriSchemaODDSiriClientEvent(InnerEventContainer) innerEvent]
+ -[ODDSiriSchemaODDSiriClientEvent(InnerEventContainer) whichInnerEventType]
+ -[ODDSiriSchemaODDSiriClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[ODDSiriSchemaODDSiriClientEvent(IsolationLevel) clockIsolationLevel]
+ -[ODDSiriSchemaODDSiriClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDSiriClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDTaskCounts deleteFlowTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts deleteFlowTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts deleteSiriTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts deleteSiriTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDTaskCounts flowTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts flowTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts hasFlowTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts hasFlowTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts hasSiriTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts hasSiriTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts hash]
+ -[ODDSiriSchemaODDTaskCounts initWithDictionary:]
+ -[ODDSiriSchemaODDTaskCounts initWithJSON:]
+ -[ODDSiriSchemaODDTaskCounts isEqual:]
+ -[ODDSiriSchemaODDTaskCounts jsonData]
+ -[ODDSiriSchemaODDTaskCounts readFrom:]
+ -[ODDSiriSchemaODDTaskCounts setFlowTasksCompleted:]
+ -[ODDSiriSchemaODDTaskCounts setFlowTasksStarted:]
+ -[ODDSiriSchemaODDTaskCounts setHasFlowTasksCompleted:]
+ -[ODDSiriSchemaODDTaskCounts setHasFlowTasksStarted:]
+ -[ODDSiriSchemaODDTaskCounts setHasSiriTasksCompleted:]
+ -[ODDSiriSchemaODDTaskCounts setHasSiriTasksStarted:]
+ -[ODDSiriSchemaODDTaskCounts setSiriTasksCompleted:]
+ -[ODDSiriSchemaODDTaskCounts setSiriTasksStarted:]
+ -[ODDSiriSchemaODDTaskCounts siriTasksCompleted]
+ -[ODDSiriSchemaODDTaskCounts siriTasksStarted]
+ -[ODDSiriSchemaODDTaskCounts writeTo:]
+ -[ODDSiriSchemaODDTaskCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDTimeInterval deleteNumberOfSeconds]
+ -[ODDSiriSchemaODDTimeInterval deleteStartTimestampInSecondsSince1970]
+ -[ODDSiriSchemaODDTimeInterval dictionaryRepresentation]
+ -[ODDSiriSchemaODDTimeInterval hasNumberOfSeconds]
+ -[ODDSiriSchemaODDTimeInterval hasStartTimestampInSecondsSince1970]
+ -[ODDSiriSchemaODDTimeInterval hash]
+ -[ODDSiriSchemaODDTimeInterval initWithDictionary:]
+ -[ODDSiriSchemaODDTimeInterval initWithJSON:]
+ -[ODDSiriSchemaODDTimeInterval isEqual:]
+ -[ODDSiriSchemaODDTimeInterval jsonData]
+ -[ODDSiriSchemaODDTimeInterval numberOfSeconds]
+ -[ODDSiriSchemaODDTimeInterval readFrom:]
+ -[ODDSiriSchemaODDTimeInterval setHasNumberOfSeconds:]
+ -[ODDSiriSchemaODDTimeInterval setHasStartTimestampInSecondsSince1970:]
+ -[ODDSiriSchemaODDTimeInterval setNumberOfSeconds:]
+ -[ODDSiriSchemaODDTimeInterval setStartTimestampInSecondsSince1970:]
+ -[ODDSiriSchemaODDTimeInterval startTimestampInSecondsSince1970]
+ -[ODDSiriSchemaODDTimeInterval writeTo:]
+ -[ODDSiriSchemaODDTimeInterval(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDTurnCounts deleteTotalTurnCount]
+ -[ODDSiriSchemaODDTurnCounts deleteValidTurnCount]
+ -[ODDSiriSchemaODDTurnCounts dictionaryRepresentation]
+ -[ODDSiriSchemaODDTurnCounts hasTotalTurnCount]
+ -[ODDSiriSchemaODDTurnCounts hasValidTurnCount]
+ -[ODDSiriSchemaODDTurnCounts hash]
+ -[ODDSiriSchemaODDTurnCounts initWithDictionary:]
+ -[ODDSiriSchemaODDTurnCounts initWithJSON:]
+ -[ODDSiriSchemaODDTurnCounts isEqual:]
+ -[ODDSiriSchemaODDTurnCounts jsonData]
+ -[ODDSiriSchemaODDTurnCounts readFrom:]
+ -[ODDSiriSchemaODDTurnCounts setHasTotalTurnCount:]
+ -[ODDSiriSchemaODDTurnCounts setHasValidTurnCount:]
+ -[ODDSiriSchemaODDTurnCounts setTotalTurnCount:]
+ -[ODDSiriSchemaODDTurnCounts setValidTurnCount:]
+ -[ODDSiriSchemaODDTurnCounts totalTurnCount]
+ -[ODDSiriSchemaODDTurnCounts validTurnCount]
+ -[ODDSiriSchemaODDTurnCounts writeTo:]
+ -[ODDSiriSchemaODDTurnCounts(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHMUXRequestEnded deleteSelectedUserEphemeralId]
+ -[ORCHSchemaORCHMUXRequestEnded hasSelectedUserEphemeralId]
+ -[ORCHSchemaORCHMUXRequestEnded selectedUserEphemeralId]
+ -[ORCHSchemaORCHMUXRequestEnded setHasSelectedUserEphemeralId:]
+ -[ORCHSchemaORCHMUXRequestEnded setSelectedUserEphemeralId:]
+ -[ORCHSchemaORCHMultiUserScore deleteUserEphemeralId]
+ -[ORCHSchemaORCHMultiUserScore hasUserEphemeralId]
+ -[ORCHSchemaORCHMultiUserScore setHasUserEphemeralId:]
+ -[ORCHSchemaORCHMultiUserScore setUserEphemeralId:]
+ -[ORCHSchemaORCHMultiUserScore userEphemeralId]
+ -[ORCHSchemaORCHMultiUserScore(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 addCitationIndices:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 citationIndicesAtIndex:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 citationIndicesCount]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 citationIndices]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 clearCitationIndices]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 deleteCitationIndices]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 deleteSubText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 hasSubText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 hash]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 setCitationIndices:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 setHasSubText:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 setSubText:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 subText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 citedText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteCitedText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteEnrichedUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteReadableAttribution]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteSourceDomain]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteThumbnail]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 deleteUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 enrichedUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasCitedText]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasEnrichedUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasReadableAttribution]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasSourceDomain]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasThumbnail]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hasUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 hash]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 readableAttribution]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setCitedText:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setEnrichedUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasCitedText:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasEnrichedUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasReadableAttribution:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasSourceDomain:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasThumbnail:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setHasUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setReadableAttribution:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setSourceDomain:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setThumbnail:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 setUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 sourceDomain]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 thumbnail]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 url]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSWebAnswerCitationTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PEGASUSSchemaPEGASUSWebAnswerExecutionTier1 deleteEntityUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerExecutionTier1 entityUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerExecutionTier1 hasEntityUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerExecutionTier1 setEntityUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerExecutionTier1 setHasEntityUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 .cxx_destruct]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 deleteFavIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 deleteImageUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 deleteTouchIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 dictionaryRepresentation]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 favIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 hasFavIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 hasImageUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 hasTouchIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 hash]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 imageUrl]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 initWithDictionary:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 initWithJSON:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 isEqual:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 jsonData]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 readFrom:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setFavIcon:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setHasFavIcon:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setHasImageUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setHasTouchIcon:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setImageUrl:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 setTouchIcon:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 touchIcon]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1 writeTo:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[PSESchemaPSEClientEvent deleteMapsSignalGenerated]
+ -[PSESchemaPSEClientEvent hasMapsSignalGenerated]
+ -[PSESchemaPSEClientEvent mapsSignalGenerated]
+ -[PSESchemaPSEClientEvent setHasMapsSignalGenerated:]
+ -[PSESchemaPSEClientEvent setMapsSignalGenerated:]
+ -[PSESchemaPSEMaps .cxx_destruct]
+ -[PSESchemaPSEMaps deleteFollowup]
+ -[PSESchemaPSEMaps deleteIsSiriResultUseful]
+ -[PSESchemaPSEMaps dictionaryRepresentation]
+ -[PSESchemaPSEMaps followup]
+ -[PSESchemaPSEMaps hasFollowup]
+ -[PSESchemaPSEMaps hasIsSiriResultUseful]
+ -[PSESchemaPSEMaps hash]
+ -[PSESchemaPSEMaps initWithDictionary:]
+ -[PSESchemaPSEMaps initWithJSON:]
+ -[PSESchemaPSEMaps isEqual:]
+ -[PSESchemaPSEMaps isSiriResultUseful]
+ -[PSESchemaPSEMaps jsonData]
+ -[PSESchemaPSEMaps readFrom:]
+ -[PSESchemaPSEMaps setFollowup:]
+ -[PSESchemaPSEMaps setHasFollowup:]
+ -[PSESchemaPSEMaps setHasIsSiriResultUseful:]
+ -[PSESchemaPSEMaps setIsSiriResultUseful:]
+ -[PSESchemaPSEMaps writeTo:]
+ -[PSESchemaPSEMaps(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PSESchemaPSEMaps(SensitiveConditions) suppressMessageUnderConditions]
+ -[PSESchemaPSEMapsSignalGenerated .cxx_destruct]
+ -[PSESchemaPSEMapsSignalGenerated commonSignal]
+ -[PSESchemaPSEMapsSignalGenerated deleteCommonSignal]
+ -[PSESchemaPSEMapsSignalGenerated deleteMapsSignal]
+ -[PSESchemaPSEMapsSignalGenerated dictionaryRepresentation]
+ -[PSESchemaPSEMapsSignalGenerated hasCommonSignal]
+ -[PSESchemaPSEMapsSignalGenerated hasMapsSignal]
+ -[PSESchemaPSEMapsSignalGenerated hash]
+ -[PSESchemaPSEMapsSignalGenerated initWithDictionary:]
+ -[PSESchemaPSEMapsSignalGenerated initWithJSON:]
+ -[PSESchemaPSEMapsSignalGenerated isEqual:]
+ -[PSESchemaPSEMapsSignalGenerated jsonData]
+ -[PSESchemaPSEMapsSignalGenerated mapsSignal]
+ -[PSESchemaPSEMapsSignalGenerated readFrom:]
+ -[PSESchemaPSEMapsSignalGenerated setCommonSignal:]
+ -[PSESchemaPSEMapsSignalGenerated setHasCommonSignal:]
+ -[PSESchemaPSEMapsSignalGenerated setHasMapsSignal:]
+ -[PSESchemaPSEMapsSignalGenerated setMapsSignal:]
+ -[PSESchemaPSEMapsSignalGenerated writeTo:]
+ -[PSESchemaPSEMapsSignalGenerated(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[PSESchemaPSEMapsSignalGenerated(SensitiveConditions) suppressMessageUnderConditions]
+ -[PSESchemaPSEMapsUserFollowup .cxx_destruct]
+ -[PSESchemaPSEMapsUserFollowup deleteFollowupType]
+ -[PSESchemaPSEMapsUserFollowup deleteMapsActionType]
+ -[PSESchemaPSEMapsUserFollowup deleteMapsAction]
+ -[PSESchemaPSEMapsUserFollowup dictionaryRepresentation]
+ -[PSESchemaPSEMapsUserFollowup followupType]
+ -[PSESchemaPSEMapsUserFollowup hasFollowupType]
+ -[PSESchemaPSEMapsUserFollowup hasMapsActionType]
+ -[PSESchemaPSEMapsUserFollowup hasMapsAction]
+ -[PSESchemaPSEMapsUserFollowup hash]
+ -[PSESchemaPSEMapsUserFollowup initWithDictionary:]
+ -[PSESchemaPSEMapsUserFollowup initWithJSON:]
+ -[PSESchemaPSEMapsUserFollowup isEqual:]
+ -[PSESchemaPSEMapsUserFollowup jsonData]
+ -[PSESchemaPSEMapsUserFollowup mapsActionType]
+ -[PSESchemaPSEMapsUserFollowup mapsAction]
+ -[PSESchemaPSEMapsUserFollowup readFrom:]
+ -[PSESchemaPSEMapsUserFollowup setFollowupType:]
+ -[PSESchemaPSEMapsUserFollowup setHasFollowupType:]
+ -[PSESchemaPSEMapsUserFollowup setHasMapsAction:]
+ -[PSESchemaPSEMapsUserFollowup setHasMapsActionType:]
+ -[PSESchemaPSEMapsUserFollowup setMapsAction:]
+ -[PSESchemaPSEMapsUserFollowup setMapsActionType:]
+ -[PSESchemaPSEMapsUserFollowup writeTo:]
+ -[PSESchemaPSEMapsUserFollowup(SensitiveConditions) suppressMessageUnderConditions]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteLocale]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteStageStatus]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted deleteVtAssetConfigVersion]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasLocale]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasStageStatus]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted hasVtAssetConfigVersion]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted locale]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasLocale:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasStageStatus:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setHasVtAssetConfigVersion:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setLocale:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setStageStatus:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted setVtAssetConfigVersion:]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted stageStatus]
+ -[SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted vtAssetConfigVersion]
+ -[SISchemaEnabledStatus deleteIsServerUserDataSyncEnabled]
+ -[SISchemaEnabledStatus hasIsServerUserDataSyncEnabled]
+ -[SISchemaEnabledStatus isServerUserDataSyncEnabled]
+ -[SISchemaEnabledStatus setHasIsServerUserDataSyncEnabled:]
+ -[SISchemaEnabledStatus setIsServerUserDataSyncEnabled:]
+ -[SUGSchemaSUGClientEvent deleteEngagementMetricReported]
+ -[SUGSchemaSUGClientEvent engagementMetricReported]
+ -[SUGSchemaSUGClientEvent hasEngagementMetricReported]
+ -[SUGSchemaSUGClientEvent setEngagementMetricReported:]
+ -[SUGSchemaSUGClientEvent setHasEngagementMetricReported:]
+ -[SUGSchemaSUGEngagementMetricReported .cxx_destruct]
+ -[SUGSchemaSUGEngagementMetricReported daysBucketType]
+ -[SUGSchemaSUGEngagementMetricReported deleteDaysBucketType]
+ -[SUGSchemaSUGEngagementMetricReported deleteHasConversion]
+ -[SUGSchemaSUGEngagementMetricReported deleteLoggingActionId]
+ -[SUGSchemaSUGEngagementMetricReported deleteNumberOfActionsAfter]
+ -[SUGSchemaSUGEngagementMetricReported deleteNumberOfActionsBefore]
+ -[SUGSchemaSUGEngagementMetricReported deleteNumberSuggestionShownBefore]
+ -[SUGSchemaSUGEngagementMetricReported deleteSecondsToConversion]
+ -[SUGSchemaSUGEngagementMetricReported deleteSuggestionId]
+ -[SUGSchemaSUGEngagementMetricReported dictionaryRepresentation]
+ -[SUGSchemaSUGEngagementMetricReported hasConversion]
+ -[SUGSchemaSUGEngagementMetricReported hasDaysBucketType]
+ -[SUGSchemaSUGEngagementMetricReported hasHasConversion]
+ -[SUGSchemaSUGEngagementMetricReported hasLoggingActionId]
+ -[SUGSchemaSUGEngagementMetricReported hasNumberOfActionsAfter]
+ -[SUGSchemaSUGEngagementMetricReported hasNumberOfActionsBefore]
+ -[SUGSchemaSUGEngagementMetricReported hasNumberSuggestionShownBefore]
+ -[SUGSchemaSUGEngagementMetricReported hasSecondsToConversion]
+ -[SUGSchemaSUGEngagementMetricReported hasSuggestionId]
+ -[SUGSchemaSUGEngagementMetricReported hash]
+ -[SUGSchemaSUGEngagementMetricReported initWithDictionary:]
+ -[SUGSchemaSUGEngagementMetricReported initWithJSON:]
+ -[SUGSchemaSUGEngagementMetricReported isEqual:]
+ -[SUGSchemaSUGEngagementMetricReported jsonData]
+ -[SUGSchemaSUGEngagementMetricReported loggingActionId]
+ -[SUGSchemaSUGEngagementMetricReported numberOfActionsAfter]
+ -[SUGSchemaSUGEngagementMetricReported numberOfActionsBefore]
+ -[SUGSchemaSUGEngagementMetricReported numberSuggestionShownBefore]
+ -[SUGSchemaSUGEngagementMetricReported readFrom:]
+ -[SUGSchemaSUGEngagementMetricReported secondsToConversion]
+ -[SUGSchemaSUGEngagementMetricReported setDaysBucketType:]
+ -[SUGSchemaSUGEngagementMetricReported setHasConversion:]
+ -[SUGSchemaSUGEngagementMetricReported setHasDaysBucketType:]
+ -[SUGSchemaSUGEngagementMetricReported setHasHasConversion:]
+ -[SUGSchemaSUGEngagementMetricReported setHasLoggingActionId:]
+ -[SUGSchemaSUGEngagementMetricReported setHasNumberOfActionsAfter:]
+ -[SUGSchemaSUGEngagementMetricReported setHasNumberOfActionsBefore:]
+ -[SUGSchemaSUGEngagementMetricReported setHasNumberSuggestionShownBefore:]
+ -[SUGSchemaSUGEngagementMetricReported setHasSecondsToConversion:]
+ -[SUGSchemaSUGEngagementMetricReported setHasSuggestionId:]
+ -[SUGSchemaSUGEngagementMetricReported setLoggingActionId:]
+ -[SUGSchemaSUGEngagementMetricReported setNumberOfActionsAfter:]
+ -[SUGSchemaSUGEngagementMetricReported setNumberOfActionsBefore:]
+ -[SUGSchemaSUGEngagementMetricReported setNumberSuggestionShownBefore:]
+ -[SUGSchemaSUGEngagementMetricReported setSecondsToConversion:]
+ -[SUGSchemaSUGEngagementMetricReported setSuggestionId:]
+ -[SUGSchemaSUGEngagementMetricReported suggestionId]
+ -[SUGSchemaSUGEngagementMetricReported writeTo:]
+ -[SUGSchemaSUGEngagementMetricReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGSuggestion deleteLoggingActionId]
+ -[SUGSchemaSUGSuggestion hasLoggingActionId]
+ -[SUGSchemaSUGSuggestion loggingActionId]
+ -[SUGSchemaSUGSuggestion setHasLoggingActionId:]
+ -[SUGSchemaSUGSuggestion setLoggingActionId:]
+ -[SessionSchemaOrderedSessionEvent .cxx_destruct]
+ -[SessionSchemaOrderedSessionEvent deleteEvent]
+ -[SessionSchemaOrderedSessionEvent deleteLogicalEventTimestampInNs]
+ -[SessionSchemaOrderedSessionEvent dictionaryRepresentation]
+ -[SessionSchemaOrderedSessionEvent event]
+ -[SessionSchemaOrderedSessionEvent hasEvent]
+ -[SessionSchemaOrderedSessionEvent hasLogicalEventTimestampInNs]
+ -[SessionSchemaOrderedSessionEvent hash]
+ -[SessionSchemaOrderedSessionEvent initWithDictionary:]
+ -[SessionSchemaOrderedSessionEvent initWithJSON:]
+ -[SessionSchemaOrderedSessionEvent isEqual:]
+ -[SessionSchemaOrderedSessionEvent jsonData]
+ -[SessionSchemaOrderedSessionEvent logicalEventTimestampInNs]
+ -[SessionSchemaOrderedSessionEvent readFrom:]
+ -[SessionSchemaOrderedSessionEvent setEvent:]
+ -[SessionSchemaOrderedSessionEvent setHasEvent:]
+ -[SessionSchemaOrderedSessionEvent setHasLogicalEventTimestampInNs:]
+ -[SessionSchemaOrderedSessionEvent setLogicalEventTimestampInNs:]
+ -[SessionSchemaOrderedSessionEvent writeTo:]
+ -[SessionSchemaOrderedSessionEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SessionSchemaOrderedSessionEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[SessionSchemaSession .cxx_destruct]
+ -[SessionSchemaSession addEvent:]
+ -[SessionSchemaSession clearEvent]
+ -[SessionSchemaSession deleteEvent]
+ -[SessionSchemaSession deleteSessionId]
+ -[SessionSchemaSession dictionaryRepresentation]
+ -[SessionSchemaSession eventAtIndex:]
+ -[SessionSchemaSession eventCount]
+ -[SessionSchemaSession events]
+ -[SessionSchemaSession hasSessionId]
+ -[SessionSchemaSession hash]
+ -[SessionSchemaSession initWithDictionary:]
+ -[SessionSchemaSession initWithJSON:]
+ -[SessionSchemaSession isEqual:]
+ -[SessionSchemaSession jsonData]
+ -[SessionSchemaSession qualifiedMessageName]
+ -[SessionSchemaSession readFrom:]
+ -[SessionSchemaSession sessionId]
+ -[SessionSchemaSession setEvents:]
+ -[SessionSchemaSession setHasSessionId:]
+ -[SessionSchemaSession setSessionId:]
+ -[SessionSchemaSession writeTo:]
+ -[SessionSchemaSession(InstrumentationAdditions) getAnyEventType]
+ -[SessionSchemaSession(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SessionSchemaSession(SensitiveConditions) suppressMessageUnderConditions]
+ -[SessionSchemaSessionId .cxx_destruct]
+ -[SessionSchemaSessionId deleteSessionId]
+ -[SessionSchemaSessionId dictionaryRepresentation]
+ -[SessionSchemaSessionId hasSessionId]
+ -[SessionSchemaSessionId hash]
+ -[SessionSchemaSessionId initWithDictionary:]
+ -[SessionSchemaSessionId initWithJSON:]
+ -[SessionSchemaSessionId isEqual:]
+ -[SessionSchemaSessionId jsonData]
+ -[SessionSchemaSessionId readFrom:]
+ -[SessionSchemaSessionId sessionId]
+ -[SessionSchemaSessionId setHasSessionId:]
+ -[SessionSchemaSessionId setSessionId:]
+ -[SessionSchemaSessionId writeTo:]
+ -[SessionSchemaSessionId(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SessionSchemaSessionId(SensitiveConditions) suppressMessageUnderConditions]
+ OBJC_IVAR_$_CDASchemaCDAParticipant._electionParticipantId
+ OBJC_IVAR_$_CDASchemaCDAParticipant._rotatedElectionParticipantId
+ OBJC_IVAR_$_DIMSchemaDIMClientEvent._ephemeralIdentifiers
+ OBJC_IVAR_$_DIMSchemaDIMClientEvent._ephemeralToAggregationIdentifierMap
+ OBJC_IVAR_$_DIMSchemaDIMClientEvent._onDeviceDigest
+ OBJC_IVAR_$_DIMSchemaDIMDeviceFixedContext._availableDictationKeyboards
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._has
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._homeEphemeralId
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._secondsSinceEphemeralIdCreation
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._userEphemeralId
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._deviceAggregationId
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._has
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._userAggregationId
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._userAggregationIdExpirationTimestampMs
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._userAggregationIdRotationTimestampMs
+ OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._userEphemeralId
+ OBJC_IVAR_$_DIMSchemaDIMOnDeviceDigest._daysWithTwoAssistantSpeechRequestsPerWeek
+ OBJC_IVAR_$_DIMSchemaDIMOnDeviceDigest._daysWithTwoValidAssistantTurnsPerWeek
+ OBJC_IVAR_$_DIMSchemaDIMOnDeviceDigest._has
+ OBJC_IVAR_$_HALSchemaHALClientEvent._nearbyPersonalDevicesReported
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._has
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._iMacCount
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._iPadCount
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._iPhoneCount
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._macBookCount
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._macStudioCount
+ OBJC_IVAR_$_HALSchemaHALNearbyPersonalDevicesReported._watchCount
+ OBJC_IVAR_$_HomeKitSchemaHKAudioTopologyReported._isLeader
+ OBJC_IVAR_$_IDENTITYSchemaIDENTITYScoreTuple._userEphemeralId
+ OBJC_IVAR_$_IDENTITYSchemaIDENTITYUserPresenceMetadata._userEphemeralId
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._isBoltEnabled
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._isCommonForegroundApp
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingDependentSignals._isRawLastNowPlayingBoolean
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._isContentFree
+ OBJC_IVAR_$_INFERENCESchemaINFERENCEMusicTrainingIndependentSignals._isUserRecognized
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._reliabilityCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._taskCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._turnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDeviceDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDeviceDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._asrLocation
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._audioInterfaceProductId
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._audioInterfaceVendorId
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._dataSharingOptInStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._nlLocation
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._siriInputLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._subDomain
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._systemBuild
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._viewInterface
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._aggregationInterval
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._deviceAggregationId
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._eventTimestampInMsSince1970
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._has
+ OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._oddId
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohort._cohortDataAvailabilityState
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohort._cohortInterval
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohort._cohortType
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohort._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohortsReported._cohorts
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceSegment._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceSegment._segmentDataAvailabilityState
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceSegment._segmentType
+ OBJC_IVAR_$_ODDSiriSchemaODDDeviceSegmentsReported._segments
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationCounts._turnCounts
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDeviceDigestsReported._digests
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDeviceDigestsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDigest._counts
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDigest._dimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._asrLocation
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._audioInterfaceProductId
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._audioInterfaceVendorId
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._dataSharingOptInStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._dictationLocale
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._systemBuild
+ OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._viewInterface
+ OBJC_IVAR_$_ODDSiriSchemaODDFixedDimensions._deviceType
+ OBJC_IVAR_$_ODDSiriSchemaODDFixedDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDFixedDimensions._programCode
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._clientErrorCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._failureResponseCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._fatalResponseCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._reliabilityRequestCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._reliabilityTurnCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._siriUnavailableResponseCount
+ OBJC_IVAR_$_ODDSiriSchemaODDReliabilityCounts._undesiredResponseCount
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriAccountInformation._assistantId
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._assistantDeviceDigestReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._deviceCohortsReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._deviceSegmentsReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._dictationDeviceDigestReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._eventMetadata
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._siriAccountInformation
+ OBJC_IVAR_$_ODDSiriSchemaODDTaskCounts._flowTasksCompleted
+ OBJC_IVAR_$_ODDSiriSchemaODDTaskCounts._flowTasksStarted
+ OBJC_IVAR_$_ODDSiriSchemaODDTaskCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDTaskCounts._siriTasksCompleted
+ OBJC_IVAR_$_ODDSiriSchemaODDTaskCounts._siriTasksStarted
+ OBJC_IVAR_$_ODDSiriSchemaODDTimeInterval._has
+ OBJC_IVAR_$_ODDSiriSchemaODDTimeInterval._numberOfSeconds
+ OBJC_IVAR_$_ODDSiriSchemaODDTimeInterval._startTimestampInSecondsSince1970
+ OBJC_IVAR_$_ODDSiriSchemaODDTurnCounts._has
+ OBJC_IVAR_$_ODDSiriSchemaODDTurnCounts._totalTurnCount
+ OBJC_IVAR_$_ODDSiriSchemaODDTurnCounts._validTurnCount
+ OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._selectedUserEphemeralId
+ OBJC_IVAR_$_ORCHSchemaORCHMultiUserScore._userEphemeralId
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1._citationIndices
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1._subText
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._citedText
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._enrichedUrl
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._readableAttribution
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._sourceDomain
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._thumbnail
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._url
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerExecutionTier1._entityUrl
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._favIcon
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._imageUrl
+ OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._touchIcon
+ OBJC_IVAR_$_PSESchemaPSEClientEvent._mapsSignalGenerated
+ OBJC_IVAR_$_PSESchemaPSEMaps._followup
+ OBJC_IVAR_$_PSESchemaPSEMaps._has
+ OBJC_IVAR_$_PSESchemaPSEMaps._isSiriResultUseful
+ OBJC_IVAR_$_PSESchemaPSEMapsSignalGenerated._commonSignal
+ OBJC_IVAR_$_PSESchemaPSEMapsSignalGenerated._mapsSignal
+ OBJC_IVAR_$_PSESchemaPSEMapsUserFollowup._followupType
+ OBJC_IVAR_$_PSESchemaPSEMapsUserFollowup._has
+ OBJC_IVAR_$_PSESchemaPSEMapsUserFollowup._mapsAction
+ OBJC_IVAR_$_PSESchemaPSEMapsUserFollowup._mapsActionType
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._locale
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._stageStatus
+ OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._vtAssetConfigVersion
+ OBJC_IVAR_$_SISchemaEnabledStatus._isServerUserDataSyncEnabled
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._engagementMetricReported
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._daysBucketType
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._has
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._hasConversion
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._loggingActionId
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._numberOfActionsAfter
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._numberOfActionsBefore
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._numberSuggestionShownBefore
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._secondsToConversion
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._suggestionId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._loggingActionId
+ OBJC_IVAR_$_SessionSchemaOrderedSessionEvent._event
+ OBJC_IVAR_$_SessionSchemaOrderedSessionEvent._has
+ OBJC_IVAR_$_SessionSchemaOrderedSessionEvent._logicalEventTimestampInNs
+ OBJC_IVAR_$_SessionSchemaSession._events
+ OBJC_IVAR_$_SessionSchemaSession._sessionId
+ OBJC_IVAR_$_SessionSchemaSessionId._sessionId
+ _DIMSchemaDIMEphemeralIdentifiersReadFrom
+ _DIMSchemaDIMEphemeralToAggregationIdentifierMapReadFrom
+ _DIMSchemaDIMOnDeviceDigestReadFrom
+ _HALSchemaHALNearbyPersonalDevicesReportedReadFrom
+ _OBJC_CLASS_$_DIMSchemaDIMEphemeralIdentifiers
+ _OBJC_CLASS_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ _OBJC_CLASS_$_DIMSchemaDIMOnDeviceDigest
+ _OBJC_CLASS_$_HALSchemaHALNearbyPersonalDevicesReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDAssistantDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDClientEventMetadata
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceCohort
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceCohortsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceSegment
+ _OBJC_CLASS_$_ODDSiriSchemaODDDeviceSegmentsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDDictationCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDDictationDeviceDigestsReported
+ _OBJC_CLASS_$_ODDSiriSchemaODDDictationDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDDictationDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDFixedDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDReliabilityCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDSiriAccountInformation
+ _OBJC_CLASS_$_ODDSiriSchemaODDSiriClientEvent
+ _OBJC_CLASS_$_ODDSiriSchemaODDTaskCounts
+ _OBJC_CLASS_$_ODDSiriSchemaODDTimeInterval
+ _OBJC_CLASS_$_ODDSiriSchemaODDTurnCounts
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ _OBJC_CLASS_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ _OBJC_CLASS_$_PSESchemaPSEMaps
+ _OBJC_CLASS_$_PSESchemaPSEMapsSignalGenerated
+ _OBJC_CLASS_$_PSESchemaPSEMapsUserFollowup
+ _OBJC_CLASS_$_SUGSchemaSUGEngagementMetricReported
+ _OBJC_CLASS_$_SessionSchemaOrderedSessionEvent
+ _OBJC_CLASS_$_SessionSchemaSession
+ _OBJC_CLASS_$_SessionSchemaSessionId
+ _OBJC_IVAR_$_CDASchemaCDAParticipant._hasElectionParticipantId
+ _OBJC_IVAR_$_CDASchemaCDAParticipant._hasRotatedElectionParticipantId
+ _OBJC_IVAR_$_DIMSchemaDIMClientEvent._hasEphemeralIdentifiers
+ _OBJC_IVAR_$_DIMSchemaDIMClientEvent._hasEphemeralToAggregationIdentifierMap
+ _OBJC_IVAR_$_DIMSchemaDIMClientEvent._hasOnDeviceDigest
+ _OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._hasHomeEphemeralId
+ _OBJC_IVAR_$_DIMSchemaDIMEphemeralIdentifiers._hasUserEphemeralId
+ _OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._hasDeviceAggregationId
+ _OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._hasUserAggregationId
+ _OBJC_IVAR_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap._hasUserEphemeralId
+ _OBJC_IVAR_$_HALSchemaHALClientEvent._hasNearbyPersonalDevicesReported
+ _OBJC_IVAR_$_IDENTITYSchemaIDENTITYScoreTuple._hasUserEphemeralId
+ _OBJC_IVAR_$_IDENTITYSchemaIDENTITYUserPresenceMetadata._hasUserEphemeralId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._hasReliabilityCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._hasTaskCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantCounts._hasTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDeviceDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._hasAudioInterfaceProductId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._hasAudioInterfaceVendorId
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._hasSiriInputLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._hasSubDomain
+ _OBJC_IVAR_$_ODDSiriSchemaODDAssistantDimensions._hasSystemBuild
+ _OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._hasAggregationInterval
+ _OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._hasDeviceAggregationId
+ _OBJC_IVAR_$_ODDSiriSchemaODDClientEventMetadata._hasOddId
+ _OBJC_IVAR_$_ODDSiriSchemaODDDeviceCohort._hasCohortInterval
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationCounts._hasTurnCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDeviceDigestsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDigest._hasCounts
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDigest._hasDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._hasAudioInterfaceProductId
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._hasAudioInterfaceVendorId
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._hasDictationLocale
+ _OBJC_IVAR_$_ODDSiriSchemaODDDictationDimensions._hasSystemBuild
+ _OBJC_IVAR_$_ODDSiriSchemaODDFixedDimensions._hasDeviceType
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriAccountInformation._hasAssistantId
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasAssistantDeviceDigestReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasDeviceCohortsReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasDeviceSegmentsReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasDictationDeviceDigestReported
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasSiriAccountInformation
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_ORCHSchemaORCHMUXRequestEnded._hasSelectedUserEphemeralId
+ _OBJC_IVAR_$_ORCHSchemaORCHMultiUserScore._hasUserEphemeralId
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1._hasSubText
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasCitedText
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasEnrichedUrl
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasReadableAttribution
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasSourceDomain
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasThumbnail
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1._hasUrl
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerExecutionTier1._hasEntityUrl
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._hasFavIcon
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._hasImageUrl
+ _OBJC_IVAR_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1._hasTouchIcon
+ _OBJC_IVAR_$_PSESchemaPSEClientEvent._hasMapsSignalGenerated
+ _OBJC_IVAR_$_PSESchemaPSEMaps._hasFollowup
+ _OBJC_IVAR_$_PSESchemaPSEMapsSignalGenerated._hasCommonSignal
+ _OBJC_IVAR_$_PSESchemaPSEMapsSignalGenerated._hasMapsSignal
+ _OBJC_IVAR_$_PSESchemaPSEMapsUserFollowup._hasMapsActionType
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._hasLocale
+ _OBJC_IVAR_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentDigitalZeroDetectionCompleted._hasVtAssetConfigVersion
+ _OBJC_IVAR_$_SUGSchemaSUGClientEvent._hasEngagementMetricReported
+ _OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._hasLoggingActionId
+ _OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._hasSuggestionId
+ _OBJC_IVAR_$_SUGSchemaSUGSuggestion._hasLoggingActionId
+ _OBJC_IVAR_$_SessionSchemaOrderedSessionEvent._hasEvent
+ _OBJC_IVAR_$_SessionSchemaSession._hasSessionId
+ _OBJC_IVAR_$_SessionSchemaSessionId._hasSessionId
+ _OBJC_METACLASS_$_DIMSchemaDIMEphemeralIdentifiers
+ _OBJC_METACLASS_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ _OBJC_METACLASS_$_DIMSchemaDIMOnDeviceDigest
+ _OBJC_METACLASS_$_HALSchemaHALNearbyPersonalDevicesReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDAssistantDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDClientEventMetadata
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceCohort
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceCohortsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceSegment
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDeviceSegmentsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDictationCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDictationDeviceDigestsReported
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDictationDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDDictationDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDFixedDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDReliabilityCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDSiriAccountInformation
+ _OBJC_METACLASS_$_ODDSiriSchemaODDSiriClientEvent
+ _OBJC_METACLASS_$_ODDSiriSchemaODDTaskCounts
+ _OBJC_METACLASS_$_ODDSiriSchemaODDTimeInterval
+ _OBJC_METACLASS_$_ODDSiriSchemaODDTurnCounts
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ _OBJC_METACLASS_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ _OBJC_METACLASS_$_PSESchemaPSEMaps
+ _OBJC_METACLASS_$_PSESchemaPSEMapsSignalGenerated
+ _OBJC_METACLASS_$_PSESchemaPSEMapsUserFollowup
+ _OBJC_METACLASS_$_SUGSchemaSUGEngagementMetricReported
+ _OBJC_METACLASS_$_SessionSchemaOrderedSessionEvent
+ _OBJC_METACLASS_$_SessionSchemaSession
+ _OBJC_METACLASS_$_SessionSchemaSessionId
+ _ODDSiriSchemaODDAssistantCountsReadFrom
+ _ODDSiriSchemaODDAssistantDeviceDigestsReportedReadFrom
+ _ODDSiriSchemaODDAssistantDigestReadFrom
+ _ODDSiriSchemaODDAssistantDimensionsReadFrom
+ _ODDSiriSchemaODDClientEventMetadataReadFrom
+ _ODDSiriSchemaODDDeviceCohortReadFrom
+ _ODDSiriSchemaODDDeviceCohortsReportedReadFrom
+ _ODDSiriSchemaODDDeviceSegmentReadFrom
+ _ODDSiriSchemaODDDeviceSegmentsReportedReadFrom
+ _ODDSiriSchemaODDDictationCountsReadFrom
+ _ODDSiriSchemaODDDictationDeviceDigestsReportedReadFrom
+ _ODDSiriSchemaODDDictationDigestReadFrom
+ _ODDSiriSchemaODDDictationDimensionsReadFrom
+ _ODDSiriSchemaODDFixedDimensionsReadFrom
+ _ODDSiriSchemaODDReliabilityCountsReadFrom
+ _ODDSiriSchemaODDSiriAccountInformationReadFrom
+ _ODDSiriSchemaODDSiriClientEventReadFrom
+ _ODDSiriSchemaODDTaskCountsReadFrom
+ _ODDSiriSchemaODDTimeIntervalReadFrom
+ _ODDSiriSchemaODDTurnCountsReadFrom
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1ReadFrom
+ _PEGASUSSchemaPEGASUSWebAnswerCitationTier1ReadFrom
+ _PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1ReadFrom
+ _PSESchemaPSEMapsReadFrom
+ _PSESchemaPSEMapsSignalGeneratedReadFrom
+ _PSESchemaPSEMapsUserFollowupReadFrom
+ _SUGSchemaSUGEngagementMetricReportedReadFrom
+ _SessionSchemaOrderedSessionEventReadFrom
+ _SessionSchemaSessionIdReadFrom
+ _SessionSchemaSessionReadFrom
+ __CATEGORY_SIOrderedEventInternal_$_SiriInstrumentation
+ __OBJC_$_CLASS_METHODS_ODDSiriSchemaODDSiriClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_DIMSchemaDIMEphemeralIdentifiers(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DIMSchemaDIMEphemeralToAggregationIdentifierMap(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_DIMSchemaDIMOnDeviceDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_HALSchemaHALNearbyPersonalDevicesReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantDeviceDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDAssistantDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceCohort(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceCohortsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceSegment(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDeviceSegmentsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDictationCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDictationDeviceDigestsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDictationDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDDictationDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDFixedDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDReliabilityCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDSiriAccountInformation(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDSiriClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDTaskCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDTimeInterval(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDTurnCounts(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSWebAnswerCitationTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PSESchemaPSEMaps(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PSESchemaPSEMapsSignalGenerated(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_PSESchemaPSEMapsUserFollowup(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SIOrderedEventInternal(SiriInstrumentation)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGEngagementMetricReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SessionSchemaOrderedSessionEvent(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SessionSchemaSession(SensitiveConditions|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_SessionSchemaSessionId(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_DIMSchemaDIMEphemeralIdentifiers
+ __OBJC_$_INSTANCE_VARIABLES_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ __OBJC_$_INSTANCE_VARIABLES_DIMSchemaDIMOnDeviceDigest
+ __OBJC_$_INSTANCE_VARIABLES_HALSchemaHALNearbyPersonalDevicesReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDAssistantDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceCohort
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceCohortsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceSegment
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDeviceSegmentsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDictationCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDictationDeviceDigestsReported
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDictationDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDDictationDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDFixedDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDReliabilityCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDSiriAccountInformation
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDSiriClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDTaskCounts
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDTimeInterval
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDTurnCounts
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ __OBJC_$_INSTANCE_VARIABLES_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ __OBJC_$_INSTANCE_VARIABLES_PSESchemaPSEMaps
+ __OBJC_$_INSTANCE_VARIABLES_PSESchemaPSEMapsSignalGenerated
+ __OBJC_$_INSTANCE_VARIABLES_PSESchemaPSEMapsUserFollowup
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGEngagementMetricReported
+ __OBJC_$_INSTANCE_VARIABLES_SessionSchemaOrderedSessionEvent
+ __OBJC_$_INSTANCE_VARIABLES_SessionSchemaSession
+ __OBJC_$_INSTANCE_VARIABLES_SessionSchemaSessionId
+ __OBJC_$_PROP_LIST_DIMSchemaDIMEphemeralIdentifiers
+ __OBJC_$_PROP_LIST_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ __OBJC_$_PROP_LIST_DIMSchemaDIMOnDeviceDigest
+ __OBJC_$_PROP_LIST_HALSchemaHALNearbyPersonalDevicesReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDAssistantDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDClientEventMetadata
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceCohort
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceCohortsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceSegment
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDeviceSegmentsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDictationCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDictationDeviceDigestsReported
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDictationDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDDictationDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDFixedDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDReliabilityCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDSiriAccountInformation
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDTaskCounts
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDTimeInterval
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDTurnCounts
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ __OBJC_$_PROP_LIST_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ __OBJC_$_PROP_LIST_PSESchemaPSEMaps
+ __OBJC_$_PROP_LIST_PSESchemaPSEMapsSignalGenerated
+ __OBJC_$_PROP_LIST_PSESchemaPSEMapsUserFollowup
+ __OBJC_$_PROP_LIST_SUGSchemaSUGEngagementMetricReported
+ __OBJC_$_PROP_LIST_SessionSchemaOrderedSessionEvent
+ __OBJC_$_PROP_LIST_SessionSchemaSession
+ __OBJC_$_PROP_LIST_SessionSchemaSessionId
+ __OBJC_CLASS_PROTOCOLS_$_ODDSiriSchemaODDSiriClientEvent(InnerEventContainer)
+ __OBJC_CLASS_PROTOCOLS_$_SIOrderedEventInternal(SiriInstrumentation)
+ __OBJC_CLASS_RO_$_DIMSchemaDIMEphemeralIdentifiers
+ __OBJC_CLASS_RO_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ __OBJC_CLASS_RO_$_DIMSchemaDIMOnDeviceDigest
+ __OBJC_CLASS_RO_$_HALSchemaHALNearbyPersonalDevicesReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDAssistantDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDClientEventMetadata
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceCohort
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceCohortsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceSegment
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDeviceSegmentsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDictationCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDictationDeviceDigestsReported
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDictationDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDDictationDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDFixedDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDReliabilityCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDSiriAccountInformation
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDSiriClientEvent
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDTaskCounts
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDTimeInterval
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDTurnCounts
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ __OBJC_CLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ __OBJC_CLASS_RO_$_PSESchemaPSEMaps
+ __OBJC_CLASS_RO_$_PSESchemaPSEMapsSignalGenerated
+ __OBJC_CLASS_RO_$_PSESchemaPSEMapsUserFollowup
+ __OBJC_CLASS_RO_$_SUGSchemaSUGEngagementMetricReported
+ __OBJC_CLASS_RO_$_SessionSchemaOrderedSessionEvent
+ __OBJC_CLASS_RO_$_SessionSchemaSession
+ __OBJC_CLASS_RO_$_SessionSchemaSessionId
+ __OBJC_METACLASS_RO_$_DIMSchemaDIMEphemeralIdentifiers
+ __OBJC_METACLASS_RO_$_DIMSchemaDIMEphemeralToAggregationIdentifierMap
+ __OBJC_METACLASS_RO_$_DIMSchemaDIMOnDeviceDigest
+ __OBJC_METACLASS_RO_$_HALSchemaHALNearbyPersonalDevicesReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantDeviceDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDAssistantDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDClientEventMetadata
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceCohort
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceCohortsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceSegment
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDeviceSegmentsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDictationCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDictationDeviceDigestsReported
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDictationDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDDictationDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDFixedDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDReliabilityCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDSiriAccountInformation
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDSiriClientEvent
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDTaskCounts
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDTimeInterval
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDTurnCounts
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerCitationTier1
+ __OBJC_METACLASS_RO_$_PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1
+ __OBJC_METACLASS_RO_$_PSESchemaPSEMaps
+ __OBJC_METACLASS_RO_$_PSESchemaPSEMapsSignalGenerated
+ __OBJC_METACLASS_RO_$_PSESchemaPSEMapsUserFollowup
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGEngagementMetricReported
+ __OBJC_METACLASS_RO_$_SessionSchemaOrderedSessionEvent
+ __OBJC_METACLASS_RO_$_SessionSchemaSession
+ __OBJC_METACLASS_RO_$_SessionSchemaSessionId
+ ___swift_memcpy48_8
+ ___swift_project_boxed_opaque_existential_1Tm
+ _associated conformance 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLOSHAASQ
+ _associated conformance 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$addCitationIndices:
+ _objc_msgSend$addCohorts:
+ _objc_msgSend$addDigests:
+ _objc_msgSend$asrLocation
+ _objc_msgSend$assistantDeviceDigestReported
+ _objc_msgSend$assistantId
+ _objc_msgSend$availableDictationKeyboards
+ _objc_msgSend$citationIndices
+ _objc_msgSend$citedText
+ _objc_msgSend$clearCitationIndices
+ _objc_msgSend$clearCohorts
+ _objc_msgSend$clearDigests
+ _objc_msgSend$clientErrorCount
+ _objc_msgSend$cohortDataAvailabilityState
+ _objc_msgSend$cohortInterval
+ _objc_msgSend$cohorts
+ _objc_msgSend$counts
+ _objc_msgSend$daysBucketType
+ _objc_msgSend$daysWithTwoAssistantSpeechRequestsPerWeek
+ _objc_msgSend$daysWithTwoValidAssistantTurnsPerWeek
+ _objc_msgSend$deleteAssistantDeviceDigestReported
+ _objc_msgSend$deleteCitedText
+ _objc_msgSend$deleteCohortInterval
+ _objc_msgSend$deleteCounts
+ _objc_msgSend$deleteDeviceAggregationId
+ _objc_msgSend$deleteDeviceCohortsReported
+ _objc_msgSend$deleteDeviceSegmentsReported
+ _objc_msgSend$deleteDictationDeviceDigestReported
+ _objc_msgSend$deleteElectionParticipantId
+ _objc_msgSend$deleteEngagementMetricReported
+ _objc_msgSend$deleteEnrichedUrl
+ _objc_msgSend$deleteEntityUrl
+ _objc_msgSend$deleteEphemeralIdentifiers
+ _objc_msgSend$deleteEphemeralToAggregationIdentifierMap
+ _objc_msgSend$deleteFavIcon
+ _objc_msgSend$deleteFixedDimensions
+ _objc_msgSend$deleteFollowup
+ _objc_msgSend$deleteHomeEphemeralId
+ _objc_msgSend$deleteImageUrl
+ _objc_msgSend$deleteMapsSignal
+ _objc_msgSend$deleteMapsSignalGenerated
+ _objc_msgSend$deleteNearbyPersonalDevicesReported
+ _objc_msgSend$deleteOddId
+ _objc_msgSend$deleteOnDeviceDigest
+ _objc_msgSend$deleteReadableAttribution
+ _objc_msgSend$deleteReliabilityCounts
+ _objc_msgSend$deleteRotatedElectionParticipantId
+ _objc_msgSend$deleteSelectedUserEphemeralId
+ _objc_msgSend$deleteSourceDomain
+ _objc_msgSend$deleteSubText
+ _objc_msgSend$deleteThumbnail
+ _objc_msgSend$deleteTouchIcon
+ _objc_msgSend$deleteTurnCounts
+ _objc_msgSend$deleteUrl
+ _objc_msgSend$deleteUserAggregationId
+ _objc_msgSend$deleteUserEphemeralId
+ _objc_msgSend$deviceAggregationId
+ _objc_msgSend$deviceCohortsReported
+ _objc_msgSend$deviceSegmentsReported
+ _objc_msgSend$dictationDeviceDigestReported
+ _objc_msgSend$digests
+ _objc_msgSend$electionParticipantId
+ _objc_msgSend$engagementMetricReported
+ _objc_msgSend$enrichedUrl
+ _objc_msgSend$entityUrl
+ _objc_msgSend$ephemeralIdentifiers
+ _objc_msgSend$ephemeralToAggregationIdentifierMap
+ _objc_msgSend$eventTimestampInMsSince1970
+ _objc_msgSend$failureResponseCount
+ _objc_msgSend$fatalResponseCount
+ _objc_msgSend$favIcon
+ _objc_msgSend$fixedDimensions
+ _objc_msgSend$flowTasksCompleted
+ _objc_msgSend$flowTasksStarted
+ _objc_msgSend$followup
+ _objc_msgSend$followupType
+ _objc_msgSend$hasConversion
+ _objc_msgSend$homeEphemeralId
+ _objc_msgSend$iMacCount
+ _objc_msgSend$iPadCount
+ _objc_msgSend$iPhoneCount
+ _objc_msgSend$imageUrl
+ _objc_msgSend$isBoltEnabled
+ _objc_msgSend$isCommonForegroundApp
+ _objc_msgSend$isContentFree
+ _objc_msgSend$isLeader
+ _objc_msgSend$isRawLastNowPlayingBoolean
+ _objc_msgSend$isServerUserDataSyncEnabled
+ _objc_msgSend$isSiriResultUseful
+ _objc_msgSend$isUserRecognized
+ _objc_msgSend$loggingActionId
+ _objc_msgSend$macBookCount
+ _objc_msgSend$macStudioCount
+ _objc_msgSend$mapsAction
+ _objc_msgSend$mapsActionType
+ _objc_msgSend$mapsSignal
+ _objc_msgSend$mapsSignalGenerated
+ _objc_msgSend$nearbyPersonalDevicesReported
+ _objc_msgSend$nlLocation
+ _objc_msgSend$numberOfActionsAfter
+ _objc_msgSend$numberOfActionsBefore
+ _objc_msgSend$numberOfSeconds
+ _objc_msgSend$numberSuggestionShownBefore
+ _objc_msgSend$oddId
+ _objc_msgSend$onDeviceDigest
+ _objc_msgSend$readableAttribution
+ _objc_msgSend$reliabilityCounts
+ _objc_msgSend$reliabilityRequestCount
+ _objc_msgSend$reliabilityTurnCount
+ _objc_msgSend$rotatedElectionParticipantId
+ _objc_msgSend$secondsSinceEphemeralIdCreation
+ _objc_msgSend$secondsToConversion
+ _objc_msgSend$segmentDataAvailabilityState
+ _objc_msgSend$segmentType
+ _objc_msgSend$selectedUserEphemeralId
+ _objc_msgSend$setAsrLocation:
+ _objc_msgSend$setAssistantDeviceDigestReported:
+ _objc_msgSend$setAssistantId:
+ _objc_msgSend$setAvailableDictationKeyboards:
+ _objc_msgSend$setCitedText:
+ _objc_msgSend$setClientErrorCount:
+ _objc_msgSend$setCohortDataAvailabilityState:
+ _objc_msgSend$setCohortInterval:
+ _objc_msgSend$setCohorts:
+ _objc_msgSend$setCounts:
+ _objc_msgSend$setDaysBucketType:
+ _objc_msgSend$setDaysWithTwoAssistantSpeechRequestsPerWeek:
+ _objc_msgSend$setDaysWithTwoValidAssistantTurnsPerWeek:
+ _objc_msgSend$setDeviceAggregationId:
+ _objc_msgSend$setDeviceCohortsReported:
+ _objc_msgSend$setDeviceSegmentsReported:
+ _objc_msgSend$setDictationDeviceDigestReported:
+ _objc_msgSend$setDigests:
+ _objc_msgSend$setElectionParticipantId:
+ _objc_msgSend$setEngagementMetricReported:
+ _objc_msgSend$setEnrichedUrl:
+ _objc_msgSend$setEntityUrl:
+ _objc_msgSend$setEphemeralIdentifiers:
+ _objc_msgSend$setEphemeralToAggregationIdentifierMap:
+ _objc_msgSend$setEventTimestampInMsSince1970:
+ _objc_msgSend$setFailureResponseCount:
+ _objc_msgSend$setFatalResponseCount:
+ _objc_msgSend$setFavIcon:
+ _objc_msgSend$setFixedDimensions:
+ _objc_msgSend$setFlowTasksCompleted:
+ _objc_msgSend$setFlowTasksStarted:
+ _objc_msgSend$setFollowup:
+ _objc_msgSend$setFollowupType:
+ _objc_msgSend$setHasConversion:
+ _objc_msgSend$setHomeEphemeralId:
+ _objc_msgSend$setIMacCount:
+ _objc_msgSend$setIPadCount:
+ _objc_msgSend$setIPhoneCount:
+ _objc_msgSend$setImageUrl:
+ _objc_msgSend$setIsBoltEnabled:
+ _objc_msgSend$setIsCommonForegroundApp:
+ _objc_msgSend$setIsContentFree:
+ _objc_msgSend$setIsLeader:
+ _objc_msgSend$setIsRawLastNowPlayingBoolean:
+ _objc_msgSend$setIsServerUserDataSyncEnabled:
+ _objc_msgSend$setIsSiriResultUseful:
+ _objc_msgSend$setIsUserRecognized:
+ _objc_msgSend$setLoggingActionId:
+ _objc_msgSend$setMacBookCount:
+ _objc_msgSend$setMacStudioCount:
+ _objc_msgSend$setMapsAction:
+ _objc_msgSend$setMapsActionType:
+ _objc_msgSend$setMapsSignal:
+ _objc_msgSend$setMapsSignalGenerated:
+ _objc_msgSend$setNearbyPersonalDevicesReported:
+ _objc_msgSend$setNlLocation:
+ _objc_msgSend$setNumberOfActionsAfter:
+ _objc_msgSend$setNumberOfActionsBefore:
+ _objc_msgSend$setNumberOfSeconds:
+ _objc_msgSend$setNumberSuggestionShownBefore:
+ _objc_msgSend$setOddId:
+ _objc_msgSend$setOnDeviceDigest:
+ _objc_msgSend$setReadableAttribution:
+ _objc_msgSend$setReliabilityCounts:
+ _objc_msgSend$setReliabilityRequestCount:
+ _objc_msgSend$setReliabilityTurnCount:
+ _objc_msgSend$setRotatedElectionParticipantId:
+ _objc_msgSend$setSecondsSinceEphemeralIdCreation:
+ _objc_msgSend$setSecondsToConversion:
+ _objc_msgSend$setSegmentDataAvailabilityState:
+ _objc_msgSend$setSegmentType:
+ _objc_msgSend$setSegments:
+ _objc_msgSend$setSelectedUserEphemeralId:
+ _objc_msgSend$setSiriTasksCompleted:
+ _objc_msgSend$setSiriTasksStarted:
+ _objc_msgSend$setSiriUnavailableResponseCount:
+ _objc_msgSend$setSourceDomain:
+ _objc_msgSend$setStageStatus:
+ _objc_msgSend$setStartTimestampInSecondsSince1970:
+ _objc_msgSend$setSubText:
+ _objc_msgSend$setThumbnail:
+ _objc_msgSend$setTotalTurnCount:
+ _objc_msgSend$setTouchIcon:
+ _objc_msgSend$setTurnCounts:
+ _objc_msgSend$setUndesiredResponseCount:
+ _objc_msgSend$setUrl:
+ _objc_msgSend$setUserAggregationId:
+ _objc_msgSend$setUserAggregationIdExpirationTimestampMs:
+ _objc_msgSend$setUserAggregationIdRotationTimestampMs:
+ _objc_msgSend$setUserEphemeralId:
+ _objc_msgSend$setValidTurnCount:
+ _objc_msgSend$setViewInterface:
+ _objc_msgSend$setVtAssetConfigVersion:
+ _objc_msgSend$setWatchCount:
+ _objc_msgSend$siriTasksCompleted
+ _objc_msgSend$siriTasksStarted
+ _objc_msgSend$siriUnavailableResponseCount
+ _objc_msgSend$sourceDomain
+ _objc_msgSend$stageStatus
+ _objc_msgSend$startTimestampInSecondsSince1970
+ _objc_msgSend$subText
+ _objc_msgSend$thumbnail
+ _objc_msgSend$totalTurnCount
+ _objc_msgSend$touchIcon
+ _objc_msgSend$turnCounts
+ _objc_msgSend$undesiredResponseCount
+ _objc_msgSend$url
+ _objc_msgSend$userAggregationId
+ _objc_msgSend$userAggregationIdExpirationTimestampMs
+ _objc_msgSend$userAggregationIdRotationTimestampMs
+ _objc_msgSend$userEphemeralId
+ _objc_msgSend$validTurnCount
+ _objc_msgSend$viewInterface
+ _objc_msgSend$vtAssetConfigVersion
+ _objc_msgSend$watchCount
+ _qname_DIMSchemaDIMClientEvent_WhichEvent_Type_ephemeralIdentifiers
+ _qname_DIMSchemaDIMClientEvent_WhichEvent_Type_ephemeralToAggregationIdentifierMap
+ _qname_DIMSchemaDIMClientEvent_WhichEvent_Type_onDeviceDigest
+ _qname_HALSchemaHALClientEvent_WhichEvent_Type_nearbyPersonalDevicesReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_None
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_assistantDeviceDigestReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_deviceCohortsReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_deviceSegmentsReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_dictationDeviceDigestReported
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_siriAccountInformation
+ _qname_PSESchemaPSEClientEvent_WhichEvent_Type_mapsSignalGenerated
+ _qname_SUGSchemaSUGClientEvent_WhichEvent_Type_engagementMetricReported
+ _qname_SessionSchemaSession_Default
+ _swift_bridgeObjectRelease_n
+ _symbolic SDy_____SSG 10Foundation4UUIDV
+ _symbolic SDy_____SaySo020SessionSchemaOrderedA5EventCGG 10Foundation4UUIDV
+ _symbolic Sb______SDyAASSGtcSg 10Foundation4UUIDV
+ _symbolic _____ 19SiriInstrumentation14SessionBuilderV
+ _symbolic _____ 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLO
+ _symbolic _____ So22PSESchemaPSEMapsActionV
+ _symbolic _____ So24PSESchemaPSEMapsFollowupV
+ _symbolic _____ So25SISchemaAssistantViewModeV
+ _symbolic _____ So32ODDSiriSchemaODDDeviceCohortTypeV
+ _symbolic _____ So33ODDSiriSchemaODDDeviceSegmentTypeV
+ _symbolic _____ So37ODDSiriSchemaODDDataAvailabilityStateV
+ _symbolic _____ So38SUGSchemaSUGEngagementMetricDaysBucketV
+ _symbolic _____ So50SIRISETUPSchemaSIRISETUPTrainingManagerStageStatusV
+ _symbolic _____3key_SaySo020SessionSchemaOrderedB5EventCG5valuet 10Foundation4UUIDV
+ _symbolic _____Sg 19SiriInstrumentation12OrderedEventC
+ _symbolic _____Sg 19SiriInstrumentation19ComponentIdentifierC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 19SiriInstrumentation19ComponentIdentifierC10CodingKeys33_4F5A7A92CBE8CF264E1368411AC4FC33LLO
+ _symbolic _____y_____SSG s17_NativeDictionaryV 10Foundation4UUIDV
+ _symbolic _____y_____SaySo020SessionSchemaOrderedA5EventCGG s17_NativeDictionaryV 10Foundation4UUIDV
CStrings:
+ "\x01\x12\x12"
+ "\x02!"
+ "\x02R"
+ "\x11\x11\x11\x11"
+ "\x11\""
+ "@\"DIMSchemaDIMEphemeralIdentifiers\""
+ "@\"DIMSchemaDIMEphemeralToAggregationIdentifierMap\""
+ "@\"DIMSchemaDIMOnDeviceDigest\""
+ "@\"HALSchemaHALNearbyPersonalDevicesReported\""
+ "@\"ODDSiriSchemaODDAssistantCounts\""
+ "@\"ODDSiriSchemaODDAssistantDeviceDigestsReported\""
+ "@\"ODDSiriSchemaODDAssistantDimensions\""
+ "@\"ODDSiriSchemaODDClientEventMetadata\""
+ "@\"ODDSiriSchemaODDDeviceCohortsReported\""
+ "@\"ODDSiriSchemaODDDeviceSegmentsReported\""
+ "@\"ODDSiriSchemaODDDictationCounts\""
+ "@\"ODDSiriSchemaODDDictationDeviceDigestsReported\""
+ "@\"ODDSiriSchemaODDDictationDimensions\""
+ "@\"ODDSiriSchemaODDFixedDimensions\""
+ "@\"ODDSiriSchemaODDReliabilityCounts\""
+ "@\"ODDSiriSchemaODDSiriAccountInformation\""
+ "@\"ODDSiriSchemaODDTaskCounts\""
+ "@\"ODDSiriSchemaODDTimeInterval\""
+ "@\"ODDSiriSchemaODDTurnCounts\""
+ "@\"PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1\""
+ "@\"PSESchemaPSEMaps\""
+ "@\"PSESchemaPSEMapsSignalGenerated\""
+ "@\"PSESchemaPSEMapsUserFollowup\""
+ "@\"SUGSchemaSUGEngagementMetricReported\""
+ "@\"SessionSchemaSessionId\""
+ "@24@0:8^v16"
+ "ASSISTANTVIEWMODE_BLUETOOTH_CAR"
+ "ASSISTANTVIEWMODE_CARPLAY"
+ "ASSISTANTVIEWMODE_COMPACT"
+ "ASSISTANTVIEWMODE_EYES_FREE"
+ "ASSISTANTVIEWMODE_NOT_APPLICABLE"
+ "ASSISTANTVIEWMODE_TV"
+ "ASSISTANTVIEWMODE_UNKNOWN"
+ "ASSISTANTVIEWMODE_VISION"
+ "ASSISTANTVIEWMODE_VOICE_ONLY"
+ "DEVICEFAMILY_VISION"
+ "DIMSchemaDIMEphemeralIdentifiers"
+ "DIMSchemaDIMEphemeralToAggregationIdentifierMap"
+ "DIMSchemaDIMOnDeviceDigest"
+ "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_BOLT_ENABLED_SIGNAL"
+ "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_FREE_MEDIA_CONTENT_SIGNAL"
+ "FLOWDOMAINEXECUTIONTYPE_MEDIAPLAYER_APP_SELECTION_USER_RECOGNIZED_SIGNAL"
+ "FLOWSTATUSREASON_AMP_SERVER_ERROR"
+ "HALSchemaHALNearbyPersonalDevicesReported"
+ "HKDEVICESAUDIOTOPOLOGY_ATV_PLUS_SINGLE"
+ "HKDEVICESAUDIOTOPOLOGY_ATV_PLUS_STEREO_PAIR"
+ "ODDDATAAVAILABILITYSTATE_COMPLETE"
+ "ODDDATAAVAILABILITYSTATE_INSUFFICIENT_DATA"
+ "ODDDATAAVAILABILITYSTATE_UNKNOWN"
+ "ODDDEVICECOHORTTYPE_NONE"
+ "ODDDEVICECOHORTTYPE_SIRI_HELP"
+ "ODDDEVICECOHORTTYPE_UNKNOWN"
+ "ODDDEVICESEGMENTTYPE_ASSISTANT_2X3"
+ "ODDDEVICESEGMENTTYPE_NONE"
+ "ODDDEVICESEGMENTTYPE_UNKNOWN"
+ "ODDSiriSchemaODDAssistantCounts"
+ "ODDSiriSchemaODDAssistantDeviceDigestsReported"
+ "ODDSiriSchemaODDAssistantDigest"
+ "ODDSiriSchemaODDAssistantDimensions"
+ "ODDSiriSchemaODDClientEventMetadata"
+ "ODDSiriSchemaODDDeviceCohort"
+ "ODDSiriSchemaODDDeviceCohortsReported"
+ "ODDSiriSchemaODDDeviceSegment"
+ "ODDSiriSchemaODDDeviceSegmentsReported"
+ "ODDSiriSchemaODDDictationCounts"
+ "ODDSiriSchemaODDDictationDeviceDigestsReported"
+ "ODDSiriSchemaODDDictationDigest"
+ "ODDSiriSchemaODDDictationDimensions"
+ "ODDSiriSchemaODDFixedDimensions"
+ "ODDSiriSchemaODDReliabilityCounts"
+ "ODDSiriSchemaODDSiriAccountInformation"
+ "ODDSiriSchemaODDSiriClientEvent"
+ "ODDSiriSchemaODDTaskCounts"
+ "ODDSiriSchemaODDTimeInterval"
+ "ODDSiriSchemaODDTurnCounts"
+ "ODD_SIRI_CLIENT_EVENT"
+ "PEGASUSSchemaPEGASUSWebAnswerCitationInfoTier1"
+ "PEGASUSSchemaPEGASUSWebAnswerCitationTier1"
+ "PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1"
+ "PSEMAPSACTION_NAVIGATION"
+ "PSEMAPSACTION_PLACE_CARD_TAP"
+ "PSEMAPSACTION_RESULT_LIST_TAP"
+ "PSEMAPSACTION_SEARCH"
+ "PSEMAPSACTION_SELECT_CATEGORY"
+ "PSEMAPSACTION_SHOW"
+ "PSEMAPSACTION_UNKNOWN"
+ "PSEMAPSFOLLOWUP_SIRI_RESULT"
+ "PSEMAPSFOLLOWUP_UNKNOWN"
+ "PSEMAPSFOLLOWUP_USER_INITIATED_NEW_SEARCH"
+ "PSESchemaPSEMaps"
+ "PSESchemaPSEMapsSignalGenerated"
+ "PSESchemaPSEMapsUserFollowup"
+ "SESSION_BYTE_EVENT"
+ "SESSION_EVENT"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_AVVC_NOT_READY"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_BAD_MIC"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_CANCEL"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_DETECT_VT"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_DETECT_VT_AND_PHRASE"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_RECORDING_ERROR"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_TIME_OUT"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_UNKNOWN"
+ "SIRISETUPTRAININGMANAGERSTAGESTATUS_VOICEPROFILE_STORAGE_FAILED"
+ "SUGDELIVERYVEHICLE_SIRI_HINTS_SPOKEN"
+ "SUGENGAGEMENTMETRICDAYSBUCKET_14_DAYS"
+ "SUGENGAGEMENTMETRICDAYSBUCKET_1_DAY"
+ "SUGENGAGEMENTMETRICDAYSBUCKET_21_DAYS"
+ "SUGENGAGEMENTMETRICDAYSBUCKET_7_DAYS"
+ "SUGENGAGEMENTMETRICDAYSBUCKET_UNKNOWN"
+ "SUGSchemaSUGEngagementMetricReported"
+ "SessionSchemaOrderedSessionEvent"
+ "SessionSchemaSession"
+ "SessionSchemaSessionId"
+ "T@\"DIMSchemaDIMEphemeralIdentifiers\",&,N,V_ephemeralIdentifiers"
+ "T@\"DIMSchemaDIMEphemeralToAggregationIdentifierMap\",&,N,V_ephemeralToAggregationIdentifierMap"
+ "T@\"DIMSchemaDIMOnDeviceDigest\",&,N,V_onDeviceDigest"
+ "T@\"HALSchemaHALNearbyPersonalDevicesReported\",&,N,V_nearbyPersonalDevicesReported"
+ "T@\"NSArray\",C,N,V_citationIndices"
+ "T@\"NSArray\",C,N,V_cohorts"
+ "T@\"NSArray\",C,N,V_digests"
+ "T@\"NSString\",C,N,V_assistantId"
+ "T@\"NSString\",C,N,V_citedText"
+ "T@\"NSString\",C,N,V_enrichedUrl"
+ "T@\"NSString\",C,N,V_entityUrl"
+ "T@\"NSString\",C,N,V_favIcon"
+ "T@\"NSString\",C,N,V_imageUrl"
+ "T@\"NSString\",C,N,V_loggingActionId"
+ "T@\"NSString\",C,N,V_mapsActionType"
+ "T@\"NSString\",C,N,V_readableAttribution"
+ "T@\"NSString\",C,N,V_sourceDomain"
+ "T@\"NSString\",C,N,V_subDomain"
+ "T@\"NSString\",C,N,V_subText"
+ "T@\"NSString\",C,N,V_touchIcon"
+ "T@\"NSString\",C,N,V_url"
+ "T@\"NSString\",C,N,V_vtAssetConfigVersion"
+ "T@\"ODDSiriSchemaODDAssistantCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDAssistantDeviceDigestsReported\",&,N,V_assistantDeviceDigestReported"
+ "T@\"ODDSiriSchemaODDAssistantDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDClientEventMetadata\",&,N,V_eventMetadata"
+ "T@\"ODDSiriSchemaODDDeviceCohortsReported\",&,N,V_deviceCohortsReported"
+ "T@\"ODDSiriSchemaODDDeviceSegmentsReported\",&,N,V_deviceSegmentsReported"
+ "T@\"ODDSiriSchemaODDDictationCounts\",&,N,V_counts"
+ "T@\"ODDSiriSchemaODDDictationDeviceDigestsReported\",&,N,V_dictationDeviceDigestReported"
+ "T@\"ODDSiriSchemaODDDictationDimensions\",&,N,V_dimensions"
+ "T@\"ODDSiriSchemaODDFixedDimensions\",&,N,V_fixedDimensions"
+ "T@\"ODDSiriSchemaODDReliabilityCounts\",&,N,V_reliabilityCounts"
+ "T@\"ODDSiriSchemaODDSiriAccountInformation\",&,N,V_siriAccountInformation"
+ "T@\"ODDSiriSchemaODDTaskCounts\",&,N,V_taskCounts"
+ "T@\"ODDSiriSchemaODDTimeInterval\",&,N,V_aggregationInterval"
+ "T@\"ODDSiriSchemaODDTimeInterval\",&,N,V_cohortInterval"
+ "T@\"ODDSiriSchemaODDTurnCounts\",&,N,V_turnCounts"
+ "T@\"PEGASUSSchemaPEGASUSWebAnswerThumbnailTier1\",&,N,V_thumbnail"
+ "T@\"PSESchemaPSEMaps\",&,N,V_mapsSignal"
+ "T@\"PSESchemaPSEMapsSignalGenerated\",&,N,V_mapsSignalGenerated"
+ "T@\"PSESchemaPSEMapsUserFollowup\",&,N,V_followup"
+ "T@\"SIComponentIdentifier\",N,&,VclusterId"
+ "T@\"SISchemaISOLocale\",&,N,V_dictationLocale"
+ "T@\"SISchemaUUID\",&,N,V_deviceAggregationId"
+ "T@\"SISchemaUUID\",&,N,V_electionParticipantId"
+ "T@\"SISchemaUUID\",&,N,V_homeEphemeralId"
+ "T@\"SISchemaUUID\",&,N,V_oddId"
+ "T@\"SISchemaUUID\",&,N,V_rotatedElectionParticipantId"
+ "T@\"SISchemaUUID\",&,N,V_selectedUserEphemeralId"
+ "T@\"SISchemaUUID\",&,N,V_userAggregationId"
+ "T@\"SISchemaUUID\",&,N,V_userEphemeralId"
+ "T@\"SUGSchemaSUGEngagementMetricReported\",&,N,V_engagementMetricReported"
+ "T@\"SessionSchemaSessionId\",&,N,V_sessionId"
+ "TB,N,V_hasAssistantDeviceDigestReported"
+ "TB,N,V_hasAssistantId"
+ "TB,N,V_hasCitedText"
+ "TB,N,V_hasCohortInterval"
+ "TB,N,V_hasConversion"
+ "TB,N,V_hasCounts"
+ "TB,N,V_hasDeviceAggregationId"
+ "TB,N,V_hasDeviceCohortsReported"
+ "TB,N,V_hasDeviceSegmentsReported"
+ "TB,N,V_hasDictationDeviceDigestReported"
+ "TB,N,V_hasElectionParticipantId"
+ "TB,N,V_hasEngagementMetricReported"
+ "TB,N,V_hasEnrichedUrl"
+ "TB,N,V_hasEntityUrl"
+ "TB,N,V_hasEphemeralIdentifiers"
+ "TB,N,V_hasEphemeralToAggregationIdentifierMap"
+ "TB,N,V_hasFavIcon"
+ "TB,N,V_hasFixedDimensions"
+ "TB,N,V_hasFollowup"
+ "TB,N,V_hasHomeEphemeralId"
+ "TB,N,V_hasImageUrl"
+ "TB,N,V_hasLoggingActionId"
+ "TB,N,V_hasMapsActionType"
+ "TB,N,V_hasMapsSignal"
+ "TB,N,V_hasMapsSignalGenerated"
+ "TB,N,V_hasNearbyPersonalDevicesReported"
+ "TB,N,V_hasOddId"
+ "TB,N,V_hasOnDeviceDigest"
+ "TB,N,V_hasReadableAttribution"
+ "TB,N,V_hasReliabilityCounts"
+ "TB,N,V_hasRotatedElectionParticipantId"
+ "TB,N,V_hasSelectedUserEphemeralId"
+ "TB,N,V_hasSourceDomain"
+ "TB,N,V_hasSubDomain"
+ "TB,N,V_hasSubText"
+ "TB,N,V_hasThumbnail"
+ "TB,N,V_hasTouchIcon"
+ "TB,N,V_hasTurnCounts"
+ "TB,N,V_hasUrl"
+ "TB,N,V_hasUserAggregationId"
+ "TB,N,V_hasUserEphemeralId"
+ "TB,N,V_hasVtAssetConfigVersion"
+ "TB,N,V_isBoltEnabled"
+ "TB,N,V_isCommonForegroundApp"
+ "TB,N,V_isContentFree"
+ "TB,N,V_isLeader"
+ "TB,N,V_isRawLastNowPlayingBoolean"
+ "TB,N,V_isServerUserDataSyncEnabled"
+ "TB,N,V_isSiriResultUseful"
+ "TB,N,V_isUserRecognized"
+ "TI,N,V_availableDictationKeyboards"
+ "TI,N,V_clientErrorCount"
+ "TI,N,V_daysWithTwoAssistantSpeechRequestsPerWeek"
+ "TI,N,V_daysWithTwoValidAssistantTurnsPerWeek"
+ "TI,N,V_failureResponseCount"
+ "TI,N,V_fatalResponseCount"
+ "TI,N,V_flowTasksCompleted"
+ "TI,N,V_flowTasksStarted"
+ "TI,N,V_iMacCount"
+ "TI,N,V_iPadCount"
+ "TI,N,V_iPhoneCount"
+ "TI,N,V_macBookCount"
+ "TI,N,V_macStudioCount"
+ "TI,N,V_numberOfActionsAfter"
+ "TI,N,V_numberOfActionsBefore"
+ "TI,N,V_numberOfSeconds"
+ "TI,N,V_numberSuggestionShownBefore"
+ "TI,N,V_reliabilityRequestCount"
+ "TI,N,V_reliabilityTurnCount"
+ "TI,N,V_secondsToConversion"
+ "TI,N,V_siriTasksCompleted"
+ "TI,N,V_siriTasksStarted"
+ "TI,N,V_siriUnavailableResponseCount"
+ "TI,N,V_totalTurnCount"
+ "TI,N,V_undesiredResponseCount"
+ "TI,N,V_validTurnCount"
+ "TI,N,V_watchCount"
+ "TQ,N,V_eventTimestampInMsSince1970"
+ "TQ,N,V_secondsSinceEphemeralIdCreation"
+ "TQ,N,V_startTimestampInSecondsSince1970"
+ "TQ,N,V_userAggregationIdExpirationTimestampMs"
+ "TQ,N,V_userAggregationIdRotationTimestampMs"
+ "Ti,N,V_asrLocation"
+ "Ti,N,V_cohortDataAvailabilityState"
+ "Ti,N,V_cohortType"
+ "Ti,N,V_daysBucketType"
+ "Ti,N,V_followupType"
+ "Ti,N,V_mapsAction"
+ "Ti,N,V_nlLocation"
+ "Ti,N,V_segmentDataAvailabilityState"
+ "Ti,N,V_segmentType"
+ "Ti,N,V_stageStatus"
+ "Ti,N,V_viewInterface"
+ "_asrLocation"
+ "_assistantDeviceDigestReported"
+ "_assistantId"
+ "_availableDictationKeyboards"
+ "_citationIndices"
+ "_citedText"
+ "_clientErrorCount"
+ "_cohortDataAvailabilityState"
+ "_cohortInterval"
+ "_cohorts"
+ "_counts"
+ "_daysBucketType"
+ "_daysWithTwoAssistantSpeechRequestsPerWeek"
+ "_daysWithTwoValidAssistantTurnsPerWeek"
+ "_deviceAggregationId"
+ "_deviceCohortsReported"
+ "_deviceSegmentsReported"
+ "_dictationDeviceDigestReported"
+ "_digests"
+ "_electionParticipantId"
+ "_engagementMetricReported"
+ "_enrichedUrl"
+ "_entityUrl"
+ "_ephemeralIdentifiers"
+ "_ephemeralToAggregationIdentifierMap"
+ "_eventTimestampInMsSince1970"
+ "_failureResponseCount"
+ "_fatalResponseCount"
+ "_favIcon"
+ "_fixedDimensions"
+ "_flowTasksCompleted"
+ "_flowTasksStarted"
+ "_followup"
+ "_followupType"
+ "_hasAssistantDeviceDigestReported"
+ "_hasAssistantId"
+ "_hasCitedText"
+ "_hasCohortInterval"
+ "_hasConversion"
+ "_hasCounts"
+ "_hasDeviceAggregationId"
+ "_hasDeviceCohortsReported"
+ "_hasDeviceSegmentsReported"
+ "_hasDictationDeviceDigestReported"
+ "_hasElectionParticipantId"
+ "_hasEngagementMetricReported"
+ "_hasEnrichedUrl"
+ "_hasEntityUrl"
+ "_hasEphemeralIdentifiers"
+ "_hasEphemeralToAggregationIdentifierMap"
+ "_hasFavIcon"
+ "_hasFixedDimensions"
+ "_hasFollowup"
+ "_hasHomeEphemeralId"
+ "_hasImageUrl"
+ "_hasLoggingActionId"
+ "_hasMapsActionType"
+ "_hasMapsSignal"
+ "_hasMapsSignalGenerated"
+ "_hasNearbyPersonalDevicesReported"
+ "_hasOddId"
+ "_hasOnDeviceDigest"
+ "_hasReadableAttribution"
+ "_hasReliabilityCounts"
+ "_hasRotatedElectionParticipantId"
+ "_hasSelectedUserEphemeralId"
+ "_hasSourceDomain"
+ "_hasSubDomain"
+ "_hasSubText"
+ "_hasThumbnail"
+ "_hasTouchIcon"
+ "_hasTurnCounts"
+ "_hasUrl"
+ "_hasUserAggregationId"
+ "_hasUserEphemeralId"
+ "_hasVtAssetConfigVersion"
+ "_homeEphemeralId"
+ "_iMacCount"
+ "_iPadCount"
+ "_iPhoneCount"
+ "_imageUrl"
+ "_isBoltEnabled"
+ "_isCommonForegroundApp"
+ "_isContentFree"
+ "_isLeader"
+ "_isRawLastNowPlayingBoolean"
+ "_isServerUserDataSyncEnabled"
+ "_isSiriResultUseful"
+ "_isUserRecognized"
+ "_loggingActionId"
+ "_macBookCount"
+ "_macStudioCount"
+ "_mapsAction"
+ "_mapsActionType"
+ "_mapsSignal"
+ "_mapsSignalGenerated"
+ "_nearbyPersonalDevicesReported"
+ "_nlLocation"
+ "_numberOfActionsAfter"
+ "_numberOfActionsBefore"
+ "_numberOfSeconds"
+ "_numberSuggestionShownBefore"
+ "_oddId"
+ "_onDeviceDigest"
+ "_readableAttribution"
+ "_reliabilityCounts"
+ "_reliabilityRequestCount"
+ "_reliabilityTurnCount"
+ "_rotatedElectionParticipantId"
+ "_secondsSinceEphemeralIdCreation"
+ "_secondsToConversion"
+ "_segmentDataAvailabilityState"
+ "_segmentType"
+ "_selectedUserEphemeralId"
+ "_siriTasksCompleted"
+ "_siriTasksStarted"
+ "_siriUnavailableResponseCount"
+ "_sourceDomain"
+ "_stageStatus"
+ "_startTimestampInSecondsSince1970"
+ "_subText"
+ "_thumbnail"
+ "_totalTurnCount"
+ "_touchIcon"
+ "_turnCounts"
+ "_undesiredResponseCount"
+ "_url"
+ "_userAggregationId"
+ "_userAggregationIdExpirationTimestampMs"
+ "_userAggregationIdRotationTimestampMs"
+ "_userEphemeralId"
+ "_validTurnCount"
+ "_viewInterface"
+ "_vtAssetConfigVersion"
+ "_watchCount"
+ "addCitationIndices:"
+ "addCohorts:"
+ "addDigests:"
+ "asrLocation"
+ "assistantDeviceDigestReported"
+ "assistantId"
+ "availableDictationKeyboards"
+ "citationIndices"
+ "citationIndicesAtIndex:"
+ "citationIndicesCount"
+ "citedText"
+ "clearCitationIndices"
+ "clearCohorts"
+ "clearDigests"
+ "clientErrorCount"
+ "clusterId"
+ "cohortDataAvailabilityState"
+ "cohortInterval"
+ "cohorts"
+ "cohortsAtIndex:"
+ "cohortsCount"
+ "com.apple.aiml.engagement.pse.PSEClientEvent.PSEMapsSignalGenerated"
+ "com.apple.aiml.platform.Session"
+ "com.apple.aiml.siri.dim.DIMClientEvent.DIMEphemeralIdentifiers"
+ "com.apple.aiml.siri.dim.DIMClientEvent.DIMEphemeralToAggregationIdentifierMap"
+ "com.apple.aiml.siri.dim.DIMClientEvent.DIMOnDeviceDigest"
+ "com.apple.aiml.siri.hal.HALClientEvent.HALNearbyPersonalDevicesReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDAssistantDeviceDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDDeviceCohortsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDDeviceSegmentsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDDictationDeviceDigestsReported"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDSiriAccountInformation"
+ "com.apple.aiml.siri.sug.SUGClientEvent.SUGEngagementMetricReported"
+ "counts"
+ "daysBucketType"
+ "daysWithTwoAssistantSpeechRequestsPerWeek"
+ "daysWithTwoValidAssistantTurnsPerWeek"
+ "deleteAsrLocation"
+ "deleteAssistantDeviceDigestReported"
+ "deleteAssistantId"
+ "deleteAvailableDictationKeyboards"
+ "deleteCitationIndices"
+ "deleteCitedText"
+ "deleteClientErrorCount"
+ "deleteCohortDataAvailabilityState"
+ "deleteCohortInterval"
+ "deleteCohorts"
+ "deleteCounts"
+ "deleteDaysBucketType"
+ "deleteDaysWithTwoAssistantSpeechRequestsPerWeek"
+ "deleteDaysWithTwoValidAssistantTurnsPerWeek"
+ "deleteDeviceAggregationId"
+ "deleteDeviceCohortsReported"
+ "deleteDeviceSegmentsReported"
+ "deleteDictationDeviceDigestReported"
+ "deleteDigests"
+ "deleteElectionParticipantId"
+ "deleteEngagementMetricReported"
+ "deleteEnrichedUrl"
+ "deleteEntityUrl"
+ "deleteEphemeralIdentifiers"
+ "deleteEphemeralToAggregationIdentifierMap"
+ "deleteEventTimestampInMsSince1970"
+ "deleteFailureResponseCount"
+ "deleteFatalResponseCount"
+ "deleteFavIcon"
+ "deleteFixedDimensions"
+ "deleteFlowTasksCompleted"
+ "deleteFlowTasksStarted"
+ "deleteFollowup"
+ "deleteFollowupType"
+ "deleteHasConversion"
+ "deleteHomeEphemeralId"
+ "deleteIMacCount"
+ "deleteIPadCount"
+ "deleteIPhoneCount"
+ "deleteImageUrl"
+ "deleteIsBoltEnabled"
+ "deleteIsCommonForegroundApp"
+ "deleteIsContentFree"
+ "deleteIsLeader"
+ "deleteIsRawLastNowPlayingBoolean"
+ "deleteIsServerUserDataSyncEnabled"
+ "deleteIsSiriResultUseful"
+ "deleteIsUserRecognized"
+ "deleteLoggingActionId"
+ "deleteMacBookCount"
+ "deleteMacStudioCount"
+ "deleteMapsAction"
+ "deleteMapsActionType"
+ "deleteMapsSignal"
+ "deleteMapsSignalGenerated"
+ "deleteNearbyPersonalDevicesReported"
+ "deleteNlLocation"
+ "deleteNumberOfActionsAfter"
+ "deleteNumberOfActionsBefore"
+ "deleteNumberOfSeconds"
+ "deleteNumberSuggestionShownBefore"
+ "deleteOddId"
+ "deleteOnDeviceDigest"
+ "deleteReadableAttribution"
+ "deleteReliabilityCounts"
+ "deleteReliabilityRequestCount"
+ "deleteReliabilityTurnCount"
+ "deleteRotatedElectionParticipantId"
+ "deleteSecondsSinceEphemeralIdCreation"
+ "deleteSecondsToConversion"
+ "deleteSegmentDataAvailabilityState"
+ "deleteSegmentType"
+ "deleteSelectedUserEphemeralId"
+ "deleteSiriTasksCompleted"
+ "deleteSiriTasksStarted"
+ "deleteSiriUnavailableResponseCount"
+ "deleteSourceDomain"
+ "deleteStageStatus"
+ "deleteStartTimestampInSecondsSince1970"
+ "deleteSubText"
+ "deleteThumbnail"
+ "deleteTotalTurnCount"
+ "deleteTouchIcon"
+ "deleteTurnCounts"
+ "deleteUndesiredResponseCount"
+ "deleteUrl"
+ "deleteUserAggregationId"
+ "deleteUserAggregationIdExpirationTimestampMs"
+ "deleteUserAggregationIdRotationTimestampMs"
+ "deleteUserEphemeralId"
+ "deleteValidTurnCount"
+ "deleteViewInterface"
+ "deleteVtAssetConfigVersion"
+ "deleteWatchCount"
+ "deviceAggregationId"
+ "deviceCohortsReported"
+ "deviceSegmentsReported"
+ "dictationDeviceDigestReported"
+ "digests"
+ "digestsAtIndex:"
+ "digestsCount"
+ "electionParticipantId"
+ "engagementMetricReported"
+ "enrichedUrl"
+ "entityUrl"
+ "ephemeralIdentifiers"
+ "ephemeralToAggregationIdentifierMap"
+ "eventTimestampInMsSince1970"
+ "failureResponseCount"
+ "fatalResponseCount"
+ "favIcon"
+ "fixedDimensions"
+ "flowTasksCompleted"
+ "flowTasksStarted"
+ "followup"
+ "followupType"
+ "hasAsrLocation"
+ "hasAssistantDeviceDigestReported"
+ "hasAssistantId"
+ "hasAvailableDictationKeyboards"
+ "hasCitedText"
+ "hasClientErrorCount"
+ "hasCohortDataAvailabilityState"
+ "hasCohortInterval"
+ "hasConversion"
+ "hasCounts"
+ "hasDaysBucketType"
+ "hasDaysWithTwoAssistantSpeechRequestsPerWeek"
+ "hasDaysWithTwoValidAssistantTurnsPerWeek"
+ "hasDeviceAggregationId"
+ "hasDeviceCohortsReported"
+ "hasDeviceSegmentsReported"
+ "hasDictationDeviceDigestReported"
+ "hasElectionParticipantId"
+ "hasEngagementMetricReported"
+ "hasEnrichedUrl"
+ "hasEntityUrl"
+ "hasEphemeralIdentifiers"
+ "hasEphemeralToAggregationIdentifierMap"
+ "hasEventTimestampInMsSince1970"
+ "hasFailureResponseCount"
+ "hasFatalResponseCount"
+ "hasFavIcon"
+ "hasFixedDimensions"
+ "hasFlowTasksCompleted"
+ "hasFlowTasksStarted"
+ "hasFollowup"
+ "hasFollowupType"
+ "hasHasConversion"
+ "hasHomeEphemeralId"
+ "hasIMacCount"
+ "hasIPadCount"
+ "hasIPhoneCount"
+ "hasImageUrl"
+ "hasIsBoltEnabled"
+ "hasIsCommonForegroundApp"
+ "hasIsContentFree"
+ "hasIsLeader"
+ "hasIsRawLastNowPlayingBoolean"
+ "hasIsServerUserDataSyncEnabled"
+ "hasIsSiriResultUseful"
+ "hasIsUserRecognized"
+ "hasLoggingActionId"
+ "hasMacBookCount"
+ "hasMacStudioCount"
+ "hasMapsAction"
+ "hasMapsActionType"
+ "hasMapsSignal"
+ "hasMapsSignalGenerated"
+ "hasNearbyPersonalDevicesReported"
+ "hasNlLocation"
+ "hasNumberOfActionsAfter"
+ "hasNumberOfActionsBefore"
+ "hasNumberOfSeconds"
+ "hasNumberSuggestionShownBefore"
+ "hasOddId"
+ "hasOnDeviceDigest"
+ "hasReadableAttribution"
+ "hasReliabilityCounts"
+ "hasReliabilityRequestCount"
+ "hasReliabilityTurnCount"
+ "hasRotatedElectionParticipantId"
+ "hasSecondsSinceEphemeralIdCreation"
+ "hasSecondsToConversion"
+ "hasSegmentDataAvailabilityState"
+ "hasSegmentType"
+ "hasSelectedUserEphemeralId"
+ "hasSiriTasksCompleted"
+ "hasSiriTasksStarted"
+ "hasSiriUnavailableResponseCount"
+ "hasSourceDomain"
+ "hasStageStatus"
+ "hasStartTimestampInSecondsSince1970"
+ "hasSubText"
+ "hasThumbnail"
+ "hasTotalTurnCount"
+ "hasTouchIcon"
+ "hasTurnCounts"
+ "hasUndesiredResponseCount"
+ "hasUrl"
+ "hasUserAggregationId"
+ "hasUserAggregationIdExpirationTimestampMs"
+ "hasUserAggregationIdRotationTimestampMs"
+ "hasUserEphemeralId"
+ "hasValidTurnCount"
+ "hasViewInterface"
+ "hasVtAssetConfigVersion"
+ "hasWatchCount"
+ "homeEphemeralId"
+ "iMacCount"
+ "iPadCount"
+ "iPhoneCount"
+ "imageUrl"
+ "isBoltEnabled"
+ "isCommonForegroundApp"
+ "isContentFree"
+ "isLeader"
+ "isRawLastNowPlayingBoolean"
+ "isServerUserDataSyncEnabled"
+ "isSiriResultUseful"
+ "isUserRecognized"
+ "loggingActionId"
+ "macBookCount"
+ "macStudioCount"
+ "mapsAction"
+ "mapsActionType"
+ "mapsSignal"
+ "mapsSignalGenerated"
+ "nearbyPersonalDevicesReported"
+ "nlLocation"
+ "numberOfActionsAfter"
+ "numberOfActionsBefore"
+ "numberOfSeconds"
+ "numberSuggestionShownBefore"
+ "oddId"
+ "onDeviceDigest"
+ "readInt32"
+ "readableAttribution"
+ "reliabilityCounts"
+ "reliabilityRequestCount"
+ "reliabilityTurnCount"
+ "rotatedElectionParticipantId"
+ "secondsSinceEphemeralIdCreation"
+ "secondsToConversion"
+ "segmentDataAvailabilityState"
+ "segmentType"
+ "selectedUserEphemeralId"
+ "setAsrLocation:"
+ "setAssistantDeviceDigestReported:"
+ "setAssistantId:"
+ "setAvailableDictationKeyboards:"
+ "setCitationIndices:"
+ "setCitedText:"
+ "setClientErrorCount:"
+ "setClusterId:"
+ "setCohortDataAvailabilityState:"
+ "setCohortInterval:"
+ "setCohorts:"
+ "setCounts:"
+ "setDaysBucketType:"
+ "setDaysWithTwoAssistantSpeechRequestsPerWeek:"
+ "setDaysWithTwoValidAssistantTurnsPerWeek:"
+ "setDeviceAggregationId:"
+ "setDeviceCohortsReported:"
+ "setDeviceSegmentsReported:"
+ "setDictationDeviceDigestReported:"
+ "setDigests:"
+ "setElectionParticipantId:"
+ "setEngagementMetricReported:"
+ "setEnrichedUrl:"
+ "setEntityUrl:"
+ "setEphemeralIdentifiers:"
+ "setEphemeralToAggregationIdentifierMap:"
+ "setEventTimestampInMsSince1970:"
+ "setFailureResponseCount:"
+ "setFatalResponseCount:"
+ "setFavIcon:"
+ "setFixedDimensions:"
+ "setFlowTasksCompleted:"
+ "setFlowTasksStarted:"
+ "setFollowup:"
+ "setFollowupType:"
+ "setHasAsrLocation:"
+ "setHasAssistantDeviceDigestReported:"
+ "setHasAssistantId:"
+ "setHasAvailableDictationKeyboards:"
+ "setHasCitedText:"
+ "setHasClientErrorCount:"
+ "setHasCohortDataAvailabilityState:"
+ "setHasCohortInterval:"
+ "setHasConversion:"
+ "setHasCounts:"
+ "setHasDaysBucketType:"
+ "setHasDaysWithTwoAssistantSpeechRequestsPerWeek:"
+ "setHasDaysWithTwoValidAssistantTurnsPerWeek:"
+ "setHasDeviceAggregationId:"
+ "setHasDeviceCohortsReported:"
+ "setHasDeviceSegmentsReported:"
+ "setHasDictationDeviceDigestReported:"
+ "setHasElectionParticipantId:"
+ "setHasEngagementMetricReported:"
+ "setHasEnrichedUrl:"
+ "setHasEntityUrl:"
+ "setHasEphemeralIdentifiers:"
+ "setHasEphemeralToAggregationIdentifierMap:"
+ "setHasEventTimestampInMsSince1970:"
+ "setHasFailureResponseCount:"
+ "setHasFatalResponseCount:"
+ "setHasFavIcon:"
+ "setHasFixedDimensions:"
+ "setHasFlowTasksCompleted:"
+ "setHasFlowTasksStarted:"
+ "setHasFollowup:"
+ "setHasFollowupType:"
+ "setHasHasConversion:"
+ "setHasHomeEphemeralId:"
+ "setHasIMacCount:"
+ "setHasIPadCount:"
+ "setHasIPhoneCount:"
+ "setHasImageUrl:"
+ "setHasIsBoltEnabled:"
+ "setHasIsCommonForegroundApp:"
+ "setHasIsContentFree:"
+ "setHasIsLeader:"
+ "setHasIsRawLastNowPlayingBoolean:"
+ "setHasIsServerUserDataSyncEnabled:"
+ "setHasIsSiriResultUseful:"
+ "setHasIsUserRecognized:"
+ "setHasLoggingActionId:"
+ "setHasMacBookCount:"
+ "setHasMacStudioCount:"
+ "setHasMapsAction:"
+ "setHasMapsActionType:"
+ "setHasMapsSignal:"
+ "setHasMapsSignalGenerated:"
+ "setHasNearbyPersonalDevicesReported:"
+ "setHasNlLocation:"
+ "setHasNumberOfActionsAfter:"
+ "setHasNumberOfActionsBefore:"
+ "setHasNumberOfSeconds:"
+ "setHasNumberSuggestionShownBefore:"
+ "setHasOddId:"
+ "setHasOnDeviceDigest:"
+ "setHasReadableAttribution:"
+ "setHasReliabilityCounts:"
+ "setHasReliabilityRequestCount:"
+ "setHasReliabilityTurnCount:"
+ "setHasRotatedElectionParticipantId:"
+ "setHasSecondsSinceEphemeralIdCreation:"
+ "setHasSecondsToConversion:"
+ "setHasSegmentDataAvailabilityState:"
+ "setHasSegmentType:"
+ "setHasSelectedUserEphemeralId:"
+ "setHasSiriTasksCompleted:"
+ "setHasSiriTasksStarted:"
+ "setHasSiriUnavailableResponseCount:"
+ "setHasSourceDomain:"
+ "setHasStageStatus:"
+ "setHasStartTimestampInSecondsSince1970:"
+ "setHasSubText:"
+ "setHasThumbnail:"
+ "setHasTotalTurnCount:"
+ "setHasTouchIcon:"
+ "setHasTurnCounts:"
+ "setHasUndesiredResponseCount:"
+ "setHasUrl:"
+ "setHasUserAggregationId:"
+ "setHasUserAggregationIdExpirationTimestampMs:"
+ "setHasUserAggregationIdRotationTimestampMs:"
+ "setHasUserEphemeralId:"
+ "setHasValidTurnCount:"
+ "setHasViewInterface:"
+ "setHasVtAssetConfigVersion:"
+ "setHasWatchCount:"
+ "setHomeEphemeralId:"
+ "setIMacCount:"
+ "setIPadCount:"
+ "setIPhoneCount:"
+ "setImageUrl:"
+ "setIsBoltEnabled:"
+ "setIsCommonForegroundApp:"
+ "setIsContentFree:"
+ "setIsLeader:"
+ "setIsRawLastNowPlayingBoolean:"
+ "setIsServerUserDataSyncEnabled:"
+ "setIsSiriResultUseful:"
+ "setIsUserRecognized:"
+ "setLoggingActionId:"
+ "setMacBookCount:"
+ "setMacStudioCount:"
+ "setMapsAction:"
+ "setMapsActionType:"
+ "setMapsSignal:"
+ "setMapsSignalGenerated:"
+ "setNearbyPersonalDevicesReported:"
+ "setNlLocation:"
+ "setNumberOfActionsAfter:"
+ "setNumberOfActionsBefore:"
+ "setNumberOfSeconds:"
+ "setNumberSuggestionShownBefore:"
+ "setOddId:"
+ "setOnDeviceDigest:"
+ "setReadableAttribution:"
+ "setReliabilityCounts:"
+ "setReliabilityRequestCount:"
+ "setReliabilityTurnCount:"
+ "setRotatedElectionParticipantId:"
+ "setSecondsSinceEphemeralIdCreation:"
+ "setSecondsToConversion:"
+ "setSegmentDataAvailabilityState:"
+ "setSegmentType:"
+ "setSelectedUserEphemeralId:"
+ "setSiriTasksCompleted:"
+ "setSiriTasksStarted:"
+ "setSiriUnavailableResponseCount:"
+ "setSourceDomain:"
+ "setStageStatus:"
+ "setStartTimestampInSecondsSince1970:"
+ "setSubText:"
+ "setThumbnail:"
+ "setTotalTurnCount:"
+ "setTouchIcon:"
+ "setTurnCounts:"
+ "setUndesiredResponseCount:"
+ "setUrl:"
+ "setUserAggregationId:"
+ "setUserAggregationIdExpirationTimestampMs:"
+ "setUserAggregationIdRotationTimestampMs:"
+ "setUserEphemeralId:"
+ "setValidTurnCount:"
+ "setViewInterface:"
+ "setVtAssetConfigVersion:"
+ "setWatchCount:"
+ "siriTasksCompleted"
+ "siriTasksStarted"
+ "siriUnavailableResponseCount"
+ "sourceDomain"
+ "stageStatus"
+ "startTimestampInSecondsSince1970"
+ "subText"
+ "thumbnail"
+ "totalTurnCount"
+ "touchIcon"
+ "turnCounts"
+ "undesiredResponseCount"
+ "url"
+ "userAggregationId"
+ "userAggregationIdExpirationTimestampMs"
+ "userAggregationIdRotationTimestampMs"
+ "userEphemeralId"
+ "validTurnCount"
+ "viewInterface"
+ "vtAssetConfigVersion"
+ "watchCount"
+ "writeInt32:forTag:"
+ "{?=\"assistantEnabled\"b1\"dictationEnabled\"b1\"hardwareButtonEnabled\"b1\"heySiriEnabled\"b1\"assistantOnLockscreen\"b1\"raiseToSpeakEnabled\"b1\"spokenNotificationsEnabled\"b1\"hasHomekitHome\"b1\"shortcutsAvailable\"b1\"dataSharingOptInStatus\"b1\"typeToSiriEnabled\"b1\"isPreciseLocationEnabled\"b1\"voiceFeedback\"b1\"isAdaptiveVolumeEnabled\"b1\"isRemoteDarwinHeySiriEnabled\"b1\"isAutoPunctuationEnabled\"b1\"isHSHangupEnabled\"b1\"isSiriInCallEnabled\"b1\"hsHangupEnablementState\"b1\"siriInCallEnablementState\"b1\"isAlwaysShowSiriCaptionsEnabled\"b1\"isAlwaysShowSpeechEnabled\"b1\"isShowAppsBehindSiriEnabled\"b1\"siriSpeechRate\"b1\"isVoiceOverEnabled\"b1\"isShowAppsBehindSiriEnabledOnCarPlay\"b1\"isSiriCapableDigitalCarKeyAvailable\"b1\"isAlwaysListenForHeySiriEnabled\"b1\"siriPauseTimeState\"b1\"isMteUploadEnabled\"b1\"isServerUserDataSyncEnabled\"b1}"
+ "{?=\"audioTopology\"b1\"isLeader\"b1}"
+ "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1\"isContentFree\"b1\"isUserRecognized\"b1}"
+ "{?=\"cohortType\"b1\"cohortDataAvailabilityState\"b1}"
+ "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1\"nlLocation\"b1}"
+ "{?=\"dataSharingOptInStatus\"b1\"viewInterface\"b1\"asrLocation\"b1}"
+ "{?=\"daysWithTwoValidAssistantTurnsPerWeek\"b1\"daysWithTwoAssistantSpeechRequestsPerWeek\"b1}"
+ "{?=\"eventTimestampInMsSince1970\"b1}"
+ "{?=\"followupType\"b1\"mapsAction\"b1}"
+ "{?=\"iPhoneCount\"b1\"iPadCount\"b1\"watchCount\"b1\"macBookCount\"b1\"macStudioCount\"b1\"iMacCount\"b1}"
+ "{?=\"isClientForegroundActiveBundle\"b1\"compoundActiveBundleScore\"b1\"compoundMediaTypeBundleScore\"b1\"entitySearchBundleRecencyS\"b1\"entitySearchBundleScore\"b1\"isForegroundBundle\"b1\"isNowPlayingBundle\"b1\"nowPlayingBundleCount\"b1\"nowPlayingBundleRecencyS\"b1\"nowPlayingBundleScore\"b1\"isNowPlayingLastBundle\"b1\"nowPlayingUsage1Day\"b1\"nowPlayingUsage7Days\"b1\"nowPlayingUsage14Days\"b1\"isRawLastNowPlayingCoreDuet\"b1\"isRawMediaCategoryAudiobookSignal\"b1\"isRawMediaCategoryMusicSignal\"b1\"isRawMediaCategoryPodcastSignal\"b1\"isRawMediaCategoryRadioSignal\"b1\"isRawMediaCategoryVideoSignal\"b1\"rawMediaTypeUsageSignalBook\"b1\"rawMediaTypeUsageSignalMusic\"b1\"rawMediaTypeUsageSignalPodcast\"b1\"rawMediaTypeUsageSignalVideo\"b1\"rawNowPlayingCountCoreDuet10Min\"b1\"rawNowPlayingCountCoreDuet1Day\"b1\"rawNowPlayingCountCoreDuet1Hr\"b1\"rawNowPlayingCountCoreDuet28Day\"b1\"rawNowPlayingCountCoreDuet2Min\"b1\"rawNowPlayingCountCoreDuet6Hr\"b1\"rawNowPlayingCountCoreDuet7Day\"b1\"rawNowPlayingRecencyCD\"b1\"rawEntitySearchRecency\"b1\"usageScoreBooks\"b1\"usageScoreMusic\"b1\"usageScorePodcasts\"b1\"isAppFirstParty\"b1\"isRequestedApp\"b1\"isNowPlayingBundlePSE1\"b1\"isNowPlayingBundlePSE2\"b1\"vq21Score\"b1\"isSupportedFlag\"b1\"isUnicornFlag\"b1\"isSupportedUnicornMatchFlag\"b1\"isDisambiguationSelectedApp\"b1\"isModelPredictedApp\"b1\"usageScoreRadio\"b1\"usageScoreMusicWithoutRadio\"b1\"rawMediaTypeUsageSignalRadio\"b1\"rawMediaTypeUsageSignalMusicWithoutRadio\"b1\"subscriptionStatus\"b1\"isRawNowPlayingBundle\"b1\"rawNowPlayingTotal\"b1\"rawNowPlayingBundleScore\"b1\"isRawLastNowPlaying\"b1\"rawNowPlaying2Minutes\"b1\"rawNowPlaying10Minutes\"b1\"rawNowPlaying1Hour\"b1\"rawNowPlaying6Hours\"b1\"rawNowPlaying1Day\"b1\"rawNowPlaying7Days\"b1\"rawNowPlaying28Days\"b1\"rawLastNowPlayingRecency\"b1\"commonForegroundBundleApp\"b1\"isRawLastNowPlayingBoolean\"b1\"isCommonForegroundApp\"b1\"isBoltEnabled\"b1}"
+ "{?=\"isSiriResultUseful\"b1}"
+ "{?=\"numberSuggestionShownBefore\"b1\"hasConversion\"b1\"secondsToConversion\"b1\"numberOfActionsBefore\"b1\"numberOfActionsAfter\"b1\"daysBucketType\"b1}"
+ "{?=\"pageNumber\"b1\"maxNumContinuousZeros\"b1\"maxNumAllowedContinuousZeros\"b1\"isMaxNumContinuousZerosOverThreshold\"b1\"stageStatus\"b1}"
+ "{?=\"programCode\"b1}"
+ "{?=\"reliabilityRequestCount\"b1\"reliabilityTurnCount\"b1\"clientErrorCount\"b1\"undesiredResponseCount\"b1\"fatalResponseCount\"b1\"failureResponseCount\"b1\"siriUnavailableResponseCount\"b1}"
+ "{?=\"secondsSinceEphemeralIdCreation\"b1}"
+ "{?=\"segmentType\"b1\"segmentDataAvailabilityState\"b1}"
+ "{?=\"siriTasksStarted\"b1\"siriTasksCompleted\"b1\"flowTasksStarted\"b1\"flowTasksCompleted\"b1}"
+ "{?=\"startTimestampInSecondsSince1970\"b1\"numberOfSeconds\"b1}"
+ "{?=\"systemLocale\"b1\"siriInputLocale\"b1\"dataSharingOptInState\"b1\"countryCode\"b1\"isStoreDemoMode\"b1\"timeIntervalSince1970\"b1\"isLowPowerModeEnabled\"b1\"programCode\"b1\"homeKitConfiguration\"b1\"availableDictationKeyboards\"b1}"
+ "{?=\"totalTurnCount\"b1\"validTurnCount\"b1}"
+ "{?=\"userAggregationIdRotationTimestampMs\"b1\"userAggregationIdExpirationTimestampMs\"b1}"
- "\x02Q"
- "\x11\x11\x11"
- "HKDEVICESAUDIOTOPOLOGY_HOME_THEATER"
- "{?=\"assistantEnabled\"b1\"dictationEnabled\"b1\"hardwareButtonEnabled\"b1\"heySiriEnabled\"b1\"assistantOnLockscreen\"b1\"raiseToSpeakEnabled\"b1\"spokenNotificationsEnabled\"b1\"hasHomekitHome\"b1\"shortcutsAvailable\"b1\"dataSharingOptInStatus\"b1\"typeToSiriEnabled\"b1\"isPreciseLocationEnabled\"b1\"voiceFeedback\"b1\"isAdaptiveVolumeEnabled\"b1\"isRemoteDarwinHeySiriEnabled\"b1\"isAutoPunctuationEnabled\"b1\"isHSHangupEnabled\"b1\"isSiriInCallEnabled\"b1\"hsHangupEnablementState\"b1\"siriInCallEnablementState\"b1\"isAlwaysShowSiriCaptionsEnabled\"b1\"isAlwaysShowSpeechEnabled\"b1\"isShowAppsBehindSiriEnabled\"b1\"siriSpeechRate\"b1\"isVoiceOverEnabled\"b1\"isShowAppsBehindSiriEnabledOnCarPlay\"b1\"isSiriCapableDigitalCarKeyAvailable\"b1\"isAlwaysListenForHeySiriEnabled\"b1\"siriPauseTimeState\"b1\"isMteUploadEnabled\"b1}"
- "{?=\"audioTopology\"b1}"
- "{?=\"clientDayOfWeek\"b1\"rawClientHourOfDay\"b1\"isMediaAlbumPresent\"b1\"isMediaArtistPresent\"b1\"isMediaGenrePresent\"b1\"isMediaMoodPresent\"b1\"isMediaNamePresent\"b1\"isMediaReleaseDatePresent\"b1\"nowPlayingLastBundleRecencyS\"b1\"rawLanguage\"b1\"rawLocale\"b1\"rawRegion\"b1\"isClientDaylight\"b1\"isClientNavigating\"b1\"isClientWorkout\"b1\"mediaType\"b1\"nowPlayingState\"b1\"isPireneRequest\"b1\"foregroundBundleRecencyS\"b1\"mediaParsecCategory\"b1\"sirikitResponseCode\"b1\"appSelectionUses\"b1\"modelVersion\"b1\"resolutionType\"b1\"rawNowPlayingState\"b1\"commonForegroundAppRecency\"b1}"
- "{?=\"isClientForegroundActiveBundle\"b1\"compoundActiveBundleScore\"b1\"compoundMediaTypeBundleScore\"b1\"entitySearchBundleRecencyS\"b1\"entitySearchBundleScore\"b1\"isForegroundBundle\"b1\"isNowPlayingBundle\"b1\"nowPlayingBundleCount\"b1\"nowPlayingBundleRecencyS\"b1\"nowPlayingBundleScore\"b1\"isNowPlayingLastBundle\"b1\"nowPlayingUsage1Day\"b1\"nowPlayingUsage7Days\"b1\"nowPlayingUsage14Days\"b1\"isRawLastNowPlayingCoreDuet\"b1\"isRawMediaCategoryAudiobookSignal\"b1\"isRawMediaCategoryMusicSignal\"b1\"isRawMediaCategoryPodcastSignal\"b1\"isRawMediaCategoryRadioSignal\"b1\"isRawMediaCategoryVideoSignal\"b1\"rawMediaTypeUsageSignalBook\"b1\"rawMediaTypeUsageSignalMusic\"b1\"rawMediaTypeUsageSignalPodcast\"b1\"rawMediaTypeUsageSignalVideo\"b1\"rawNowPlayingCountCoreDuet10Min\"b1\"rawNowPlayingCountCoreDuet1Day\"b1\"rawNowPlayingCountCoreDuet1Hr\"b1\"rawNowPlayingCountCoreDuet28Day\"b1\"rawNowPlayingCountCoreDuet2Min\"b1\"rawNowPlayingCountCoreDuet6Hr\"b1\"rawNowPlayingCountCoreDuet7Day\"b1\"rawNowPlayingRecencyCD\"b1\"rawEntitySearchRecency\"b1\"usageScoreBooks\"b1\"usageScoreMusic\"b1\"usageScorePodcasts\"b1\"isAppFirstParty\"b1\"isRequestedApp\"b1\"isNowPlayingBundlePSE1\"b1\"isNowPlayingBundlePSE2\"b1\"vq21Score\"b1\"isSupportedFlag\"b1\"isUnicornFlag\"b1\"isSupportedUnicornMatchFlag\"b1\"isDisambiguationSelectedApp\"b1\"isModelPredictedApp\"b1\"usageScoreRadio\"b1\"usageScoreMusicWithoutRadio\"b1\"rawMediaTypeUsageSignalRadio\"b1\"rawMediaTypeUsageSignalMusicWithoutRadio\"b1\"subscriptionStatus\"b1\"isRawNowPlayingBundle\"b1\"rawNowPlayingTotal\"b1\"rawNowPlayingBundleScore\"b1\"isRawLastNowPlaying\"b1\"rawNowPlaying2Minutes\"b1\"rawNowPlaying10Minutes\"b1\"rawNowPlaying1Hour\"b1\"rawNowPlaying6Hours\"b1\"rawNowPlaying1Day\"b1\"rawNowPlaying7Days\"b1\"rawNowPlaying28Days\"b1\"rawLastNowPlayingRecency\"b1\"commonForegroundBundleApp\"b1}"
- "{?=\"pageNumber\"b1\"maxNumContinuousZeros\"b1\"maxNumAllowedContinuousZeros\"b1\"isMaxNumContinuousZerosOverThreshold\"b1}"
- "{?=\"systemLocale\"b1\"siriInputLocale\"b1\"dataSharingOptInState\"b1\"countryCode\"b1\"isStoreDemoMode\"b1\"timeIntervalSince1970\"b1\"isLowPowerModeEnabled\"b1\"programCode\"b1\"homeKitConfiguration\"b1}"

```
