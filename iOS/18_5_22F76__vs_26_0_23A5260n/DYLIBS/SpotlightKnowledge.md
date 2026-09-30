## SpotlightKnowledge

> `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x13d04
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0xd80
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x2d25
-  __TEXT.__oslogstring: 0x98e
-  __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x508
-  __TEXT.__objc_classname: 0x10e
-  __TEXT.__objc_methname: 0x33a9
-  __TEXT.__objc_methtype: 0x467
-  __TEXT.__objc_stubs: 0x24e0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xd58
+2374.0.1.0.0
+  __TEXT.__text: 0x12fc4
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0xf00
+  __TEXT.__const: 0xcc
+  __TEXT.__cstring: 0x2459
+  __TEXT.__gcc_except_tab: 0x318
+  __TEXT.__oslogstring: 0x913
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__objc_classname: 0x108
+  __TEXT.__objc_methname: 0x389b
+  __TEXT.__objc_methtype: 0x375
+  __TEXT.__objc_stubs: 0x2540
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xb28
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc90
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x6a0
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x4c80
-  __AUTH_CONST.__objc_const: 0xe10
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__objc_selrefs: 0xd20
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_arraydata: 0x6a8
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__cfstring: 0x4300
+  __AUTH_CONST.__objc_const: 0x1178
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xac
-  __DATA.__bss: 0x128
+  __DATA.__objc_ivar: 0xf0
+  __DATA.__bss: 0x1f0
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7C4A69CD-28BF-35FF-A43A-B9C28006BB05
-  Functions: 458
-  Symbols:   1645
-  CStrings:  1895
+  UUID: 3BD0A056-D56D-3223-B3A9-EAD42CB3E0C4
+  Functions: 507
+  Symbols:   1769
+  CStrings:  1779
 
Symbols:
+ +[SKGUtilities sharedSKGUtilities]
+ +[SKGUtilities sharedSKGUtilities].cold.1
+ -[SKGAttributeProcessor getHistoricalProgressReportsJSONDataForDateInterval:reportHandler:]
+ -[SKGBundleStatus .cxx_destruct]
+ -[SKGBundleStatus awaitingRedonationCount]
+ -[SKGBundleStatus breadcrumbsCount]
+ -[SKGBundleStatus bundleFileQuery]
+ -[SKGBundleStatus bundleQuery]
+ -[SKGBundleStatus count]
+ -[SKGBundleStatus documentUnderstandingCount]
+ -[SKGBundleStatus init]
+ -[SKGBundleStatus itemsRedonationRequestCapReachedCount]
+ -[SKGBundleStatus keyphrasesCount]
+ -[SKGBundleStatus locationsCount]
+ -[SKGBundleStatus needDocumentUnderstandingCount]
+ -[SKGBundleStatus needEmbedCount]
+ -[SKGBundleStatus needKeyphrasesCount]
+ -[SKGBundleStatus needProcessCount]
+ -[SKGBundleStatus needSuggestedEventsCount]
+ -[SKGBundleStatus primaryEmbeddingCount]
+ -[SKGBundleStatus processedCount]
+ -[SKGBundleStatus secondaryEmbeddingCount]
+ -[SKGBundleStatus setAwaitingRedonationCount:]
+ -[SKGBundleStatus setBreadcrumbsCount:]
+ -[SKGBundleStatus setBundleFileQuery:]
+ -[SKGBundleStatus setBundleQuery:]
+ -[SKGBundleStatus setCount:]
+ -[SKGBundleStatus setDocumentUnderstandingCount:]
+ -[SKGBundleStatus setItemsRedonationRequestCapReachedCount:]
+ -[SKGBundleStatus setKeyphrasesCount:]
+ -[SKGBundleStatus setLocationsCount:]
+ -[SKGBundleStatus setNeedDocumentUnderstandingCount:]
+ -[SKGBundleStatus setNeedEmbedCount:]
+ -[SKGBundleStatus setNeedKeyphrasesCount:]
+ -[SKGBundleStatus setNeedProcessCount:]
+ -[SKGBundleStatus setNeedSuggestedEventsCount:]
+ -[SKGBundleStatus setPrimaryEmbeddingCount:]
+ -[SKGBundleStatus setProcessedCount:]
+ -[SKGBundleStatus setSecondaryEmbeddingCount:]
+ -[SKGBundleStatus setSuggestedEventsCount:]
+ -[SKGBundleStatus suggestedEventsCount]
+ -[SKGProcessorConnection getHistoricalProgressReportsJSONDataForDateInterval:reportHandler:]
+ -[SKGProcessorContext enableExtractions].cold.1
+ -[SKGProcessorContext enableReceiverDebugging]
+ -[SKGProcessorContext enableReceiverDebugging].cold.1
+ -[SKGProcessorContext enableScheduledReceivers]
+ -[SKGUtilities getSKGDictionary:filterBundle:protectionClasses:processorFlags:]
+ -[SKGUtilities init]
+ GCC_except_table19
+ GCC_except_table3
+ GCC_except_table5
+ GCC_except_table9
+ _CSLinkTypeMap
+ _OBJC_CLASS_$_SKGBundleStatus
+ _OBJC_CLASS_$_SKGUtilities
+ _OBJC_IVAR_$_SKGBundleStatus._awaitingRedonationCount
+ _OBJC_IVAR_$_SKGBundleStatus._breadcrumbsCount
+ _OBJC_IVAR_$_SKGBundleStatus._bundleFileQuery
+ _OBJC_IVAR_$_SKGBundleStatus._bundleQuery
+ _OBJC_IVAR_$_SKGBundleStatus._count
+ _OBJC_IVAR_$_SKGBundleStatus._documentUnderstandingCount
+ _OBJC_IVAR_$_SKGBundleStatus._itemsRedonationRequestCapReachedCount
+ _OBJC_IVAR_$_SKGBundleStatus._keyphrasesCount
+ _OBJC_IVAR_$_SKGBundleStatus._locationsCount
+ _OBJC_IVAR_$_SKGBundleStatus._needDocumentUnderstandingCount
+ _OBJC_IVAR_$_SKGBundleStatus._needEmbedCount
+ _OBJC_IVAR_$_SKGBundleStatus._needKeyphrasesCount
+ _OBJC_IVAR_$_SKGBundleStatus._needProcessCount
+ _OBJC_IVAR_$_SKGBundleStatus._needSuggestedEventsCount
+ _OBJC_IVAR_$_SKGBundleStatus._primaryEmbeddingCount
+ _OBJC_IVAR_$_SKGBundleStatus._processedCount
+ _OBJC_IVAR_$_SKGBundleStatus._secondaryEmbeddingCount
+ _OBJC_IVAR_$_SKGBundleStatus._suggestedEventsCount
+ _OBJC_METACLASS_$_SKGBundleStatus
+ _OBJC_METACLASS_$_SKGUtilities
+ _SKGLogAgentInit
+ _SKGLogAgentInit.cold.1
+ _SKGLogAgentInit.sOnceAgent
+ _SKGLogAgentInit.sSKGAgentLog
+ _SKGLogCategoryDefault
+ _SKGLogDocUnderstandingInit
+ _SKGLogDocUnderstandingInit.cold.1
+ _SKGLogDocUnderstandingInit.sOnceDocUnderstanding
+ _SKGLogDocUnderstandingInit.sSKGDocUnderstandingLog
+ _SKGLogEventInit
+ _SKGLogEventInit.cold.1
+ _SKGLogEventInit.sOnceEvent
+ _SKGLogEventInit.sSKGEventLog
+ _SKGLogGraphInit
+ _SKGLogGraphInit.cold.1
+ _SKGLogGraphInit.sOnceGraph
+ _SKGLogGraphInit.sSKGGraphLog
+ _SKGLogJournalInit
+ _SKGLogJournalInit.cold.1
+ _SKGLogJournalInit.sOnceJournals
+ _SKGLogJournalInit.sSKGJournalLog
+ _SKGLogKeyphraseInit
+ _SKGLogKeyphraseInit.cold.1
+ _SKGLogKeyphraseInit.sOnceKeyphrase
+ _SKGLogKeyphraseInit.sSKGKeyphraseLog
+ _SKGLogPipelineInit
+ _SKGLogPipelineInit.cold.1
+ _SKGLogPipelineInit.sOncePipeline
+ _SKGLogPipelineInit.sSKGPipelineLog
+ _SKGLogScheduledReceiverInit
+ _SKGLogScheduledReceiverInit.cold.1
+ _SKGLogScheduledReceiverInit.sOnceScheduledReceiver
+ _SKGLogScheduledReceiverInit.sSKGScheduledReceiverLog
+ _SKGLogSuggestedEventsInit
+ _SKGLogSuggestedEventsInit.cold.1
+ _SKGLogSuggestedEventsInit.sOnceSuggestedEvents
+ _SKGLogSuggestedEventsInit.sSKGSuggestedEventsLog
+ _SKGLogUpdaterInit
+ _SKGLogUpdaterInit.cold.1
+ _SKGLogUpdaterInit.sOnceUpdater
+ _SKGLogUpdaterInit.sSKGUpdaterLog
+ __OBJC_$_CLASS_METHODS_SKGProcessor(KeyphraserUtils|ItemsUtils|DocUnderstandingUtils|SuggestedEventsUtils|EmbeddingsUtils)
+ __OBJC_$_CLASS_METHODS_SKGUtilities
+ __OBJC_$_CLASS_PROP_LIST_SKGUtilities
+ __OBJC_$_INSTANCE_METHODS_SKGBundleStatus
+ __OBJC_$_INSTANCE_METHODS_SKGProcessor(KeyphraserUtils|ItemsUtils|DocUnderstandingUtils|SuggestedEventsUtils|EmbeddingsUtils)
+ __OBJC_$_INSTANCE_METHODS_SKGUtilities
+ __OBJC_$_INSTANCE_VARIABLES_SKGBundleStatus
+ __OBJC_$_PROP_LIST_SKGBundleStatus
+ __OBJC_CLASS_RO_$_SKGBundleStatus
+ __OBJC_CLASS_RO_$_SKGUtilities
+ __OBJC_METACLASS_RO_$_SKGBundleStatus
+ __OBJC_METACLASS_RO_$_SKGUtilities
+ ___34+[SKGUtilities sharedSKGUtilities]_block_invoke
+ ___40-[SKGProcessorContext enableExtractions]_block_invoke
+ ___44-[SKGProcessorConnection launchUpgradeTasks]_block_invoke
+ ___46-[SKGProcessorContext enableReceiverDebugging]_block_invoke
+ ___79-[SKGUtilities getSKGDictionary:filterBundle:protectionClasses:processorFlags:]_block_invoke
+ ___79-[SKGUtilities getSKGDictionary:filterBundle:protectionClasses:processorFlags:]_block_invoke_2
+ ___92-[SKGProcessorConnection getHistoricalProgressReportsJSONDataForDateInterval:reportHandler:]_block_invoke
+ ___SKGLogAgentInit_block_invoke
+ ___SKGLogDocUnderstandingInit_block_invoke
+ ___SKGLogEventInit_block_invoke
+ ___SKGLogGraphInit_block_invoke
+ ___SKGLogJournalInit_block_invoke
+ ___SKGLogKeyphraseInit_block_invoke
+ ___SKGLogPipelineInit_block_invoke
+ ___SKGLogScheduledReceiverInit_block_invoke
+ ___SKGLogSuggestedEventsInit_block_invoke
+ ___SKGLogUpdaterInit_block_invoke
+ ___block_descriptor_184_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_literal_global.10
+ ___block_literal_global.16
+ ___block_literal_global.19
+ ___block_literal_global.215
+ ___block_literal_global.22
+ ___block_literal_global.25
+ ___block_literal_global.31
+ ___block_literal_global.325
+ ___block_literal_global.328
+ ___block_literal_global.34
+ ___block_literal_global.4
+ ___block_literal_global.417
+ ___block_literal_global.46
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.53
+ ___block_literal_global.58
+ ___block_literal_global.7
+ ___block_literal_global.99
+ _enableExtractions.onceToken
+ _enableExtractions.sEnableExtractions
+ _enableReceiverDebugging.onceToken
+ _enableReceiverDebugging.sRecDebugEnabled
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$copyArrayFromRecord:key:
+ _objc_msgSend$decorateTextContentWithDescription:isDescriptive:delimiter:
+ _objc_msgSend$getGenerationProgressReportForProtectionClasses:processorFlags:reportHandler:completionHandler:
+ _objc_msgSend$getHistoricalProgressReportsJSONDataForDateInterval:reportHandler:
+ _objc_msgSend$setAwaitingRedonationCount:
+ _objc_msgSend$setBreadcrumbsCount:
+ _objc_msgSend$setBundleFileQuery:
+ _objc_msgSend$setBundleQuery:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setDocumentUnderstandingCount:
+ _objc_msgSend$setItemsRedonationRequestCapReachedCount:
+ _objc_msgSend$setKeyphrasesCount:
+ _objc_msgSend$setLocationsCount:
+ _objc_msgSend$setNeedDocumentUnderstandingCount:
+ _objc_msgSend$setNeedEmbedCount:
+ _objc_msgSend$setNeedKeyphrasesCount:
+ _objc_msgSend$setNeedProcessCount:
+ _objc_msgSend$setNeedSuggestedEventsCount:
+ _objc_msgSend$setPrimaryEmbeddingCount:
+ _objc_msgSend$setProcessedCount:
+ _objc_msgSend$setSecondaryEmbeddingCount:
+ _objc_msgSend$setSuggestedEventsCount:
+ _objc_msgSend$sortUsingSelector:
+ _objc_opt_new
+ _objc_release_x10
+ _sharedSKGUtilities.onceToken
+ _sharedSKGUtilities.sSharedSKGUtilities
+ _xpc_array_get_string
+ _xpc_dictionary_get_array
- +[SKGActivityJournalDecoder SKGActivityJournalPlayback:block:]
- +[SKGActivityJournalDecoder _SKGActivityDump:dst:]
- +[SKGActivityJournalDecoder _SKGEmbeddingTimeline:includePerf:block:]
- +[SKGActivityJournalDecoder _SKGEmbeddingTimelineDump:includePerf:dst:]
- +[SKGActivityJournalDecoder _SKGEmbeddingXPCTimeline:updater:block:]
- -[EventCollector .cxx_destruct]
- -[EventCollector clear]
- -[EventCollector collectedData]
- -[EventCollector handleEventWithStr1:str2:num:]
- -[EventCollector init]
- -[EventCollector printResultsWithBlock:]
- -[EventCollector setCollectedData:]
- -[SKGProcessor(EmbeddingsUtils) embeddingRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:]
- -[SKGProcessor(EmbeddingsUtils) embeddingRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:].cold.1
- GCC_except_table10
- GCC_except_table13
- GCC_except_table18
- GCC_except_table23
- GCC_except_table6
- GCC_except_table7
- GCC_except_table8
- _CFCalendarCreateWithIdentifier
- _CFCalendarDecomposeAbsoluteTime
- _CFCalendarSetTimeZone
- _CFTimeZoneCopySystem
- _NSLog
- _NewAggregateStats
- _OBJC_CLASS_$_EventCollector
- _OBJC_CLASS_$_NSMutableData
- _OBJC_CLASS_$_SKGActivityJournalDecoder
- _OBJC_IVAR_$_EventCollector._collectedData
- _OBJC_METACLASS_$_EventCollector
- _OBJC_METACLASS_$_SKGActivityJournalDecoder
- _OUTLINED_FUNCTION_3
- _PrintAggregateStats
- __OBJC_$_CLASS_METHODS_SKGActivityJournalDecoder
- __OBJC_$_CLASS_METHODS_SKGProcessor(DocUnderstandingUtils|ItemsUtils|SuggestedEventsUtils|EmbeddingsUtils|KeyphraserUtils)
- __OBJC_$_INSTANCE_METHODS_EventCollector
- __OBJC_$_INSTANCE_METHODS_SKGProcessor(DocUnderstandingUtils|ItemsUtils|SuggestedEventsUtils|EmbeddingsUtils|KeyphraserUtils)
- __OBJC_$_INSTANCE_VARIABLES_EventCollector
- __OBJC_$_PROP_LIST_EventCollector
- __OBJC_CLASS_RO_$_EventCollector
- __OBJC_CLASS_RO_$_SKGActivityJournalDecoder
- __OBJC_METACLASS_RO_$_EventCollector
- __OBJC_METACLASS_RO_$_SKGActivityJournalDecoder
- ___36-[SKGSystemListener parsecIsEnabled]_block_invoke
- ___50+[SKGActivityJournalDecoder _SKGActivityDump:dst:]_block_invoke
- ___68+[SKGActivityJournalDecoder _SKGEmbeddingXPCTimeline:updater:block:]_block_invoke
- ___69+[SKGActivityJournalDecoder _SKGEmbeddingTimeline:includePerf:block:]_block_invoke
- ___71+[SKGActivityJournalDecoder _SKGEmbeddingTimelineDump:includePerf:dst:]_block_invoke
- ___71+[SKGActivityJournalDecoder _SKGEmbeddingTimelineDump:includePerf:dst:]_block_invoke_2
- ___71+[SKGActivityJournalDecoder _SKGEmbeddingTimelineDump:includePerf:dst:]_block_invoke_3
- ___assert_rtn
- ___block_descriptor_129_e8_32s40s48s56s64bs72r80r88r96r104r112r120r_e17_v16?0r^{?=CQ}8lr72l8r80l8s32l8r88l8r96l8s64l8s40l8r104l8s48l8r112l8r120l8s56l8
- ___block_descriptor_40_e18_v16?0"NSString"8l
- ___block_descriptor_40_e8_v16?0*8l
- ___block_descriptor_72_e8_32r40r48r_e17_v16?0r^{?=CQ}8lr32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40bs48r56r_e17_v16?0r^{?=CQ}8ls32l8r48l8s40l8r56l8
- ___block_literal_global.108
- ___block_literal_global.224
- ___block_literal_global.313
- ___block_literal_global.316
- ___block_literal_global.35
- ___block_literal_global.405
- ___block_literal_global.47
- ___sprintf_chk
- ___stderrp
- _bzero
- _calculateAverage
- _calculatePercentile
- _crc32
- _createReportLine
- _eventTypeToStr
- _fprintf
- _fputc
- _fputs
- _fwrite
- _getCalendar
- _getDataTypeForParamType
- _getDateString
- _getStringFromParam
- _getStringFromParam.cold.1
- _getUInt32FromParam
- _getUInt32FromParam.cold.1
- _getUInt64FromParam
- _getUInt64FromParam.cold.1
- _kCFAllocatorSystemDefault
- _kCFGregorianCalendar
- _objc_msgSend$SKGActivityJournalPlayback:block:
- _objc_msgSend$_SKGEmbeddingTimeline:includePerf:block:
- _objc_msgSend$_SKGEmbeddingXPCTimeline:updater:block:
- _objc_msgSend$allKeys
- _objc_msgSend$clear
- _objc_msgSend$collectedData
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$dataWithLength:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$handleEventWithStr1:str2:num:
- _objc_msgSend$initWithBytes:length:encoding:
- _objc_msgSend$integerValue
- _objc_msgSend$mutableBytes
- _objc_msgSend$mutableCopy
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$numberWithInt:
- _objc_msgSend$printResultsWithBlock:
- _objc_msgSend$removeAllObjects
- _objc_msgSend$setValue:forKey:
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$unsignedLongLongValue
- _paramTypeToStr
- _read
- _sprintf
CStrings:
+ "%@;%@"
+ ";"
+ "@48@0:8@16@24@32Q40"
+ "OB"
+ "SKGBundleStatus"
+ "SKGUtilities"
+ "SpotlightKnowledgeAgent"
+ "SpotlightKnowledgeDocUnderstanding"
+ "SpotlightKnowledgeEvent"
+ "SpotlightKnowledgeGraph"
+ "SpotlightKnowledgeJournals"
+ "SpotlightKnowledgeKeyphrases"
+ "SpotlightKnowledgePipeline"
+ "SpotlightKnowledgeScheduledReceiver"
+ "SpotlightKnowledgeSuggestedEvents"
+ "SpotlightKnowledgeTextUnderstanding"
+ "SpotlightKnowledgeUpdater"
+ "SpotlightScheduledReceiverDebug"
+ "T@\"NSString\",&,N,V_bundleFileQuery"
+ "T@\"NSString\",&,N,V_bundleQuery"
+ "T@\"SKGUtilities\",R"
+ "TQ,N,V_awaitingRedonationCount"
+ "TQ,N,V_breadcrumbsCount"
+ "TQ,N,V_count"
+ "TQ,N,V_documentUnderstandingCount"
+ "TQ,N,V_itemsRedonationRequestCapReachedCount"
+ "TQ,N,V_keyphrasesCount"
+ "TQ,N,V_locationsCount"
+ "TQ,N,V_needDocumentUnderstandingCount"
+ "TQ,N,V_needEmbedCount"
+ "TQ,N,V_needKeyphrasesCount"
+ "TQ,N,V_needProcessCount"
+ "TQ,N,V_needSuggestedEventsCount"
+ "TQ,N,V_primaryEmbeddingCount"
+ "TQ,N,V_processedCount"
+ "TQ,N,V_secondaryEmbeddingCount"
+ "TQ,N,V_suggestedEventsCount"
+ "_awaitingRedonationCount"
+ "_breadcrumbsCount"
+ "_bundleFileQuery"
+ "_bundleQuery"
+ "_count"
+ "_documentUnderstandingCount"
+ "_itemsRedonationRequestCapReachedCount"
+ "_keyphrasesCount"
+ "_locationsCount"
+ "_needDocumentUnderstandingCount"
+ "_needEmbedCount"
+ "_needKeyphrasesCount"
+ "_needProcessCount"
+ "_needSuggestedEventsCount"
+ "_primaryEmbeddingCount"
+ "_processedCount"
+ "_secondaryEmbeddingCount"
+ "_suggestedEventsCount"
+ "address"
+ "album name"
+ "arrayWithCapacity:"
+ "artist name"
+ "awaitingRedonationCount"
+ "breadcrumbsCount"
+ "bundleFileQueriesDict"
+ "bundleFileQuery"
+ "bundleIDs"
+ "bundleQueriesDict"
+ "bundleQuery"
+ "caseInsensitiveCompare:"
+ "com.apple.duetexpertd"
+ "documentUnderstandingCount"
+ "enableReceiverDebugging"
+ "enableScheduledReceivers"
+ "episode name"
+ "getHistoricalProgressReportsJSONDataForDateInterval:reportHandler:"
+ "getSKGDictionary:filterBundle:protectionClasses:processorFlags:"
+ "includeSKG"
+ "itemsAwaitingRedonationDict"
+ "itemsNeedDocumentUnderstandingDict"
+ "itemsNeedEmbedDict"
+ "itemsNeedKeyphrasesDict"
+ "itemsNeedProcessingDict"
+ "itemsNeedSuggestedEventsDict"
+ "itemsProcessedDict"
+ "itemsRedonationRequestCapReachedCount"
+ "itemsRedonationRequestCapReachedDict"
+ "itemsWithBreadcrumbsDict"
+ "itemsWithDocumentUnderstandingDict"
+ "itemsWithKeyphrasesDict"
+ "itemsWithLocationsDict"
+ "itemsWithPrimaryTextEmbeddingDict"
+ "itemsWithSecondaryTextEmbeddingDict"
+ "itemsWithSuggestedEventsDict"
+ "kMDItemCreator"
+ "kMDItemLinkSubType"
+ "keyphrasesCount"
+ "link description"
+ "link name"
+ "link subtype"
+ "link type"
+ "locationsCount"
+ "needDocumentUnderstandingCount"
+ "needEmbedCount"
+ "needKeyphrasesCount"
+ "needProcessCount"
+ "needSuggestedEventsCount"
+ "podcast name"
+ "primaryEmbeddingCount"
+ "processedCount"
+ "secondaryEmbeddingCount"
+ "setAwaitingRedonationCount:"
+ "setBreadcrumbsCount:"
+ "setBundleFileQuery:"
+ "setBundleQuery:"
+ "setCount:"
+ "setDocumentUnderstandingCount:"
+ "setItemsRedonationRequestCapReachedCount:"
+ "setKeyphrasesCount:"
+ "setLocationsCount:"
+ "setNeedDocumentUnderstandingCount:"
+ "setNeedEmbedCount:"
+ "setNeedKeyphrasesCount:"
+ "setNeedProcessCount:"
+ "setNeedSuggestedEventsCount:"
+ "setPrimaryEmbeddingCount:"
+ "setProcessedCount:"
+ "setSecondaryEmbeddingCount:"
+ "setSuggestedEventsCount:"
+ "sharedSKGUtilities"
+ "sortUsingSelector:"
+ "suggestedEventsCount"
+ "totalItemsDict"
+ "v16@?0@\"NSError\"8"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
- "### file open failed"
- "%-4s %-20s %-20s %6.1f %5llu %5llu %5llu %5llu %5llu %5llu %8.2f%% %c"
- "%04d-%02d-%02d %02d:%02d:%02d"
- "%10u %10u %10u %10u %10u %10u"
- "%20s %10s %10s %10s %10s %10s"
- "%20s %@"
- "%@\n"
- "%@ - %@\n"
- "%@|%@"
- "------------------------- Embedding Journal Queue Timeline -------------------------------\n"
- "------------------------- Priority Journal Queue Timeline -------------------------------\n"
- "------------------end------------------"
- "---------------BG Task Emb Efficiency End---------------\n"
- "---------------BG Task Emb Efficiency---------------"
- "---------------PRI Task Emb Efficiency End---------------\n"
- "---------------PRI Task Emb Efficiency---------------"
- "---------------Profiling---------------"
- "Avg w/o 0s:\t%.2f"
- "Avg:\t%.2f"
- "CancelledFromEmbUpdater"
- "CancelledFromPriorityUpdater"
- "CannotProcessFromEmbUpdater1"
- "CannotProcessFromEmbUpdater2"
- "CannotProcessFromEmbUpdater3"
- "CannotProcesseFromPriorityUpdater"
- "Checksum mismatch, skipping event."
- "DOMAIN_PARSEC"
- "EmbCountFromEmbCachedUpdater"
- "EmbCountFromEmbUpdater"
- "EmbCountFromPriorityUpdater"
- "EmbeddingHandleItem"
- "EmbeddingHandleItemFromPriorityUpdater"
- "EmbeddingHitRate"
- "EventCollector"
- "IndexCompleteFromEmbeddingUpdater"
- "IndexCompleteFromPriorityUpdater"
- "IndexErrorFromEmbeddingUpdater"
- "IndexErrorFromFromPriorityUpdater"
- "IndexFromEmbeddingUpdater"
- "IndexFromPriorityUpdater"
- "IndexTimeoutFromEmbeddingUpdater"
- "IndexTimeoutFromPriorityUpdater"
- "Init"
- "InvalidMaxSize!!!"
- "ItemLanguageNotSupportedForEmbedding"
- "JournalCount"
- "JournalProcessed"
- "JournalSkip"
- "Log"
- "NotAcceptingJournals"
- "Overall BG emb efficiency(max 36k): %.2f"
- "Overall BG emb throughput(items/hr): %.2f"
- "Overall PRI emb efficiency(max 36k): %.2f"
- "Overall PRI emb throughput(items/hr): %.2f"
- "PRI"
- "PrimaryEmbeddingComplete"
- "PrimaryEmbeddingEmpty"
- "PrimaryEmbeddingNoTextInput"
- "Priority"
- "PriorityCountFromPriorityUpdater"
- "Process"
- "ProcessedItemFromPriorityUpdater"
- "ProfilingEvent"
- "PurgeJournals"
- "Receive"
- "Reset"
- "SBSearchDisabledDomains"
- "SELF != 0"
- "SKGActivityJournalDecoder"
- "SKGActivityJournalPlayback:block:"
- "SKGActivityJournalTypes.m"
- "SKGProcessor+EmbeddingsUtils#recordNeedsProcessing bundle=%@ returning=%{BOOL}d isJunkMailBox=%{BOOL}d isJunkItem=%{BOOL}d"
- "SecondaryEmbeddingComplete"
- "SecondaryEmbeddingNoTextInput"
- "T@\"NSMutableDictionary\",&,N,V_collectedData"
- "ThrottlingChangedOffEmbeddings"
- "ThrottlingChangedOffKeyphrases"
- "ThrottlingChangedOffPreExtraction"
- "ThrottlingChangedOffPriority"
- "ThrottlingChangedOnEmbeddings"
- "ThrottlingChangedOnKeyphrases"
- "ThrottlingChangedOnPreExtraction"
- "ThrottlingChangedOnPriority"
- "Total BG embeddings generated: %llu"
- "Total BG runtime granted: %fs"
- "Total PRI embeddings generated: %llu"
- "Total PRI runtime granted: %fs"
- "Total: embCountFromPriorityUpdater:%llu priorityCountFromPriorityUpdater:%llu skipCountFromPriorityUpdater:%llu \n"
- "Type, from_date_time, to_date_time, elapsed_time_secs, handled, skipped, processed, indexed, index_error, index_timeout, efficiency(max 36k/h), cancelFlag"
- "XPCEventAdd"
- "XPCEventComplete"
- "XPCEventUpdate"
- "_SKGActivityDump:dst:"
- "_SKGEmbeddingTimeline:includePerf:block:"
- "_SKGEmbeddingTimelineDump:includePerf:dst:"
- "_SKGEmbeddingXPCTimeline:updater:block:"
- "_collectedData"
- "allKeys"
- "build"
- "bundleID"
- "cacheHitRate"
- "clear"
- "collectedData"
- "com.apple."
- "com.apple.spotlightui"
- "componentsSeparatedByString:"
- "cp_a"
- "cp_b"
- "cp_c"
- "cp_cx"
- "cs_mail"
- "cs_pc_a"
- "cs_pc_b"
- "cs_pc_c"
- "cs_pc_cx"
- "cs_priority"
- "dataWithLength:"
- "embeddingRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:"
- "eventType"
- "filePath"
- "filteredArrayUsingPredicate:"
- "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeString"
- "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt32"
- "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt64"
- "getStringFromParam"
- "getUInt32FromParam"
- "getUInt64FromParam"
- "handleEventWithStr1:str2:num:"
- "identifier"
- "indexType"
- "initWithBytes:length:encoding:"
- "integerValue"
- "invalid"
- "kind"
- "mutableBytes"
- "mutableCopy"
- "numberWithDouble:"
- "numberWithInt:"
- "outcome"
- "p05:\t%.2f"
- "p25:\t%.2f"
- "p50:\t%.2f"
- "p75:\t%.2f"
- "p90:\t%.2f"
- "p95:\t%.2f"
- "p99:\t%.2f"
- "pid"
- "printResultsWithBlock:"
- "priority"
- "removeAllObjects"
- "setCollectedData:"
- "setValue:forKey:"
- "size"
- "sortedArrayUsingSelector:"
- "task"
- "timestamp"
- "total"
- "type"
- "type: %s, outcome: %s -> count: %llu, avg: %.2f, total:%llu"
- "unknown"
- "unsignedLongLongValue"
- "v16@?0*8"
- "v16@?0@\"NSString\"8"
- "v16@?0r^{?=CQ@@}8"
- "v32@0:8@16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
- "v32@0:8r*16@?24"
- "v36@0:8@16B24@?28"
- "v36@0:8@16B24^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}28"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "yMdHms"
- "|"

```
