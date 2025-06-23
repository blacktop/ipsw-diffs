## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation`

```diff

-3500.90.2.0.0
-  __TEXT.__text: 0x9ebc5c
+3500.96.1.0.0
+  __TEXT.__text: 0x9f9440
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0xcf78c
-  __TEXT.__const: 0x11988
-  __TEXT.__cstring: 0x7823f
-  __TEXT.__constg_swiftt: 0x62c0
-  __TEXT.__swift5_typeref: 0x1882
-  __TEXT.__swift5_builtin: 0x3930
+  __TEXT.__objc_methlist: 0xd0b5c
+  __TEXT.__const: 0x11acc
+  __TEXT.__cstring: 0x78944
+  __TEXT.__constg_swiftt: 0x6320
+  __TEXT.__swift5_typeref: 0x1894
+  __TEXT.__swift5_builtin: 0x396c
   __TEXT.__swift5_reflstr: 0x214
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_proto: 0xeb4
-  __TEXT.__swift5_types: 0xbc0
+  __TEXT.__swift5_proto: 0xec4
+  __TEXT.__swift5_types: 0xbcc
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x29df0
+  __TEXT.__unwind_info: 0x2a198
   __TEXT.__eh_frame: 0x22b0
-  __TEXT.__objc_classname: 0x15599
-  __TEXT.__objc_methname: 0x11e1c0
-  __TEXT.__objc_methtype: 0x27a27
-  __TEXT.__objc_stubs: 0x68080
-  __DATA_CONST.__got: 0x4c10
-  __DATA_CONST.__const: 0x346f8
-  __DATA_CONST.__objc_classlist: 0x4af0
+  __TEXT.__objc_classname: 0x1580a
+  __TEXT.__objc_methname: 0x1202d4
+  __TEXT.__objc_methtype: 0x27f3a
+  __TEXT.__objc_stubs: 0x68ba0
+  __DATA_CONST.__got: 0x4c80
+  __DATA_CONST.__const: 0x349c0
+  __DATA_CONST.__objc_classlist: 0x4b60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35cc8
+  __DATA_CONST.__objc_selrefs: 0x362c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x7448
+  __DATA_CONST.__objc_superrefs: 0x7500
   __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x20f80
-  __AUTH_CONST.__cfstring: 0x68420
-  __AUTH_CONST.__objc_const: 0x119180
+  __AUTH_CONST.__const: 0x20ff8
+  __AUTH_CONST.__cfstring: 0x68ca0
+  __AUTH_CONST.__objc_const: 0x11ac90
   __AUTH_CONST.__objc_intobj: 0xb70
-  __AUTH.__objc_data: 0x11058
-  __DATA.__objc_ivar: 0xdfa4
-  __DATA.__data: 0x1fd0
-  __DATA.__bss: 0x18680
+  __AUTH.__objc_data: 0x114b8
+  __DATA.__objc_ivar: 0xe100
+  __DATA.__data: 0x1ff0
+  __DATA.__bss: 0x18800
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x1df58
   __DATA_DIRTY.__data: 0x590

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0CF55D6F-5259-36C7-A52B-AC9D0E7FA2BC
-  Functions: 75126
-  Symbols:   186924
-  CStrings:  76910
+  UUID: 587F8B74-C746-39A7-9F8C-017C5BDFAE91
+  Functions: 75561
+  Symbols:   188031
+  CStrings:  77382
 
Symbols:
+ +[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(InnerEventContainer) getInnerTypeStringByTag:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent .cxx_destruct]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent deleteEventMetadata]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent deleteSpeechProfileUpdateContext]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent eventMetadata]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent hasEventMetadata]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent hasSpeechProfileUpdateContext]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent qualifiedMessageName]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent setEventMetadata:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent setHasEventMetadata:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent setHasSpeechProfileUpdateContext:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent setSpeechProfileUpdateContext:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent speechProfileUpdateContext]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent whichEvent_Type]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(InnerEventContainer) innerEvent]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(InnerEventContainer) whichInnerEventType]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(InstrumentationAdditions) getAnyEventType]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(IsolationLevel) clockIsolationLevel]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEvent(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata .cxx_destruct]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata deleteSpeechProfileId]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata hasSpeechProfileId]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata setHasSpeechProfileId:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata setSpeechProfileId:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata speechProfileId]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics deleteIsCleanupIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics deleteNumEntitiesCleaned]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics deleteNumEntitiesContainingEmoji]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics deleteNumEntitiesContainingSpecialCharacters]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics hasIsCleanupIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics hasNumEntitiesCleaned]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics hasNumEntitiesContainingEmoji]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics hasNumEntitiesContainingSpecialCharacters]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics isCleanupIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics numEntitiesCleaned]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics numEntitiesContainingEmoji]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics numEntitiesContainingSpecialCharacters]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setHasIsCleanupIngestionEnabled:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setHasNumEntitiesCleaned:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setHasNumEntitiesContainingEmoji:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setHasNumEntitiesContainingSpecialCharacters:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setIsCleanupIngestionEnabled:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setNumEntitiesCleaned:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setNumEntitiesContainingEmoji:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics setNumEntitiesContainingSpecialCharacters:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics deleteIsExtractionIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics deleteIsExtractionSetupSuccessful]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics deleteNumEntitiesContainingExtractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics deleteNumEntitiesExtracted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics deleteNumEntitiesExtractionAttempted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hasIsExtractionIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hasIsExtractionSetupSuccessful]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hasNumEntitiesContainingExtractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hasNumEntitiesExtracted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hasNumEntitiesExtractionAttempted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics isExtractionIngestionEnabled]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics isExtractionSetupSuccessful]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics numEntitiesContainingExtractions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics numEntitiesExtracted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics numEntitiesExtractionAttempted]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setHasIsExtractionIngestionEnabled:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setHasIsExtractionSetupSuccessful:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setHasNumEntitiesContainingExtractions:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setHasNumEntitiesExtracted:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setHasNumEntitiesExtractionAttempted:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setIsExtractionIngestionEnabled:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setIsExtractionSetupSuccessful:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setNumEntitiesContainingExtractions:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setNumEntitiesExtracted:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics setNumEntitiesExtractionAttempted:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext .cxx_destruct]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext deleteEnded]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext deleteFailed]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext deleteStartedOrChanged]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext ended]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext failed]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext hasEnded]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext hasFailed]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext hasStartedOrChanged]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setEnded:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setFailed:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setHasEnded:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setHasFailed:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setHasStartedOrChanged:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext setStartedOrChanged:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext startedOrChanged]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext whichContextevent]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded .cxx_destruct]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteEntityCleanupMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteEntityExtractionMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded deleteTotalNumEntitiesReceived]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded entityCleanupMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded entityExtractionMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded hasEntityCleanupMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded hasEntityExtractionMetrics]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded hasTotalNumEntitiesReceived]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setEntityCleanupMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setEntityExtractionMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setHasEntityCleanupMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setHasEntityExtractionMetrics:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setHasTotalNumEntitiesReceived:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded setTotalNumEntitiesReceived:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded totalNumEntitiesReceived]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed deleteSpeechProfileUpdateFailureReason]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed hasSpeechProfileUpdateFailureReason]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed setHasSpeechProfileUpdateFailureReason:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed setSpeechProfileUpdateFailureReason:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed speechProfileUpdateFailureReason]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted deleteExists]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted dictionaryRepresentation]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted exists]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted hasExists]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted hash]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted initWithDictionary:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted initWithJSON:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted isEqual:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted jsonData]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted readFrom:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted setExists:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted setHasExists:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted writeTo:]
+ -[ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDGeneralProperties dataCollectionId]
+ -[ODDSiriSchemaODDGeneralProperties deleteDataCollectionId]
+ -[ODDSiriSchemaODDGeneralProperties hasDataCollectionId]
+ -[ODDSiriSchemaODDGeneralProperties setDataCollectionId:]
+ -[ODDSiriSchemaODDGeneralProperties setHasDataCollectionId:]
+ -[ODDSiriSchemaODDMAErrorsDigest .cxx_destruct]
+ -[ODDSiriSchemaODDMAErrorsDigest deleteMaErrorsDimensions]
+ -[ODDSiriSchemaODDMAErrorsDigest deleteMaFailureCount]
+ -[ODDSiriSchemaODDMAErrorsDigest deleteMaSuccessCount]
+ -[ODDSiriSchemaODDMAErrorsDigest dictionaryRepresentation]
+ -[ODDSiriSchemaODDMAErrorsDigest hasMaErrorsDimensions]
+ -[ODDSiriSchemaODDMAErrorsDigest hasMaFailureCount]
+ -[ODDSiriSchemaODDMAErrorsDigest hasMaSuccessCount]
+ -[ODDSiriSchemaODDMAErrorsDigest hash]
+ -[ODDSiriSchemaODDMAErrorsDigest initWithDictionary:]
+ -[ODDSiriSchemaODDMAErrorsDigest initWithJSON:]
+ -[ODDSiriSchemaODDMAErrorsDigest isEqual:]
+ -[ODDSiriSchemaODDMAErrorsDigest jsonData]
+ -[ODDSiriSchemaODDMAErrorsDigest maErrorsDimensions]
+ -[ODDSiriSchemaODDMAErrorsDigest maFailureCount]
+ -[ODDSiriSchemaODDMAErrorsDigest maSuccessCount]
+ -[ODDSiriSchemaODDMAErrorsDigest readFrom:]
+ -[ODDSiriSchemaODDMAErrorsDigest setHasMaErrorsDimensions:]
+ -[ODDSiriSchemaODDMAErrorsDigest setHasMaFailureCount:]
+ -[ODDSiriSchemaODDMAErrorsDigest setHasMaSuccessCount:]
+ -[ODDSiriSchemaODDMAErrorsDigest setMaErrorsDimensions:]
+ -[ODDSiriSchemaODDMAErrorsDigest setMaFailureCount:]
+ -[ODDSiriSchemaODDMAErrorsDigest setMaSuccessCount:]
+ -[ODDSiriSchemaODDMAErrorsDigest writeTo:]
+ -[ODDSiriSchemaODDMAErrorsDigest(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDMAErrorsDigest(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDMAErrorsDimensions .cxx_destruct]
+ -[ODDSiriSchemaODDMAErrorsDimensions AssetSpecifier]
+ -[ODDSiriSchemaODDMAErrorsDimensions AssetType]
+ -[ODDSiriSchemaODDMAErrorsDimensions AssetVersion]
+ -[ODDSiriSchemaODDMAErrorsDimensions IsDiscretionary]
+ -[ODDSiriSchemaODDMAErrorsDimensions IsMAAutoAsset]
+ -[ODDSiriSchemaODDMAErrorsDimensions IsUserPriority]
+ -[ODDSiriSchemaODDMAErrorsDimensions Result]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteAssetSpecifier]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteAssetType]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteAssetVersion]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteIsDiscretionary]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteIsMAAutoAsset]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteIsUserPriority]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteNetworkAccessType]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteOperationFailureReason]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteOperationResult]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteOperationType]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteResult]
+ -[ODDSiriSchemaODDMAErrorsDimensions deleteSubSystemName]
+ -[ODDSiriSchemaODDMAErrorsDimensions dictionaryRepresentation]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasAssetSpecifier]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasAssetType]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasAssetVersion]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasIsDiscretionary]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasIsMAAutoAsset]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasIsUserPriority]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasNetworkAccessType]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasOperationFailureReason]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasOperationResult]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasOperationType]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasResult]
+ -[ODDSiriSchemaODDMAErrorsDimensions hasSubSystemName]
+ -[ODDSiriSchemaODDMAErrorsDimensions hash]
+ -[ODDSiriSchemaODDMAErrorsDimensions initWithDictionary:]
+ -[ODDSiriSchemaODDMAErrorsDimensions initWithJSON:]
+ -[ODDSiriSchemaODDMAErrorsDimensions isEqual:]
+ -[ODDSiriSchemaODDMAErrorsDimensions jsonData]
+ -[ODDSiriSchemaODDMAErrorsDimensions networkAccessType]
+ -[ODDSiriSchemaODDMAErrorsDimensions operationFailureReason]
+ -[ODDSiriSchemaODDMAErrorsDimensions operationResult]
+ -[ODDSiriSchemaODDMAErrorsDimensions operationType]
+ -[ODDSiriSchemaODDMAErrorsDimensions readFrom:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setAssetSpecifier:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setAssetType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setAssetVersion:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasAssetSpecifier:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasAssetType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasAssetVersion:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasIsDiscretionary:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasIsMAAutoAsset:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasIsUserPriority:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasNetworkAccessType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasOperationFailureReason:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasOperationResult:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasOperationType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasResult:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setHasSubSystemName:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setIsDiscretionary:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setIsMAAutoAsset:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setIsUserPriority:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setNetworkAccessType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setOperationFailureReason:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setOperationResult:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setOperationType:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setResult:]
+ -[ODDSiriSchemaODDMAErrorsDimensions setSubSystemName:]
+ -[ODDSiriSchemaODDMAErrorsDimensions subSystemName]
+ -[ODDSiriSchemaODDMAErrorsDimensions writeTo:]
+ -[ODDSiriSchemaODDMAErrorsDimensions(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDMAErrorsDimensions(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDMANetworkAccessTypes cellularAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes cellularAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes constrainedNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes constrainedNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteCellularAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteCellularAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteConstrainedNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteConstrainedNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteExpensiveNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes deleteExpensiveNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes dictionaryRepresentation]
+ -[ODDSiriSchemaODDMANetworkAccessTypes expensiveNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes expensiveNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasCellularAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasCellularAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasConstrainedNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasConstrainedNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasExpensiveNetworkAccessRequest]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hasExpensiveNetworkAccessResponse]
+ -[ODDSiriSchemaODDMANetworkAccessTypes hash]
+ -[ODDSiriSchemaODDMANetworkAccessTypes initWithDictionary:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes initWithJSON:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes isEqual:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes jsonData]
+ -[ODDSiriSchemaODDMANetworkAccessTypes readFrom:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setCellularAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setCellularAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setConstrainedNetworkAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setConstrainedNetworkAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setExpensiveNetworkAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setExpensiveNetworkAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasCellularAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasCellularAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasConstrainedNetworkAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasConstrainedNetworkAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasExpensiveNetworkAccessRequest:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes setHasExpensiveNetworkAccessResponse:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes writeTo:]
+ -[ODDSiriSchemaODDMANetworkAccessTypes(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported .cxx_destruct]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported addMaErrorsDigest:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported clearMaErrorsDigest]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported deleteFixedDimensions]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported deleteMaErrorsDigest]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported deleteMaEventType]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported fixedDimensions]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported hasFixedDimensions]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported hasMaEventType]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported hash]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported initWithDictionary:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported initWithJSON:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported isEqual:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported jsonData]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported maErrorsDigestAtIndex:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported maErrorsDigestCount]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported maErrorsDigests]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported maEventType]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported readFrom:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported setFixedDimensions:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported setHasFixedDimensions:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported setHasMaEventType:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported setMaErrorsDigests:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported setMaEventType:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported writeTo:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ODDSiriSchemaODDMobileAssetErrorsReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriClientEvent deleteMobileAssetErrorsReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasMobileAssetErrorsReported]
+ -[ODDSiriSchemaODDSiriClientEvent mobileAssetErrorsReported]
+ -[ODDSiriSchemaODDSiriClientEvent setHasMobileAssetErrorsReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setMobileAssetErrorsReported:]
+ -[ORCHSchemaORCHError .cxx_destruct]
+ -[ORCHSchemaORCHError deleteErrorCode]
+ -[ORCHSchemaORCHError deleteErrorDomain]
+ -[ORCHSchemaORCHError dictionaryRepresentation]
+ -[ORCHSchemaORCHError errorCode]
+ -[ORCHSchemaORCHError errorDomain]
+ -[ORCHSchemaORCHError hasErrorCode]
+ -[ORCHSchemaORCHError hasErrorDomain]
+ -[ORCHSchemaORCHError hash]
+ -[ORCHSchemaORCHError initWithDictionary:]
+ -[ORCHSchemaORCHError initWithJSON:]
+ -[ORCHSchemaORCHError isEqual:]
+ -[ORCHSchemaORCHError jsonData]
+ -[ORCHSchemaORCHError readFrom:]
+ -[ORCHSchemaORCHError setErrorCode:]
+ -[ORCHSchemaORCHError setErrorDomain:]
+ -[ORCHSchemaORCHError setHasErrorCode:]
+ -[ORCHSchemaORCHError setHasErrorDomain:]
+ -[ORCHSchemaORCHError writeTo:]
+ -[ORCHSchemaORCHError(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHIFFlowError .cxx_destruct]
+ -[ORCHSchemaORCHIFFlowError deleteIfflowErrorCode]
+ -[ORCHSchemaORCHIFFlowError deleteUnderLyingError]
+ -[ORCHSchemaORCHIFFlowError dictionaryRepresentation]
+ -[ORCHSchemaORCHIFFlowError hasIfflowErrorCode]
+ -[ORCHSchemaORCHIFFlowError hasUnderLyingError]
+ -[ORCHSchemaORCHIFFlowError hash]
+ -[ORCHSchemaORCHIFFlowError ifflowErrorCode]
+ -[ORCHSchemaORCHIFFlowError initWithDictionary:]
+ -[ORCHSchemaORCHIFFlowError initWithJSON:]
+ -[ORCHSchemaORCHIFFlowError isEqual:]
+ -[ORCHSchemaORCHIFFlowError jsonData]
+ -[ORCHSchemaORCHIFFlowError readFrom:]
+ -[ORCHSchemaORCHIFFlowError setHasIfflowErrorCode:]
+ -[ORCHSchemaORCHIFFlowError setHasUnderLyingError:]
+ -[ORCHSchemaORCHIFFlowError setIfflowErrorCode:]
+ -[ORCHSchemaORCHIFFlowError setUnderLyingError:]
+ -[ORCHSchemaORCHIFFlowError underLyingError]
+ -[ORCHSchemaORCHIFFlowError writeTo:]
+ -[ORCHSchemaORCHIFFlowError(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[ORCHSchemaORCHIFFlowError(SensitiveConditions) suppressMessageUnderConditions]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed .cxx_destruct]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed deleteIfflowError]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed hasIfflowError]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed ifflowError]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setHasIfflowError:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed setIfflowError:]
+ -[ORCHSchemaORCHIntelligenceFlowRequestFailed(SensitiveConditions) applySensitiveConditionsPolicy:]
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent._eventMetadata
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent._speechProfileUpdateContext
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata._speechProfileId
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics._isCleanupIngestionEnabled
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics._numEntitiesCleaned
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics._numEntitiesContainingEmoji
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics._numEntitiesContainingSpecialCharacters
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._isExtractionIngestionEnabled
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._isExtractionSetupSuccessful
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._numEntitiesContainingExtractions
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._numEntitiesExtracted
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics._numEntitiesExtractionAttempted
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._ended
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._failed
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._startedOrChanged
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._entityCleanupMetrics
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._entityExtractionMetrics
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._totalNumEntitiesReceived
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed._has
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed._speechProfileUpdateFailureReason
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted._exists
+ OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted._has
+ OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._dataCollectionId
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDigest._has
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDigest._maErrorsDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDigest._maFailureCount
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDigest._maSuccessCount
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._AssetSpecifier
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._AssetType
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._AssetVersion
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._IsDiscretionary
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._IsMAAutoAsset
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._IsUserPriority
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._Result
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._has
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._networkAccessType
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._operationFailureReason
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._operationResult
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._operationType
+ OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._subSystemName
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._cellularAccessRequest
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._cellularAccessResponse
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._constrainedNetworkAccessRequest
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._constrainedNetworkAccessResponse
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._expensiveNetworkAccessRequest
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._expensiveNetworkAccessResponse
+ OBJC_IVAR_$_ODDSiriSchemaODDMANetworkAccessTypes._has
+ OBJC_IVAR_$_ODDSiriSchemaODDMobileAssetErrorsReported._fixedDimensions
+ OBJC_IVAR_$_ODDSiriSchemaODDMobileAssetErrorsReported._has
+ OBJC_IVAR_$_ODDSiriSchemaODDMobileAssetErrorsReported._maErrorsDigests
+ OBJC_IVAR_$_ODDSiriSchemaODDMobileAssetErrorsReported._maEventType
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._mobileAssetErrorsReported
+ OBJC_IVAR_$_ORCHSchemaORCHError._errorCode
+ OBJC_IVAR_$_ORCHSchemaORCHError._errorDomain
+ OBJC_IVAR_$_ORCHSchemaORCHError._has
+ OBJC_IVAR_$_ORCHSchemaORCHIFFlowError._has
+ OBJC_IVAR_$_ORCHSchemaORCHIFFlowError._ifflowErrorCode
+ OBJC_IVAR_$_ORCHSchemaORCHIFFlowError._underLyingError
+ OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestFailed._ifflowError
+ _ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadataReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileClientEventReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetricsReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetricsReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileUpdateContextReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileUpdateEndedReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileUpdateFailedReadFrom
+ _ASRSpeechProfileSchemaASRSpeechProfileUpdateStartedReadFrom
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ _OBJC_CLASS_$_ODDSiriSchemaODDMAErrorsDigest
+ _OBJC_CLASS_$_ODDSiriSchemaODDMAErrorsDimensions
+ _OBJC_CLASS_$_ODDSiriSchemaODDMANetworkAccessTypes
+ _OBJC_CLASS_$_ODDSiriSchemaODDMobileAssetErrorsReported
+ _OBJC_CLASS_$_ORCHSchemaORCHError
+ _OBJC_CLASS_$_ORCHSchemaORCHIFFlowError
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent._hasEventMetadata
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent._hasSpeechProfileUpdateContext
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent._whichEvent_Type
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata._hasSpeechProfileId
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._hasEnded
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._hasFailed
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._hasStartedOrChanged
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext._whichContextevent
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._hasEntityCleanupMetrics
+ _OBJC_IVAR_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded._hasEntityExtractionMetrics
+ _OBJC_IVAR_$_ODDSiriSchemaODDGeneralProperties._hasDataCollectionId
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDigest._hasMaErrorsDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasAssetSpecifier
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasAssetType
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasAssetVersion
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasNetworkAccessType
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasOperationFailureReason
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasOperationResult
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasResult
+ _OBJC_IVAR_$_ODDSiriSchemaODDMAErrorsDimensions._hasSubSystemName
+ _OBJC_IVAR_$_ODDSiriSchemaODDMobileAssetErrorsReported._hasFixedDimensions
+ _OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasMobileAssetErrorsReported
+ _OBJC_IVAR_$_ORCHSchemaORCHError._hasErrorDomain
+ _OBJC_IVAR_$_ORCHSchemaORCHIFFlowError._hasUnderLyingError
+ _OBJC_IVAR_$_ORCHSchemaORCHIntelligenceFlowRequestFailed._hasIfflowError
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ _OBJC_METACLASS_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMAErrorsDigest
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMAErrorsDimensions
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMANetworkAccessTypes
+ _OBJC_METACLASS_$_ODDSiriSchemaODDMobileAssetErrorsReported
+ _OBJC_METACLASS_$_ORCHSchemaORCHError
+ _OBJC_METACLASS_$_ORCHSchemaORCHIFFlowError
+ _ODDSiriSchemaODDMAErrorsDigestReadFrom
+ _ODDSiriSchemaODDMAErrorsDimensionsReadFrom
+ _ODDSiriSchemaODDMANetworkAccessTypesReadFrom
+ _ODDSiriSchemaODDMobileAssetErrorsReportedReadFrom
+ _ORCHSchemaORCHErrorReadFrom
+ _ORCHSchemaORCHIFFlowErrorReadFrom
+ __OBJC_$_CLASS_METHODS_ASRSpeechProfileSchemaASRSpeechProfileClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMAErrorsDigest(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMAErrorsDimensions(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMANetworkAccessTypes(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDMobileAssetErrorsReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHError(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHIFFlowError(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ __OBJC_$_INSTANCE_VARIABLES_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMAErrorsDigest
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMAErrorsDimensions
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMANetworkAccessTypes
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDMobileAssetErrorsReported
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHError
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHIFFlowError
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ __OBJC_$_PROP_LIST_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMAErrorsDigest
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMAErrorsDimensions
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMANetworkAccessTypes
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDMobileAssetErrorsReported
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHError
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHIFFlowError
+ __OBJC_CLASS_PROTOCOLS_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent(SensitiveConditions|InnerEventContainer|IsolationLevel|InstrumentationAdditions)
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ __OBJC_CLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMAErrorsDigest
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMAErrorsDimensions
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMANetworkAccessTypes
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDMobileAssetErrorsReported
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHError
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHIFFlowError
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileClientEvent
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateContext
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed
+ __OBJC_METACLASS_RO_$_ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMAErrorsDigest
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMAErrorsDimensions
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMANetworkAccessTypes
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDMobileAssetErrorsReported
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHError
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHIFFlowError
+ _objc_msgSend$AssetSpecifier
+ _objc_msgSend$AssetType
+ _objc_msgSend$AssetVersion
+ _objc_msgSend$IsDiscretionary
+ _objc_msgSend$IsMAAutoAsset
+ _objc_msgSend$IsUserPriority
+ _objc_msgSend$Result
+ _objc_msgSend$addMaErrorsDigest:
+ _objc_msgSend$cellularAccessRequest
+ _objc_msgSend$cellularAccessResponse
+ _objc_msgSend$clearMaErrorsDigest
+ _objc_msgSend$constrainedNetworkAccessRequest
+ _objc_msgSend$constrainedNetworkAccessResponse
+ _objc_msgSend$deleteEntityCleanupMetrics
+ _objc_msgSend$deleteEntityExtractionMetrics
+ _objc_msgSend$deleteIfflowError
+ _objc_msgSend$deleteMaErrorsDimensions
+ _objc_msgSend$deleteMobileAssetErrorsReported
+ _objc_msgSend$deleteNetworkAccessType
+ _objc_msgSend$deleteSpeechProfileId
+ _objc_msgSend$deleteSpeechProfileUpdateContext
+ _objc_msgSend$deleteUnderLyingError
+ _objc_msgSend$entityCleanupMetrics
+ _objc_msgSend$entityExtractionMetrics
+ _objc_msgSend$expensiveNetworkAccessRequest
+ _objc_msgSend$expensiveNetworkAccessResponse
+ _objc_msgSend$ifflowError
+ _objc_msgSend$ifflowErrorCode
+ _objc_msgSend$isCleanupIngestionEnabled
+ _objc_msgSend$isExtractionIngestionEnabled
+ _objc_msgSend$isExtractionSetupSuccessful
+ _objc_msgSend$maErrorsDigests
+ _objc_msgSend$maErrorsDimensions
+ _objc_msgSend$maEventType
+ _objc_msgSend$maFailureCount
+ _objc_msgSend$maSuccessCount
+ _objc_msgSend$mobileAssetErrorsReported
+ _objc_msgSend$networkAccessType
+ _objc_msgSend$numEntitiesCleaned
+ _objc_msgSend$numEntitiesContainingEmoji
+ _objc_msgSend$numEntitiesContainingExtractions
+ _objc_msgSend$numEntitiesContainingSpecialCharacters
+ _objc_msgSend$numEntitiesExtracted
+ _objc_msgSend$numEntitiesExtractionAttempted
+ _objc_msgSend$operationFailureReason
+ _objc_msgSend$operationResult
+ _objc_msgSend$setCellularAccessRequest:
+ _objc_msgSend$setCellularAccessResponse:
+ _objc_msgSend$setConstrainedNetworkAccessRequest:
+ _objc_msgSend$setConstrainedNetworkAccessResponse:
+ _objc_msgSend$setEntityCleanupMetrics:
+ _objc_msgSend$setEntityExtractionMetrics:
+ _objc_msgSend$setExpensiveNetworkAccessRequest:
+ _objc_msgSend$setExpensiveNetworkAccessResponse:
+ _objc_msgSend$setIfflowError:
+ _objc_msgSend$setIfflowErrorCode:
+ _objc_msgSend$setIsCleanupIngestionEnabled:
+ _objc_msgSend$setIsDiscretionary:
+ _objc_msgSend$setIsExtractionIngestionEnabled:
+ _objc_msgSend$setIsExtractionSetupSuccessful:
+ _objc_msgSend$setIsMAAutoAsset:
+ _objc_msgSend$setIsUserPriority:
+ _objc_msgSend$setMaErrorsDigests:
+ _objc_msgSend$setMaErrorsDimensions:
+ _objc_msgSend$setMaEventType:
+ _objc_msgSend$setMaFailureCount:
+ _objc_msgSend$setMaSuccessCount:
+ _objc_msgSend$setMobileAssetErrorsReported:
+ _objc_msgSend$setNetworkAccessType:
+ _objc_msgSend$setNumEntitiesCleaned:
+ _objc_msgSend$setNumEntitiesContainingEmoji:
+ _objc_msgSend$setNumEntitiesContainingExtractions:
+ _objc_msgSend$setNumEntitiesContainingSpecialCharacters:
+ _objc_msgSend$setNumEntitiesExtracted:
+ _objc_msgSend$setNumEntitiesExtractionAttempted:
+ _objc_msgSend$setOperationFailureReason:
+ _objc_msgSend$setOperationResult:
+ _objc_msgSend$setSpeechProfileId:
+ _objc_msgSend$setSpeechProfileUpdateContext:
+ _objc_msgSend$setSpeechProfileUpdateFailureReason:
+ _objc_msgSend$setSubSystemName:
+ _objc_msgSend$setTotalNumEntitiesReceived:
+ _objc_msgSend$setUnderLyingError:
+ _objc_msgSend$speechProfileId
+ _objc_msgSend$speechProfileUpdateContext
+ _objc_msgSend$speechProfileUpdateFailureReason
+ _objc_msgSend$subSystemName
+ _objc_msgSend$totalNumEntitiesReceived
+ _objc_msgSend$underLyingError
+ _qname_ASRSpeechProfileSchemaASRSpeechProfileClientEvent_WhichEvent_Type_None
+ _qname_ASRSpeechProfileSchemaASRSpeechProfileClientEvent_WhichEvent_Type_speechProfileUpdateContext
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_mobileAssetErrorsReported
+ _symbolic _____ So022ASRSpeechProfileSchemaaB19UpdateFailureReasonV
+ _symbolic _____ So27ODDSiriSchemaODDMAEventTypeV
+ _symbolic _____ So27ODDSiriSchemaODDMAOperationV
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SiriInstrumentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SiriInstrumentation
CStrings:
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateContext\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed\""
+ "@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted\""
+ "@\"ODDSiriSchemaODDMAErrorsDimensions\""
+ "@\"ODDSiriSchemaODDMANetworkAccessTypes\""
+ "@\"ODDSiriSchemaODDMobileAssetErrorsReported\""
+ "@\"ORCHSchemaORCHError\""
+ "@\"ORCHSchemaORCHIFFlowError\""
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_API_VIOLATION"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_CONNECTION_REJECTED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_INVALID_INPUT"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_PROFILE_CONNECTION_INTERRUPTED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_PROFILE_DELETION_FAILED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_PROFILE_READ_FAILED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_PROFILE_WRITE_FAILED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_SPEECH_ASSET_LOAD_FAILED"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_UNKNOWN"
+ "ASRSPEECHPROFILEUPDATEFAILUREREASON_UNSUPPORTED_SPEECH_CATEGORY"
+ "ASRSpeechProfileSchemaASRSpeechProfileClientEvent"
+ "ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata"
+ "ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics"
+ "ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics"
+ "ASRSpeechProfileSchemaASRSpeechProfileUpdateContext"
+ "ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded"
+ "ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed"
+ "ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted"
+ "ASR_SPEECH_PROFILE_CLIENT_EVENT"
+ "AssetSpecifier"
+ "AssetType"
+ "AssetVersion"
+ "COMPONENTNAME_ASR_SPEECH_PROFILE"
+ "IsDiscretionary"
+ "IsMAAutoAsset"
+ "IsUserPriority"
+ "ODDMAEVENTTYPE_DOWNLOAD_ERROR"
+ "ODDMAEVENTTYPE_SECURE_DETAIL"
+ "ODDMAEVENTTYPE_UNKNOWN"
+ "ODDMAOPERATION_DEPERSONALIZATION"
+ "ODDMAOPERATION_GRAFTING"
+ "ODDMAOPERATION_MOUNTING"
+ "ODDMAOPERATION_NOOP"
+ "ODDMAOPERATION_PERSONALIZATION"
+ "ODDMAOPERATION_UNGRAFTING"
+ "ODDMAOPERATION_UNKNOWN"
+ "ODDMAOPERATION_UNMOUNTING"
+ "ODDSiriSchemaODDMAErrorsDigest"
+ "ODDSiriSchemaODDMAErrorsDimensions"
+ "ODDSiriSchemaODDMANetworkAccessTypes"
+ "ODDSiriSchemaODDMobileAssetErrorsReported"
+ "ORCHSchemaORCHError"
+ "ORCHSchemaORCHIFFlowError"
+ "RESPONSECATEGORY_OFFER"
+ "Result"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileClientEventMetadata\",&,N,V_eventMetadata"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileEntityCleanupMetrics\",&,N,V_entityCleanupMetrics"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileEntityExtractionMetrics\",&,N,V_entityExtractionMetrics"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateContext\",&,N,V_speechProfileUpdateContext"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateEnded\",&,N,V_ended"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateFailed\",&,N,V_failed"
+ "T@\"ASRSpeechProfileSchemaASRSpeechProfileUpdateStarted\",&,N,V_startedOrChanged"
+ "T@\"NSArray\",C,N,V_maErrorsDigests"
+ "T@\"NSString\",C,N,V_AssetSpecifier"
+ "T@\"NSString\",C,N,V_AssetType"
+ "T@\"NSString\",C,N,V_AssetVersion"
+ "T@\"NSString\",C,N,V_Result"
+ "T@\"NSString\",C,N,V_operationFailureReason"
+ "T@\"NSString\",C,N,V_operationResult"
+ "T@\"NSString\",C,N,V_subSystemName"
+ "T@\"ODDSiriSchemaODDMAErrorsDimensions\",&,N,V_maErrorsDimensions"
+ "T@\"ODDSiriSchemaODDMANetworkAccessTypes\",&,N,V_networkAccessType"
+ "T@\"ODDSiriSchemaODDMobileAssetErrorsReported\",&,N,V_mobileAssetErrorsReported"
+ "T@\"ORCHSchemaORCHError\",&,N,V_underLyingError"
+ "T@\"ORCHSchemaORCHIFFlowError\",&,N,V_ifflowError"
+ "T@\"SISchemaUUID\",&,N,V_speechProfileId"
+ "TB,N,V_IsDiscretionary"
+ "TB,N,V_IsMAAutoAsset"
+ "TB,N,V_IsUserPriority"
+ "TB,N,V_cellularAccessRequest"
+ "TB,N,V_cellularAccessResponse"
+ "TB,N,V_constrainedNetworkAccessRequest"
+ "TB,N,V_constrainedNetworkAccessResponse"
+ "TB,N,V_expensiveNetworkAccessRequest"
+ "TB,N,V_expensiveNetworkAccessResponse"
+ "TB,N,V_hasEntityCleanupMetrics"
+ "TB,N,V_hasEntityExtractionMetrics"
+ "TB,N,V_hasIfflowError"
+ "TB,N,V_hasMaErrorsDimensions"
+ "TB,N,V_hasMobileAssetErrorsReported"
+ "TB,N,V_hasNetworkAccessType"
+ "TB,N,V_hasOperationFailureReason"
+ "TB,N,V_hasOperationResult"
+ "TB,N,V_hasSpeechProfileId"
+ "TB,N,V_hasSpeechProfileUpdateContext"
+ "TB,N,V_hasSubSystemName"
+ "TB,N,V_hasUnderLyingError"
+ "TB,N,V_isCleanupIngestionEnabled"
+ "TB,N,V_isExtractionIngestionEnabled"
+ "TB,N,V_isExtractionSetupSuccessful"
+ "TI,N,V_maFailureCount"
+ "TI,N,V_maSuccessCount"
+ "TI,N,V_numEntitiesCleaned"
+ "TI,N,V_numEntitiesContainingEmoji"
+ "TI,N,V_numEntitiesContainingExtractions"
+ "TI,N,V_numEntitiesContainingSpecialCharacters"
+ "TI,N,V_numEntitiesExtracted"
+ "TI,N,V_numEntitiesExtractionAttempted"
+ "TI,N,V_totalNumEntitiesReceived"
+ "Ti,N,V_maEventType"
+ "Ti,N,V_speechProfileUpdateFailureReason"
+ "Tq,N,V_ifflowErrorCode"
+ "_AssetSpecifier"
+ "_AssetType"
+ "_AssetVersion"
+ "_IsDiscretionary"
+ "_IsMAAutoAsset"
+ "_IsUserPriority"
+ "_Result"
+ "_cellularAccessRequest"
+ "_cellularAccessResponse"
+ "_constrainedNetworkAccessRequest"
+ "_constrainedNetworkAccessResponse"
+ "_entityCleanupMetrics"
+ "_entityExtractionMetrics"
+ "_expensiveNetworkAccessRequest"
+ "_expensiveNetworkAccessResponse"
+ "_hasEntityCleanupMetrics"
+ "_hasEntityExtractionMetrics"
+ "_hasIfflowError"
+ "_hasMaErrorsDimensions"
+ "_hasMobileAssetErrorsReported"
+ "_hasNetworkAccessType"
+ "_hasOperationFailureReason"
+ "_hasOperationResult"
+ "_hasSpeechProfileId"
+ "_hasSpeechProfileUpdateContext"
+ "_hasSubSystemName"
+ "_hasUnderLyingError"
+ "_ifflowError"
+ "_ifflowErrorCode"
+ "_isCleanupIngestionEnabled"
+ "_isExtractionIngestionEnabled"
+ "_isExtractionSetupSuccessful"
+ "_maErrorsDigests"
+ "_maErrorsDimensions"
+ "_maEventType"
+ "_maFailureCount"
+ "_maSuccessCount"
+ "_mobileAssetErrorsReported"
+ "_networkAccessType"
+ "_numEntitiesCleaned"
+ "_numEntitiesContainingEmoji"
+ "_numEntitiesContainingExtractions"
+ "_numEntitiesContainingSpecialCharacters"
+ "_numEntitiesExtracted"
+ "_numEntitiesExtractionAttempted"
+ "_operationFailureReason"
+ "_operationResult"
+ "_speechProfileId"
+ "_speechProfileUpdateContext"
+ "_speechProfileUpdateFailureReason"
+ "_subSystemName"
+ "_totalNumEntitiesReceived"
+ "_underLyingError"
+ "addMaErrorsDigest:"
+ "cellularAccessRequest"
+ "cellularAccessResponse"
+ "clearMaErrorsDigest"
+ "com.apple.aiml.siri.asrspeechprofile.ASRSpeechProfileClientEvent"
+ "com.apple.aiml.siri.asrspeechprofile.ASRSpeechProfileClientEvent.ASRSpeechProfileUpdateContext"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDMobileAssetErrorsReported"
+ "constrainedNetworkAccessRequest"
+ "constrainedNetworkAccessResponse"
+ "deleteCellularAccessRequest"
+ "deleteCellularAccessResponse"
+ "deleteConstrainedNetworkAccessRequest"
+ "deleteConstrainedNetworkAccessResponse"
+ "deleteEntityCleanupMetrics"
+ "deleteEntityExtractionMetrics"
+ "deleteExpensiveNetworkAccessRequest"
+ "deleteExpensiveNetworkAccessResponse"
+ "deleteIfflowError"
+ "deleteIfflowErrorCode"
+ "deleteIsCleanupIngestionEnabled"
+ "deleteIsDiscretionary"
+ "deleteIsExtractionIngestionEnabled"
+ "deleteIsExtractionSetupSuccessful"
+ "deleteIsMAAutoAsset"
+ "deleteIsUserPriority"
+ "deleteMaErrorsDigest"
+ "deleteMaErrorsDimensions"
+ "deleteMaEventType"
+ "deleteMaFailureCount"
+ "deleteMaSuccessCount"
+ "deleteMobileAssetErrorsReported"
+ "deleteNetworkAccessType"
+ "deleteNumEntitiesCleaned"
+ "deleteNumEntitiesContainingEmoji"
+ "deleteNumEntitiesContainingExtractions"
+ "deleteNumEntitiesContainingSpecialCharacters"
+ "deleteNumEntitiesExtracted"
+ "deleteNumEntitiesExtractionAttempted"
+ "deleteOperationFailureReason"
+ "deleteOperationResult"
+ "deleteSpeechProfileId"
+ "deleteSpeechProfileUpdateContext"
+ "deleteSpeechProfileUpdateFailureReason"
+ "deleteSubSystemName"
+ "deleteTotalNumEntitiesReceived"
+ "deleteUnderLyingError"
+ "entityCleanupMetrics"
+ "entityExtractionMetrics"
+ "expensiveNetworkAccessRequest"
+ "expensiveNetworkAccessResponse"
+ "hasCellularAccessRequest"
+ "hasCellularAccessResponse"
+ "hasConstrainedNetworkAccessRequest"
+ "hasConstrainedNetworkAccessResponse"
+ "hasEntityCleanupMetrics"
+ "hasEntityExtractionMetrics"
+ "hasExpensiveNetworkAccessRequest"
+ "hasExpensiveNetworkAccessResponse"
+ "hasIfflowError"
+ "hasIfflowErrorCode"
+ "hasIsCleanupIngestionEnabled"
+ "hasIsDiscretionary"
+ "hasIsExtractionIngestionEnabled"
+ "hasIsExtractionSetupSuccessful"
+ "hasIsMAAutoAsset"
+ "hasIsUserPriority"
+ "hasMaErrorsDimensions"
+ "hasMaEventType"
+ "hasMaFailureCount"
+ "hasMaSuccessCount"
+ "hasMobileAssetErrorsReported"
+ "hasNetworkAccessType"
+ "hasNumEntitiesCleaned"
+ "hasNumEntitiesContainingEmoji"
+ "hasNumEntitiesContainingExtractions"
+ "hasNumEntitiesContainingSpecialCharacters"
+ "hasNumEntitiesExtracted"
+ "hasNumEntitiesExtractionAttempted"
+ "hasOperationFailureReason"
+ "hasOperationResult"
+ "hasSpeechProfileId"
+ "hasSpeechProfileUpdateContext"
+ "hasSpeechProfileUpdateFailureReason"
+ "hasSubSystemName"
+ "hasTotalNumEntitiesReceived"
+ "hasUnderLyingError"
+ "ifflowError"
+ "ifflowErrorCode"
+ "isCleanupIngestionEnabled"
+ "isExtractionIngestionEnabled"
+ "isExtractionSetupSuccessful"
+ "maErrorsDigest"
+ "maErrorsDigestAtIndex:"
+ "maErrorsDigestCount"
+ "maErrorsDigests"
+ "maErrorsDimensions"
+ "maEventType"
+ "maFailureCount"
+ "maSuccessCount"
+ "mobileAssetErrorsReported"
+ "networkAccessType"
+ "numEntitiesCleaned"
+ "numEntitiesContainingEmoji"
+ "numEntitiesContainingExtractions"
+ "numEntitiesContainingSpecialCharacters"
+ "numEntitiesExtracted"
+ "numEntitiesExtractionAttempted"
+ "operationFailureReason"
+ "operationResult"
+ "setCellularAccessRequest:"
+ "setCellularAccessResponse:"
+ "setConstrainedNetworkAccessRequest:"
+ "setConstrainedNetworkAccessResponse:"
+ "setEntityCleanupMetrics:"
+ "setEntityExtractionMetrics:"
+ "setExpensiveNetworkAccessRequest:"
+ "setExpensiveNetworkAccessResponse:"
+ "setHasCellularAccessRequest:"
+ "setHasCellularAccessResponse:"
+ "setHasConstrainedNetworkAccessRequest:"
+ "setHasConstrainedNetworkAccessResponse:"
+ "setHasEntityCleanupMetrics:"
+ "setHasEntityExtractionMetrics:"
+ "setHasExpensiveNetworkAccessRequest:"
+ "setHasExpensiveNetworkAccessResponse:"
+ "setHasIfflowError:"
+ "setHasIfflowErrorCode:"
+ "setHasIsCleanupIngestionEnabled:"
+ "setHasIsDiscretionary:"
+ "setHasIsExtractionIngestionEnabled:"
+ "setHasIsExtractionSetupSuccessful:"
+ "setHasIsMAAutoAsset:"
+ "setHasIsUserPriority:"
+ "setHasMaErrorsDimensions:"
+ "setHasMaEventType:"
+ "setHasMaFailureCount:"
+ "setHasMaSuccessCount:"
+ "setHasMobileAssetErrorsReported:"
+ "setHasNetworkAccessType:"
+ "setHasNumEntitiesCleaned:"
+ "setHasNumEntitiesContainingEmoji:"
+ "setHasNumEntitiesContainingExtractions:"
+ "setHasNumEntitiesContainingSpecialCharacters:"
+ "setHasNumEntitiesExtracted:"
+ "setHasNumEntitiesExtractionAttempted:"
+ "setHasOperationFailureReason:"
+ "setHasOperationResult:"
+ "setHasSpeechProfileId:"
+ "setHasSpeechProfileUpdateContext:"
+ "setHasSpeechProfileUpdateFailureReason:"
+ "setHasSubSystemName:"
+ "setHasTotalNumEntitiesReceived:"
+ "setHasUnderLyingError:"
+ "setIfflowError:"
+ "setIfflowErrorCode:"
+ "setIsCleanupIngestionEnabled:"
+ "setIsDiscretionary:"
+ "setIsExtractionIngestionEnabled:"
+ "setIsExtractionSetupSuccessful:"
+ "setIsMAAutoAsset:"
+ "setIsUserPriority:"
+ "setMaErrorsDigests:"
+ "setMaErrorsDimensions:"
+ "setMaEventType:"
+ "setMaFailureCount:"
+ "setMaSuccessCount:"
+ "setMobileAssetErrorsReported:"
+ "setNetworkAccessType:"
+ "setNumEntitiesCleaned:"
+ "setNumEntitiesContainingEmoji:"
+ "setNumEntitiesContainingExtractions:"
+ "setNumEntitiesContainingSpecialCharacters:"
+ "setNumEntitiesExtracted:"
+ "setNumEntitiesExtractionAttempted:"
+ "setOperationFailureReason:"
+ "setOperationResult:"
+ "setSpeechProfileId:"
+ "setSpeechProfileUpdateContext:"
+ "setSpeechProfileUpdateFailureReason:"
+ "setSubSystemName:"
+ "setTotalNumEntitiesReceived:"
+ "setUnderLyingError:"
+ "speechProfileId"
+ "speechProfileUpdateContext"
+ "speechProfileUpdateFailureReason"
+ "subSystemName"
+ "totalNumEntitiesReceived"
+ "underLyingError"
+ "{?=\"IsMAAutoAsset\"b1\"IsDiscretionary\"b1\"IsUserPriority\"b1\"operationType\"b1}"
+ "{?=\"cellularAccessRequest\"b1\"cellularAccessResponse\"b1\"constrainedNetworkAccessRequest\"b1\"constrainedNetworkAccessResponse\"b1\"expensiveNetworkAccessRequest\"b1\"expensiveNetworkAccessResponse\"b1}"
+ "{?=\"ifflowErrorCode\"b1}"
+ "{?=\"isCleanupIngestionEnabled\"b1\"numEntitiesContainingEmoji\"b1\"numEntitiesContainingSpecialCharacters\"b1\"numEntitiesCleaned\"b1}"
+ "{?=\"isExtractionIngestionEnabled\"b1\"isExtractionSetupSuccessful\"b1\"numEntitiesExtractionAttempted\"b1\"numEntitiesContainingExtractions\"b1\"numEntitiesExtracted\"b1}"
+ "{?=\"maEventType\"b1}"
+ "{?=\"maFailureCount\"b1\"maSuccessCount\"b1}"
+ "{?=\"speechProfileUpdateFailureReason\"b1}"
+ "{?=\"totalNumEntitiesReceived\"b1}"

```
