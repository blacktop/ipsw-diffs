## SiriInstrumentation

> `/System/Library/PrivateFrameworks/SiriInstrumentation.framework/Versions/A/SiriInstrumentation`

```diff

-3400.112.1.0.0
-  __TEXT.__text: 0x8b21f0
+3400.118.2.4.1
+  __TEXT.__text: 0x8c1620
   __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0xb0230
-  __TEXT.__cstring: 0x66c5a
-  __TEXT.__const: 0xf02c
-  __TEXT.__constg_swiftt: 0x5508
-  __TEXT.__swift5_typeref: 0x15d3
-  __TEXT.__swift5_builtin: 0x3098
+  __TEXT.__objc_methlist: 0xb14c8
+  __TEXT.__cstring: 0x67ea2
+  __TEXT.__const: 0xf41c
+  __TEXT.__constg_swiftt: 0x5648
+  __TEXT.__swift5_typeref: 0x160f
+  __TEXT.__swift5_builtin: 0x3160
   __TEXT.__swift5_reflstr: 0x20b
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_proto: 0xc8c
-  __TEXT.__swift5_types: 0xa08
+  __TEXT.__swift5_proto: 0xcc4
+  __TEXT.__swift5_types: 0xa30
   __TEXT.__swift5_fieldmd: 0x3e8
   __TEXT.__oslogstring: 0x95
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x24098
+  __TEXT.__unwind_info: 0x244a8
   __TEXT.__eh_frame: 0x1aa8
-  __TEXT.__objc_classname: 0x11f41
-  __TEXT.__objc_methname: 0xf5793
-  __TEXT.__objc_methtype: 0x21d75
-  __TEXT.__objc_stubs: 0x5a080
-  __DATA_CONST.__got: 0x40d0
-  __DATA_CONST.__const: 0x2cc40
-  __DATA_CONST.__objc_classlist: 0x3fc0
+  __TEXT.__objc_classname: 0x121ca
+  __TEXT.__objc_methname: 0xf7211
+  __TEXT.__objc_methtype: 0x221ad
+  __TEXT.__objc_stubs: 0x5a8e0
+  __DATA_CONST.__got: 0x4148
+  __DATA_CONST.__const: 0x2d828
+  __DATA_CONST.__objc_classlist: 0x4038
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb88
+  __DATA_CONST.__objc_selrefs: 0x2efc0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x6230
+  __DATA_CONST.__objc_superrefs: 0x62f0
   __AUTH_CONST.__auth_got: 0x768
   __AUTH_CONST.__auth_ptr: 0x378
-  __AUTH_CONST.__const: 0x1b498
-  __AUTH_CONST.__cfstring: 0x5a280
-  __AUTH_CONST.__objc_const: 0xef258
+  __AUTH_CONST.__const: 0x1ba18
+  __AUTH_CONST.__cfstring: 0x5ae80
+  __AUTH_CONST.__objc_const: 0xf0be8
   __AUTH_CONST.__objc_intobj: 0xb10
-  __AUTH.__objc_data: 0x261d8
+  __AUTH.__objc_data: 0x26688
   __AUTH.__data: 0x338
-  __DATA.__objc_ivar: 0xbdac
-  __DATA.__data: 0x1e18
-  __DATA.__bss: 0x14e00
+  __DATA.__objc_ivar: 0xbee4
+  __DATA.__data: 0x1e68
+  __DATA.__bss: 0x15300
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x1e00
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 64396
-  Symbols:   100391
-  CStrings:  12397
+  Functions: 64842
+  Symbols:   101057
+  CStrings:  12504
 
Symbols:
+ -[FLOWSchemaFLOWAppContext deleteProtectedAppType]
+ -[FLOWSchemaFLOWAppContext hasProtectedAppType]
+ -[FLOWSchemaFLOWAppContext protectedAppType]
+ -[FLOWSchemaFLOWAppContext setHasProtectedAppType:]
+ -[FLOWSchemaFLOWAppContext setProtectedAppType:]
+ -[FLOWSchemaFLOWClientEvent deleteLocationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent hasLocationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent locationAccessPermissionPromptContext]
+ -[FLOWSchemaFLOWClientEvent setHasLocationAccessPermissionPromptContext:]
+ -[FLOWSchemaFLOWClientEvent setLocationAccessPermissionPromptContext:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext .cxx_destruct]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteEnded]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteFailed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext deleteStartedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext ended]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext failed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasEnded]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasFailed]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hasStartedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setEnded:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setFailed:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasEnded:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasFailed:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setHasStartedOrChanged:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext setStartedOrChanged:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext startedOrChanged]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext whichContextevent]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded deleteIsPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded deletePermissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hasIsPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hasPermissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded isPreciseLocationResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded permissionStatusResult]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setHasIsPreciseLocationResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setHasPermissionStatusResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setIsPreciseLocationResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded setPermissionStatusResult:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptEnded(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed deleteFailureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed failureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed hasFailureReason]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed setFailureReason:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed setHasFailureReason:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptFailed(SensitiveConditions) suppressMessageUnderConditions]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted deleteExists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted dictionaryRepresentation]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted exists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted hasExists]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted hash]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted initWithDictionary:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted initWithJSON:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted isEqual:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted jsonData]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted readFrom:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted setExists:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted setHasExists:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted writeTo:]
+ -[FLOWSchemaFLOWLocationAccessPermissionPromptStarted(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaHeuristicsHandleEndedData .cxx_destruct]
+ -[NLRouterSchemaHeuristicsHandleEndedData deleteLinkId]
+ -[NLRouterSchemaHeuristicsHandleEndedData dictionaryRepresentation]
+ -[NLRouterSchemaHeuristicsHandleEndedData hasLinkId]
+ -[NLRouterSchemaHeuristicsHandleEndedData hash]
+ -[NLRouterSchemaHeuristicsHandleEndedData initWithDictionary:]
+ -[NLRouterSchemaHeuristicsHandleEndedData initWithJSON:]
+ -[NLRouterSchemaHeuristicsHandleEndedData isEqual:]
+ -[NLRouterSchemaHeuristicsHandleEndedData jsonData]
+ -[NLRouterSchemaHeuristicsHandleEndedData linkId]
+ -[NLRouterSchemaHeuristicsHandleEndedData readFrom:]
+ -[NLRouterSchemaHeuristicsHandleEndedData setHasLinkId:]
+ -[NLRouterSchemaHeuristicsHandleEndedData setLinkId:]
+ -[NLRouterSchemaHeuristicsHandleEndedData writeTo:]
+ -[NLRouterSchemaHeuristicsHandleEndedData(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaHeuristicsHandleEndedData(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaNLRouterClientEvent deleteNlRouterSubComponentTriggeredHeuristicRuleTier1]
+ -[NLRouterSchemaNLRouterClientEvent hasNlRouterSubComponentTriggeredHeuristicRuleTier1]
+ -[NLRouterSchemaNLRouterClientEvent nlRouterSubComponentTriggeredHeuristicRuleTier1]
+ -[NLRouterSchemaNLRouterClientEvent setHasNlRouterSubComponentTriggeredHeuristicRuleTier1:]
+ -[NLRouterSchemaNLRouterClientEvent setNlRouterSubComponentTriggeredHeuristicRuleTier1:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded .cxx_destruct]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded deleteNlRouterSubComponentHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded hasNlRouterSubComponentHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded nlRouterSubComponentHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded setHasNlRouterSubComponentHandleEndedData:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded setNlRouterSubComponentHandleEndedData:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEnded(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData .cxx_destruct]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData deleteHeuristicsHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData hasHeuristicsHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData hash]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData heuristicsHandleEndedData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData initWithDictionary:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData initWithJSON:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData isEqual:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData jsonData]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData readFrom:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData setHasHeuristicsHandleEndedData:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData setHeuristicsHandleEndedData:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData writeTo:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterSubComponentHandleEndedData(SensitiveConditions) suppressMessageUnderConditions]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 .cxx_destruct]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 deleteLinkId]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 deleteTriggeredHeuristicRule]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 dictionaryRepresentation]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 hasLinkId]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 hasTriggeredHeuristicRule]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 hash]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 initWithDictionary:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 initWithJSON:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 isEqual:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 jsonData]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 linkId]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 readFrom:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 setHasLinkId:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 setHasTriggeredHeuristicRule:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 setLinkId:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 setTriggeredHeuristicRule:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 triggeredHeuristicRule]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1 writeTo:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDAssistantProperties deleteLocationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties hasLocationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties locationAccessPermission]
+ -[ODDSiriSchemaODDAssistantProperties setHasLocationAccessPermission:]
+ -[ODDSiriSchemaODDAssistantProperties setLocationAccessPermission:]
+ -[ODDSiriSchemaODDExecutionMetadataReported deleteExecutionStatus]
+ -[ODDSiriSchemaODDExecutionMetadataReported deleteExtensionName]
+ -[ODDSiriSchemaODDExecutionMetadataReported dictionaryRepresentation]
+ -[ODDSiriSchemaODDExecutionMetadataReported executionStatus]
+ -[ODDSiriSchemaODDExecutionMetadataReported extensionName]
+ -[ODDSiriSchemaODDExecutionMetadataReported hasExecutionStatus]
+ -[ODDSiriSchemaODDExecutionMetadataReported hasExtensionName]
+ -[ODDSiriSchemaODDExecutionMetadataReported hash]
+ -[ODDSiriSchemaODDExecutionMetadataReported initWithDictionary:]
+ -[ODDSiriSchemaODDExecutionMetadataReported initWithJSON:]
+ -[ODDSiriSchemaODDExecutionMetadataReported isEqual:]
+ -[ODDSiriSchemaODDExecutionMetadataReported jsonData]
+ -[ODDSiriSchemaODDExecutionMetadataReported readFrom:]
+ -[ODDSiriSchemaODDExecutionMetadataReported setExecutionStatus:]
+ -[ODDSiriSchemaODDExecutionMetadataReported setExtensionName:]
+ -[ODDSiriSchemaODDExecutionMetadataReported setHasExecutionStatus:]
+ -[ODDSiriSchemaODDExecutionMetadataReported setHasExtensionName:]
+ -[ODDSiriSchemaODDExecutionMetadataReported writeTo:]
+ -[ODDSiriSchemaODDExecutionMetadataReported(SensitiveConditions) suppressMessageUnderConditions]
+ -[ODDSiriSchemaODDSiriClientEvent deleteExecutionMetadataReported]
+ -[ODDSiriSchemaODDSiriClientEvent executionMetadataReported]
+ -[ODDSiriSchemaODDSiriClientEvent hasExecutionMetadataReported]
+ -[ODDSiriSchemaODDSiriClientEvent setExecutionMetadataReported:]
+ -[ODDSiriSchemaODDSiriClientEvent setHasExecutionMetadataReported:]
+ -[ORCHSchemaORCHClientEvent deleteUnsupportedLanguageDetected]
+ -[ORCHSchemaORCHClientEvent hasUnsupportedLanguageDetected]
+ -[ORCHSchemaORCHClientEvent setHasUnsupportedLanguageDetected:]
+ -[ORCHSchemaORCHClientEvent setUnsupportedLanguageDetected:]
+ -[ORCHSchemaORCHClientEvent unsupportedLanguageDetected]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected deleteLanguageDetected]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected dictionaryRepresentation]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected hasLanguageDetected]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected hash]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected initWithDictionary:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected initWithJSON:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected isEqual:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected jsonData]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected languageDetected]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected readFrom:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected setHasLanguageDetected:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected setLanguageDetected:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected writeTo:]
+ -[ORCHSchemaORCHUnsupportedLanguageDetected(SensitiveConditions) suppressMessageUnderConditions]
+ -[SISchemaEnabledStatus deleteLocationAccessPermission]
+ -[SISchemaEnabledStatus hasLocationAccessPermission]
+ -[SISchemaEnabledStatus locationAccessPermission]
+ -[SISchemaEnabledStatus setHasLocationAccessPermission:]
+ -[SISchemaEnabledStatus setLocationAccessPermission:]
+ -[SUGSchemaSUGAutoCompleteQuery deleteNumCharactersInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery deleteNumWordsInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery dictionaryRepresentation]
+ -[SUGSchemaSUGAutoCompleteQuery hasNumCharactersInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery hasNumWordsInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery hash]
+ -[SUGSchemaSUGAutoCompleteQuery initWithDictionary:]
+ -[SUGSchemaSUGAutoCompleteQuery initWithJSON:]
+ -[SUGSchemaSUGAutoCompleteQuery isEqual:]
+ -[SUGSchemaSUGAutoCompleteQuery jsonData]
+ -[SUGSchemaSUGAutoCompleteQuery numCharactersInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery numWordsInQuery]
+ -[SUGSchemaSUGAutoCompleteQuery readFrom:]
+ -[SUGSchemaSUGAutoCompleteQuery setHasNumCharactersInQuery:]
+ -[SUGSchemaSUGAutoCompleteQuery setHasNumWordsInQuery:]
+ -[SUGSchemaSUGAutoCompleteQuery setNumCharactersInQuery:]
+ -[SUGSchemaSUGAutoCompleteQuery setNumWordsInQuery:]
+ -[SUGSchemaSUGAutoCompleteQuery writeTo:]
+ -[SUGSchemaSUGAutoCompleteQuery(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData autoCompleteSuggestionSource]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData deleteAutoCompleteSuggestionSource]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData dictionaryRepresentation]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData hasAutoCompleteSuggestionSource]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData hash]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData initWithDictionary:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData initWithJSON:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData isEqual:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData jsonData]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData readFrom:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData setAutoCompleteSuggestionSource:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData setHasAutoCompleteSuggestionSource:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData writeTo:]
+ -[SUGSchemaSUGAutoCompleteSuggestionMetaData(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGClientEvent deleteSugGeneratedTier1]
+ -[SUGSchemaSUGClientEvent deleteTypingWindowEnded]
+ -[SUGSchemaSUGClientEvent deleteUiActivityTier1]
+ -[SUGSchemaSUGClientEvent hasSugGeneratedTier1]
+ -[SUGSchemaSUGClientEvent hasTypingWindowEnded]
+ -[SUGSchemaSUGClientEvent hasUiActivityTier1]
+ -[SUGSchemaSUGClientEvent setHasSugGeneratedTier1:]
+ -[SUGSchemaSUGClientEvent setHasTypingWindowEnded:]
+ -[SUGSchemaSUGClientEvent setHasUiActivityTier1:]
+ -[SUGSchemaSUGClientEvent setSugGeneratedTier1:]
+ -[SUGSchemaSUGClientEvent setTypingWindowEnded:]
+ -[SUGSchemaSUGClientEvent setUiActivityTier1:]
+ -[SUGSchemaSUGClientEvent sugGeneratedTier1]
+ -[SUGSchemaSUGClientEvent typingWindowEnded]
+ -[SUGSchemaSUGClientEvent uiActivityTier1]
+ -[SUGSchemaSUGEngagementMetricReported conversionMetricType]
+ -[SUGSchemaSUGEngagementMetricReported deleteConversionMetricType]
+ -[SUGSchemaSUGEngagementMetricReported hasConversionMetricType]
+ -[SUGSchemaSUGEngagementMetricReported setConversionMetricType:]
+ -[SUGSchemaSUGEngagementMetricReported setHasConversionMetricType:]
+ -[SUGSchemaSUGSuggestion autoCompleteSuggestionMetaData]
+ -[SUGSchemaSUGSuggestion deleteAutoCompleteSuggestionMetaData]
+ -[SUGSchemaSUGSuggestion deleteLinkId]
+ -[SUGSchemaSUGSuggestion deleteNumCharactersInSuggestion]
+ -[SUGSchemaSUGSuggestion deleteNumWordsInSuggestion]
+ -[SUGSchemaSUGSuggestion deleteSmartSuppressionScore]
+ -[SUGSchemaSUGSuggestion hasAutoCompleteSuggestionMetaData]
+ -[SUGSchemaSUGSuggestion hasLinkId]
+ -[SUGSchemaSUGSuggestion hasNumCharactersInSuggestion]
+ -[SUGSchemaSUGSuggestion hasNumWordsInSuggestion]
+ -[SUGSchemaSUGSuggestion hasSmartSuppressionScore]
+ -[SUGSchemaSUGSuggestion linkId]
+ -[SUGSchemaSUGSuggestion numCharactersInSuggestion]
+ -[SUGSchemaSUGSuggestion numWordsInSuggestion]
+ -[SUGSchemaSUGSuggestion setAutoCompleteSuggestionMetaData:]
+ -[SUGSchemaSUGSuggestion setHasAutoCompleteSuggestionMetaData:]
+ -[SUGSchemaSUGSuggestion setHasLinkId:]
+ -[SUGSchemaSUGSuggestion setHasNumCharactersInSuggestion:]
+ -[SUGSchemaSUGSuggestion setHasNumWordsInSuggestion:]
+ -[SUGSchemaSUGSuggestion setHasSmartSuppressionScore:]
+ -[SUGSchemaSUGSuggestion setLinkId:]
+ -[SUGSchemaSUGSuggestion setNumCharactersInSuggestion:]
+ -[SUGSchemaSUGSuggestion setNumWordsInSuggestion:]
+ -[SUGSchemaSUGSuggestion setSmartSuppressionScore:]
+ -[SUGSchemaSUGSuggestion smartSuppressionScore]
+ -[SUGSchemaSUGSuggestionTier1 .cxx_destruct]
+ -[SUGSchemaSUGSuggestionTier1 deleteLinkId]
+ -[SUGSchemaSUGSuggestionTier1 deleteSuggestionId]
+ -[SUGSchemaSUGSuggestionTier1 dictionaryRepresentation]
+ -[SUGSchemaSUGSuggestionTier1 hasLinkId]
+ -[SUGSchemaSUGSuggestionTier1 hasSuggestionId]
+ -[SUGSchemaSUGSuggestionTier1 hash]
+ -[SUGSchemaSUGSuggestionTier1 initWithDictionary:]
+ -[SUGSchemaSUGSuggestionTier1 initWithJSON:]
+ -[SUGSchemaSUGSuggestionTier1 isEqual:]
+ -[SUGSchemaSUGSuggestionTier1 jsonData]
+ -[SUGSchemaSUGSuggestionTier1 linkId]
+ -[SUGSchemaSUGSuggestionTier1 readFrom:]
+ -[SUGSchemaSUGSuggestionTier1 setHasLinkId:]
+ -[SUGSchemaSUGSuggestionTier1 setHasSuggestionId:]
+ -[SUGSchemaSUGSuggestionTier1 setLinkId:]
+ -[SUGSchemaSUGSuggestionTier1 setSuggestionId:]
+ -[SUGSchemaSUGSuggestionTier1 suggestionId]
+ -[SUGSchemaSUGSuggestionTier1 writeTo:]
+ -[SUGSchemaSUGSuggestionTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SUGSchemaSUGSuggestionTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGSuggestionsGenerated autoCompleteQuery]
+ -[SUGSchemaSUGSuggestionsGenerated deleteAutoCompleteQuery]
+ -[SUGSchemaSUGSuggestionsGenerated deleteLinkId]
+ -[SUGSchemaSUGSuggestionsGenerated hasAutoCompleteQuery]
+ -[SUGSchemaSUGSuggestionsGenerated hasLinkId]
+ -[SUGSchemaSUGSuggestionsGenerated linkId]
+ -[SUGSchemaSUGSuggestionsGenerated setAutoCompleteQuery:]
+ -[SUGSchemaSUGSuggestionsGenerated setHasAutoCompleteQuery:]
+ -[SUGSchemaSUGSuggestionsGenerated setHasLinkId:]
+ -[SUGSchemaSUGSuggestionsGenerated setLinkId:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 .cxx_destruct]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 addSuggestions:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 clearSuggestions]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 deleteLinkId]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 deleteSuggestions]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 dictionaryRepresentation]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 hasLinkId]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 hash]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 initWithDictionary:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 initWithJSON:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 isEqual:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 jsonData]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 linkId]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 readFrom:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 setHasLinkId:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 setLinkId:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 setSuggestions:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 suggestionsAtIndex:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 suggestionsCount]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 suggestions]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1 writeTo:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SUGSchemaSUGSuggestionsGeneratedTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGSuggestionsUIActivity addSuggestions:]
+ -[SUGSchemaSUGSuggestionsUIActivity clearSuggestions]
+ -[SUGSchemaSUGSuggestionsUIActivity deleteLinkId]
+ -[SUGSchemaSUGSuggestionsUIActivity deleteSuggestions]
+ -[SUGSchemaSUGSuggestionsUIActivity hasLinkId]
+ -[SUGSchemaSUGSuggestionsUIActivity linkId]
+ -[SUGSchemaSUGSuggestionsUIActivity setHasLinkId:]
+ -[SUGSchemaSUGSuggestionsUIActivity setLinkId:]
+ -[SUGSchemaSUGSuggestionsUIActivity setSuggestions:]
+ -[SUGSchemaSUGSuggestionsUIActivity suggestionsAtIndex:]
+ -[SUGSchemaSUGSuggestionsUIActivity suggestionsCount]
+ -[SUGSchemaSUGSuggestionsUIActivity suggestions]
+ -[SUGSchemaSUGSuggestionsUIActivity(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 .cxx_destruct]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 addSuggestions:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 clearSuggestions]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 deleteLinkId]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 deleteSuggestions]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 dictionaryRepresentation]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 hasLinkId]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 hash]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 initWithDictionary:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 initWithJSON:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 isEqual:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 jsonData]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 linkId]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 readFrom:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 setHasLinkId:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 setLinkId:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 setSuggestions:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 suggestionsAtIndex:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 suggestionsCount]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 suggestions]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1 writeTo:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1(SensitiveConditions) applySensitiveConditionsPolicy:]
+ -[SUGSchemaSUGSuggestionsUIActivityTier1(SensitiveConditions) suppressMessageUnderConditions]
+ -[SUGSchemaSUGTypingWindowEnded deleteTypingWindowEndReason]
+ -[SUGSchemaSUGTypingWindowEnded dictionaryRepresentation]
+ -[SUGSchemaSUGTypingWindowEnded hasTypingWindowEndReason]
+ -[SUGSchemaSUGTypingWindowEnded hash]
+ -[SUGSchemaSUGTypingWindowEnded initWithDictionary:]
+ -[SUGSchemaSUGTypingWindowEnded initWithJSON:]
+ -[SUGSchemaSUGTypingWindowEnded isEqual:]
+ -[SUGSchemaSUGTypingWindowEnded jsonData]
+ -[SUGSchemaSUGTypingWindowEnded readFrom:]
+ -[SUGSchemaSUGTypingWindowEnded setHasTypingWindowEndReason:]
+ -[SUGSchemaSUGTypingWindowEnded setTypingWindowEndReason:]
+ -[SUGSchemaSUGTypingWindowEnded typingWindowEndReason]
+ -[SUGSchemaSUGTypingWindowEnded writeTo:]
+ -[SUGSchemaSUGTypingWindowEnded(SensitiveConditions) suppressMessageUnderConditions]
+ OBJC_IVAR_$_FLOWSchemaFLOWAppContext._protectedAppType
+ OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._hasLocationAccessPermissionPromptContext
+ OBJC_IVAR_$_FLOWSchemaFLOWClientEvent._locationAccessPermissionPromptContext
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._ended
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._failed
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasEnded
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasFailed
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._hasStartedOrChanged
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._startedOrChanged
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext._whichContextevent
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._has
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._isPreciseLocationResult
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded._permissionStatusResult
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed._failureReason
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed._has
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted._exists
+ OBJC_IVAR_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted._has
+ OBJC_IVAR_$_NLRouterSchemaHeuristicsHandleEndedData._hasLinkId
+ OBJC_IVAR_$_NLRouterSchemaHeuristicsHandleEndedData._linkId
+ OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._hasNlRouterSubComponentTriggeredHeuristicRuleTier1
+ OBJC_IVAR_$_NLRouterSchemaNLRouterClientEvent._nlRouterSubComponentTriggeredHeuristicRuleTier1
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentHandleEnded._hasNlRouterSubComponentHandleEndedData
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentHandleEnded._nlRouterSubComponentHandleEndedData
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentHandleEndedData._hasHeuristicsHandleEndedData
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentHandleEndedData._heuristicsHandleEndedData
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1._hasLinkId
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1._hasTriggeredHeuristicRule
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1._linkId
+ OBJC_IVAR_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1._triggeredHeuristicRule
+ OBJC_IVAR_$_ODDSiriSchemaODDAssistantProperties._locationAccessPermission
+ OBJC_IVAR_$_ODDSiriSchemaODDExecutionMetadataReported._executionStatus
+ OBJC_IVAR_$_ODDSiriSchemaODDExecutionMetadataReported._extensionName
+ OBJC_IVAR_$_ODDSiriSchemaODDExecutionMetadataReported._has
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._executionMetadataReported
+ OBJC_IVAR_$_ODDSiriSchemaODDSiriClientEvent._hasExecutionMetadataReported
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._hasUnsupportedLanguageDetected
+ OBJC_IVAR_$_ORCHSchemaORCHClientEvent._unsupportedLanguageDetected
+ OBJC_IVAR_$_ORCHSchemaORCHUnsupportedLanguageDetected._has
+ OBJC_IVAR_$_ORCHSchemaORCHUnsupportedLanguageDetected._languageDetected
+ OBJC_IVAR_$_SISchemaEnabledStatus._locationAccessPermission
+ OBJC_IVAR_$_SUGSchemaSUGAutoCompleteQuery._has
+ OBJC_IVAR_$_SUGSchemaSUGAutoCompleteQuery._numCharactersInQuery
+ OBJC_IVAR_$_SUGSchemaSUGAutoCompleteQuery._numWordsInQuery
+ OBJC_IVAR_$_SUGSchemaSUGAutoCompleteSuggestionMetaData._autoCompleteSuggestionSource
+ OBJC_IVAR_$_SUGSchemaSUGAutoCompleteSuggestionMetaData._has
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._hasSugGeneratedTier1
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._hasTypingWindowEnded
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._hasUiActivityTier1
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._sugGeneratedTier1
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._typingWindowEnded
+ OBJC_IVAR_$_SUGSchemaSUGClientEvent._uiActivityTier1
+ OBJC_IVAR_$_SUGSchemaSUGEngagementMetricReported._conversionMetricType
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._autoCompleteSuggestionMetaData
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._hasAutoCompleteSuggestionMetaData
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._numCharactersInSuggestion
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._numWordsInSuggestion
+ OBJC_IVAR_$_SUGSchemaSUGSuggestion._smartSuppressionScore
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionTier1._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionTier1._hasSuggestionId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionTier1._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionTier1._suggestionId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGenerated._autoCompleteQuery
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGenerated._hasAutoCompleteQuery
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGenerated._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGenerated._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGeneratedTier1._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGeneratedTier1._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsGeneratedTier1._suggestions
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivity._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivity._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivity._suggestions
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivityTier1._hasLinkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivityTier1._linkId
+ OBJC_IVAR_$_SUGSchemaSUGSuggestionsUIActivityTier1._suggestions
+ OBJC_IVAR_$_SUGSchemaSUGTypingWindowEnded._has
+ OBJC_IVAR_$_SUGSchemaSUGTypingWindowEnded._typingWindowEndReason
+ _FLOWSchemaFLOWLocationAccessPermissionPromptContextReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptEndedReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptFailedReadFrom
+ _FLOWSchemaFLOWLocationAccessPermissionPromptStartedReadFrom
+ _NLRouterSchemaHeuristicsHandleEndedDataReadFrom
+ _NLRouterSchemaNLRouterSubComponentHandleEndedDataReadFrom
+ _NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1ReadFrom
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ _OBJC_CLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ _OBJC_CLASS_$_NLRouterSchemaHeuristicsHandleEndedData
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ _OBJC_CLASS_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ _OBJC_CLASS_$_ODDSiriSchemaODDExecutionMetadataReported
+ _OBJC_CLASS_$_ORCHSchemaORCHUnsupportedLanguageDetected
+ _OBJC_CLASS_$_SUGSchemaSUGAutoCompleteQuery
+ _OBJC_CLASS_$_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionTier1
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionsGeneratedTier1
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionsUIActivityTier1
+ _OBJC_CLASS_$_SUGSchemaSUGTypingWindowEnded
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ _OBJC_METACLASS_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ _OBJC_METACLASS_$_NLRouterSchemaHeuristicsHandleEndedData
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ _OBJC_METACLASS_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ _OBJC_METACLASS_$_ODDSiriSchemaODDExecutionMetadataReported
+ _OBJC_METACLASS_$_ORCHSchemaORCHUnsupportedLanguageDetected
+ _OBJC_METACLASS_$_SUGSchemaSUGAutoCompleteQuery
+ _OBJC_METACLASS_$_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ _OBJC_METACLASS_$_SUGSchemaSUGSuggestionTier1
+ _OBJC_METACLASS_$_SUGSchemaSUGSuggestionsGeneratedTier1
+ _OBJC_METACLASS_$_SUGSchemaSUGSuggestionsUIActivityTier1
+ _OBJC_METACLASS_$_SUGSchemaSUGTypingWindowEnded
+ _ODDSiriSchemaODDExecutionMetadataReportedReadFrom
+ _ORCHSchemaORCHUnsupportedLanguageDetectedReadFrom
+ _SUGSchemaSUGAutoCompleteQueryReadFrom
+ _SUGSchemaSUGAutoCompleteSuggestionMetaDataReadFrom
+ _SUGSchemaSUGSuggestionTier1ReadFrom
+ _SUGSchemaSUGSuggestionsGeneratedTier1ReadFrom
+ _SUGSchemaSUGSuggestionsUIActivityTier1ReadFrom
+ _SUGSchemaSUGTypingWindowEndedReadFrom
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptContext(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptFailed(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_FLOWSchemaFLOWLocationAccessPermissionPromptStarted(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaHeuristicsHandleEndedData(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterSubComponentHandleEndedData(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ODDSiriSchemaODDExecutionMetadataReported(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_ORCHSchemaORCHUnsupportedLanguageDetected(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGAutoCompleteQuery(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGAutoCompleteSuggestionMetaData(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGSuggestionTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGSuggestionsGeneratedTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGSuggestionsUIActivityTier1(SensitiveConditions)
+ __OBJC_$_INSTANCE_METHODS_SUGSchemaSUGTypingWindowEnded(SensitiveConditions)
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_$_INSTANCE_VARIABLES_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaHeuristicsHandleEndedData
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ __OBJC_$_INSTANCE_VARIABLES_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ __OBJC_$_INSTANCE_VARIABLES_ODDSiriSchemaODDExecutionMetadataReported
+ __OBJC_$_INSTANCE_VARIABLES_ORCHSchemaORCHUnsupportedLanguageDetected
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGAutoCompleteQuery
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGSuggestionTier1
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGSuggestionsGeneratedTier1
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGSuggestionsUIActivityTier1
+ __OBJC_$_INSTANCE_VARIABLES_SUGSchemaSUGTypingWindowEnded
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_$_PROP_LIST_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_$_PROP_LIST_NLRouterSchemaHeuristicsHandleEndedData
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ __OBJC_$_PROP_LIST_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ __OBJC_$_PROP_LIST_ODDSiriSchemaODDExecutionMetadataReported
+ __OBJC_$_PROP_LIST_ORCHSchemaORCHUnsupportedLanguageDetected
+ __OBJC_$_PROP_LIST_SUGSchemaSUGAutoCompleteQuery
+ __OBJC_$_PROP_LIST_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ __OBJC_$_PROP_LIST_SUGSchemaSUGSuggestionTier1
+ __OBJC_$_PROP_LIST_SUGSchemaSUGSuggestionsGeneratedTier1
+ __OBJC_$_PROP_LIST_SUGSchemaSUGSuggestionsUIActivityTier1
+ __OBJC_$_PROP_LIST_SUGSchemaSUGTypingWindowEnded
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_CLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_CLASS_RO_$_NLRouterSchemaHeuristicsHandleEndedData
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ __OBJC_CLASS_RO_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ __OBJC_CLASS_RO_$_ODDSiriSchemaODDExecutionMetadataReported
+ __OBJC_CLASS_RO_$_ORCHSchemaORCHUnsupportedLanguageDetected
+ __OBJC_CLASS_RO_$_SUGSchemaSUGAutoCompleteQuery
+ __OBJC_CLASS_RO_$_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ __OBJC_CLASS_RO_$_SUGSchemaSUGSuggestionTier1
+ __OBJC_CLASS_RO_$_SUGSchemaSUGSuggestionsGeneratedTier1
+ __OBJC_CLASS_RO_$_SUGSchemaSUGSuggestionsUIActivityTier1
+ __OBJC_CLASS_RO_$_SUGSchemaSUGTypingWindowEnded
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptContext
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptEnded
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptFailed
+ __OBJC_METACLASS_RO_$_FLOWSchemaFLOWLocationAccessPermissionPromptStarted
+ __OBJC_METACLASS_RO_$_NLRouterSchemaHeuristicsHandleEndedData
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterSubComponentHandleEndedData
+ __OBJC_METACLASS_RO_$_NLRouterSchemaNLRouterSubComponentTriggeredHeuristicRuleTier1
+ __OBJC_METACLASS_RO_$_ODDSiriSchemaODDExecutionMetadataReported
+ __OBJC_METACLASS_RO_$_ORCHSchemaORCHUnsupportedLanguageDetected
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGAutoCompleteQuery
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGSuggestionTier1
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGSuggestionsGeneratedTier1
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGSuggestionsUIActivityTier1
+ __OBJC_METACLASS_RO_$_SUGSchemaSUGTypingWindowEnded
+ _objc_msgSend$autoCompleteQuery
+ _objc_msgSend$autoCompleteSuggestionMetaData
+ _objc_msgSend$autoCompleteSuggestionSource
+ _objc_msgSend$conversionMetricType
+ _objc_msgSend$deleteAutoCompleteQuery
+ _objc_msgSend$deleteAutoCompleteSuggestionMetaData
+ _objc_msgSend$deleteExecutionMetadataReported
+ _objc_msgSend$deleteHeuristicsHandleEndedData
+ _objc_msgSend$deleteLocationAccessPermissionPromptContext
+ _objc_msgSend$deleteNlRouterSubComponentHandleEndedData
+ _objc_msgSend$deleteNlRouterSubComponentTriggeredHeuristicRuleTier1
+ _objc_msgSend$deleteSugGeneratedTier1
+ _objc_msgSend$deleteSuggestions
+ _objc_msgSend$deleteTriggeredHeuristicRule
+ _objc_msgSend$deleteTypingWindowEnded
+ _objc_msgSend$deleteUiActivityTier1
+ _objc_msgSend$deleteUnsupportedLanguageDetected
+ _objc_msgSend$executionMetadataReported
+ _objc_msgSend$executionStatus
+ _objc_msgSend$extensionName
+ _objc_msgSend$heuristicsHandleEndedData
+ _objc_msgSend$isPreciseLocationResult
+ _objc_msgSend$languageDetected
+ _objc_msgSend$locationAccessPermission
+ _objc_msgSend$locationAccessPermissionPromptContext
+ _objc_msgSend$nlRouterSubComponentHandleEndedData
+ _objc_msgSend$nlRouterSubComponentTriggeredHeuristicRuleTier1
+ _objc_msgSend$numCharactersInQuery
+ _objc_msgSend$numCharactersInSuggestion
+ _objc_msgSend$numWordsInQuery
+ _objc_msgSend$numWordsInSuggestion
+ _objc_msgSend$permissionStatusResult
+ _objc_msgSend$protectedAppType
+ _objc_msgSend$setAutoCompleteQuery:
+ _objc_msgSend$setAutoCompleteSuggestionMetaData:
+ _objc_msgSend$setAutoCompleteSuggestionSource:
+ _objc_msgSend$setConversionMetricType:
+ _objc_msgSend$setExecutionMetadataReported:
+ _objc_msgSend$setExecutionStatus:
+ _objc_msgSend$setExtensionName:
+ _objc_msgSend$setHeuristicsHandleEndedData:
+ _objc_msgSend$setIsPreciseLocationResult:
+ _objc_msgSend$setLanguageDetected:
+ _objc_msgSend$setLocationAccessPermission:
+ _objc_msgSend$setLocationAccessPermissionPromptContext:
+ _objc_msgSend$setNlRouterSubComponentHandleEndedData:
+ _objc_msgSend$setNlRouterSubComponentTriggeredHeuristicRuleTier1:
+ _objc_msgSend$setNumCharactersInQuery:
+ _objc_msgSend$setNumCharactersInSuggestion:
+ _objc_msgSend$setNumWordsInQuery:
+ _objc_msgSend$setNumWordsInSuggestion:
+ _objc_msgSend$setPermissionStatusResult:
+ _objc_msgSend$setProtectedAppType:
+ _objc_msgSend$setSmartSuppressionScore:
+ _objc_msgSend$setSugGeneratedTier1:
+ _objc_msgSend$setTriggeredHeuristicRule:
+ _objc_msgSend$setTypingWindowEndReason:
+ _objc_msgSend$setTypingWindowEnded:
+ _objc_msgSend$setUiActivityTier1:
+ _objc_msgSend$setUnsupportedLanguageDetected:
+ _objc_msgSend$smartSuppressionScore
+ _objc_msgSend$sugGeneratedTier1
+ _objc_msgSend$triggeredHeuristicRule
+ _objc_msgSend$typingWindowEndReason
+ _objc_msgSend$typingWindowEnded
+ _objc_msgSend$uiActivityTier1
+ _objc_msgSend$unsupportedLanguageDetected
+ _qname_FLOWSchemaFLOWClientEvent_WhichEvent_Type_locationAccessPermissionPromptContext
+ _qname_NLRouterSchemaNLRouterClientEvent_WhichEvent_Type_nlRouterSubComponentTriggeredHeuristicRuleTier1
+ _qname_ODDSiriSchemaODDSiriClientEvent_WhichEvent_Type_executionMetadataReported
+ _qname_ORCHSchemaORCHClientEvent_WhichEvent_Type_unsupportedLanguageDetected
+ _qname_SUGSchemaSUGClientEvent_WhichEvent_Type_sugGeneratedTier1
+ _qname_SUGSchemaSUGClientEvent_WhichEvent_Type_typingWindowEnded
+ _qname_SUGSchemaSUGClientEvent_WhichEvent_Type_uiActivityTier1
+ _symbolic _____ So29ODDSiriSchemaODDExtensionNameV
+ _symbolic _____ So30FLOWSchemaFLOWProtectedAppTypeV
+ _symbolic _____ So31ODDSiriSchemaODDExecutionStatusV
+ _symbolic _____ So32SISchemaLocationAccessPermissionV
+ _symbolic _____ So32SUGSchemaSUGConversionMetricTypeV
+ _symbolic _____ So33SUGSchemaSUGTypingWindowEndReasonV
+ _symbolic _____ So40ODDSiriSchemaODDLocationAccessPermissionV
+ _symbolic _____ So40SUGSchemaSUGAutoCompleteSuggestionSourceV
+ _symbolic _____ So50FLOWSchemaFLOWLocationAccessPermissionStatusResultV
+ _symbolic _____ So51FLOWSchemaFLOWLocationAccessPermissionFailureReasonV
CStrings:
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_DISABLED_LOCATION_SERVICE"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_INSUFFICIENT_PRECISION"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_LOCKED_DEVICE"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_TIMEOUT"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_UNKNOWN"
+ "FLOWLOCATIONACCESSPERMISSIONFAILUREREASON_UNSUPPORTED_RESPONSE"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_ALLOW_ONCE"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_ALLOW_WHILE_USING_SIRI"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_NEVER"
+ "FLOWLOCATIONACCESSPERMISSIONSTATUSRESULT_UNKNOWN"
+ "FLOWPROTECTEDAPPTYPE_HIDDEN"
+ "FLOWPROTECTEDAPPTYPE_LOCKED"
+ "FLOWPROTECTEDAPPTYPE_NOT_RELATED"
+ "FLOWPROTECTEDAPPTYPE_UNKNOWN"
+ "FLOWSTATETYPE_AUTHENTICATION_PROTECTED_APP_FAILED"
+ "FLOWSTATETYPE_HIDDEN_PROTECTED_APP"
+ "INFERENCEAPPSELECTIONUSERPERSONA_ZERO_COUNTS"
+ "LOCATIONACCESSPERMISSION_ALLOW_ALWAYS"
+ "LOCATIONACCESSPERMISSION_ALLOW_WHILE_USING_SIRI"
+ "LOCATIONACCESSPERMISSION_ASK_NEXT_TIME"
+ "LOCATIONACCESSPERMISSION_DENIED"
+ "LOCATIONACCESSPERMISSION_LOCATION_SERVICES_OFF"
+ "LOCATIONACCESSPERMISSION_RESTRICTED"
+ "LOCATIONACCESSPERMISSION_UNKNOWN"
+ "ODDEXECUTIONSTATUS_COMPLETED"
+ "ODDEXECUTIONSTATUS_UNKNOWN"
+ "ODDEXTENSIONNAME_DEVICE_PROPERTIES_EXTENSION"
+ "ODDEXTENSIONNAME_EXPERIMENTATION_EXTENSION"
+ "ODDEXTENSIONNAME_METRICS_EXTENSION"
+ "ODDEXTENSIONNAME_UNKNOWN"
+ "ODDLOCATIONACCESSPERMISSION_ALLOW_ALWAYS"
+ "ODDLOCATIONACCESSPERMISSION_ALLOW_WHILE_USING_SIRI"
+ "ODDLOCATIONACCESSPERMISSION_ASK_NEXT_TIME"
+ "ODDLOCATIONACCESSPERMISSION_DENIED"
+ "ODDLOCATIONACCESSPERMISSION_LOCATION_SERVICES_OFF"
+ "ODDLOCATIONACCESSPERMISSION_RESTRICTED"
+ "ODDLOCATIONACCESSPERMISSION_UNKNOWN"
+ "ORCHNLROUTERBRIDGEROUTINGDECISIONSOURCE_NL_ROUTER_TIMEOUT"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_APP_INTENT"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_APP_LAUNCH"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_CONV_STARTER_SUGGESTION"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_SHORTCUTS"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_SIRI_X_INTENT"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_SUGGESTIONS_POOL"
+ "SUGAUTOCOMPLETESUGGESTIONSOURCE_UNKNOWN"
+ "SUGCONVERSIONMETRICTYPE_CONVERTED"
+ "SUGCONVERSIONMETRICTYPE_NOT_CONVERTED"
+ "SUGCONVERSIONMETRICTYPE_UNKNOWN"
+ "SUGDELIVERYVEHICLE_SIRI_AUTO_COMPLETE"
+ "SUGINVOCATIONTYPE_ASSISTANTTURN_ZEROTURN_AUTOCOMPLETE"
+ "SUGSUPPRESSIONREASON_APP_NOT_USED_RECENTLY"
+ "SUGSUPPRESSIONREASON_DIDNOT_MEET_MIN_SIRI_INIT_ACTIONCOUNT_FOR_DELIVERY_VEHICLE"
+ "SUGSUPPRESSIONREASON_EXPOSED_TOOMANY_SUGGESTIONSPOLICY"
+ "SUGSUPPRESSIONREASON_NOT_PASSED_SUPPRESSIONWINDOW_SINCE_LASTDELIVERYVEHICLEPOLICY"
+ "SUGSUPPRESSIONREASON_SMART_SUPPRESSION_SUPPRESSED"
+ "SUGSUPPRESSIONREASON_SUGGESTION_SHOWN_RECENTLY"
+ "SUGSUPPRESSIONREASON_SUGGESTION_SPOKEN_ALREADY"
+ "SUGSUPPRESSIONREASON_SUGGESTION_SPOKEN_RECENTLY"
+ "SUGTYPINGWINDOWENDREASON_DISSMISSED"
+ "SUGTYPINGWINDOWENDREASON_SUBMIT_REQUEST"
+ "SUGTYPINGWINDOWENDREASON_SUGGESTION_TAPPED"
+ "SUGTYPINGWINDOWENDREASON_UNKNOWN"
+ "autoCompleteQuery"
+ "autoCompleteSuggestionMetaData"
+ "autoCompleteSuggestionSource"
+ "com.apple.aiml.siri.flow.FLOWClientEvent.FLOWLocationAccessPermissionPromptContext"
+ "com.apple.aiml.siri.nlrouter.NLRouterClientEvent.NLRouterSubComponentTriggeredHeuristicRuleTier1"
+ "com.apple.aiml.siri.odd.ODDSiriClientEvent.ODDExecutionMetadataReported"
+ "com.apple.aiml.siri.orch.ORCHClientEvent.ORCHUnsupportedLanguageDetected"
+ "com.apple.aiml.siri.sug.SUGClientEvent.SUGSuggestionsGeneratedTier1"
+ "com.apple.aiml.siri.sug.SUGClientEvent.SUGSuggestionsUIActivityTier1"
+ "com.apple.aiml.siri.sug.SUGClientEvent.SUGTypingWindowEnded"
+ "conversionMetricType"
+ "executionMetadataReported"
+ "executionStatus"
+ "extensionName"
+ "heuristicsHandleEndedData"
+ "isPreciseLocationResult"
+ "languageDetected"
+ "locationAccessPermission"
+ "locationAccessPermissionPromptContext"
+ "nlRouterSubComponentHandleEndedData"
+ "nlRouterSubComponentTriggeredHeuristicRuleTier1"
+ "nlRouterSubComponentTriggeredHeuristicRuleTier1.triggeredHeuristicRule"
+ "numCharactersInQuery"
+ "numCharactersInSuggestion"
+ "numWordsInQuery"
+ "numWordsInSuggestion"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.sugGeneratedTier1"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.sugGeneratedTier1.suggestions"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.sugGeneratedTier1.suggestions.suggestionId"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.uiActivityTier1"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.uiActivityTier1.suggestions"
+ "orderedMessages.siriEventTypeUnion.sugClientEvent.uiActivityTier1.suggestions.suggestionId"
+ "permissionStatusResult"
+ "protectedAppType"
+ "smartSuppressionScore"
+ "sugGeneratedTier1"
+ "sugGeneratedTier1.suggestions"
+ "sugGeneratedTier1.suggestions.suggestionId"
+ "triggeredHeuristicRule"
+ "typingWindowEndReason"
+ "typingWindowEnded"
+ "uiActivityTier1"
+ "uiActivityTier1.suggestions"
+ "uiActivityTier1.suggestions.suggestionId"
+ "unsupportedLanguageDetected"

```
