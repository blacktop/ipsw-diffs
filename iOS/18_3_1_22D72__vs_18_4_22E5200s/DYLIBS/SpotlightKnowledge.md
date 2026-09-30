## SpotlightKnowledge

> `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge`

```diff

-2328.7.8.5.0
-  __TEXT.__text: 0x1073c
-  __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0xb80
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x2ae5
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__oslogstring: 0xaf
-  __TEXT.__unwind_info: 0x408
-  __TEXT.__objc_classname: 0x10d
-  __TEXT.__objc_methname: 0x29d6
-  __TEXT.__objc_methtype: 0x3ac
-  __TEXT.__objc_stubs: 0x1fe0
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0xad0
+2333.18.0.8.0
+  __TEXT.__text: 0x12214
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_methlist: 0xc0c
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x2b10
+  __TEXT.__oslogstring: 0xa5c
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__objc_classname: 0x10e
+  __TEXT.__objc_methname: 0x2d97
+  __TEXT.__objc_methtype: 0x400
+  __TEXT.__objc_stubs: 0x2260
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x588
-  __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x3ee0
-  __AUTH_CONST.__objc_const: 0xd20
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_selrefs: 0xb90
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x600
+  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x4a40
+  __AUTH_CONST.__objc_const: 0xd50
+  __AUTH_CONST.__objc_intobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x9c
-  __DATA.__bss: 0x1c8
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
   - /System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding

   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 370
-  Symbols:   597
-  CStrings:  1146
+  - /usr/lib/libz.1.dylib
+  Functions: 424
+  Symbols:   671
+  CStrings:  1219
 
Symbols:
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
+ _NSLog
+ _OBJC_CLASS_$_CSGenerativeModelsAvailabilityManager
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_SKGManager
+ _OBJC_METACLASS_$_SKGManager
+ ___assert_rtn
+ __dispatch_main_q
+ __os_log_debug_impl
+ _crc32
+ _dispatch_group_notify
+ _read
+ _xpc_array_append_value
+ _xpc_array_create_empty
+ _xpc_dictionary_set_value
+ _xpc_string_create
- _SKGLogAgentInit
- _SKGLogCategoryDefault
- _SKGLogDocUnderstandingInit
- _SKGLogEmbedInit
- _SKGLogEventInit
- _SKGLogGraphInit
- _SKGLogInit
- _SKGLogJournalInit
- _SKGLogKeyphraseInit
- _SKGLogSuggestedEventsInit
- _SKGLogUpdaterInit
- _lseek
- _mmap
- _munmap
- _objc_setProperty_nonatomic_copy
- _snprintf
- _strlen
CStrings:
+ "%10u %10u %10u %10u %10u %10u"
+ "%@\n"
+ "%@ - %@\n"
+ "%@: %@"
+ "3\x14\x16"
+ "@\"NSNumber\""
+ "@36@0:8@16B24@28"
+ "AppEntities"
+ "B36@0:8@16@24B32"
+ "CannotProcessFromEmbUpdater1"
+ "CannotProcessFromEmbUpdater2"
+ "CannotProcessFromEmbUpdater3"
+ "Checksum mismatch, skipping event."
+ "EmbCountFromEmbCachedUpdater"
+ "Failed to deserialize donated JSON dictionary from Wallet"
+ "Failed to deserialize donated JSON dictionary from Wallet with error: %@"
+ "InvalidMaxSize!!!"
+ "Logging level updated to: %ld"
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
+ "SKGProcessor+EmbeddingsUtils#processorAttributesForRecord returning empty as _kMDItemNeedsEmbeddings=%@"
+ "SKGProcessor+EmbeddingsUtils#processorAttributesForRecord returning empty as _kMDItemNeedsPriority=%@"
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
+ "com.apple.spotlightknowledge.LoggingLevel"
+ "com.apple.spotlightknowledge.LoggingLevelChanged"
+ "com.apple.spotlightknowledge.logger"
+ "completeSuggestedEventsAttributes:"
+ "config.plist"
+ "copyDoubleValueFromRecord:key:"
+ "cs_mail"
+ "dataWithLength:"
+ "decorateTextContentWithDescription:isDescriptive:delimiter:"
+ "duration"
+ "enableAppEntities"
+ "enablePreExtractionScanning"
+ "eventType"
+ "geo.cache"
+ "geoPatternsResourcesURL"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeString"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt32"
+ "getDataTypeForParamType(paramType) == SKGActivityJournalDataTypeUInt64"
+ "getGenerationProgressReportForTypes:protectionClasses:reportHandler:completionHandler:"
+ "getProgressReportForProtectionClasses:processorFlags:reportHandler:completionHandler:"
+ "getStringFromParam"
+ "getUInt32FromParam"
+ "getUInt64FromParam"
+ "hasSuffix:"
+ "identifier"
+ "indexType"
+ "initWithBytes:length:encoding:"
+ "initWithDouble:"
+ "integerForKey:"
+ "invalid"
+ "isTextPersonExtractionAvailable"
+ "kMDItemAlbum"
+ "kMDItemArtist"
+ "kMDItemEpisode"
+ "kMDItemLatitude"
+ "kMDItemLinkName"
+ "kMDItemLinkType"
+ "kMDItemLongitude"
+ "kMDItemPodcastName"
+ "kMDItemURLDescription"
+ "keyphrase"
+ "keyphraseExcludeDomains"
+ "keyphraseOptionalExtractionAttributes"
+ "kind"
+ "markForProcessingSuggestedEventsAttributes:"
+ "maxKeyphraseCount"
+ "maxQueryUpdatesSize"
+ "mutableBytes"
+ "numberWithInt:"
+ "outcome"
+ "pid"
+ "protectionClasses"
+ "reindexExcludeBundles"
+ "setInteger:forKey:"
+ "setLoggingVerbosity:"
+ "setMaxKeyphraseCount:"
+ "setMaxQueryUpdatesSize:"
+ "shouldGenerateEmbeddingsForRecord:bundleID:skipFpRecordCheck:"
+ "size"
+ "suggestedEventsRecordNeedsProcessing:bundleID:isUpdate:hasTextContent:shouldClear:shouldMarkComplete:"
+ "synchronize"
+ "task"
+ "type"
+ "updateSKGProcessorSuggestedEventsAttributes:record:bundleID:protectionClass:recordHasText:itemHasText:isUpdate:"
+ "updateSKGReindexerSuggestedEventsAttributes:record:bundleID:itemHasText:"
+ "v16@?0r^{?=CQ@@}8"
+ "v20@0:8i16"
+ "v48@0:8@16@24@?32@?40"
+ "v48@0:8@16Q24@?32@?40"
- "\nTotal: embCountFromPriorityUpdater:%llu priorityCountFromPriorityUpdater:%llu skipCountFromPriorityUpdater:%llu \n"
- "### mismatch repeat event %d at offset %ld\n"
- "### mmap failed"
- "### unknown type %d at offset %ld\n"
- "%10u %10u %10u %10u %10u"
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
- "3\x14\x15"
- "@40@0:8@16Q24Q32"
- "CannotProcessFromEmbUpdater"
- "FileEntry"
- "Journal was reset at time %s, size before reset: %llu, size after reset: %llu "
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
