## SpotlightKnowledge

> `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/Versions/A/SpotlightKnowledge`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x11f38
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0xb80
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x2ae9
-  __TEXT.__gcc_except_tab: 0x18c
-  __TEXT.__oslogstring: 0xaf
-  __TEXT.__unwind_info: 0x428
-  __TEXT.__objc_classname: 0x10d
-  __TEXT.__objc_methname: 0x29d6
-  __TEXT.__objc_methtype: 0x3ac
-  __TEXT.__objc_stubs: 0x1fe0
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x878
+2333.22.13.7.0
+  __TEXT.__text: 0x14930
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0xc98
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x2c76
+  __TEXT.__oslogstring: 0x98e
+  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__objc_classname: 0x10e
+  __TEXT.__objc_methname: 0x2ffe
+  __TEXT.__objc_methtype: 0x441
+  __TEXT.__objc_stubs: 0x23e0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0xab0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x588
-  __AUTH_CONST.__auth_got: 0x348
+  __DATA_CONST.__objc_selrefs: 0xc10
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x610
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x3f00
-  __AUTH_CONST.__objc_const: 0xd20
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__cfstring: 0x4c40
+  __AUTH_CONST.__objc_const: 0xd50
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x9c
-  __DATA.__bss: 0x208
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x1c0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions
   - /System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/Versions/A/DocumentUnderstandingClient
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /System/Library/PrivateFrameworks/SpotlightEmbedding.framework/Versions/A/SpotlightEmbedding
   - /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex

   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA427BDD-AA9E-3F28-904D-B2937FC31CE4
-  Functions: 391
-  Symbols:   1042
-  CStrings:  1648
+  - /usr/lib/libz.1.dylib
+  UUID: 3D6A4CFB-B13E-3D88-AC86-5F5EADA78C8E
+  Functions: 457
+  Symbols:   1159
+  CStrings:  1862
 
Symbols:
+ +[SKGAttributeProcessor sharedImporterProcessor].cold.1
+ +[SKGAttributeProcessor sharedProcessor].cold.1
+ +[SKGManager setLoggingVerbosity:]
+ +[SKGProcessor sharedProcessor].cold.1
+ +[SKGProcessor(EmbeddingsUtils) normalizeForEmbeddingGeneration:bundleID:].cold.1
+ +[SKGProcessorContext sharedContext].cold.1
+ +[SKGSystemListener sharedClientListener].cold.1
+ +[SKGSystemListener sharedProcessorListener].cold.1
+ -[SKGAttributeProcessor getGenerationProgressReportForProtectionClasses:processorFlags:reportHandler:completionHandler:]
+ -[SKGAttributeProcessor getHistoricalProgressReportsForDateInterval:reportHandler:]
+ -[SKGAttributeProcessor getProgressReportWithVerbosity:processorFlags:protectionClasses:reportHandler:]
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.1
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.2
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.3
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.4
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.5
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.6
+ -[SKGAttributeProcessor processorAttributesForRecord:bundleID:protectionClass:isUpdate:].cold.7
+ -[SKGProcessor copyArrayFromRecord:key:]
+ -[SKGProcessor copyDoubleValueFromRecord:key:]
+ -[SKGProcessor copyStringArrayFromRecordAndConcatenate:key:]
+ -[SKGProcessor decorateTextContentWithDescription:isDescriptive:delimiter:]
+ -[SKGProcessor(EmbeddingsUtils) embeddingRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:].cold.1
+ -[SKGProcessor(EmbeddingsUtils) extractContentFromRecordForMessages:bundleID:content:maxChunkCountPtr:textLength:].cold.1
+ -[SKGProcessor(EmbeddingsUtils) extractContentFromRecordForWallet:bundleID:content:maxChunkCountPtr:textLength:].cold.1
+ -[SKGProcessor(EmbeddingsUtils) extractContentFromRecordForWallet:bundleID:content:maxChunkCountPtr:textLength:].cold.2
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.1
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.2
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.3
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.4
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.5
+ -[SKGProcessor(EmbeddingsUtils) needsEmbeddingsForRecord:bundleID:].cold.6
+ -[SKGProcessor(EmbeddingsUtils) shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:]
+ -[SKGProcessor(EmbeddingsUtils) shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:].cold.1
+ -[SKGProcessor(EmbeddingsUtils) shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:].cold.2
+ -[SKGProcessor(EmbeddingsUtils) shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:].cold.3
+ -[SKGProcessor(ItemsUtils) isUpdateFromSpotlightknowledged:]
+ -[SKGProcessor(ItemsUtils) needsSKGReindexingForRecord:bundleID:processorFlags:]
+ -[SKGProcessor(KeyphraserUtils) needsSKGJournalKeyphrasesRecord:bundleID:protectionClass:recordHasText:shouldMarkComplete:isUpdate:]
+ -[SKGProcessor(KeyphraserUtils) needsSKGReindexerKeyphrasesForRecord:bundleID:itemHasText:]
+ -[SKGProcessor(SuggestedEventsUtils) clearSuggestedEventsAttributes:]
+ -[SKGProcessor(SuggestedEventsUtils) completeSuggestedEventsAttributes:]
+ -[SKGProcessor(SuggestedEventsUtils) markForProcessingSuggestedEventsAttributes:]
+ -[SKGProcessor(SuggestedEventsUtils) suggestedEventsRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:]
+ -[SKGProcessor(SuggestedEventsUtils) updateSKGProcessorSuggestedEventsAttributes:record:bundleID:protectionClass:recordHasText:itemHasText:isUpdate:]
+ -[SKGProcessor(SuggestedEventsUtils) updateSKGReindexerSuggestedEventsAttributes:record:bundleID:itemHasText:]
+ -[SKGProcessorConnection getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:]
+ -[SKGProcessorConnection getHistoricalProgressReportsForDateInterval:reportHandler:]
+ -[SKGProcessorConnection getProgressReportWithVerbosity:processorFlags:protectionClasses:reportHandler:]
+ -[SKGProcessorContext breadcrumbsVersion]
+ -[SKGProcessorContext embeddingExcludeContentTypes].cold.1
+ -[SKGProcessorContext embeddingExcludeDomainIdentifier].cold.1
+ -[SKGProcessorContext enableAppEntities]
+ -[SKGProcessorContext enableCalendarEventClassification].cold.1
+ -[SKGProcessorContext enableEmbeddings].cold.1
+ -[SKGProcessorContext enablePreExtractionScanning]
+ -[SKGProcessorContext keyphraseExcludeDomains]
+ -[SKGProcessorContext keyphraseIncludeBundles]
+ -[SKGProcessorContext keyphraseOptionalExtractionAttributes]
+ -[SKGProcessorContext keyphrasesSupportsBundle:domainID:]
+ -[SKGProcessorContext maxKeyphraseCount]
+ -[SKGProcessorContext maxQueryUpdatesSize]
+ -[SKGProcessorContext reindexExcludeBundles]
+ -[SKGProcessorContext setMaxKeyphraseCount:]
+ -[SKGProcessorContext setMaxQueryUpdatesSize:]
+ -[SKGProcessorContext suggestedEventsAllowListAttributes].cold.1
+ -[SKGSystemListener geoPatternsResourcesURL]
+ -[SKGSystemListener parsecIsEnabled]
+ GCC_except_table15
+ GCC_except_table27
+ GCC_except_table7
+ GCC_except_table8
+ OBJC_IVAR_$_SKGProcessorContext._maxKeyphraseCount
+ OBJC_IVAR_$_SKGProcessorContext._maxQueryUpdatesSize
+ OBJC_IVAR_$_SKGSystemListener._locked_geoIndexVersion
+ SKGLogEmbedInit.cold.1
+ SKGLogGetCurrentLoggingLevel.cold.1
+ SKGLogGetCurrentLoggingLevel.onceToken
+ SKGLogInit.cold.1
+ SKGLogInitialize.onceToken
+ SKGLogSetLoggingLevel.cold.1
+ SKGLogSetLoggingLevel.onceToken
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _NSLog
+ _OBJC_CLASS_$_CSGenerativeModelsAvailabilityManager
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SKGManager
+ _OBJC_METACLASS_$_SKGManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _SKGLogGetCurrentLoggingLevel
+ _SKGLogSetLoggingLevel
+ __112-[SKGProcessorConnection getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:]_block_invoke.39
+ __OBJC_$_CLASS_METHODS_SKGManager
+ __OBJC_CLASS_RO_$_SKGManager
+ __OBJC_METACLASS_RO_$_SKGManager
+ __SKGLogGetCurrentLoggingLevel_block_invoke.cold.1
+ __SKGLogSetLoggingLevel_block_invoke.cold.1
+ ___104-[SKGProcessorConnection getProgressReportWithVerbosity:processorFlags:protectionClasses:reportHandler:]_block_invoke
+ ___112-[SKGProcessorConnection getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:]_block_invoke
+ ___36-[SKGSystemListener parsecIsEnabled]_block_invoke
+ ___44-[SKGSystemListener geoPatternsResourcesURL]_block_invoke
+ ___84-[SKGProcessorConnection getHistoricalProgressReportsForDateInterval:reportHandler:]_block_invoke
+ ___SKGLogGetCurrentLoggingLevel_block_invoke
+ ___SKGLogGetCurrentLoggingLevel_block_invoke_2
+ ___SKGLogInitialize_block_invoke
+ ___SKGLogSetLoggingLevel_block_invoke
+ ___SKGLogSetLoggingLevel_block_invoke_2
+ ___assert_rtn
+ ___block_descriptor_129_e8_32s40s48s56s64bs72r80r88r96r104r112r120r_e17_v16?0r^{?=CQ}8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_72_e8_32r40r48r_e17_v16?0r^{?=CQ}8l
+ ___block_descriptor_72_e8_32s40bs48r56r_e17_v16?0r^{?=CQ}8l
+ ___copy_helper_block_e8_32s40b48r56r
+ ___copy_helper_block_e8_32s40s48b
+ ___destroy_helper_block_e8_32s40s48r56r
+ ___destroy_helper_block_e8_32s40s48s
+ ___loggingLevelChangedCallback_block_invoke
+ ___loggingLevelChangedCallback_block_invoke_2
+ __block_literal_global.113
+ __block_literal_global.229
+ __block_literal_global.312
+ __block_literal_global.315
+ __block_literal_global.35
+ __block_literal_global.407
+ __block_literal_global.41
+ __block_literal_global.43
+ __block_literal_global.47
+ __cachedLoggingLevel
+ __defaults
+ __dispatch_main_q
+ __loggerQueue
+ __loggingLevelChangedCallback_block_invoke.cold.1
+ __os_log_debug_impl
+ __xpc_type_array
+ __xpc_type_data
+ _crc32
+ _dispatch_group_notify
+ _eventTypeToStr
+ _getDataTypeForParamType
+ _getStringFromParam
+ _getUInt32FromParam
+ _getUInt64FromParam
+ _loggingLevelChangedCallback
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$clearSuggestedEventsAttributes:
+ _objc_msgSend$completeSuggestedEventsAttributes:
+ _objc_msgSend$copyStringArrayFromRecordAndConcatenate:key:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$duration
+ _objc_msgSend$enableExtractions
+ _objc_msgSend$getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:
+ _objc_msgSend$getHistoricalProgressReportsForDateInterval:reportHandler:
+ _objc_msgSend$getProgressReportWithVerbosity:processorFlags:protectionClasses:reportHandler:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isTextPersonExtractionAvailable
+ _objc_msgSend$isUpdateFromSpotlightknowledged:
+ _objc_msgSend$keyphraseExcludeDomains
+ _objc_msgSend$keyphraseIncludeBundles
+ _objc_msgSend$keyphraseOptionalExtractionAttributes
+ _objc_msgSend$keyphrasesSupportsBundle:domainID:
+ _objc_msgSend$loadAllParametersForClient:
+ _objc_msgSend$markForProcessingSuggestedEventsAttributes:
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$needsSKGReindexerKeyphrasesForRecord:bundleID:itemHasText:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$startDate
+ _objc_msgSend$suggestedEventsRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:
+ _objc_msgSend$synchronize
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$updateSKGProcessorSuggestedEventsAttributes:record:bundleID:protectionClass:recordHasText:itemHasText:isUpdate:
+ _objc_msgSend$updateSKGReindexerSuggestedEventsAttributes:record:bundleID:itemHasText:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _paramTypeToStr
+ _read
+ _xpc_array_append_value
+ _xpc_array_create_empty
+ _xpc_array_get_count
+ _xpc_array_get_value
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ _xpc_dictionary_set_double
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_value
+ _xpc_string_create
+ copyNormalizedLocaleForIdentifier.cold.1
+ getStringFromParam.cold.1
+ getUInt32FromParam.cold.1
+ getUInt64FromParam.cold.1
+ loggingLevelChangedCallback.cold.1
+ loggingLevelChangedCallback.cold.2
+ loggingLevelChangedCallback.onceToken
+ normalizeForEmbeddingGeneration:bundleID:.cMultipleLineRegex
- -[FileEntry .cxx_destruct]
- -[FileEntry filePath]
- -[FileEntry fileSize]
- -[FileEntry initWithFilePath:journalNumber:fileSize:]
- -[FileEntry journalNumber]
- -[FileEntry setFilePath:]
- -[FileEntry setFileSize:]
- -[FileEntry setJournalNumber:]
- -[SKGAttributeProcessor getDocumentUnderstandingProgressReport:]
- -[SKGAttributeProcessor getEmbeddingProgressReport:]
- -[SKGAttributeProcessor getSuggestedEventsProgressReport:]
- -[SKGProcessor copyStringArrayFromRecordAndConcatnate:key:]
- -[SKGProcessorConnection getGenerationProgressReportFor:completion:]
- GCC_except_table11
- GCC_except_table18
- GCC_except_table30
- OBJC_IVAR_$_FileEntry._filePath
- OBJC_IVAR_$_FileEntry._fileSize
- OBJC_IVAR_$_FileEntry._journalNumber
- SKGLogAgentInit.sOnceAgent
- SKGLogAgentInit.sSKGAgentLog
- SKGLogDocUnderstandingInit.sOnceDocUnderstanding
- SKGLogDocUnderstandingInit.sSKGDocUnderstandingLog
- SKGLogEventInit.sOnceEvent
- SKGLogEventInit.sSKGEventLog
- SKGLogGraphInit.sOnceGraph
- SKGLogGraphInit.sSKGGraphLog
- SKGLogJournalInit.sOnceJournals
- SKGLogJournalInit.sSKGJournalLog
- SKGLogKeyphraseInit.sOnceKeyphrase
- SKGLogKeyphraseInit.sSKGKeyphraseLog
- SKGLogSuggestedEventsInit.sOnceSuggestedEvents
- SKGLogSuggestedEventsInit.sSKGSuggestedEventsLog
- SKGLogUpdaterInit.sOnceUpdater
- SKGLogUpdaterInit.sSKGUpdaterLog
- _OBJC_CLASS_$_FileEntry
- _OBJC_METACLASS_$_FileEntry
- _SKGLogAgentInit
- _SKGLogCategoryDefault
- _SKGLogDocUnderstandingInit
- _SKGLogEventInit
- _SKGLogGraphInit
- _SKGLogJournalInit
- _SKGLogKeyphraseInit
- _SKGLogSuggestedEventsInit
- _SKGLogUpdaterInit
- __OBJC_$_INSTANCE_METHODS_FileEntry
- __OBJC_$_INSTANCE_VARIABLES_FileEntry
- __OBJC_$_PROP_LIST_FileEntry
- __OBJC_CLASS_RO_$_FileEntry
- __OBJC_METACLASS_RO_$_FileEntry
- ___68-[SKGProcessorConnection getGenerationProgressReportFor:completion:]_block_invoke
- ___SKGLogAgentInit_block_invoke
- ___SKGLogDocUnderstandingInit_block_invoke
- ___SKGLogEventInit_block_invoke
- ___SKGLogGraphInit_block_invoke
- ___SKGLogJournalInit_block_invoke
- ___SKGLogKeyphraseInit_block_invoke
- ___SKGLogSuggestedEventsInit_block_invoke
- ___SKGLogUpdaterInit_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64bs72r80r88r96r104r112r120r_e99_v16?0r^{skg_playback_info=IdIBii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I}{?=**q*}{?=dQ*}{?=d**QQ})}8l
- ___block_descriptor_48_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_72_e8_32r40r48r_e99_v16?0r^{skg_playback_info=IdIBii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I}{?=**q*}{?=dQ*}{?=d**QQ})}8l
- ___block_descriptor_96_e8_32s40s48bs56r64r72r80r_e99_v16?0r^{skg_playback_info=IdIBii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I}{?=**q*}{?=dQ*}{?=d**QQ})}8l
- ___copy_helper_block_e8_32s40b
- ___copy_helper_block_e8_32s40s48b56r64r72r80r
- ___destroy_helper_block_e8_32s40s
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r
- __block_literal_global.10
- __block_literal_global.16
- __block_literal_global.19
- __block_literal_global.202
- __block_literal_global.22
- __block_literal_global.25
- __block_literal_global.275
- __block_literal_global.278
- __block_literal_global.337
- __block_literal_global.4
- __block_literal_global.7
- __block_literal_global.92
- _isVerboseEvent
- _lseek
- _mmap
- _munmap
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_msgSend$copyStringArrayFromRecordAndConcatnate:key:
- _objc_msgSend$getGenerationProgressReportFor:completion:
- _objc_msgSend$needsSuggestedEventsForRecord:bundleID:
- _objc_msgSend$shouldGenerateSuggestedEventsForRecord:bundleID:
- _objc_setProperty_nonatomic_copy
- _snprintf
- _strlen
- _typeToEventDataType
- _v2_readVInt64
CStrings:
+ "%10u %10u %10u %10u %10u %10u"
+ "%@\n"
+ "%@\n%@\n%@\n%@"
+ "%@ - %@\n"
+ "%@: %@"
+ ":INC:_kMDItemEmbeddingsError"
+ ":INC:_kMDItemKeyphrasesError"
+ "@\"NSNumber\""
+ "@36@0:8@16B24@28"
+ "AppEntities"
+ "B36@0:8@16@24B32"
+ "B40@0:8@16@24Q32"
+ "B56@0:8@16@24@32B40^B44B52"
+ "CannotProcessFromEmbUpdater1"
+ "CannotProcessFromEmbUpdater2"
+ "CannotProcessFromEmbUpdater3"
+ "Checksum mismatch, skipping event."
+ "DocumentUnderstandingProgressReport"
+ "EmbCountFromEmbCachedUpdater"
+ "EmbeddingsProgressReport"
+ "Failed to deserialize donated JSON dictionary from Wallet"
+ "Failed to deserialize donated JSON dictionary from Wallet with error: %@"
+ "InvalidMaxSize!!!"
+ "KeyphraseProgressReport"
+ "Logging level updated to: %ld"
+ "MENU_SPOTLIGHT_SUGGESTIONS"
+ "ProgressReport"
+ "SKGActivityJournalTypes.m"
+ "SKGAttributeProcessor#processorAttributesForRecord bundleID=%@ canHaveEmbeddings=%{BOOL}d needsEmbeddings=%{BOOL}d resulting extractEmbeddings=%{BOOL}d"
+ "SKGAttributeProcessor#processorAttributesForRecord bundleID=%@ needsPriotity=%{BOOL}d"
+ "SKGLogging"
+ "SKGManager"
+ "SKGProcessor+EmbeddingsUtils#canGenerateEmbeddingsForFPRecord bundle=%@ fpId=%@ returning=%{BOOL}d requiresImport=%@"
+ "SKGProcessor+EmbeddingsUtils#canGenerateEmbeddingsForMailRecord bundle=%@ returning=%{BOOL}d isJunkMailBox=%{BOOL}d isJunkItem=%{BOOL}d"
+ "SKGProcessor+EmbeddingsUtils#extractContentFromRecordForMessages. TextContent: %@"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning NO content type is not provided"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning NO embeddingVersion=%@ embeddingModelVersion=%@"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning NO unsupported Content Type %@"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning NO unsupported bundle %@"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning YES embeddingVersion=%@ embeddingModelVersion=%@"
+ "SKGProcessor+EmbeddingsUtils#needsEmbeddingsForRecord returning no as deviceSupportsEmbedding=NO"
+ "SKGProcessor+EmbeddingsUtils#processorAttributesForRecord includeEmbeddings=%{BOOL}d"
+ "SKGProcessor+EmbeddingsUtils#processorAttributesForRecord skipping adding NeedsEmbeddings as notHasItemEmbeddingsSN=%{BOOL}d notHasItemEmbeddingVersion=%{BOOL}d"
+ "SKGProcessor+EmbeddingsUtils#recordNeedsProcessing bundle=%@ returning=%{BOOL}d isJunkMailBox=%{BOOL}d isJunkItem=%{BOOL}d"
+ "SKGProcessor+EmbeddingsUtils#shouldGenerateEmbeddingsForRecord bundle=%@ returning=NO as extractContentFromRecord failed textContLen=%lu"
+ "SKGProcessor+EmbeddingsUtils#shouldGenerateEmbeddingsForRecord bundle=%@ returning=YES"
+ "SKGProcessor+EmbeddingsUtils#shouldGenerateEmbeddingsForRecord bundle=%@ returning=YES for FileProvider item with URL"
+ "SKGProcessor+processorAttributesForRecord includeDocUnderstanding=YES"
+ "SKGProcessor+processorAttributesForRecord includeKeyphrases=YES"
+ "SKGProcessor+processorAttributesForRecord includeSuggestedEvents=YES"
+ "SKGTask: %d disabled"
+ "SpotlightKnowledgePreExtractionScanning"
+ "SuggestedEventsProgressReport"
+ "TQ,N,V_maxQueryUpdatesSize"
+ "TextSemanticSearchPhone"
+ "ThrottlingChangedOffEmbeddings"
+ "ThrottlingChangedOffKeyphrases"
+ "ThrottlingChangedOffPreExtraction"
+ "ThrottlingChangedOnEmbeddings"
+ "ThrottlingChangedOnKeyphrases"
+ "ThrottlingChangedOnPreExtraction"
+ "Total: embCountFromPriorityUpdater:%llu priorityCountFromPriorityUpdater:%llu skipCountFromPriorityUpdater:%llu \n"
+ "Tq,N,V_maxKeyphraseCount"
+ "URLByAppendingPathComponent:"
+ "[\n]+"
+ "^[0-9[:punct:]\\s+]+$"
+ "_SIGeoIndexVersion"
+ "_kMDItemTextContentIsTranscribed"
+ "_locked_geoIndexVersion"
+ "_maxKeyphraseCount"
+ "_maxQueryUpdatesSize"
+ "array"
+ "arrayByAddingObject:"
+ "breadcrumbsVersion"
+ "build"
+ "bundleID"
+ "cacheHitRate"
+ "clearSuggestedEventsAttributes:"
+ "com.apple.Notes"
+ "com.apple.journal"
+ "com.apple.spotlightknowledge.LoggingLevel"
+ "com.apple.spotlightknowledge.LoggingLevelChanged"
+ "com.apple.spotlightknowledge.logger"
+ "com.apple.tips"
+ "completeSuggestedEventsAttributes:"
+ "config.plist"
+ "copyArrayFromRecord:key:"
+ "copyDoubleValueFromRecord:key:"
+ "copyStringArrayFromRecordAndConcatenate:key:"
+ "cs_mail"
+ "dataWithBytes:length:"
+ "dataWithLength:"
+ "decorateTextContentWithDescription:isDescriptive:delimiter:"
+ "duration"
+ "enableAppEntities"
+ "enablePreExtractionScanning"
+ "enabled"
+ "eventType"
+ "geo.cache"
+ "geoPatternsResourcesURL"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeString"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt32"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt64"
+ "getGenerationProgressReportForProtectionClasses:processorFlags:reportHandler:completionHandler:"
+ "getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:"
+ "getHistoricalProgressReportsForDateInterval:reportHandler:"
+ "getProgressReportWithVerbosity:processorFlags:protectionClasses:reportHandler:"
+ "getStringFromParam"
+ "getUInt32FromParam"
+ "getUInt64FromParam"
+ "hasSuffix:"
+ "historicalReports"
+ "identifier"
+ "indexType"
+ "initWithBytes:length:encoding:"
+ "initWithDouble:"
+ "integerForKey:"
+ "invalid"
+ "isTextPersonExtractionAvailable"
+ "isUpdateFromSpotlightknowledged:"
+ "kMDItemAlbum"
+ "kMDItemArtist"
+ "kMDItemBreadcrumbsVersion"
+ "kMDItemEpisode"
+ "kMDItemLatitude"
+ "kMDItemLinkName"
+ "kMDItemLinkType"
+ "kMDItemLongitude"
+ "kMDItemPodcastName"
+ "kMDItemURLDescription"
+ "keyphrase"
+ "keyphraseExcludeDomains"
+ "keyphraseIncludeBundles"
+ "keyphraseOptionalExtractionAttributes"
+ "keyphrasesSupportsBundle:domainID:"
+ "kind"
+ "loadAllParametersForClient:"
+ "markForProcessingSuggestedEventsAttributes:"
+ "maxKeyphraseCount"
+ "maxQueryUpdatesSize"
+ "mutableBytes"
+ "name"
+ "needsSKGJournalKeyphrasesRecord:bundleID:protectionClass:recordHasText:shouldMarkComplete:isUpdate:"
+ "needsSKGReindexerKeyphrasesForRecord:bundleID:itemHasText:"
+ "needsSKGReindexingForRecord:bundleID:processorFlags:"
+ "numberWithInt:"
+ "orderedItems"
+ "outcome"
+ "parsecIsEnabled"
+ "pid"
+ "progressReport"
+ "protectionClasses"
+ "reindexExcludeBundles"
+ "setInteger:forKey:"
+ "setLoggingVerbosity:"
+ "setMaxKeyphraseCount:"
+ "setMaxQueryUpdatesSize:"
+ "shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:"
+ "size"
+ "standardUserDefaults"
+ "startDate"
+ "suggestedEventsRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:"
+ "synchronize"
+ "task"
+ "timeIntervalSinceReferenceDate"
+ "type"
+ "updateSKGProcessorSuggestedEventsAttributes:record:bundleID:protectionClass:recordHasText:itemHasText:isUpdate:"
+ "updateSKGReindexerSuggestedEventsAttributes:record:bundleID:itemHasText:"
+ "v16@?0r^{?=CQ@@}8"
+ "v20@0:8i16"
+ "v48@0:8@16@24@?32@?40"
+ "v48@0:8@16Q24@?32@?40"
+ "v48@0:8q16Q24@32@?40"
+ "verbose"
- "\nTotal: embCountFromPriorityUpdater:%llu priorityCountFromPriorityUpdater:%llu skipCountFromPriorityUpdater:%llu \n"
- "### mismatch repeat event %d at offset %ld\n"
- "### mmap failed"
- "### unknown type %d at offset %ld\n"
- "%10u %10u %10u %10u %10u"
- "%@\n%@\n%@\n%@\n%@"
- "%s "
- "%s at time %s "
- "%s at time %s for item - bundle: %s identifier: %s oid: 0x%llx "
- "%s at time %s for item - bundle: %s identifier: %s oid: 0x%llx info:%s "
- "%s at time(s) %s - path:%s size: %llu "
- "%s for item - bundle: %s identifier: %s oid: 0x%llx "
- "%s for item - oid: 0x%llx "
- "%s pid: %d time: %ssbuild: %s "
- "%s: %d "
- "%s: %s "
- "%s: time: %s str1: %s str2: %s num1: %llu num2: %llu"
- "@40@0:8@16Q24Q32"
- "CannotProcessFromEmbUpdater"
- "FileEntry"
- "Journal was reset at time %s, size before reset: %llu, size after reset: %llu "
- "MMMM d, Y"
- "Num"
- "Repeat"
- "SpotlightKnowledgeAgent"
- "SpotlightKnowledgeDocUnderstanding"
- "SpotlightKnowledgeEvent"
- "SpotlightKnowledgeGraph"
- "SpotlightKnowledgeJournals"
- "SpotlightKnowledgeKeyphrases"
- "SpotlightKnowledgeSuggestedEvents"
- "SpotlightKnowledgeUpdater"
- "T@\"NSString\",C,N,V_filePath"
- "TQ,N,V_fileSize"
- "TQ,N,V_journalNumber"
- "ThrottlingChangedOffBackground"
- "ThrottlingChangedOnBackground"
- "Unknown"
- "VerboseEmbUpToDate"
- "VerboseEvent"
- "VerboseExcludeBundle"
- "VerboseExtractContentFail"
- "VerboseGenerateEmbedFail"
- "VerboseInvalidIndex"
- "VerboseInvalidItem"
- "VerboseNoContent"
- "VerboseProcessLanguageFail"
- "VerboseSemanticSearchDisabled"
- "VerboseShortText"
- "VerboseUpdateChunksFail"
- "[OnBattery]"
- "^[0-9[:punct:]\\s]+$"
- "_filePath"
- "_fileSize"
- "_journalNumber"
- "arrayByAddingObjectsFromArray:"
- "copyStringArrayFromRecordAndConcatnate:key:"
- "fileSize"
- "getDocumentUnderstandingProgressReport:"
- "getEmbeddingProgressReport:"
- "getGenerationProgressReportFor:completion:"
- "getSuggestedEventsProgressReport:"
- "initWithFilePath:journalNumber:fileSize:"
- "journalNumber"
- "setFilePath:"
- "setFileSize:"
- "setJournalNumber:"
- "v16@?0r^{skg_playback_info=IdIBii(?={?=Id*}{?=dqq}{?=*}{?=**q}{?=d}{?=I}{?=**q*}{?=dQ*}{?=d**QQ})}8"

```
