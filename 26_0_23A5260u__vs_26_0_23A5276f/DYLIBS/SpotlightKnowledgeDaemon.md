## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2374.0.1.0.0
-  __TEXT.__text: 0xceca8
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0x6ee4
-  __TEXT.__const: 0x6d8
-  __TEXT.__oslogstring: 0x7eed
-  __TEXT.__cstring: 0x7e77
-  __TEXT.__gcc_except_tab: 0x57bc
+2381.0.1.0.0
+  __TEXT.__text: 0xd85d0
+  __TEXT.__auth_stubs: 0x1ff0
+  __TEXT.__objc_methlist: 0x72a8
+  __TEXT.__const: 0xb40
+  __TEXT.__oslogstring: 0x8214
+  __TEXT.__cstring: 0x83a4
+  __TEXT.__gcc_except_tab: 0x5a18
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x2dc8
-  __TEXT.__objc_classname: 0xc76
-  __TEXT.__objc_methname: 0x102cb
-  __TEXT.__objc_methtype: 0x1a1d
-  __TEXT.__objc_stubs: 0xe0e0
-  __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__const: 0x2ef0
-  __DATA_CONST.__objc_classlist: 0x510
+  __TEXT.__swift5_typeref: 0x1ca
+  __TEXT.__swift5_fieldmd: 0x18c
+  __TEXT.__constg_swiftt: 0x300
+  __TEXT.__swift5_reflstr: 0x69
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__unwind_info: 0x30f8
+  __TEXT.__objc_classname: 0xd4d
+  __TEXT.__objc_methname: 0x10723
+  __TEXT.__objc_methtype: 0x1ac6
+  __TEXT.__objc_stubs: 0xe580
+  __DATA_CONST.__got: 0xb70
+  __DATA_CONST.__const: 0x3078
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4158
+  __DATA_CONST.__objc_selrefs: 0x4270
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x348
-  __DATA_CONST.__objc_arraydata: 0x780
-  __AUTH_CONST.__auth_got: 0xe50
-  __AUTH_CONST.__const: 0x1650
-  __AUTH_CONST.__cfstring: 0x8640
-  __AUTH_CONST.__objc_const: 0xcf70
-  __AUTH_CONST.__objc_intobj: 0x8e8
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x368
+  __DATA_CONST.__objc_arraydata: 0x7e8
+  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__const: 0x1ca8
+  __AUTH_CONST.__cfstring: 0x88e0
+  __AUTH_CONST.__objc_const: 0xd918
+  __AUTH_CONST.__objc_arrayobj: 0x600
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x32a0
-  __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x8b8
-  __DATA.__data: 0x7c0
-  __DATA.__bss: 0xeb8
+  __AUTH.__objc_data: 0x3540
+  __AUTH.__data: 0x248
+  __DATA.__objc_ivar: 0x8d0
+  __DATA.__data: 0xb80
+  __DATA.__bss: 0x10f0
   __DATA.__common: 0xc
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 91DC1E8C-6B86-369D-9D13-EFD6FC996F4F
-  Functions: 3684
-  Symbols:   12855
-  CStrings:  6363
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: 0F48ABBC-5747-3F9E-8655-098BD69CC590
+  Functions: 4024
+  Symbols:   13276
+  CStrings:  6503
 
Symbols:
+ +[SKDPipelineDescriptor descriptorFromSetDescription:processorNames:]
+ +[SKDPipelineManager sharedManager]
+ +[SKDPipelineManager sharedManager].cold.1
+ +[SKDPipelineQueryBuilder queryForItemsFromBundles:inverse:]
+ +[SKDPipelineQueryBuilder queryForItemsFromProtectionClasses:inverse:]
+ +[SKDPipelineQueryBuilder queryForItemsNeedingProcessingByPipelineWithName:inverse:]
+ +[SKDPipelineQueryBuilder queryForItemsProcessedByPipelineWithName:inverse:]
+ +[SKDPipelineQueryBuilder queryForValidItems]
+ +[SKDRecordProcessorCache sharedCache]
+ +[SKDRecordProcessorCache sharedCache].cold.1
+ -[CSEventListenerManager _processJournalsWithProcessedJournalsCount:completionHandler:]
+ -[CSEventListenerManager _processJournalsWithProcessedJournalsCount:completionHandler:].cold.1
+ -[CSEventListenerManager deleteFirstJournal:]
+ -[CSEventListenerManager deleteFirstJournal:].cold.1
+ -[CSEventListenerManager purgeJournalsProactive]
+ -[CSEventListenerManager setSignposter:]
+ -[CSEventListenerManager setTotalJournalSize:]
+ -[CSEventListenerManager signposter]
+ -[CSEventListenerManager totalJournalSize]
+ -[CSEventListenerManagerDefaultSignposter beginProcessJournalsInterval]
+ -[CSEventListenerManagerDefaultSignposter endProcessJournalsIntervalWithSignpostID:stopReason:indexType:taskName:processedJournalsCount:journalQueueCount:]
+ -[CSJournalProcessor journal_file_size]
+ -[CSJournalProcessor setJournal_file_size:]
+ -[CSJournalProcessor setupFromSpotlightDaemonJournalWithParentFd:spotlightBasePath:].cold.3
+ -[CSJournalProcessor setupFromTopLevelJournalWithParentFd:journalBasePath:].cold.3
+ -[CSJournalProcessor setupWithParentFd:name:].cold.1
+ -[CSProcessorPipelineJobUpdater .cxx_destruct]
+ -[CSProcessorPipelineJobUpdater config]
+ -[CSProcessorPipelineJobUpdater description]
+ -[CSProcessorPipelineJobUpdater eventFlags]
+ -[CSProcessorPipelineJobUpdater eventType]
+ -[CSProcessorPipelineJobUpdater excludeBundleIDs]
+ -[CSProcessorPipelineJobUpdater excludeContentTypes]
+ -[CSProcessorPipelineJobUpdater handleDeletion:turboEnabled:completionHandler:cancelBlock:]
+ -[CSProcessorPipelineJobUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]
+ -[CSProcessorPipelineJobUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:].cold.1
+ -[CSProcessorPipelineJobUpdater includeBundleIDs]
+ -[CSProcessorPipelineJobUpdater includeContentTypes]
+ -[CSProcessorPipelineJobUpdater initWithJournalJob:]
+ -[CSProcessorPipelineJobUpdater isAcceptingJournals]
+ -[CSProcessorPipelineJobUpdater shouldHandleJournalItem:bundleID:]
+ -[CSProcessorPipelineJobUpdater supportsCSIndexType:]
+ -[CSProcessorPipelineJobUpdater taskConfig]
+ -[CSProcessorPipelineJobUpdater taskName]
+ -[NSDictionary(BundleProgressReport) bundleProgressNumerator:denominator:]
+ -[NSDictionary(BundleProgressReport) featureCheckpointForProgress]
+ -[SKDBaseCSItemProcessingJob .cxx_destruct]
+ -[SKDBaseCSItemProcessingJob processItemWithRecord:uniqueID:bundleID:]
+ -[SKDBaseCSItemProcessingJob updateAttributeSet:forPipeline:withAttributes:]
+ -[SKDBaseCSItemProcessingJob(Testing) itemProcessor]
+ -[SKDBaseCSItemProcessingJob(Testing) setItemProcessor:]
+ -[SKDBaseCSQueryProcessingJob .cxx_destruct]
+ -[SKDBaseCSQueryProcessingJob configure]
+ -[SKDBaseCSQueryProcessingJob fetchAttributes]
+ -[SKDBaseCSQueryProcessingJob initWithName:version:pipelines:]
+ -[SKDBaseCSQueryProcessingJob pipelineQueries]
+ -[SKDBaseCSQueryProcessingJob queryContext]
+ -[SKDBaseCSQueryProcessingJob queryString]
+ -[SKDBaseCSQueryProcessingJob query]
+ -[SKDBaseCSQueryProcessingJob setFetchAttributes:]
+ -[SKDBaseCSQueryProcessingJob setPipelineQueries:]
+ -[SKDBaseCSQueryProcessingJob setQueryString:queryContext:query:]
+ -[SKDBaseCSQueryProcessingJob supportedQueryForPipeline:]
+ -[SKDBaseItemProcessingJob processItemWithRecord:uniqueID:bundleID:]
+ -[SKDBaseJob .cxx_destruct]
+ -[SKDBaseJob initWithName:version:pipelines:]
+ -[SKDBaseJob name]
+ -[SKDBaseJob pipelines]
+ -[SKDBaseJob version]
+ -[SKDBreadcrumbProcessor .cxx_destruct]
+ -[SKDBreadcrumbProcessor detector]
+ -[SKDBreadcrumbProcessor initWithDataDetector:listener:]
+ -[SKDBreadcrumbProcessor init]
+ -[SKDBreadcrumbProcessor listener]
+ -[SKDBreadcrumbProcessor load]
+ -[SKDBreadcrumbProcessor maxEntityCount]
+ -[SKDBreadcrumbProcessor optionalAttributes]
+ -[SKDBreadcrumbProcessor processRecord:bundleID:]
+ -[SKDBreadcrumbProcessor processedAttributes]
+ -[SKDBreadcrumbProcessor processedAttributes].cold.1
+ -[SKDBreadcrumbProcessor requiredAttributes]
+ -[SKDBreadcrumbProcessor requiredAttributes].cold.1
+ -[SKDBreadcrumbProcessor willProcessRecord:bundleID:]
+ -[SKDCSItemProcessor enumerateRecordsForRecord:bundleID:usingBlock:]
+ -[SKDCSItemProcessor markCompleteWithPipeline:recordUpdate:]
+ -[SKDCSItemProcessor processItemWithRecord:uniqueID:bundleID:]
+ -[SKDCSItemUpdate .cxx_destruct]
+ -[SKDCSItemUpdate initWithItem:]
+ -[SKDCSItemUpdate item]
+ -[SKDEmbeddingProcessor .cxx_destruct]
+ -[SKDEmbeddingProcessor initWithProcessor:]
+ -[SKDEmbeddingProcessor init]
+ -[SKDEmbeddingProcessor load]
+ -[SKDEmbeddingProcessor optionalAttributes]
+ -[SKDEmbeddingProcessor processRecord:bundleID:]
+ -[SKDEmbeddingProcessor processedAttributes]
+ -[SKDEmbeddingProcessor processedAttributes].cold.1
+ -[SKDEmbeddingProcessor requiredAttributes]
+ -[SKDEmbeddingProcessor requiredAttributes].cold.1
+ -[SKDEmbeddingProcessor willProcessRecord:bundleID:]
+ -[SKDIndexProcessingJob configure]
+ -[SKDIndexProcessingJob supportedQueryForPipeline:]
+ -[SKDItemProcessor .cxx_destruct]
+ -[SKDItemProcessor enumerateRecordsForRecord:bundleID:usingBlock:]
+ -[SKDItemProcessor fetchAttributes]
+ -[SKDItemProcessor initWithPipelines:recordCache:]
+ -[SKDItemProcessor pipelines]
+ -[SKDItemProcessor processItemWithRecord:filePath:]
+ -[SKDItemProcessor processItemWithRecord:uniqueID:bundleID:]
+ -[SKDItemProcessor recordCache]
+ -[SKDItemProcessor resume]
+ -[SKDItemProcessor setFetchAttributes:]
+ -[SKDItemProcessor suspend]
+ -[SKDItemUpdate .cxx_destruct]
+ -[SKDItemUpdate addEntriesFromDictionary:]
+ -[SKDItemUpdate addEntryForAttribute:value:]
+ -[SKDItemUpdate attributes]
+ -[SKDItemUpdate init]
+ -[SKDItemUpdate setStatus:]
+ -[SKDItemUpdate status]
+ -[SKDJournalItemProcessor markCompleteWithPipeline:recordUpdate:]
+ -[SKDJournalProcessingJob .cxx_destruct]
+ -[SKDJournalProcessingJob bgstOptions]
+ -[SKDJournalProcessingJob excludedBundleIDs]
+ -[SKDJournalProcessingJob fetchAttributes]
+ -[SKDJournalProcessingJob initWithName:version:pipelines:]
+ -[SKDJournalProcessingJob initWithName:version:pipelines:].cold.1
+ -[SKDJournalProcessingJob requiredAttributes]
+ -[SKDJournalProcessingJob requiredBundleIDs]
+ -[SKDKeyphraseProcessor .cxx_destruct]
+ -[SKDKeyphraseProcessor initWithListener:]
+ -[SKDKeyphraseProcessor init]
+ -[SKDKeyphraseProcessor listener]
+ -[SKDKeyphraseProcessor load]
+ -[SKDKeyphraseProcessor maxEntityCount]
+ -[SKDKeyphraseProcessor optionalAttributes]
+ -[SKDKeyphraseProcessor processRecord:bundleID:]
+ -[SKDKeyphraseProcessor processedAttributes]
+ -[SKDKeyphraseProcessor processedAttributes].cold.1
+ -[SKDKeyphraseProcessor requiredAttributes]
+ -[SKDKeyphraseProcessor requiredAttributes].cold.1
+ -[SKDKeyphraseProcessor willProcessRecord:bundleID:]
+ -[SKDLanguageProcessor .cxx_destruct]
+ -[SKDLanguageProcessor initWithLanguageIdentifier:listener:]
+ -[SKDLanguageProcessor init]
+ -[SKDLanguageProcessor languageIdentifier]
+ -[SKDLanguageProcessor listener]
+ -[SKDLanguageProcessor load]
+ -[SKDLanguageProcessor optionalAttributes]
+ -[SKDLanguageProcessor processRecord:bundleID:]
+ -[SKDLanguageProcessor processedAttributes]
+ -[SKDLanguageProcessor processedAttributes].cold.1
+ -[SKDLanguageProcessor requiredAttributes]
+ -[SKDLanguageProcessor requiredAttributes].cold.1
+ -[SKDLanguageProcessor willProcessRecord:bundleID:]
+ -[SKDLocationProcessor .cxx_destruct]
+ -[SKDLocationProcessor detector]
+ -[SKDLocationProcessor initWithDataDetector:listener:]
+ -[SKDLocationProcessor init]
+ -[SKDLocationProcessor listener]
+ -[SKDLocationProcessor load]
+ -[SKDLocationProcessor maxEntityCount]
+ -[SKDLocationProcessor optionalAttributes]
+ -[SKDLocationProcessor processRecord:bundleID:]
+ -[SKDLocationProcessor processedAttributes]
+ -[SKDLocationProcessor processedAttributes].cold.1
+ -[SKDLocationProcessor requiredAttributes]
+ -[SKDLocationProcessor requiredAttributes].cold.1
+ -[SKDLocationProcessor willProcessRecord:bundleID:]
+ -[SKDPipeline .cxx_destruct]
+ -[SKDPipeline canRun]
+ -[SKDPipeline description]
+ -[SKDPipeline descriptor]
+ -[SKDPipeline errorAttribute]
+ -[SKDPipeline fetchAttributes]
+ -[SKDPipeline initWithDescriptor:processors:]
+ -[SKDPipeline needsProcessingAttribute]
+ -[SKDPipeline processedAttributes]
+ -[SKDPipeline processors]
+ -[SKDPipeline requiredAttributes]
+ -[SKDPipeline setCanRun:]
+ -[SKDPipeline supportedQuery]
+ -[SKDPipeline supportedSetQuery]
+ -[SKDPipeline supportsRecord:bundleID:]
+ -[SKDPipeline versionAttribute]
+ -[SKDPipeline versionValue]
+ -[SKDPipelineDescriptor .cxx_destruct]
+ -[SKDPipelineDescriptor description]
+ -[SKDPipelineDescriptor enabled]
+ -[SKDPipelineDescriptor excludedAttributes]
+ -[SKDPipelineDescriptor excludedBundles]
+ -[SKDPipelineDescriptor excludedProtectionClasses]
+ -[SKDPipelineDescriptor initWithSetDescription:processorNames:]
+ -[SKDPipelineDescriptor name]
+ -[SKDPipelineDescriptor processedAttributes]
+ -[SKDPipelineDescriptor processorNames]
+ -[SKDPipelineDescriptor requiredAttributes]
+ -[SKDPipelineDescriptor requiredBundles]
+ -[SKDPipelineDescriptor requiredProtectionClasses]
+ -[SKDPipelineDescriptor setDescription]
+ -[SKDPipelineDescriptor version]
+ -[SKDPipelineManager .cxx_destruct]
+ -[SKDPipelineManager cleanupJob]
+ -[SKDPipelineManager indexProcessingJobWithProtectionClasses:]
+ -[SKDPipelineManager indexProcessingJobWithProtectionClasses:].cold.1
+ -[SKDPipelineManager journalProcessingJobs]
+ -[SKDPipelineManager reindexJob]
+ -[SKDPipelineManager reportingJob]
+ -[SKDPipelineManager resetJob]
+ -[SKDPipelineManager(Testing) initWithDescriptors:processorCache:]
+ -[SKDPipelineManager(Testing) pipelineForName:]
+ -[SKDPipelineManager(Testing) pipelines]
+ -[SKDPipelineSetDescription .cxx_destruct]
+ -[SKDPipelineSetDescription description]
+ -[SKDPipelineSetDescription enabled]
+ -[SKDPipelineSetDescription excludedAttributes]
+ -[SKDPipelineSetDescription excludedBundles]
+ -[SKDPipelineSetDescription excludedProtectionClasses]
+ -[SKDPipelineSetDescription initWithName:version:]
+ -[SKDPipelineSetDescription name]
+ -[SKDPipelineSetDescription processedAttributes]
+ -[SKDPipelineSetDescription requiredAttributes]
+ -[SKDPipelineSetDescription requiredBundles]
+ -[SKDPipelineSetDescription requiredProtectionClasses]
+ -[SKDPipelineSetDescription setEnabled:]
+ -[SKDPipelineSetDescription setExcludedAttributes:]
+ -[SKDPipelineSetDescription setExcludedBundles:]
+ -[SKDPipelineSetDescription setExcludedProtectionClasses:]
+ -[SKDPipelineSetDescription setProcessedAttributes:]
+ -[SKDPipelineSetDescription setRequiredAttributes:]
+ -[SKDPipelineSetDescription setRequiredBundles:]
+ -[SKDPipelineSetDescription setRequiredProtectionClasses:]
+ -[SKDPipelineSetDescription version]
+ -[SKDRecordCache .cxx_destruct]
+ -[SKDRecordCache addEntriesFromAttributes:]
+ -[SKDRecordCache addEntryForAttribute:value:]
+ -[SKDRecordCache cacheForRecord:]
+ -[SKDRecordCache init]
+ -[SKDRecordCache objectForKey:]
+ -[SKDRecordProcessor .cxx_destruct]
+ -[SKDRecordProcessor enabled]
+ -[SKDRecordProcessor fetchedAttributes]
+ -[SKDRecordProcessor initWithName:]
+ -[SKDRecordProcessor init]
+ -[SKDRecordProcessor load]
+ -[SKDRecordProcessor marker]
+ -[SKDRecordProcessor name]
+ -[SKDRecordProcessor optionalAttributes]
+ -[SKDRecordProcessor processRecord:bundleID:]
+ -[SKDRecordProcessor processedAttributes]
+ -[SKDRecordProcessor queue]
+ -[SKDRecordProcessor requiredAttributes]
+ -[SKDRecordProcessor resume]
+ -[SKDRecordProcessor setEnabled:]
+ -[SKDRecordProcessor suspend]
+ -[SKDRecordProcessor suspended]
+ -[SKDRecordProcessor willProcessRecord:bundleID:]
+ -[SKDRecordProcessorCache .cxx_destruct]
+ -[SKDRecordProcessorCache init]
+ -[SKDRecordProcessorCache processorWithName:]
+ -[SKDRecordProcessorCache processorsWithNames:]
+ -[SKDRecordUpdate .cxx_destruct]
+ -[SKDRecordUpdate addAttributeForKey:value:]
+ -[SKDRecordUpdate addAttributesFromDictionary:]
+ -[SKDRecordUpdate attributes]
+ -[SKDRecordUpdate error]
+ -[SKDRecordUpdate initWithStatus:]
+ -[SKDRecordUpdate setError:]
+ -[SKDRecordUpdate setStatus:]
+ -[SKDRecordUpdate status]
+ -[SKDTestProcessor initWithName:]
+ -[SKDTestProcessor optionalAttributes]
+ -[SKDTestProcessor processRecord:bundleID:]
+ -[SKDTestProcessor processedAttributes]
+ -[SKDTestProcessor requiredAttributes]
+ -[SKDTestProcessor requiredAttributes].cold.1
+ -[SKDTestProcessor willProcessRecord:bundleID:]
+ -[SKGJob(Pipeline) _coreSpotlightIndexWithBundleIdentifier:protectionClass:]
+ -[SKGJob(Pipeline) _runCSPollingQuery:foundItemBlock:]
+ -[SKGJob(Pipeline) _updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:]
+ -[SKGJob(Pipeline) _updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:].cold.1
+ -[SKGJob(Pipeline) performCSIndexProcessingJob:cancelBlock:]
+ GCC_except_table198
+ GCC_except_table26
+ GCC_except_table61
+ _MDItemSnippet
+ _OBJC_CLASS_$_CSEventListenerManagerDefaultSignposter
+ _OBJC_CLASS_$_CSProcessorPipelineJobUpdater
+ _OBJC_CLASS_$_SKDBaseCSItemProcessingJob
+ _OBJC_CLASS_$_SKDBaseCSQueryProcessingJob
+ _OBJC_CLASS_$_SKDBaseItemProcessingJob
+ _OBJC_CLASS_$_SKDBaseItemUpdate
+ _OBJC_CLASS_$_SKDBaseJob
+ _OBJC_CLASS_$_SKDBreadcrumbProcessor
+ _OBJC_CLASS_$_SKDCSItemProcessor
+ _OBJC_CLASS_$_SKDCSItemUpdate
+ _OBJC_CLASS_$_SKDEmbeddingProcessor
+ _OBJC_CLASS_$_SKDIndexProcessingJob
+ _OBJC_CLASS_$_SKDItemProcessor
+ _OBJC_CLASS_$_SKDItemUpdate
+ _OBJC_CLASS_$_SKDJournalItemProcessor
+ _OBJC_CLASS_$_SKDJournalProcessingJob
+ _OBJC_CLASS_$_SKDKeyphraseProcessor
+ _OBJC_CLASS_$_SKDLanguageProcessor
+ _OBJC_CLASS_$_SKDLocationProcessor
+ _OBJC_CLASS_$_SKDPipeline
+ _OBJC_CLASS_$_SKDPipelineDescriptor
+ _OBJC_CLASS_$_SKDPipelineManager
+ _OBJC_CLASS_$_SKDPipelineQueryBuilder
+ _OBJC_CLASS_$_SKDPipelineSetDescription
+ _OBJC_CLASS_$_SKDQuery
+ _OBJC_CLASS_$_SKDRecordCache
+ _OBJC_CLASS_$_SKDRecordProcessor
+ _OBJC_CLASS_$_SKDRecordProcessorCache
+ _OBJC_CLASS_$_SKDRecordUpdate
+ _OBJC_CLASS_$_SKDTestProcessor
+ _OBJC_IVAR_$_CSEventListenerManager._signposter
+ _OBJC_IVAR_$_CSEventListenerManager._totalJournalSize
+ _OBJC_IVAR_$_CSJournalProcessor._journal_file_size
+ _OBJC_IVAR_$_CSProcessorPipelineJobUpdater._event
+ _OBJC_IVAR_$_CSProcessorPipelineJobUpdater._job
+ _OBJC_IVAR_$_CSProcessorPipelineJobUpdater._taskConfig
+ _OBJC_IVAR_$_SKDBaseCSItemProcessingJob._processor
+ _OBJC_IVAR_$_SKDBaseCSQueryProcessingJob._fetchAttributes
+ _OBJC_IVAR_$_SKDBaseCSQueryProcessingJob._pipelineQueries
+ _OBJC_IVAR_$_SKDBaseCSQueryProcessingJob._query
+ _OBJC_IVAR_$_SKDBaseCSQueryProcessingJob._queryContext
+ _OBJC_IVAR_$_SKDBaseCSQueryProcessingJob._queryString
+ _OBJC_IVAR_$_SKDBaseJob._name
+ _OBJC_IVAR_$_SKDBaseJob._pipelines
+ _OBJC_IVAR_$_SKDBaseJob._version
+ _OBJC_IVAR_$_SKDBreadcrumbProcessor._detector
+ _OBJC_IVAR_$_SKDBreadcrumbProcessor._listener
+ _OBJC_IVAR_$_SKDCSItemUpdate._item
+ _OBJC_IVAR_$_SKDEmbeddingProcessor._processor
+ _OBJC_IVAR_$_SKDItemProcessor._fetchAttributes
+ _OBJC_IVAR_$_SKDItemProcessor._pipelines
+ _OBJC_IVAR_$_SKDItemProcessor._recordCache
+ _OBJC_IVAR_$_SKDItemUpdate._attributes
+ _OBJC_IVAR_$_SKDItemUpdate._status
+ _OBJC_IVAR_$_SKDJournalProcessingJob._bgstOptions
+ _OBJC_IVAR_$_SKDJournalProcessingJob._excludedBundleIDs
+ _OBJC_IVAR_$_SKDJournalProcessingJob._fetchAttributes
+ _OBJC_IVAR_$_SKDJournalProcessingJob._requiredAttributes
+ _OBJC_IVAR_$_SKDJournalProcessingJob._requiredBundleIDs
+ _OBJC_IVAR_$_SKDKeyphraseProcessor._listener
+ _OBJC_IVAR_$_SKDLanguageProcessor._langIdentifier
+ _OBJC_IVAR_$_SKDLanguageProcessor._listener
+ _OBJC_IVAR_$_SKDLocationProcessor._detector
+ _OBJC_IVAR_$_SKDLocationProcessor._listener
+ _OBJC_IVAR_$_SKDPipeline._canRun
+ _OBJC_IVAR_$_SKDPipeline._descriptor
+ _OBJC_IVAR_$_SKDPipeline._processors
+ _OBJC_IVAR_$_SKDPipelineDescriptor._processorNames
+ _OBJC_IVAR_$_SKDPipelineDescriptor._setDescription
+ _OBJC_IVAR_$_SKDPipelineManager._pipelines
+ _OBJC_IVAR_$_SKDPipelineManager._processorCache
+ _OBJC_IVAR_$_SKDPipelineSetDescription._enabled
+ _OBJC_IVAR_$_SKDPipelineSetDescription._excludedAttributes
+ _OBJC_IVAR_$_SKDPipelineSetDescription._excludedBundles
+ _OBJC_IVAR_$_SKDPipelineSetDescription._excludedProtectionClasses
+ _OBJC_IVAR_$_SKDPipelineSetDescription._name
+ _OBJC_IVAR_$_SKDPipelineSetDescription._processedAttributes
+ _OBJC_IVAR_$_SKDPipelineSetDescription._requiredAttributes
+ _OBJC_IVAR_$_SKDPipelineSetDescription._requiredBundles
+ _OBJC_IVAR_$_SKDPipelineSetDescription._requiredProtectionClasses
+ _OBJC_IVAR_$_SKDPipelineSetDescription._version
+ _OBJC_IVAR_$_SKDRecordCache._cache
+ _OBJC_IVAR_$_SKDRecordProcessor._is_enabled
+ _OBJC_IVAR_$_SKDRecordProcessor._is_suspended
+ _OBJC_IVAR_$_SKDRecordProcessor._marker
+ _OBJC_IVAR_$_SKDRecordProcessor._name
+ _OBJC_IVAR_$_SKDRecordProcessor._queue
+ _OBJC_IVAR_$_SKDRecordProcessorCache._cache
+ _OBJC_IVAR_$_SKDRecordUpdate._attributes
+ _OBJC_IVAR_$_SKDRecordUpdate._error
+ _OBJC_IVAR_$_SKDRecordUpdate._status
+ _OBJC_METACLASS_$_CSEventListenerManagerDefaultSignposter
+ _OBJC_METACLASS_$_CSProcessorPipelineJobUpdater
+ _OBJC_METACLASS_$_SKDBaseCSItemProcessingJob
+ _OBJC_METACLASS_$_SKDBaseCSQueryProcessingJob
+ _OBJC_METACLASS_$_SKDBaseItemProcessingJob
+ _OBJC_METACLASS_$_SKDBaseItemUpdate
+ _OBJC_METACLASS_$_SKDBaseJob
+ _OBJC_METACLASS_$_SKDBreadcrumbProcessor
+ _OBJC_METACLASS_$_SKDCSItemProcessor
+ _OBJC_METACLASS_$_SKDCSItemUpdate
+ _OBJC_METACLASS_$_SKDEmbeddingProcessor
+ _OBJC_METACLASS_$_SKDIndexProcessingJob
+ _OBJC_METACLASS_$_SKDItemProcessor
+ _OBJC_METACLASS_$_SKDItemUpdate
+ _OBJC_METACLASS_$_SKDJournalItemProcessor
+ _OBJC_METACLASS_$_SKDJournalProcessingJob
+ _OBJC_METACLASS_$_SKDKeyphraseProcessor
+ _OBJC_METACLASS_$_SKDLanguageProcessor
+ _OBJC_METACLASS_$_SKDLocationProcessor
+ _OBJC_METACLASS_$_SKDPipeline
+ _OBJC_METACLASS_$_SKDPipelineDescriptor
+ _OBJC_METACLASS_$_SKDPipelineManager
+ _OBJC_METACLASS_$_SKDPipelineQueryBuilder
+ _OBJC_METACLASS_$_SKDPipelineSetDescription
+ _OBJC_METACLASS_$_SKDQuery
+ _OBJC_METACLASS_$_SKDRecordCache
+ _OBJC_METACLASS_$_SKDRecordProcessor
+ _OBJC_METACLASS_$_SKDRecordProcessorCache
+ _OBJC_METACLASS_$_SKDRecordUpdate
+ _OBJC_METACLASS_$_SKDTestProcessor
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _SKDItemAttributeTextContentEntityRanges
+ _SKGDaemonMain.cold.2
+ _SKGDaemonMain.cold.3
+ __DATA_SKDQuery
+ __INSTANCE_METHODS__TtC24SpotlightKnowledgeDaemon17_SKDQueryConcrete
+ __IVARS__TtC24SpotlightKnowledgeDaemon17_SKDQueryConcrete
+ __METACLASS_DATA_SKDQuery
+ __OBJC_$_CLASS_METHODS_SKDBreadcrumbProcessor(SpotlightKnowledgeDaemon)
+ __OBJC_$_CLASS_METHODS_SKDPipelineDescriptor
+ __OBJC_$_CLASS_METHODS_SKDPipelineManager
+ __OBJC_$_CLASS_METHODS_SKDPipelineQueryBuilder
+ __OBJC_$_CLASS_METHODS_SKDRecordProcessorCache
+ __OBJC_$_INSTANCE_METHODS_CSEventListenerManagerDefaultSignposter
+ __OBJC_$_INSTANCE_METHODS_CSProcessorPipelineJobUpdater
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(SKGQueryRecordValidation|SKGJournalRecordValidation|BundleProgressReport)
+ __OBJC_$_INSTANCE_METHODS_SKDBaseCSItemProcessingJob(Testing)
+ __OBJC_$_INSTANCE_METHODS_SKDBaseCSQueryProcessingJob
+ __OBJC_$_INSTANCE_METHODS_SKDBaseItemProcessingJob
+ __OBJC_$_INSTANCE_METHODS_SKDBaseJob
+ __OBJC_$_INSTANCE_METHODS_SKDBreadcrumbProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDCSItemProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDCSItemUpdate
+ __OBJC_$_INSTANCE_METHODS_SKDEmbeddingProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDIndexProcessingJob
+ __OBJC_$_INSTANCE_METHODS_SKDItemProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDItemUpdate
+ __OBJC_$_INSTANCE_METHODS_SKDJournalItemProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDJournalProcessingJob
+ __OBJC_$_INSTANCE_METHODS_SKDKeyphraseProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDLanguageProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDLocationProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDPipeline
+ __OBJC_$_INSTANCE_METHODS_SKDPipelineDescriptor
+ __OBJC_$_INSTANCE_METHODS_SKDPipelineManager(Testing)
+ __OBJC_$_INSTANCE_METHODS_SKDPipelineSetDescription
+ __OBJC_$_INSTANCE_METHODS_SKDQuery(SpotlightKnowledgeDaemon)
+ __OBJC_$_INSTANCE_METHODS_SKDRecordCache
+ __OBJC_$_INSTANCE_METHODS_SKDRecordProcessor
+ __OBJC_$_INSTANCE_METHODS_SKDRecordProcessorCache
+ __OBJC_$_INSTANCE_METHODS_SKDRecordUpdate
+ __OBJC_$_INSTANCE_METHODS_SKDTestProcessor
+ __OBJC_$_INSTANCE_METHODS_SKGJob(People|Pipeline|Updates)
+ __OBJC_$_INSTANCE_VARIABLES_CSProcessorPipelineJobUpdater
+ __OBJC_$_INSTANCE_VARIABLES_SKDBaseCSItemProcessingJob
+ __OBJC_$_INSTANCE_VARIABLES_SKDBaseCSQueryProcessingJob
+ __OBJC_$_INSTANCE_VARIABLES_SKDBaseJob
+ __OBJC_$_INSTANCE_VARIABLES_SKDBreadcrumbProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDCSItemUpdate
+ __OBJC_$_INSTANCE_VARIABLES_SKDEmbeddingProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDItemProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDItemUpdate
+ __OBJC_$_INSTANCE_VARIABLES_SKDJournalProcessingJob
+ __OBJC_$_INSTANCE_VARIABLES_SKDKeyphraseProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDLanguageProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDLocationProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDPipeline
+ __OBJC_$_INSTANCE_VARIABLES_SKDPipelineDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_SKDPipelineManager
+ __OBJC_$_INSTANCE_VARIABLES_SKDPipelineSetDescription
+ __OBJC_$_INSTANCE_VARIABLES_SKDRecordCache
+ __OBJC_$_INSTANCE_VARIABLES_SKDRecordProcessor
+ __OBJC_$_INSTANCE_VARIABLES_SKDRecordProcessorCache
+ __OBJC_$_INSTANCE_VARIABLES_SKDRecordUpdate
+ __OBJC_$_PROP_LIST_CSEventListenerManagerDefaultSignposter
+ __OBJC_$_PROP_LIST_CSProcessorPipelineJobUpdater
+ __OBJC_$_PROP_LIST_SKDBaseCSQueryProcessingJob
+ __OBJC_$_PROP_LIST_SKDBaseJob
+ __OBJC_$_PROP_LIST_SKDBreadcrumbProcessor
+ __OBJC_$_PROP_LIST_SKDCSItemUpdate
+ __OBJC_$_PROP_LIST_SKDItemProcessor
+ __OBJC_$_PROP_LIST_SKDItemUpdate
+ __OBJC_$_PROP_LIST_SKDJournalProcessingJob
+ __OBJC_$_PROP_LIST_SKDKeyphraseProcessor
+ __OBJC_$_PROP_LIST_SKDLanguageProcessor
+ __OBJC_$_PROP_LIST_SKDLocationProcessor
+ __OBJC_$_PROP_LIST_SKDPipeline
+ __OBJC_$_PROP_LIST_SKDPipelineDescriptor
+ __OBJC_$_PROP_LIST_SKDPipelineSetDescription
+ __OBJC_$_PROP_LIST_SKDRecordProcessor
+ __OBJC_$_PROP_LIST_SKDRecordProcessor.128
+ __OBJC_$_PROP_LIST_SKDRecordUpdate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEventListenerManagerSignposter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKDRecordProcessor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEventListenerManagerSignposter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKDRecordProcessor
+ __OBJC_$_PROTOCOL_REFS_CSEventListenerManagerSignposter
+ __OBJC_$_PROTOCOL_REFS_SKDRecordProcessor
+ __OBJC_CLASS_PROTOCOLS_$_CSEventListenerManagerDefaultSignposter
+ __OBJC_CLASS_PROTOCOLS_$_CSProcessorPipelineJobUpdater
+ __OBJC_CLASS_PROTOCOLS_$_SKDRecordProcessor
+ __OBJC_CLASS_RO_$_CSEventListenerManagerDefaultSignposter
+ __OBJC_CLASS_RO_$_CSProcessorPipelineJobUpdater
+ __OBJC_CLASS_RO_$_SKDBaseCSItemProcessingJob
+ __OBJC_CLASS_RO_$_SKDBaseCSQueryProcessingJob
+ __OBJC_CLASS_RO_$_SKDBaseItemProcessingJob
+ __OBJC_CLASS_RO_$_SKDBaseItemUpdate
+ __OBJC_CLASS_RO_$_SKDBaseJob
+ __OBJC_CLASS_RO_$_SKDBreadcrumbProcessor
+ __OBJC_CLASS_RO_$_SKDCSItemProcessor
+ __OBJC_CLASS_RO_$_SKDCSItemUpdate
+ __OBJC_CLASS_RO_$_SKDEmbeddingProcessor
+ __OBJC_CLASS_RO_$_SKDIndexProcessingJob
+ __OBJC_CLASS_RO_$_SKDItemProcessor
+ __OBJC_CLASS_RO_$_SKDItemUpdate
+ __OBJC_CLASS_RO_$_SKDJournalItemProcessor
+ __OBJC_CLASS_RO_$_SKDJournalProcessingJob
+ __OBJC_CLASS_RO_$_SKDKeyphraseProcessor
+ __OBJC_CLASS_RO_$_SKDLanguageProcessor
+ __OBJC_CLASS_RO_$_SKDLocationProcessor
+ __OBJC_CLASS_RO_$_SKDPipeline
+ __OBJC_CLASS_RO_$_SKDPipelineDescriptor
+ __OBJC_CLASS_RO_$_SKDPipelineManager
+ __OBJC_CLASS_RO_$_SKDPipelineQueryBuilder
+ __OBJC_CLASS_RO_$_SKDPipelineSetDescription
+ __OBJC_CLASS_RO_$_SKDRecordCache
+ __OBJC_CLASS_RO_$_SKDRecordProcessor
+ __OBJC_CLASS_RO_$_SKDRecordProcessorCache
+ __OBJC_CLASS_RO_$_SKDRecordUpdate
+ __OBJC_CLASS_RO_$_SKDTestProcessor
+ __OBJC_LABEL_PROTOCOL_$_CSEventListenerManagerSignposter
+ __OBJC_LABEL_PROTOCOL_$_SKDRecordProcessor
+ __OBJC_METACLASS_RO_$_CSEventListenerManagerDefaultSignposter
+ __OBJC_METACLASS_RO_$_CSProcessorPipelineJobUpdater
+ __OBJC_METACLASS_RO_$_SKDBaseCSItemProcessingJob
+ __OBJC_METACLASS_RO_$_SKDBaseCSQueryProcessingJob
+ __OBJC_METACLASS_RO_$_SKDBaseItemProcessingJob
+ __OBJC_METACLASS_RO_$_SKDBaseItemUpdate
+ __OBJC_METACLASS_RO_$_SKDBaseJob
+ __OBJC_METACLASS_RO_$_SKDBreadcrumbProcessor
+ __OBJC_METACLASS_RO_$_SKDCSItemProcessor
+ __OBJC_METACLASS_RO_$_SKDCSItemUpdate
+ __OBJC_METACLASS_RO_$_SKDEmbeddingProcessor
+ __OBJC_METACLASS_RO_$_SKDIndexProcessingJob
+ __OBJC_METACLASS_RO_$_SKDItemProcessor
+ __OBJC_METACLASS_RO_$_SKDItemUpdate
+ __OBJC_METACLASS_RO_$_SKDJournalItemProcessor
+ __OBJC_METACLASS_RO_$_SKDJournalProcessingJob
+ __OBJC_METACLASS_RO_$_SKDKeyphraseProcessor
+ __OBJC_METACLASS_RO_$_SKDLanguageProcessor
+ __OBJC_METACLASS_RO_$_SKDLocationProcessor
+ __OBJC_METACLASS_RO_$_SKDPipeline
+ __OBJC_METACLASS_RO_$_SKDPipelineDescriptor
+ __OBJC_METACLASS_RO_$_SKDPipelineManager
+ __OBJC_METACLASS_RO_$_SKDPipelineQueryBuilder
+ __OBJC_METACLASS_RO_$_SKDPipelineSetDescription
+ __OBJC_METACLASS_RO_$_SKDRecordCache
+ __OBJC_METACLASS_RO_$_SKDRecordProcessor
+ __OBJC_METACLASS_RO_$_SKDRecordProcessorCache
+ __OBJC_METACLASS_RO_$_SKDRecordUpdate
+ __OBJC_METACLASS_RO_$_SKDTestProcessor
+ __OBJC_PROTOCOL_$_CSEventListenerManagerSignposter
+ __OBJC_PROTOCOL_$_SKDRecordProcessor
+ __PROPERTIES__TtC24SpotlightKnowledgeDaemon17_SKDQueryConcrete
+ ___108-[SpotlightKnowledge processEmbeddingsReportWithJobContext:group:progressBlock:checkpointBlock:cancelBlock:]_block_invoke.194
+ ___108-[SpotlightKnowledge processEmbeddingsReportWithJobContext:group:progressBlock:checkpointBlock:cancelBlock:]_block_invoke.196
+ ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.318
+ ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.318.cold.1
+ ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.319
+ ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.319.cold.1
+ ___22-[SKGTaskAgent _setup]_block_invoke.147
+ ___22-[SKGTaskAgent _setup]_block_invoke.156
+ ___22-[SKGTaskAgent _setup]_block_invoke.163
+ ___22-[SKGTaskAgent _setup]_block_invoke.166
+ ___22-[SKGTaskAgent _setup]_block_invoke.169
+ ___22-[SKGTaskAgent _setup]_block_invoke.171
+ ___22-[SKGTaskAgent _setup]_block_invoke.177
+ ___22-[SKGTaskAgent _setup]_block_invoke.178
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.150
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.162
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.175
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.181
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.165
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.176
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.184
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.184.cold.1
+ ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.235
+ ___35+[SKDPipelineManager sharedManager]_block_invoke
+ ___38+[SKDRecordProcessorCache sharedCache]_block_invoke
+ ___38-[SKDTestProcessor requiredAttributes]_block_invoke
+ ___42-[SKDLanguageProcessor requiredAttributes]_block_invoke
+ ___42-[SKDLocationProcessor requiredAttributes]_block_invoke
+ ___43-[SKDEmbeddingProcessor requiredAttributes]_block_invoke
+ ___43-[SKDKeyphraseProcessor requiredAttributes]_block_invoke
+ ___43-[SKDLanguageProcessor processedAttributes]_block_invoke
+ ___43-[SKDLocationProcessor processedAttributes]_block_invoke
+ ___44-[SKDBreadcrumbProcessor requiredAttributes]_block_invoke
+ ___44-[SKDEmbeddingProcessor processedAttributes]_block_invoke
+ ___44-[SKDKeyphraseProcessor processedAttributes]_block_invoke
+ ___45-[SKDBreadcrumbProcessor processedAttributes]_block_invoke
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke_2
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke_3
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke_4
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke_5
+ ___47-[SKDLocationProcessor processRecord:bundleID:]_block_invoke_6
+ ___48-[SKDEmbeddingProcessor processRecord:bundleID:]_block_invoke
+ ___48-[SKDKeyphraseProcessor processRecord:bundleID:]_block_invoke
+ ___48-[SKDKeyphraseProcessor processRecord:bundleID:]_block_invoke.28
+ ___48-[SKDKeyphraseProcessor processRecord:bundleID:]_block_invoke.cold.1
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.170
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.179
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.189
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.173
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.182
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.176
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.185
+ ___49-[SKDBreadcrumbProcessor processRecord:bundleID:]_block_invoke
+ ___49-[SKDBreadcrumbProcessor processRecord:bundleID:]_block_invoke_2
+ ___54-[SKGJob(Pipeline) _runCSPollingQuery:foundItemBlock:]_block_invoke
+ ___54-[SKGJob(Pipeline) _runCSPollingQuery:foundItemBlock:]_block_invoke.10
+ ___54-[SKGJob(Pipeline) _runCSPollingQuery:foundItemBlock:]_block_invoke.cold.1
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.295
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.298
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.302
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.304
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.304.cold.1
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.306
+ ___60-[SKGJob(Pipeline) performCSIndexProcessingJob:cancelBlock:]_block_invoke
+ ___60-[SKGJob(Pipeline) performCSIndexProcessingJob:cancelBlock:]_block_invoke_2
+ ___62-[SKDCSItemProcessor processItemWithRecord:uniqueID:bundleID:]_block_invoke
+ ___62-[SKDCSItemProcessor processItemWithRecord:uniqueID:bundleID:]_block_invoke_2
+ ___62-[SKDPipelineManager indexProcessingJobWithProtectionClasses:]_block_invoke
+ ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke.267
+ ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke_2.268
+ ___67-[CSEventListenerManager handleMessage:basePath:withDispatchGroup:]_block_invoke.139
+ ___77-[SpotlightKnowledge processSuggestedEventsReportWithJobContext:cancelBlock:]_block_invoke.214
+ ___77-[SpotlightKnowledge processSuggestedEventsReportWithJobContext:cancelBlock:]_block_invoke_2.218
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.100
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.100.cold.1
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.34
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.74
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.87
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.99
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.99.cold.1
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.39
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.39.cold.1
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.39.cold.2
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.39.cold.3
+ ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.76
+ ___83-[SKGJob(Pipeline) _updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:]_block_invoke
+ ___83-[SKGJob(Pipeline) _updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:]_block_invoke.cold.1
+ ___83-[SpotlightKnowledge processDocumentUnderstandingReportWithJobContext:cancelBlock:]_block_invoke.236
+ ___83-[SpotlightKnowledge processDocumentUnderstandingReportWithJobContext:cancelBlock:]_block_invoke_2.240
+ ___87-[CSEventListenerManager _processJournalsWithProcessedJournalsCount:completionHandler:]_block_invoke
+ ___87-[CSEventListenerManager _processJournalsWithProcessedJournalsCount:completionHandler:]_block_invoke.119
+ ___87-[CSEventListenerManager _processJournalsWithProcessedJournalsCount:completionHandler:]_block_invoke.cold.1
+ ___91-[CSProcessorPipelineJobUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke
+ ___91-[CSProcessorPipelineJobUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.29
+ ___91-[CSProcessorPipelineJobUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.29.cold.1
+ ___block_descriptor_104_e8_32s40s48s56s64r72r80r88r_e5_v8?0ls32l8r64l8s40l8s48l8r72l8r80l8r88l8s56l8
+ ___block_descriptor_112_e8_32s40s48s56bs64bs72bs80r_e17_v16?0"NSError"8ls32l8s40l8r80l8s56l8s64l8s48l8s72l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72bs80r88r96r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8s48l8r80l8s56l8r88l8s64l8r96l8s72l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs104r112r_e26_B16?0"SKGProcessedItem"8lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r112l8s96l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80bs88bs96r104r_e25_B16?0?<v?"NSString">8ls32l8s40l8r96l8r104l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_145_e8_32s40s48s56s64s72s80s88bs96r104r112r120r128r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8s48l8r96l8s88l8r104l8s56l8r112l8s64l8r120l8s72l8s80l8r128l8
+ ___block_descriptor_153_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r136r_e25_B16?0?<v?"NSString">8ls32l8s40l8s48l8r104l8s96l8s56l8r112l8s64l8r120l8s72l8r128l8s80l8s88l8r136l8
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_32_e31_v16?0"BGRepeatingSystemTask"8l
+ ___block_descriptor_40_e8_32r_e31_B24?0"NSString"8"NSString"16lr32l8
+ ___block_descriptor_48_e8_32bs40r_e5_B8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e21_v24?0Q8"NSString"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e42_v32?0"NSDictionary"8"SKDPipeline"16^B24ls32l8s40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64r_e39_B24?0"NSString"8"CSSearchableItem"16ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e27_v28?0"NSString"8i16i20i24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r72w_e17_v16?0"NSArray"8lr48l8s40l8r56l8w72l8r64l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8r80l8
+ ___block_literal_global.12
+ ___block_literal_global.129
+ ___block_literal_global.138
+ ___block_literal_global.149
+ ___block_literal_global.150
+ ___block_literal_global.172
+ ___block_literal_global.175
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.187
+ ___block_literal_global.190
+ ___block_literal_global.193
+ ___block_literal_global.204
+ ___block_literal_global.211
+ ___block_literal_global.226
+ ___block_literal_global.249
+ ___block_literal_global.254
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.281
+ ___block_literal_global.296
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.31
+ ___block_literal_global.321
+ ___block_literal_global.338
+ ___block_literal_global.344
+ ___block_literal_global.68
+ ___block_literal_global.71
+ ___block_literal_global.94
+ ___getAllCSManagedIndexPathsFromConfig_block_invoke
+ ___handleEmbeddingsTask_block_invoke.330
+ ___handleKeyphrasesTask_block_invoke.334
+ ___handlePreExtractionTask_block_invoke.335
+ ___handlePriorityTask_block_invoke.333
+ ___handleQueryCleanupTask_block_invoke.269
+ ___handleQueryCleanupTask_block_invoke.270
+ ___handleQueryCleanupTask_block_invoke.271
+ ___handleQueryCleanupTask_block_invoke.272
+ ___handleQueryUpdatesTask_block_invoke.339
+ ___handleQueryUpdatesTask_block_invoke.340
+ ___handleQueryUpdatesTask_block_invoke.341
+ ___handleQueryUpdatesTask_block_invoke.342
+ ___setupQueryCleanupTasks_block_invoke.331
+ ___setupQueryUpdatesTasks_block_invoke.336
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy32_8
+ ___swift_memcpy40_8
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_reflection_version
+ ___unnamed_4
+ __swiftEmptyArrayStorage
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SpotlightKnowledgeDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SpotlightKnowledgeDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SpotlightKnowledgeDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SpotlightKnowledgeDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SpotlightKnowledgeDaemon
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SpotlightKnowledgeDaemon
+ __swift_stdlib_malloc_size
+ _associated conformance 24SpotlightKnowledgeDaemon5QueryO08NegationD0Vy_xGAA0D8ProtocolAA07NegatedD0AaGP_AaG
+ _associated conformance 24SpotlightKnowledgeDaemon5QueryO15AttributeEqualsVAA0D8ProtocolAA07NegatedD0AaFP_AaF
+ _associated conformance 24SpotlightKnowledgeDaemon5QueryO18AttributeNotEqualsVAA0D8ProtocolAA07NegatedD0AaFP_AaF
+ _associated conformance 24SpotlightKnowledgeDaemon5QueryO2OrVy_xGAA0D8ProtocolAA07NegatedD0AaGP_AaG
+ _associated conformance 24SpotlightKnowledgeDaemon5QueryO3AndVy_xGAA0D8ProtocolAA07NegatedD0AaGP_AaG
+ _associated conformance 24SpotlightKnowledgeDaemon8AnyQueryVAA0E8ProtocolAA07NegatedE0AaDP_AaD
+ _associated conformance So8SKDQueryC24SpotlightKnowledgeDaemon13QueryProtocolAC07NegatedE0AcDP_AcD
+ _getAllCSManagedIndexPathsFromConfig
+ _getMockDescriptors
+ _getSystemDefinedDescriptors
+ _getrlimit
+ _indexProcessingJobWithProtectionClasses:.onceToken
+ _indexProcessingJobWithProtectionClasses:.sIndexingIgnoreAttrs
+ _malloc_size
+ _objc_allocWithZone
+ _objc_msgSend$_processJournalsWithProcessedJournalsCount:completionHandler:
+ _objc_msgSend$_runCSPollingQuery:foundItemBlock:
+ _objc_msgSend$_updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:
+ _objc_msgSend$addAttributeForKey:value:
+ _objc_msgSend$addEntriesFromAttributes:
+ _objc_msgSend$addEntryForAttribute:value:
+ _objc_msgSend$beginProcessJournalsInterval
+ _objc_msgSend$bgstOptions
+ _objc_msgSend$bundleProgressNumerator:denominator:
+ _objc_msgSend$deleteFirstJournal:
+ _objc_msgSend$descriptorFromSetDescription:processorNames:
+ _objc_msgSend$enableMockPipeline
+ _objc_msgSend$endProcessJournalsIntervalWithSignpostID:stopReason:indexType:taskName:processedJournalsCount:journalQueueCount:
+ _objc_msgSend$errorAttribute
+ _objc_msgSend$excludedAttributes
+ _objc_msgSend$excludedBundleIDs
+ _objc_msgSend$featureCheckpointForProgress
+ _objc_msgSend$incrementAttributeValue:forKey:
+ _objc_msgSend$indexProcessingJobWithProtectionClasses:
+ _objc_msgSend$initWithDescriptor:processors:
+ _objc_msgSend$initWithDescriptors:processorCache:
+ _objc_msgSend$initWithItem:
+ _objc_msgSend$initWithJournalJob:
+ _objc_msgSend$initWithName:version:
+ _objc_msgSend$initWithName:version:pipelines:
+ _objc_msgSend$initWithPipelines:recordCache:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$item
+ _objc_msgSend$itemProcessor
+ _objc_msgSend$journalProcessingJobs
+ _objc_msgSend$journalSizeGetBelowLimit
+ _objc_msgSend$markCompleteWithPipeline:recordUpdate:
+ _objc_msgSend$maxJournalSizeInQueue
+ _objc_msgSend$needsProcessingAttribute
+ _objc_msgSend$optionalAttributes
+ _objc_msgSend$performCSIndexProcessingJob:cancelBlock:
+ _objc_msgSend$pipelineQueries
+ _objc_msgSend$pipelines
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$processItemWithRecord:uniqueID:bundleID:
+ _objc_msgSend$processorNames
+ _objc_msgSend$processorWithName:
+ _objc_msgSend$processorsWithNames:
+ _objc_msgSend$purgeJournalsProactive
+ _objc_msgSend$query
+ _objc_msgSend$queryContext
+ _objc_msgSend$queryForItemsNeedingProcessingByPipelineWithName:inverse:
+ _objc_msgSend$queryForItemsProcessedByPipelineWithName:inverse:
+ _objc_msgSend$recordCache
+ _objc_msgSend$referenceDateFor:
+ _objc_msgSend$requiredBundleIDs
+ _objc_msgSend$resume
+ _objc_msgSend$setExcludedBundles:
+ _objc_msgSend$setItemProcessor:
+ _objc_msgSend$setPipelineQueries:
+ _objc_msgSend$setPowerBudgeted:
+ _objc_msgSend$setProcessedAttributes:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$supportedQueryForPipeline:
+ _objc_msgSend$updateAttributeSet:forPipeline:withAttributes:
+ _objc_msgSend$versionAttribute
+ _objectdestroyTm
+ _requiredAttributes.sTestRequired
+ _setrlimit
+ _sharedCache.onceToken
+ _sharedCache.sRecordProcessorCache
+ _swift_allocBox
+ _swift_allocObject
+ _swift_allocateGenericClassMetadata
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_checkMetadataState
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getGenericMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTupleTypeMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initClassMetadata2
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_release
+ _swift_setDeallocating
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic $s24SpotlightKnowledgeDaemon9QueryListP
+ _symbolic 12NegatedQuery_____Qz 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic SS
+ _symbolic Say______pG 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic Say______pG 24SpotlightKnowledgeDaemon9QueryListP
+ _symbolic So8SKDQueryC
+ _symbolic _____ 24SpotlightKnowledgeDaemon10QueryArrayV
+ _symbolic _____ 24SpotlightKnowledgeDaemon10QueryTupleV
+ _symbolic _____ 24SpotlightKnowledgeDaemon12QueryBuilderO
+ _symbolic _____ 24SpotlightKnowledgeDaemon14EmptyQueryListV
+ _symbolic _____ 24SpotlightKnowledgeDaemon17_SKDQueryConcreteC
+ _symbolic _____ 24SpotlightKnowledgeDaemon20ConditionalQueryListO
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO08NegationD0V
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO15AttributeEqualsV
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO18AttributeNotEqualsV
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO2OrV
+ _symbolic _____ 24SpotlightKnowledgeDaemon5QueryO3AndV
+ _symbolic _____ 24SpotlightKnowledgeDaemon8AnyQueryV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic ______p 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySay______pGSSG s15LazyMapSequenceV 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic _____y_AAy_xGG 24SpotlightKnowledgeDaemon5QueryO08NegationD0V
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic _____y______y_xGG 24SpotlightKnowledgeDaemon5QueryO08NegationD0V AC2OrV
+ _symbolic _____y______y_xGG 24SpotlightKnowledgeDaemon5QueryO08NegationD0V AC3AndV
+ _symbolic _____y_____ySay______pGShySSGG_G s15FlattenSequenceV8IteratorV s07LazyMapB0V 24SpotlightKnowledgeDaemon13QueryProtocolP
+ _symbolic q_
+ _symbolic x
+ _symbolic xxQp_t
+ _type_layout_string 24SpotlightKnowledgeDaemon10QueryArrayV
+ _type_layout_string 24SpotlightKnowledgeDaemon5QueryO15AttributeEqualsV
+ _type_layout_string 24SpotlightKnowledgeDaemon8AnyQueryV
- +[SKGProcessingDescriptor descriptorFromSetDescription:processorNames:]
- +[SKGProcessingPipelineManager sharedManager]
- +[SKGProcessingPipelineManager sharedManager].cold.1
- +[SKGProcessingQueryBuilder queryForItemsFromBundles:inverse:]
- +[SKGProcessingQueryBuilder queryForItemsFromProtectionClasses:inverse:]
- +[SKGProcessingQueryBuilder queryForItemsNeedingProcessingByTaskWithName:inverse:]
- +[SKGProcessingQueryBuilder queryForItemsProcessedByTaskWithName:inverse:]
- +[SKGProcessingQueryBuilder queryForValidItems]
- -[CSEventListenerConfig setSupportsUpdatedItems:]
- -[CSEventListenerConfig setTrackingAttributes:]
- -[CSEventListenerConfig supportsUpdatedItems]
- -[CSEventListenerConfig trackingAttributes]
- -[CSEventListenerManager processJournals].cold.1
- -[CSProcessorTaskUpdater .cxx_destruct]
- -[CSProcessorTaskUpdater config]
- -[CSProcessorTaskUpdater description]
- -[CSProcessorTaskUpdater eventFlags]
- -[CSProcessorTaskUpdater eventType]
- -[CSProcessorTaskUpdater excludeBundleIDs]
- -[CSProcessorTaskUpdater excludeContentTypes]
- -[CSProcessorTaskUpdater handleDeletion:turboEnabled:completionHandler:cancelBlock:]
- -[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]
- -[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:].cold.1
- -[CSProcessorTaskUpdater includeBundleIDs]
- -[CSProcessorTaskUpdater includeContentTypes]
- -[CSProcessorTaskUpdater initWithTask:]
- -[CSProcessorTaskUpdater isAcceptingJournals]
- -[CSProcessorTaskUpdater shouldHandleJournalItem:bundleID:]
- -[CSProcessorTaskUpdater supportsCSIndexType:]
- -[CSProcessorTaskUpdater taskConfig]
- -[CSProcessorTaskUpdater taskName]
- -[SKGBreadcrumbProcessor .cxx_destruct]
- -[SKGBreadcrumbProcessor detector]
- -[SKGBreadcrumbProcessor initWithDataDetector:listener:]
- -[SKGBreadcrumbProcessor init]
- -[SKGBreadcrumbProcessor listener]
- -[SKGBreadcrumbProcessor load]
- -[SKGBreadcrumbProcessor maxEntityCount]
- -[SKGBreadcrumbProcessor processRecord:bundleID:]
- -[SKGBreadcrumbProcessor processedAttributes]
- -[SKGBreadcrumbProcessor processedAttributes].cold.1
- -[SKGBreadcrumbProcessor requiredAttributes]
- -[SKGBreadcrumbProcessor requiredAttributes].cold.1
- -[SKGBreadcrumbProcessor willProcessRecord:bundleID:]
- -[SKGEmbeddingProcessor .cxx_destruct]
- -[SKGEmbeddingProcessor initWithProcessor:]
- -[SKGEmbeddingProcessor init]
- -[SKGEmbeddingProcessor load]
- -[SKGEmbeddingProcessor processRecord:bundleID:]
- -[SKGEmbeddingProcessor processedAttributes]
- -[SKGEmbeddingProcessor processedAttributes].cold.1
- -[SKGEmbeddingProcessor requiredAttributes]
- -[SKGEmbeddingProcessor requiredAttributes].cold.1
- -[SKGEmbeddingProcessor willProcessRecord:bundleID:]
- -[SKGIndexProcessingJob configure]
- -[SKGIndexProcessingJob supportedQueryForTask:]
- -[SKGItemProcessor .cxx_destruct]
- -[SKGItemProcessor enabled]
- -[SKGItemProcessor fetchedAttributes]
- -[SKGItemProcessor initWithName:]
- -[SKGItemProcessor init]
- -[SKGItemProcessor load]
- -[SKGItemProcessor marker]
- -[SKGItemProcessor name]
- -[SKGItemProcessor processRecord:bundleID:]
- -[SKGItemProcessor processedAttributes]
- -[SKGItemProcessor requiredAttributes]
- -[SKGItemProcessor resume]
- -[SKGItemProcessor setEnabled:]
- -[SKGItemProcessor suspend]
- -[SKGItemProcessor suspended]
- -[SKGItemProcessor willProcessRecord:bundleID:]
- -[SKGJournalProcessingJob .cxx_destruct]
- -[SKGJournalProcessingJob bgstOptions]
- -[SKGKeyphraseProcessor .cxx_destruct]
- -[SKGKeyphraseProcessor initWithListener:]
- -[SKGKeyphraseProcessor init]
- -[SKGKeyphraseProcessor listener]
- -[SKGKeyphraseProcessor load]
- -[SKGKeyphraseProcessor maxEntityCount]
- -[SKGKeyphraseProcessor processRecord:bundleID:]
- -[SKGKeyphraseProcessor processedAttributes]
- -[SKGKeyphraseProcessor processedAttributes].cold.1
- -[SKGKeyphraseProcessor requiredAttributes]
- -[SKGKeyphraseProcessor requiredAttributes].cold.1
- -[SKGKeyphraseProcessor willProcessRecord:bundleID:]
- -[SKGLanguageProcessor .cxx_destruct]
- -[SKGLanguageProcessor initWithLanguageIdentifier:listener:]
- -[SKGLanguageProcessor init]
- -[SKGLanguageProcessor languageIdentifier]
- -[SKGLanguageProcessor listener]
- -[SKGLanguageProcessor load]
- -[SKGLanguageProcessor processRecord:bundleID:]
- -[SKGLanguageProcessor processedAttributes]
- -[SKGLanguageProcessor processedAttributes].cold.1
- -[SKGLanguageProcessor requiredAttributes]
- -[SKGLanguageProcessor requiredAttributes].cold.1
- -[SKGLanguageProcessor willProcessRecord:bundleID:]
- -[SKGLocationProcessor .cxx_destruct]
- -[SKGLocationProcessor detector]
- -[SKGLocationProcessor initWithDataDetector:listener:]
- -[SKGLocationProcessor init]
- -[SKGLocationProcessor listener]
- -[SKGLocationProcessor load]
- -[SKGLocationProcessor maxEntityCount]
- -[SKGLocationProcessor processRecord:bundleID:]
- -[SKGLocationProcessor processedAttributes]
- -[SKGLocationProcessor processedAttributes].cold.1
- -[SKGLocationProcessor requiredAttributes]
- -[SKGLocationProcessor requiredAttributes].cold.1
- -[SKGLocationProcessor willProcessRecord:bundleID:]
- -[SKGProcessedUpdate .cxx_destruct]
- -[SKGProcessedUpdate attributes]
- -[SKGProcessedUpdate error]
- -[SKGProcessedUpdate setAttributes:]
- -[SKGProcessedUpdate setError:]
- -[SKGProcessedUpdate setStatus:]
- -[SKGProcessedUpdate status]
- -[SKGProcessingDescriptor .cxx_destruct]
- -[SKGProcessingDescriptor description]
- -[SKGProcessingDescriptor excludedBundles]
- -[SKGProcessingDescriptor excludedProtectionClasses]
- -[SKGProcessingDescriptor initWithSetDescription:processorNames:]
- -[SKGProcessingDescriptor name]
- -[SKGProcessingDescriptor processorNames]
- -[SKGProcessingDescriptor requiredBundles]
- -[SKGProcessingDescriptor requiredProtectionClasses]
- -[SKGProcessingDescriptor setDescription]
- -[SKGProcessingDescriptor version]
- -[SKGProcessingJob .cxx_destruct]
- -[SKGProcessingJob initWithName:version:tasks:]
- -[SKGProcessingJob logger]
- -[SKGProcessingJob name]
- -[SKGProcessingJob tasks]
- -[SKGProcessingJob version]
- -[SKGProcessingPipelineManager .cxx_destruct]
- -[SKGProcessingPipelineManager cleanupJob]
- -[SKGProcessingPipelineManager indexProcessingJobWithProtectionClasses:]
- -[SKGProcessingPipelineManager journalProcessingJob]
- -[SKGProcessingPipelineManager reindexJob]
- -[SKGProcessingPipelineManager reportingJob]
- -[SKGProcessingPipelineManager resetJob]
- -[SKGProcessingPipelineManager(Testing) initWithTasks:processors:]
- -[SKGProcessingPipelineManager(Testing) taskForName:]
- -[SKGProcessingPipelineManager(Testing) tasks]
- -[SKGProcessingSetDescription .cxx_destruct]
- -[SKGProcessingSetDescription description]
- -[SKGProcessingSetDescription excludedBundles]
- -[SKGProcessingSetDescription excludedProtectionClasses]
- -[SKGProcessingSetDescription initWithName:version:]
- -[SKGProcessingSetDescription name]
- -[SKGProcessingSetDescription requiredBundles]
- -[SKGProcessingSetDescription requiredProtectionClasses]
- -[SKGProcessingSetDescription setExcludedBundles:]
- -[SKGProcessingSetDescription setExcludedProtectionClasses:]
- -[SKGProcessingSetDescription setRequiredBundles:]
- -[SKGProcessingSetDescription setRequiredProtectionClasses:]
- -[SKGProcessingSetDescription version]
- -[SKGProcessingTask .cxx_destruct]
- -[SKGProcessingTask canRun]
- -[SKGProcessingTask descriptor]
- -[SKGProcessingTask enabled]
- -[SKGProcessingTask fetchAttributes]
- -[SKGProcessingTask initWithDescriptor:processors:enabled:]
- -[SKGProcessingTask processedAttributes]
- -[SKGProcessingTask processors]
- -[SKGProcessingTask requiredAttributes]
- -[SKGProcessingTask setCanRun:]
- -[SKGProcessingTask supportedQuery]
- -[SKGProcessingTask supportedSetQuery]
- -[SKGProcessingTask supportsRecord:bundleID:]
- -[SKGQueryProcessingJob .cxx_destruct]
- -[SKGQueryProcessingJob configure]
- -[SKGQueryProcessingJob fetchAttributes]
- -[SKGQueryProcessingJob initWithName:version:tasks:]
- -[SKGQueryProcessingJob processor]
- -[SKGQueryProcessingJob queryContext]
- -[SKGQueryProcessingJob queryString]
- -[SKGQueryProcessingJob query]
- -[SKGQueryProcessingJob setFetchAttributes:]
- -[SKGQueryProcessingJob setProcessor:]
- -[SKGQueryProcessingJob setQueryString:queryContext:query:]
- -[SKGQueryProcessingJob setTaskQueries:]
- -[SKGQueryProcessingJob supportedQueryForTask:]
- -[SKGQueryProcessingJob taskQueries]
- -[SKGQueryRecordProcessor enumerateRecordsForRecord:bundleID:usingBlock:]
- -[SKGQueryRecordProcessor processRecord:uniqueID:bundleID:]
- -[SKGRecordCache .cxx_destruct]
- -[SKGRecordCache addEntriesFromProcessedUpdate:]
- -[SKGRecordCache cacheForRecord:]
- -[SKGRecordCache init]
- -[SKGRecordCache objectForKey:]
- -[SKGRecordProcessor .cxx_destruct]
- -[SKGRecordProcessor cache]
- -[SKGRecordProcessor enumerateRecordsForRecord:bundleID:usingBlock:]
- -[SKGRecordProcessor fetchAttributes]
- -[SKGRecordProcessor initWithTasks:cache:]
- -[SKGRecordProcessor processRecord:uniqueID:bundleID:]
- -[SKGRecordProcessor resume]
- -[SKGRecordProcessor suspend]
- -[SKGRecordProcessor suspended]
- -[SKGRecordProcessor tasks]
- -[SKGRecordUpdate .cxx_destruct]
- -[SKGRecordUpdate addEntriesFromDictionary:]
- -[SKGRecordUpdate attributes]
- -[SKGRecordUpdate error]
- -[SKGRecordUpdate initWithUniqueID:status:error:]
- -[SKGRecordUpdate status]
- -[SKGRecordUpdate uniqueID]
- -[SKGTestProcessor init]
- -[SKGTestProcessor processRecord:bundleID:]
- -[SKGTestProcessor processedAttributes]
- -[SKGTestProcessor requiredAttributes]
- -[SKGTestProcessor requiredAttributes].cold.1
- -[SKGTestProcessor willProcessRecord:bundleID:]
- GCC_except_table192
- GCC_except_table250
- _OBJC_CLASS_$_CSProcessorTaskUpdater
- _OBJC_CLASS_$_SKGBreadcrumbProcessor
- _OBJC_CLASS_$_SKGEmbeddingProcessor
- _OBJC_CLASS_$_SKGIndexProcessingJob
- _OBJC_CLASS_$_SKGItemProcessor
- _OBJC_CLASS_$_SKGJournalProcessingJob
- _OBJC_CLASS_$_SKGKeyphraseProcessor
- _OBJC_CLASS_$_SKGLanguageProcessor
- _OBJC_CLASS_$_SKGLocationProcessor
- _OBJC_CLASS_$_SKGProcessedUpdate
- _OBJC_CLASS_$_SKGProcessingDescriptor
- _OBJC_CLASS_$_SKGProcessingJob
- _OBJC_CLASS_$_SKGProcessingPipelineManager
- _OBJC_CLASS_$_SKGProcessingQueryBuilder
- _OBJC_CLASS_$_SKGProcessingSetDescription
- _OBJC_CLASS_$_SKGProcessingTask
- _OBJC_CLASS_$_SKGQueryProcessingJob
- _OBJC_CLASS_$_SKGQueryRecordProcessor
- _OBJC_CLASS_$_SKGRecordCache
- _OBJC_CLASS_$_SKGRecordProcessor
- _OBJC_CLASS_$_SKGRecordUpdate
- _OBJC_CLASS_$_SKGTestProcessor
- _OBJC_IVAR_$_CSEventListenerConfig._supportsUpdatedItems
- _OBJC_IVAR_$_CSEventListenerConfig._trackingAttributes
- _OBJC_IVAR_$_CSProcessorTaskUpdater._event
- _OBJC_IVAR_$_CSProcessorTaskUpdater._task
- _OBJC_IVAR_$_CSProcessorTaskUpdater._taskConfig
- _OBJC_IVAR_$_SKGBreadcrumbProcessor._detector
- _OBJC_IVAR_$_SKGBreadcrumbProcessor._listener
- _OBJC_IVAR_$_SKGEmbeddingProcessor._processor
- _OBJC_IVAR_$_SKGItemProcessor._is_enabled
- _OBJC_IVAR_$_SKGItemProcessor._is_suspended
- _OBJC_IVAR_$_SKGItemProcessor._marker
- _OBJC_IVAR_$_SKGItemProcessor._name
- _OBJC_IVAR_$_SKGItemProcessor._queue
- _OBJC_IVAR_$_SKGJournalProcessingJob._bgstOptions
- _OBJC_IVAR_$_SKGKeyphraseProcessor._listener
- _OBJC_IVAR_$_SKGLanguageProcessor._langIdentifier
- _OBJC_IVAR_$_SKGLanguageProcessor._listener
- _OBJC_IVAR_$_SKGLocationProcessor._detector
- _OBJC_IVAR_$_SKGLocationProcessor._listener
- _OBJC_IVAR_$_SKGProcessedUpdate._attributes
- _OBJC_IVAR_$_SKGProcessedUpdate._error
- _OBJC_IVAR_$_SKGProcessedUpdate._status
- _OBJC_IVAR_$_SKGProcessingDescriptor._processorNames
- _OBJC_IVAR_$_SKGProcessingDescriptor._setDescription
- _OBJC_IVAR_$_SKGProcessingJob._logger
- _OBJC_IVAR_$_SKGProcessingJob._name
- _OBJC_IVAR_$_SKGProcessingJob._tasks
- _OBJC_IVAR_$_SKGProcessingJob._version
- _OBJC_IVAR_$_SKGProcessingPipelineManager._processors
- _OBJC_IVAR_$_SKGProcessingPipelineManager._tasks
- _OBJC_IVAR_$_SKGProcessingSetDescription._excludedBundles
- _OBJC_IVAR_$_SKGProcessingSetDescription._excludedProtectionClasses
- _OBJC_IVAR_$_SKGProcessingSetDescription._name
- _OBJC_IVAR_$_SKGProcessingSetDescription._requiredBundles
- _OBJC_IVAR_$_SKGProcessingSetDescription._requiredProtectionClasses
- _OBJC_IVAR_$_SKGProcessingSetDescription._version
- _OBJC_IVAR_$_SKGProcessingTask._canRun
- _OBJC_IVAR_$_SKGProcessingTask._descriptor
- _OBJC_IVAR_$_SKGProcessingTask._enabled
- _OBJC_IVAR_$_SKGProcessingTask._processors
- _OBJC_IVAR_$_SKGQueryProcessingJob._fetchAttributes
- _OBJC_IVAR_$_SKGQueryProcessingJob._processor
- _OBJC_IVAR_$_SKGQueryProcessingJob._query
- _OBJC_IVAR_$_SKGQueryProcessingJob._queryContext
- _OBJC_IVAR_$_SKGQueryProcessingJob._queryString
- _OBJC_IVAR_$_SKGQueryProcessingJob._taskQueries
- _OBJC_IVAR_$_SKGRecordCache._cache
- _OBJC_IVAR_$_SKGRecordProcessor._cache
- _OBJC_IVAR_$_SKGRecordProcessor._fetchAttributes
- _OBJC_IVAR_$_SKGRecordProcessor._suspended
- _OBJC_IVAR_$_SKGRecordProcessor._tasks
- _OBJC_IVAR_$_SKGRecordUpdate._attributes
- _OBJC_IVAR_$_SKGRecordUpdate._error
- _OBJC_IVAR_$_SKGRecordUpdate._status
- _OBJC_IVAR_$_SKGRecordUpdate._uniqueID
- _OBJC_METACLASS_$_CSProcessorTaskUpdater
- _OBJC_METACLASS_$_SKGBreadcrumbProcessor
- _OBJC_METACLASS_$_SKGEmbeddingProcessor
- _OBJC_METACLASS_$_SKGIndexProcessingJob
- _OBJC_METACLASS_$_SKGItemProcessor
- _OBJC_METACLASS_$_SKGJournalProcessingJob
- _OBJC_METACLASS_$_SKGKeyphraseProcessor
- _OBJC_METACLASS_$_SKGLanguageProcessor
- _OBJC_METACLASS_$_SKGLocationProcessor
- _OBJC_METACLASS_$_SKGProcessedUpdate
- _OBJC_METACLASS_$_SKGProcessingDescriptor
- _OBJC_METACLASS_$_SKGProcessingJob
- _OBJC_METACLASS_$_SKGProcessingPipelineManager
- _OBJC_METACLASS_$_SKGProcessingQueryBuilder
- _OBJC_METACLASS_$_SKGProcessingSetDescription
- _OBJC_METACLASS_$_SKGProcessingTask
- _OBJC_METACLASS_$_SKGQueryProcessingJob
- _OBJC_METACLASS_$_SKGQueryRecordProcessor
- _OBJC_METACLASS_$_SKGRecordCache
- _OBJC_METACLASS_$_SKGRecordProcessor
- _OBJC_METACLASS_$_SKGRecordUpdate
- _OBJC_METACLASS_$_SKGTestProcessor
- __OBJC_$_CLASS_METHODS_SKGProcessingDescriptor
- __OBJC_$_CLASS_METHODS_SKGProcessingPipelineManager
- __OBJC_$_CLASS_METHODS_SKGProcessingQueryBuilder
- __OBJC_$_INSTANCE_METHODS_CSProcessorTaskUpdater
- __OBJC_$_INSTANCE_METHODS_NSDictionary(SKGQueryRecordValidation|SKGJournalRecordValidation)
- __OBJC_$_INSTANCE_METHODS_SKGBreadcrumbProcessor
- __OBJC_$_INSTANCE_METHODS_SKGEmbeddingProcessor
- __OBJC_$_INSTANCE_METHODS_SKGIndexProcessingJob
- __OBJC_$_INSTANCE_METHODS_SKGItemProcessor
- __OBJC_$_INSTANCE_METHODS_SKGJob(People|Updates)
- __OBJC_$_INSTANCE_METHODS_SKGJournalProcessingJob
- __OBJC_$_INSTANCE_METHODS_SKGKeyphraseProcessor
- __OBJC_$_INSTANCE_METHODS_SKGLanguageProcessor
- __OBJC_$_INSTANCE_METHODS_SKGLocationProcessor
- __OBJC_$_INSTANCE_METHODS_SKGProcessedUpdate
- __OBJC_$_INSTANCE_METHODS_SKGProcessingDescriptor
- __OBJC_$_INSTANCE_METHODS_SKGProcessingJob
- __OBJC_$_INSTANCE_METHODS_SKGProcessingPipelineManager(Testing)
- __OBJC_$_INSTANCE_METHODS_SKGProcessingSetDescription
- __OBJC_$_INSTANCE_METHODS_SKGProcessingTask
- __OBJC_$_INSTANCE_METHODS_SKGQueryProcessingJob
- __OBJC_$_INSTANCE_METHODS_SKGQueryRecordProcessor
- __OBJC_$_INSTANCE_METHODS_SKGRecordCache
- __OBJC_$_INSTANCE_METHODS_SKGRecordProcessor
- __OBJC_$_INSTANCE_METHODS_SKGRecordUpdate
- __OBJC_$_INSTANCE_METHODS_SKGTestProcessor
- __OBJC_$_INSTANCE_VARIABLES_CSProcessorTaskUpdater
- __OBJC_$_INSTANCE_VARIABLES_SKGBreadcrumbProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGEmbeddingProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGItemProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGJournalProcessingJob
- __OBJC_$_INSTANCE_VARIABLES_SKGKeyphraseProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGLanguageProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGLocationProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessedUpdate
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessingDescriptor
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessingJob
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessingPipelineManager
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessingSetDescription
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessingTask
- __OBJC_$_INSTANCE_VARIABLES_SKGQueryProcessingJob
- __OBJC_$_INSTANCE_VARIABLES_SKGRecordCache
- __OBJC_$_INSTANCE_VARIABLES_SKGRecordProcessor
- __OBJC_$_INSTANCE_VARIABLES_SKGRecordUpdate
- __OBJC_$_PROP_LIST_CSProcessorTaskUpdater
- __OBJC_$_PROP_LIST_SKGBreadcrumbProcessor
- __OBJC_$_PROP_LIST_SKGItemProcessor
- __OBJC_$_PROP_LIST_SKGItemProcessor.115
- __OBJC_$_PROP_LIST_SKGJournalProcessingJob
- __OBJC_$_PROP_LIST_SKGKeyphraseProcessor
- __OBJC_$_PROP_LIST_SKGLanguageProcessor
- __OBJC_$_PROP_LIST_SKGLocationProcessor
- __OBJC_$_PROP_LIST_SKGProcessedUpdate
- __OBJC_$_PROP_LIST_SKGProcessingDescriptor
- __OBJC_$_PROP_LIST_SKGProcessingJob
- __OBJC_$_PROP_LIST_SKGProcessingSetDescription
- __OBJC_$_PROP_LIST_SKGProcessingTask
- __OBJC_$_PROP_LIST_SKGQueryProcessingJob
- __OBJC_$_PROP_LIST_SKGRecordProcessor
- __OBJC_$_PROP_LIST_SKGRecordUpdate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKGItemProcessor
- __OBJC_$_PROTOCOL_METHOD_TYPES_SKGItemProcessor
- __OBJC_$_PROTOCOL_REFS_SKGItemProcessor
- __OBJC_CLASS_PROTOCOLS_$_CSProcessorTaskUpdater
- __OBJC_CLASS_PROTOCOLS_$_SKGItemProcessor
- __OBJC_CLASS_RO_$_CSProcessorTaskUpdater
- __OBJC_CLASS_RO_$_SKGBreadcrumbProcessor
- __OBJC_CLASS_RO_$_SKGEmbeddingProcessor
- __OBJC_CLASS_RO_$_SKGIndexProcessingJob
- __OBJC_CLASS_RO_$_SKGItemProcessor
- __OBJC_CLASS_RO_$_SKGJournalProcessingJob
- __OBJC_CLASS_RO_$_SKGKeyphraseProcessor
- __OBJC_CLASS_RO_$_SKGLanguageProcessor
- __OBJC_CLASS_RO_$_SKGLocationProcessor
- __OBJC_CLASS_RO_$_SKGProcessedUpdate
- __OBJC_CLASS_RO_$_SKGProcessingDescriptor
- __OBJC_CLASS_RO_$_SKGProcessingJob
- __OBJC_CLASS_RO_$_SKGProcessingPipelineManager
- __OBJC_CLASS_RO_$_SKGProcessingQueryBuilder
- __OBJC_CLASS_RO_$_SKGProcessingSetDescription
- __OBJC_CLASS_RO_$_SKGProcessingTask
- __OBJC_CLASS_RO_$_SKGQueryProcessingJob
- __OBJC_CLASS_RO_$_SKGQueryRecordProcessor
- __OBJC_CLASS_RO_$_SKGRecordCache
- __OBJC_CLASS_RO_$_SKGRecordProcessor
- __OBJC_CLASS_RO_$_SKGRecordUpdate
- __OBJC_CLASS_RO_$_SKGTestProcessor
- __OBJC_LABEL_PROTOCOL_$_SKGItemProcessor
- __OBJC_METACLASS_RO_$_CSProcessorTaskUpdater
- __OBJC_METACLASS_RO_$_SKGBreadcrumbProcessor
- __OBJC_METACLASS_RO_$_SKGEmbeddingProcessor
- __OBJC_METACLASS_RO_$_SKGIndexProcessingJob
- __OBJC_METACLASS_RO_$_SKGItemProcessor
- __OBJC_METACLASS_RO_$_SKGJournalProcessingJob
- __OBJC_METACLASS_RO_$_SKGKeyphraseProcessor
- __OBJC_METACLASS_RO_$_SKGLanguageProcessor
- __OBJC_METACLASS_RO_$_SKGLocationProcessor
- __OBJC_METACLASS_RO_$_SKGProcessedUpdate
- __OBJC_METACLASS_RO_$_SKGProcessingDescriptor
- __OBJC_METACLASS_RO_$_SKGProcessingJob
- __OBJC_METACLASS_RO_$_SKGProcessingPipelineManager
- __OBJC_METACLASS_RO_$_SKGProcessingQueryBuilder
- __OBJC_METACLASS_RO_$_SKGProcessingSetDescription
- __OBJC_METACLASS_RO_$_SKGProcessingTask
- __OBJC_METACLASS_RO_$_SKGQueryProcessingJob
- __OBJC_METACLASS_RO_$_SKGQueryRecordProcessor
- __OBJC_METACLASS_RO_$_SKGRecordCache
- __OBJC_METACLASS_RO_$_SKGRecordProcessor
- __OBJC_METACLASS_RO_$_SKGRecordUpdate
- __OBJC_METACLASS_RO_$_SKGTestProcessor
- __OBJC_PROTOCOL_$_SKGItemProcessor
- ___108-[SpotlightKnowledge processEmbeddingsReportWithJobContext:group:progressBlock:checkpointBlock:cancelBlock:]_block_invoke.200
- ___108-[SpotlightKnowledge processEmbeddingsReportWithJobContext:group:progressBlock:checkpointBlock:cancelBlock:]_block_invoke.202
- ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.324
- ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.324.cold.1
- ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.325
- ___108-[SpotlightKnowledge runWithQueue:group:progressBlock:checkpointBlock:completeBlock:cancelBlock:deferBlock:]_block_invoke.325.cold.1
- ___22-[SKGTaskAgent _setup]_block_invoke.144
- ___22-[SKGTaskAgent _setup]_block_invoke.146
- ___22-[SKGTaskAgent _setup]_block_invoke.149
- ___22-[SKGTaskAgent _setup]_block_invoke.152
- ___22-[SKGTaskAgent _setup]_block_invoke.154
- ___22-[SKGTaskAgent _setup]_block_invoke.160
- ___22-[SKGTaskAgent _setup]_block_invoke_2.145
- ___22-[SKGTaskAgent _setup]_block_invoke_2.147
- ___22-[SKGTaskAgent _setup]_block_invoke_2.158
- ___22-[SKGTaskAgent _setup]_block_invoke_3.148
- ___22-[SKGTaskAgent _setup]_block_invoke_3.159
- ___22-[SKGTaskAgent _setup]_block_invoke_3.167
- ___22-[SKGTaskAgent _setup]_block_invoke_3.167.cold.1
- ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.234
- ___38-[SKGTestProcessor requiredAttributes]_block_invoke
- ___41-[CSEventListenerManager processJournals]_block_invoke.120
- ___41-[CSEventListenerManager processJournals]_block_invoke.cold.1
- ___42-[SKGLanguageProcessor requiredAttributes]_block_invoke
- ___42-[SKGLocationProcessor requiredAttributes]_block_invoke
- ___43-[SKGEmbeddingProcessor requiredAttributes]_block_invoke
- ___43-[SKGKeyphraseProcessor requiredAttributes]_block_invoke
- ___43-[SKGLanguageProcessor processedAttributes]_block_invoke
- ___43-[SKGLocationProcessor processedAttributes]_block_invoke
- ___44-[SKGBreadcrumbProcessor requiredAttributes]_block_invoke
- ___44-[SKGEmbeddingProcessor processedAttributes]_block_invoke
- ___44-[SKGKeyphraseProcessor processedAttributes]_block_invoke
- ___45+[SKGProcessingPipelineManager sharedManager]_block_invoke
- ___45-[SKGBreadcrumbProcessor processedAttributes]_block_invoke
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke_2
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke_3
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke_4
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke_5
- ___47-[SKGLocationProcessor processRecord:bundleID:]_block_invoke_6
- ___48-[SKGEmbeddingProcessor processRecord:bundleID:]_block_invoke
- ___48-[SKGKeyphraseProcessor processRecord:bundleID:]_block_invoke
- ___48-[SKGKeyphraseProcessor processRecord:bundleID:]_block_invoke.31
- ___48-[SKGKeyphraseProcessor processRecord:bundleID:]_block_invoke.cold.1
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.134
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.143
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.171
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.137
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.146
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.149
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.158
- ___49-[SKGBreadcrumbProcessor processRecord:bundleID:]_block_invoke
- ___49-[SKGBreadcrumbProcessor processRecord:bundleID:]_block_invoke_2
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.282
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.285
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.289
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.291
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.291.cold.1
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.293
- ___59-[SKGQueryRecordProcessor processRecord:uniqueID:bundleID:]_block_invoke
- ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke.273
- ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke_2.274
- ___67-[CSEventListenerManager handleMessage:basePath:withDispatchGroup:]_block_invoke.134
- ___77-[SpotlightKnowledge processSuggestedEventsReportWithJobContext:cancelBlock:]_block_invoke.220
- ___77-[SpotlightKnowledge processSuggestedEventsReportWithJobContext:cancelBlock:]_block_invoke_2.224
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.70
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.83
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.95
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.95.cold.1
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.96
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.96.cold.1
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.72
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.cold.1
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.cold.2
- ___81-[CSEmbeddingsUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2.cold.3
- ___83-[SpotlightKnowledge processDocumentUnderstandingReportWithJobContext:cancelBlock:]_block_invoke.242
- ___83-[SpotlightKnowledge processDocumentUnderstandingReportWithJobContext:cancelBlock:]_block_invoke_2.246
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.21
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.36
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.36.cold.1
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_2
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_3
- ___84-[CSProcessorTaskUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke_4
- ___block_descriptor_112_e8_32s40s48s56bs64bs72r_e17_v16?0"NSError"8ls32l8s40l8r72l8s56l8s48l8s64l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88s96bs104r_e26_B16?0"SKGProcessedItem"8lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80bs88r96r_e25_B16?0?<v?"NSString">8ls32l8s40l8r88l8r96l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_137_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8s48l8r96l8s88l8r104l8s56l8r112l8s64l8r120l8s72l8s80l8
- ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96bs104r112r120r_e36_B16?0"CSEventDonationJournalItem"8ls32l8s40l8s48l8r104l8s56l8r112l8s64l8s72l8s80l8s96l8s88l8r120l8
- ___block_descriptor_145_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r_e25_B16?0?<v?"NSString">8ls32l8s40l8s48l8r104l8s96l8s56l8r112l8s64l8r120l8s72l8r128l8s80l8s88l8
- ___block_descriptor_56_e8_32s40s48r_e27_v28?0"NSString"8i16i20i24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e48_v32?0"NSDictionary"8"SKGProcessingTask"16^B24ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e26_B16?0"SKGProcessedItem"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.104
- ___block_literal_global.124
- ___block_literal_global.132
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.139
- ___block_literal_global.142
- ___block_literal_global.145
- ___block_literal_global.148
- ___block_literal_global.151
- ___block_literal_global.165
- ___block_literal_global.170
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.185
- ___block_literal_global.189
- ___block_literal_global.192
- ___block_literal_global.216
- ___block_literal_global.231
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.257
- ___block_literal_global.259
- ___block_literal_global.261
- ___block_literal_global.263
- ___block_literal_global.265
- ___block_literal_global.267
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.278
- ___block_literal_global.287
- ___block_literal_global.32
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.327
- ___block_literal_global.70
- ___handleEmbeddingsTask_block_invoke.312
- ___handleKeyphrasesTask_block_invoke.316
- ___handlePreExtractionTask_block_invoke.317
- ___handlePriorityTask_block_invoke.315
- ___handleQueryCleanupTask_block_invoke.251
- ___handleQueryCleanupTask_block_invoke.252
- ___handleQueryCleanupTask_block_invoke.253
- ___handleQueryCleanupTask_block_invoke.254
- ___handleQueryUpdatesTask_block_invoke.321
- ___handleQueryUpdatesTask_block_invoke.322
- ___handleQueryUpdatesTask_block_invoke.323
- ___handleQueryUpdatesTask_block_invoke.324
- ___setupQueryCleanupTasks_block_invoke.313
- ___setupQueryUpdatesTasks_block_invoke.318
- _kSKGDomainSpotlight
- _objc_msgSend$addEntriesFromProcessedUpdate:
- _objc_msgSend$cache
- _objc_msgSend$fetchedAttributes
- _objc_msgSend$hitError
- _objc_msgSend$includeUpdatedItems
- _objc_msgSend$initWithName:version:tasks:
- _objc_msgSend$initWithTask:
- _objc_msgSend$initWithTasks:cache:
- _objc_msgSend$initWithTasks:processors:
- _objc_msgSend$initWithUniqueID:status:error:
- _objc_msgSend$isUpdate
- _objc_msgSend$loadWithProcessorFlags:
- _objc_msgSend$processorAttributesForEvent:failed:
- _objc_msgSend$queryForItemsNeedingProcessingByTaskWithName:inverse:
- _objc_msgSend$queryForItemsProcessedByTaskWithName:inverse:
- _objc_msgSend$setAttributes:
- _objc_msgSend$setProcessor:
- _objc_msgSend$setSupportsUpdatedItems:
- _objc_msgSend$setTaskQueries:
- _objc_msgSend$setTrackingAttributes:
- _objc_msgSend$supportedQueryForTask:
- _objc_msgSend$supportsEvent:bundleID:
- _objc_msgSend$supportsUpdatedItems
- _objc_msgSend$taskQueries
- _objc_release_x10
- _requiredAttributes.sMockRequired
CStrings:
+ "### EmbeddingCache HitRate = %u%%, (%s) Total Items = %u"
+ "### Unable to determine journal file size: %d, %s, %d"
+ "###purgeJournalsProactive Total journal size %lld (qc: %lu) exceeds %lld, skipping journal %s"
+ "%@: processed update <%@> for processor <%@>"
+ "%@: reqBun. <%@>, excBun. <%@>, reqProt. <%@>, excProt. <%@>, reqAtt. <%@>, excAtt. <%@>, proAtt. <%@>"
+ "%@: skipping update <%@> for processor <%@>"
+ "%@: skipping update <%@> for processor <%@> due to suspension"
+ "%@: skipping update <%@> for processor <%@> due to unknown status"
+ "%@: supQuery <%@>"
+ "-[SKDJournalProcessingJob initWithName:version:pipelines:]"
+ "<%@:%p:%u; n: %llu pfd: %d offset: %lld jsz: %lld, tsz: %lld err: %d (%@)>"
+ "<%@:%p:%u; n: %llu pfd: %d offset: %lld jsz:%lld, tsz: %lld csz: %lld err: %d (%@)>"
+ "=== Requesting scheduled processing of %@ <%@>"
+ "@\"<CSEventListenerManagerSignposter>\""
+ "@\"CSSearchableItem\""
+ "@\"SKDCSItemProcessor\""
+ "@\"SKDJournalProcessingJob\""
+ "@\"SKDPipelineDescriptor\""
+ "@\"SKDPipelineSetDescription\""
+ "@\"SKDRecordCache\""
+ "@\"SKDRecordProcessorCache\""
+ "@\"SKDRecordUpdate\"32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "ANE"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B48@0:8@16@24@32@?40"
+ "Base class implementation of SKDQuery.attributes should not be callable."
+ "Base class implementation of SKDQuery.isLeaf should not be callable."
+ "Base class implementation of SKDQuery.negated() should not be callable."
+ "Base class implementation of SKDQuery.queryAttributes() should not be callable."
+ "Base class implementation of SKDQuery.queryString() should not be callable."
+ "Base class implementation of SKDQuery.string should not be callable."
+ "BundleProgressReport"
+ "CPU"
+ "CSEventListenerManagerDefaultSignposter"
+ "CSEventListenerManagerSignposter"
+ "CSPipelineUpdaterHandleDonation"
+ "CSPipelineUpdaterProcessSingleItem"
+ "CSProcessorPipelineJobUpdater"
+ "Disk"
+ "FAILING_TEST_PROCESSOR"
+ "FPDownloaded"
+ "Fatal error"
+ "GPU"
+ "HandleDonation"
+ "Memory"
+ "MockTest"
+ "PASSING_TEST_PROCESSOR"
+ "Pipeline"
+ "PipelineIndex"
+ "ProcessJournals"
+ "SKDBaseCSItemProcessingJob"
+ "SKDBaseCSQueryProcessingJob"
+ "SKDBaseItemProcessingJob"
+ "SKDBaseItemUpdate"
+ "SKDBaseJob"
+ "SKDBreadcrumbProcessor"
+ "SKDCSItemProcessor"
+ "SKDCSItemUpdate"
+ "SKDEmbeddingProcessor"
+ "SKDIndexProcessingJob"
+ "SKDItemProcessor"
+ "SKDItemUpdate"
+ "SKDJournalItemProcessor"
+ "SKDJournalProcessingJob"
+ "SKDJournalProcessingJob.m"
+ "SKDKeyphraseProcessor"
+ "SKDLanguageProcessor"
+ "SKDLocationProcessor"
+ "SKDPipeline"
+ "SKDPipelineDescriptor"
+ "SKDPipelineManager"
+ "SKDPipelineQueryBuilder"
+ "SKDPipelineSetDescription"
+ "SKDRecordCache"
+ "SKDRecordProcessor"
+ "SKDRecordProcessorCache"
+ "SKDRecordUpdate"
+ "SKDTestProcessor"
+ "SpotlightKnowledgeDaemon"
+ "SpotlightKnowledgeDaemon/SKDQuery.swift"
+ "SpotlightKnowledgePipeline"
+ "SpotlightKnowledgePipelineDebug"
+ "T@\"CSSearchableItem\",R,N,V_item"
+ "T@\"NSArray\",R,N,V_excludedBundleIDs"
+ "T@\"NSArray\",R,N,V_fetchAttributes"
+ "T@\"NSArray\",R,N,V_pipelines"
+ "T@\"NSArray\",R,N,V_requiredAttributes"
+ "T@\"NSArray\",R,N,V_requiredBundleIDs"
+ "T@\"NSSet\",N,R"
+ "T@\"NSString\",N,R"
+ "T@\"SKDCSItemProcessor\",R,N"
+ "T@\"SKDPipelineDescriptor\",R,N,V_descriptor"
+ "T@\"SKDPipelineSetDescription\",R,N"
+ "TB,N,R"
+ "TEST_PROCESSOR"
+ "_excludedAttributes"
+ "_excludedBundleIDs"
+ "_item"
+ "_job"
+ "_journal_file_size"
+ "_kMDItem%@ErrorCount"
+ "_pipelineQueries"
+ "_pipelines"
+ "_processJournalsWithProcessedJournalsCount:completionHandler:"
+ "_processedAttributes"
+ "_processorCache"
+ "_recordCache"
+ "_requiredBundleIDs"
+ "_runCSPollingQuery:foundItemBlock:"
+ "_signposter"
+ "_totalJournalSize"
+ "_updateCoreSpotlightItems:bundleID:protectionClass:cancelBlock:"
+ "addAttributeForKey:value:"
+ "addEntriesFromAttributes:"
+ "addEntryForAttribute:value:"
+ "beginProcessJournalsInterval"
+ "bundleProgressNumerator:denominator:"
+ "cancelled"
+ "com.apple.CoreSuggestions"
+ "com.apple.corespotlight.knowledge.indexing"
+ "com.apple.spotlight.events"
+ "com.apple.spotlight.indexing.task"
+ "com.apple.spotlightknowledge.processor.%@"
+ "deleteFirstJournal:"
+ "didCancel=%{BOOL}d bundle=%@ indexType=%d totalItemsCount=%u donationsWithNeedsEmbedding=%lu processedItemsCount=%lu embeddingsCount=%lu cacheHitRate=%u cacheItemCount=%u"
+ "empty-queue"
+ "enableMockPipeline"
+ "endProcessJournalsIntervalWithSignpostID:stopReason:indexType:taskName:processedJournalsCount:journalQueueCount:"
+ "eof-or-error"
+ "errorAttribute"
+ "excludedAttributes"
+ "excludedBundleIDs"
+ "featureCheckpointForProgress"
+ "incrementAttributeValue:forKey:"
+ "indexing attrs"
+ "initWithDescriptor:processors:"
+ "initWithDescriptors:processorCache:"
+ "initWithItem:"
+ "initWithJournalJob:"
+ "initWithName:version:pipelines:"
+ "initWithPipelines:recordCache:"
+ "initWithStatus:"
+ "isLeaf"
+ "item"
+ "itemProcessor"
+ "journal-%@"
+ "journalProcessingJobs"
+ "journalSizeGetBelowLimit"
+ "kMDItemContentURL"
+ "kSKDItemAttributeTextContentEntityRanges"
+ "last-journal"
+ "markCompleteWithPipeline:recordUpdate:"
+ "maxJournalSizeInQueue"
+ "needsProcessingAttribute"
+ "negated"
+ "performCSIndexProcessingJob:cancelBlock:"
+ "pipelineForName:"
+ "pipelineQueries"
+ "pipelines"
+ "pipelines.count == 1"
+ "predicateWithBlock:"
+ "processItemWithRecord:filePath:"
+ "processItemWithRecord:uniqueID:bundleID:"
+ "processorWithName:"
+ "processorsWithNames:"
+ "purgeJournalsProactive"
+ "queryAttributes"
+ "queryForItemsNeedingProcessingByPipelineWithName:inverse:"
+ "queryForItemsProcessedByPipelineWithName:inverse:"
+ "recordCache"
+ "referenceDateFor:"
+ "requiredBundleIDs"
+ "setExcludedAttributes:"
+ "setItemProcessor:"
+ "setPipelineQueries:"
+ "setPowerBudgeted:"
+ "setProcessedAttributes:"
+ "sharedCache"
+ "stopReason=%{public}@ indexType=%d taskName=%@ processedJournalsCount=%lu journalQueueCount=%lu"
+ "string"
+ "supportedQueryForPipeline:"
+ "unable to getrlimit, error %d."
+ "unable to setrlimit, error %d."
+ "updateAttributeSet:forPipeline:withAttributes:"
+ "v24@?0Q8@\"NSString\"16"
+ "v32@0:8Q16@?24"
+ "v32@0:8^Q16^Q24"
+ "v32@?0@\"NSDictionary\"8@\"SKDPipeline\"16^B24"
+ "v60@0:8Q16@\"NSString\"24i32@\"NSString\"36Q44Q52"
+ "v60@0:8Q16@24i32@36Q44Q52"
+ "versionAttribute"
+ "\x81\xc3"
- "### EmbeddingCache HitRate = %u, (%d) Total Items = %u"
- "%"
- "%@: reqBun. <%@>, excBun. <%@>, reqProt. <%@>, excProt. <%@>"
- "%@EntityRanges"
- "<%@:%p:%u; n: %llu pfd: %d offset: %lld sz: %lld csz: %lld err: %d (%@)>"
- "<%@:%p:%u; n: %llu pfd: %d offset: %lld sz: %lld err: %d (%@)>"
- "@\"SKGProcessedUpdate\"32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "@\"SKGProcessingDescriptor\""
- "@\"SKGProcessingLogger\""
- "@\"SKGProcessingSetDescription\""
- "@\"SKGProcessorTask\""
- "@\"SKGRecordCache\""
- "@\"SKGRecordProcessor\""
- "@40@0:8@16q24@32"
- "CSEmbeddingsUpdaterHandleDonation"
- "CSProcessorTaskUpdater"
- "SKGBreadcrumbProcessor"
- "SKGEmbeddingProcessor"
- "SKGIndexProcessingJob"
- "SKGItemProcessor"
- "SKGJournalProcessingJob"
- "SKGKeyphraseProcessor"
- "SKGLanguageProcessor"
- "SKGLocationProcessor"
- "SKGProcessedUpdate"
- "SKGProcessingDescriptor"
- "SKGProcessingJob"
- "SKGProcessingPipelineManager"
- "SKGProcessingQueryBuilder"
- "SKGProcessingSetDescription"
- "SKGProcessingTask"
- "SKGQueryProcessingJob"
- "SKGQueryRecordProcessor"
- "SKGRecordCache"
- "SKGRecordProcessor"
- "SKGRecordUpdate"
- "SKGTestProcessor"
- "T@\"NSArray\",C,N,V_trackingAttributes"
- "T@\"NSArray\",R,N,V_tasks"
- "T@\"NSDictionary\",C,N,V_attributes"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSString\",R,N,V_uniqueID"
- "T@\"SKGProcessingDescriptor\",R,N,V_descriptor"
- "T@\"SKGProcessingLogger\",R,N,V_logger"
- "T@\"SKGProcessingSetDescription\",R,N"
- "T@\"SKGRecordCache\",R,N"
- "TB,N,V_supportsUpdatedItems"
- "TB,R,N,V_enabled"
- "Tq,R,N,V_status"
- "_logger"
- "_supportsUpdatedItems"
- "_suspended"
- "_taskQueries"
- "_uniqueID"
- "addEntriesFromProcessedUpdate:"
- "cache"
- "includeUpdatedItems"
- "initWithDescriptor:processors:enabled:"
- "initWithName:version:tasks:"
- "initWithTask:"
- "initWithTasks:cache:"
- "initWithTasks:processors:"
- "initWithUniqueID:status:error:"
- "journalProcessingJob"
- "kMDItemOriginApplicationIdentifier"
- "kMDItemRelatedAppBundleIdentifier"
- "kMDItemTextContentEntityRanges"
- "logger"
- "processRecord:uniqueID:bundleID:"
- "processor"
- "queryForItemsNeedingProcessingByTaskWithName:inverse:"
- "queryForItemsProcessedByTaskWithName:inverse:"
- "setAttributes:"
- "setProcessor:"
- "setSupportsUpdatedItems:"
- "setTaskQueries:"
- "supportedQueryForTask:"
- "supportsUpdatedItems"
- "taskQueries"
- "uniqueID"
- "v32@?0@\"NSDictionary\"8@\"SKGProcessingTask\"16^B24"
- "\x81\xb3"

```
