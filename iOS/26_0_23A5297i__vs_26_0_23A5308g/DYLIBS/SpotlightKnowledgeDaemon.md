## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0xed924
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_methlist: 0x7d00
+2391.1.0.0.0
+  __TEXT.__text: 0xef9a8
+  __TEXT.__auth_stubs: 0x2570
+  __TEXT.__objc_methlist: 0x7fc0
   __TEXT.__const: 0x1b78
   __TEXT.__oslogstring: 0x8903
-  __TEXT.__cstring: 0x9277
-  __TEXT.__gcc_except_tab: 0x5a94
+  __TEXT.__cstring: 0x9347
+  __TEXT.__gcc_except_tab: 0x5a8c
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__swift5_typeref: 0x847
   __TEXT.__swift5_fieldmd: 0x6a4

   __TEXT.__swift5_assocty: 0x1d8
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3638
+  __TEXT.__unwind_info: 0x36a0
   __TEXT.__eh_frame: 0x378
-  __TEXT.__objc_classname: 0xe7e
-  __TEXT.__objc_methname: 0x114aa
-  __TEXT.__objc_methtype: 0x1dcd
-  __TEXT.__objc_stubs: 0xec80
-  __DATA_CONST.__got: 0xc68
+  __TEXT.__objc_classname: 0xeee
+  __TEXT.__objc_methname: 0x115be
+  __TEXT.__objc_methtype: 0x1e3d
+  __TEXT.__objc_stubs: 0xef00
+  __DATA_CONST.__got: 0xc90
   __DATA_CONST.__const: 0x3318
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4558
+  __DATA_CONST.__objc_selrefs: 0x4600
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x3b0
-  __DATA_CONST.__objc_arraydata: 0x868
-  __AUTH_CONST.__auth_got: 0x12c0
-  __AUTH_CONST.__const: 0x30f0
-  __AUTH_CONST.__cfstring: 0x9040
-  __AUTH_CONST.__objc_const: 0x10110
-  __AUTH_CONST.__objc_intobj: 0x978
-  __AUTH_CONST.__objc_arrayobj: 0x648
+  __DATA_CONST.__objc_superrefs: 0x3d0
+  __DATA_CONST.__objc_arraydata: 0x878
+  __AUTH_CONST.__auth_got: 0x12d0
+  __AUTH_CONST.__const: 0x3318
+  __AUTH_CONST.__cfstring: 0x9160
+  __AUTH_CONST.__objc_const: 0x10450
+  __AUTH_CONST.__objc_intobj: 0xa08
+  __AUTH_CONST.__objc_arrayobj: 0x660
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x3dc8
+  __AUTH.__objc_data: 0x2c98
   __AUTH.__data: 0x7d0
-  __DATA.__objc_ivar: 0x97c
-  __DATA.__data: 0x1308
-  __DATA.__bss: 0x2460
-  __DATA.__common: 0x30
+  __DATA.__objc_ivar: 0x9a4
+  __DATA.__data: 0xfa8
+  __DATA.__bss: 0x1c30
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__objc_data: 0x12c0
+  __DATA_DIRTY.__data: 0x3c0
+  __DATA_DIRTY.__bss: 0xa34
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3F5ABCBC-F3C9-385B-A5B8-B9221A68A172
-  Functions: 4800
-  Symbols:   14218
-  CStrings:  6945
+  UUID: 49A294B5-B1C8-3A2A-9D1F-1381F24040C6
+  Functions: 4862
+  Symbols:   14415
+  CStrings:  6997
 
Symbols:
+ -[CSAppEntityUpdater didCompleteJournal]
+ -[CSDocumentUnderstandingUpdater didCompleteJournal]
+ -[CSEmbeddingsUpdater didCompleteJournal]
+ -[CSEventDonationJournalItem containsAnyInAttributes:]
+ -[CSKeyPhrasesUpdater didCompleteJournal]
+ -[CSPriorityUpdater didCompleteJournal]
+ -[CSProcessingStateUpdater didCompleteJournal]
+ -[CSProcessorPipelineJobUpdater didCompleteJournal]
+ -[CSScheduledReceiverUpdater didCompleteJournal]
+ -[CSScheduledReceiverUpdater supportedJournalItem:]
+ -[SKDAnalyticsLogProvider .cxx_destruct]
+ -[SKDAnalyticsLogProvider init]
+ -[SKDAnalyticsLogProvider sendLog:domain:]
+ -[SKDAnalyticsLogger .cxx_destruct]
+ -[SKDAnalyticsLogger dealloc]
+ -[SKDAnalyticsLogger flush]
+ -[SKDAnalyticsLogger initWithDomain:analyticsProvider:]
+ -[SKDAnalyticsLogger logEvent:]
+ -[SKDAnalyticsLogger logEvent:level:]
+ -[SKDAnalyticsLogger logEvent:level:].cold.1
+ -[SKDAnalyticsLogger logEvent:level:].cold.2
+ -[SKDAnalyticsLogger logs]
+ -[SKDAnalyticsLogger supportedEvent:]
+ -[SKDAnalyticsLogger supportedTrackingEvent:]
+ -[SKDAnalyticsLogger trackingEventBeginWithName:event:]
+ -[SKDAnalyticsLogger trackingEventEnd:]
+ -[SKDAnalyticsLogger(Testing) setMaxLogCount:]
+ -[SKDAnalyticsTrackingEvent .cxx_destruct]
+ -[SKDAnalyticsTrackingEvent initWithName:event:domain:]
+ -[SKDAnalyticsTrackingEvent logEvent:]
+ -[SKDAnalyticsTrackingEvent logs]
+ -[SKDAnalyticsTrackingEvent supportedEvent:]
+ -[SKDBaseItemProcessingJob currentTrackingEvent]
+ -[SKDBaseItemProcessingJob endBatch]
+ -[SKDBaseItemProcessingJob startBatch]
+ -[SKDDefaults enabledForPipeline:]
+ -[SKDDefaults pipelineDebugEnabled]
+ -[SKDDefaults pipelineKeyphrasesEnabled]
+ -[SKDDefaults versionForPipeline:]
+ -[SKDDefaults(Testing) defaultsProvider]
+ -[SKDDefaults(Testing) featureFlagsProvider]
+ -[SKDDefaults(Testing) setDefaultsProvider:]
+ -[SKDDefaults(Testing) setFeatureFlagsProvider:]
+ -[SKDDefaultsProvider versionForPipeline:]
+ -[SKDEventLogger .cxx_destruct]
+ -[SKDEventLogger initWithDomain:]
+ -[SKDEventLogger logs]
+ -[SKDEventLogger supportedEvent:]
+ -[SKDEventLogger supportedTrackingEvent:]
+ -[SKDItemUpdate setTextContentLanguage:]
+ -[SKDItemUpdate setTextContentLength:]
+ -[SKDPipelineLogger(Testing) analyticsLogger]
+ -[SKDPipelineLogger(Testing) setAnalyticsLogger:]
+ -[SKDPipelineTrackingEvent analyticsTracker]
+ -[SKDPipelineTrackingEvent initWithName:event:domain:]
+ -[SKDPipelineTrackingEvent setAnalyticsTracker:]
+ -[SKDPowerLogger dealloc]
+ -[SKDPowerLogger logs]
+ -[SKDTrackingEvent .cxx_destruct]
+ -[SKDTrackingEvent domain]
+ -[SKDTrackingEvent event]
+ -[SKDTrackingEvent initWithName:event:domain:]
+ -[SKDTrackingEvent logEvent:]
+ -[SKDTrackingEvent logs]
+ -[SKDTrackingEvent message]
+ -[SKDTrackingEvent name]
+ -[SKGProcessor(Keyphraser) flushKeyphraser]
+ -[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]
+ GCC_except_table259
+ GCC_except_table84
+ GCC_except_table89
+ _CFStringCreateWithBytesNoCopy
+ _OBJC_CLASS_$_SKDAnalyticsLogProvider
+ _OBJC_CLASS_$_SKDAnalyticsLogger
+ _OBJC_CLASS_$_SKDAnalyticsTrackingEvent
+ _OBJC_CLASS_$_SKDDefaultsProvider
+ _OBJC_CLASS_$_SKDTrackingEvent
+ _OBJC_IVAR_$_SKDAnalyticsLogProvider._queue
+ _OBJC_IVAR_$_SKDAnalyticsLogger._analyticsProvider
+ _OBJC_IVAR_$_SKDAnalyticsLogger._lock
+ _OBJC_IVAR_$_SKDAnalyticsLogger._logs
+ _OBJC_IVAR_$_SKDAnalyticsLogger._maxLogCount
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._batchCount
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._completedCount
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._errorCount
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._lastEventTime
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._logs
+ _OBJC_IVAR_$_SKDAnalyticsTrackingEvent._startTime
+ _OBJC_IVAR_$_SKDBaseItemProcessingJob._currentTrackingEvent
+ _OBJC_IVAR_$_SKDDefaults._defaultsProvider
+ _OBJC_IVAR_$_SKDDefaults._featureFlagsProvider
+ _OBJC_IVAR_$_SKDEventLogger._domain
+ _OBJC_IVAR_$_SKDPipelineLogger._analyticsLogger
+ _OBJC_IVAR_$_SKDPipelineTrackingEvent._analyticsTracker
+ _OBJC_IVAR_$_SKDTrackingEvent._domain
+ _OBJC_IVAR_$_SKDTrackingEvent._event
+ _OBJC_IVAR_$_SKDTrackingEvent._name
+ _OBJC_METACLASS_$_SKDAnalyticsLogProvider
+ _OBJC_METACLASS_$_SKDAnalyticsLogger
+ _OBJC_METACLASS_$_SKDAnalyticsTrackingEvent
+ _OBJC_METACLASS_$_SKDDefaultsProvider
+ _OBJC_METACLASS_$_SKDTrackingEvent
+ __MDPlistDictionaryIterate
+ __OBJC_$_INSTANCE_METHODS_SKDAnalyticsLogProvider
+ __OBJC_$_INSTANCE_METHODS_SKDAnalyticsLogger(Testing)
+ __OBJC_$_INSTANCE_METHODS_SKDAnalyticsTrackingEvent
+ __OBJC_$_INSTANCE_METHODS_SKDDefaults(Testing)
+ __OBJC_$_INSTANCE_METHODS_SKDDefaultsProvider
+ __OBJC_$_INSTANCE_METHODS_SKDTrackingEvent
+ __OBJC_$_INSTANCE_VARIABLES_SKDAnalyticsLogProvider
+ __OBJC_$_INSTANCE_VARIABLES_SKDAnalyticsLogger
+ __OBJC_$_INSTANCE_VARIABLES_SKDAnalyticsTrackingEvent
+ __OBJC_$_INSTANCE_VARIABLES_SKDEventLogger
+ __OBJC_$_INSTANCE_VARIABLES_SKDTrackingEvent
+ __OBJC_$_PROP_LIST_SKDEventLogger.178
+ __OBJC_$_PROP_LIST_SKDTrackingEvent.158
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKDDefaultsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKDDefaultsProviding
+ __OBJC_CLASS_PROTOCOLS_$_SKDAnalyticsLogProvider
+ __OBJC_CLASS_PROTOCOLS_$_SKDDefaultsProvider
+ __OBJC_CLASS_PROTOCOLS_$_SKDTrackingEvent
+ __OBJC_CLASS_RO_$_SKDAnalyticsLogProvider
+ __OBJC_CLASS_RO_$_SKDAnalyticsLogger
+ __OBJC_CLASS_RO_$_SKDAnalyticsTrackingEvent
+ __OBJC_CLASS_RO_$_SKDDefaultsProvider
+ __OBJC_CLASS_RO_$_SKDTrackingEvent
+ __OBJC_LABEL_PROTOCOL_$_SKDDefaultsProviding
+ __OBJC_METACLASS_RO_$_SKDAnalyticsLogProvider
+ __OBJC_METACLASS_RO_$_SKDAnalyticsLogger
+ __OBJC_METACLASS_RO_$_SKDAnalyticsTrackingEvent
+ __OBJC_METACLASS_RO_$_SKDDefaultsProvider
+ __OBJC_METACLASS_RO_$_SKDTrackingEvent
+ __OBJC_PROTOCOL_$_SKDDefaultsProviding
+ ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.247
+ ___38-[CSIndexEventListener handleMessage:]_block_invoke.133
+ ___42-[SKDAnalyticsLogProvider sendLog:domain:]_block_invoke
+ ___46-[CSXPCEventListener startWithEventListeners:]_block_invoke.42
+ ___46-[CSXPCEventListener startWithEventListeners:]_block_invoke.42.cold.1
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.153
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.162
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.171
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.180
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.190
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.156
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.165
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.174
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.183
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.168
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.177
+ ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.186
+ ___54-[CSEventDonationJournalItem containsAnyInAttributes:]_block_invoke
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.297
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.300
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.306.cold.1
+ ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.308
+ ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.77
+ ___97-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]_block_invoke
+ ___97-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]_block_invoke.37
+ ___97-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]_block_invoke.37.cold.1
+ ___97-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]_block_invoke_2
+ ___97-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:]_block_invoke_2.cold.1
+ ___block_descriptor_149_e8_32s40s48s56s64s72s80s88s96s104r112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8r104l8s80l8r112l8s88l8s96l8
+ ___block_descriptor_48_e8_32s40r_e26_v48?0r*8Q16{?=*Q{?=IC}}24lr40l8s32l8
+ ___block_literal_global.104
+ ___block_literal_global.151
+ ___block_literal_global.155
+ ___block_literal_global.158
+ ___block_literal_global.161
+ ___block_literal_global.164
+ ___block_literal_global.167
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.182
+ ___block_literal_global.185
+ ___block_literal_global.188
+ ___block_literal_global.205
+ ___block_literal_global.223
+ ___block_literal_global.244
+ ___block_literal_global.250
+ ___block_literal_global.255
+ ___block_literal_global.276
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.286
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.297
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.339
+ ___block_literal_global.345
+ ___block_literal_global.50
+ ___getAnalyticsAliases_block_invoke
+ ___getAnalyticsKeys_block_invoke
+ ___handleEmbeddingsTask_block_invoke.331
+ ___handleKeyphrasesTask_block_invoke.335
+ ___handlePreExtractionTask_block_invoke.336
+ ___handlePriorityTask_block_invoke.334
+ ___handleQueryCleanupTask_block_invoke.273
+ ___handleQueryUpdatesTask_block_invoke.343
+ ___setupQueryCleanupTasks_block_invoke.332
+ ___setupQueryUpdatesTasks_block_invoke.337
+ ___swift_memcpy8_8
+ __analyticsKeys
+ _configureMockDescriptor
+ _getAnalyticsAliases.onceToken
+ _getAnalyticsAliases.sAnalyticsAliases
+ _getAnalyticsKeys.onceToken
+ _getAnalyticsKeys.sAnalyticsKeys
+ _kCFAllocatorNull
+ _loadLanguageModels
+ _objc_msgSend$addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:
+ _objc_msgSend$analyticsLogger
+ _objc_msgSend$analyticsTracker
+ _objc_msgSend$containsAnyInAttributes:
+ _objc_msgSend$defaultsProvider
+ _objc_msgSend$didCompleteJournal
+ _objc_msgSend$enabledForPipeline:
+ _objc_msgSend$endBatch
+ _objc_msgSend$event
+ _objc_msgSend$featureFlagsProvider
+ _objc_msgSend$flushKeyphraser
+ _objc_msgSend$generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:
+ _objc_msgSend$initWithDomain:analyticsProvider:
+ _objc_msgSend$initWithName:event:domain:
+ _objc_msgSend$isPipelineDebugEnabled
+ _objc_msgSend$isPipelineEnabled
+ _objc_msgSend$isPipelineKeyphrasesEnabled
+ _objc_msgSend$logs
+ _objc_msgSend$pipelineDebugEnabled
+ _objc_msgSend$pipelineKeyphrasesEnabled
+ _objc_msgSend$processingBatchEvent
+ _objc_msgSend$setAnalyticsTracker:
+ _objc_msgSend$setTextContentLanguage:
+ _objc_msgSend$setTextContentLength:
+ _objc_msgSend$startBatch
+ _objc_msgSend$supportedJournalItem:
+ _objc_msgSend$versionForPipeline:
+ _purgeLanguageModels
+ _sTimestamps
- -[SKDDefaults debugPipelineEnabled]
- -[SKDDefaults init]
- -[SKDDefaults keyphrasePipelineEnabled]
- -[SKDDefaults keyphrasePipelineVersion]
- -[SKDPipelineLogger dealloc]
- -[SKDPipelineLogger domain]
- -[SKDPipelineTrackingEvent attributes]
- -[SKDPipelineTrackingEvent event]
- -[SKDPipelineTrackingEvent identifier]
- -[SKDPipelineTrackingEvent initWithIdentifier:event:domain:]
- -[SKDPipelineTrackingEvent message]
- -[SKDPowerLogger domain]
- -[SKDPowerLogger log]
- -[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]
- GCC_except_table198
- GCC_except_table49
- GCC_except_table60
- GCC_except_table63
- GCC_except_table83
- _OBJC_IVAR_$_SKDDefaults._anyPipelineEnabled
- _OBJC_IVAR_$_SKDDefaults._debugPipelineEnabled
- _OBJC_IVAR_$_SKDDefaults._excludeBundles
- _OBJC_IVAR_$_SKDDefaults._keyphrasePipelineEnabled
- _OBJC_IVAR_$_SKDDefaults._keyphrasePipelineVersion
- _OBJC_IVAR_$_SKDDefaults._pipelineEnabled
- _OBJC_IVAR_$_SKDPipelineTrackingEvent._domain
- _OBJC_IVAR_$_SKDPipelineTrackingEvent._event
- _OBJC_IVAR_$_SKDPipelineTrackingEvent._identifier
- _OBJC_IVAR_$_SKDPowerLogger._domain
- __OBJC_$_INSTANCE_METHODS_SKDDefaults
- __OBJC_$_PROP_LIST_SKDDefaults
- __OBJC_$_PROP_LIST_SKDEventLogger.153
- __OBJC_$_PROP_LIST_SKDPowerLogger
- __OBJC_CLASS_PROTOCOLS_$_SKDPipelineTrackingEvent
- ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.244
- ___38-[CSIndexEventListener handleMessage:]_block_invoke.132
- ___46-[CSXPCEventListener startWithEventListeners:]_block_invoke.40
- ___46-[CSXPCEventListener startWithEventListeners:]_block_invoke.40.cold.1
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.152
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.161
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.170
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.179
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke.189
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.155
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.164
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.173
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_2.182
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.167
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.176
- ___49-[CSEventListenerTasksManager endJobForDelegate:]_block_invoke_3.185
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.295
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.298
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.302
- ___56-[CSJournalProcessor _processOffsetAtOffset:completion:]_block_invoke.304.cold.1
- ___82-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]_block_invoke
- ___82-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]_block_invoke.36
- ___82-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]_block_invoke.36.cold.1
- ___82-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]_block_invoke_2
- ___82-[SKGProcessor(Keyphraser) generateKeyphrasesForRecord:processedItem:cancelBlock:]_block_invoke_2.cold.1
- ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.81
- ___88-[CSScheduledReceiverUpdater handleDonation:turboEnabled:completionHandler:cancelBlock:]_block_invoke.82
- ___block_descriptor_149_e8_32s40s48s56s64s72s80s88s96s104r112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r104l8s72l8r112l8s80l8s88l8s96l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_literal_global.150
- ___block_literal_global.154
- ___block_literal_global.157
- ___block_literal_global.160
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.169
- ___block_literal_global.172
- ___block_literal_global.175
- ___block_literal_global.184
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.220
- ___block_literal_global.241
- ___block_literal_global.249
- ___block_literal_global.254
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.296
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.338
- ___block_literal_global.344
- ___block_literal_global.37
- ___block_literal_global.48
- ___block_literal_global.51
- ___block_literal_global.77
- ___handleEmbeddingsTask_block_invoke.330
- ___handleKeyphrasesTask_block_invoke.334
- ___handlePreExtractionTask_block_invoke.335
- ___handlePriorityTask_block_invoke.333
- ___handleQueryCleanupTask_block_invoke.269
- ___handleQueryUpdatesTask_block_invoke.339
- ___setupQueryCleanupTasks_block_invoke.331
- ___setupQueryUpdatesTasks_block_invoke.336
- _getMockDescriptors
- _objc_msgSend$addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:
- _objc_msgSend$debugPipelineEnabled
- _objc_msgSend$generateKeyphrasesForRecord:processedItem:cancelBlock:
- _objc_msgSend$initWithIdentifier:event:domain:
- _objc_msgSend$keyphrasePipelineEnabled
- _objc_msgSend$keyphrasePipelineVersion
- _objc_msgSend$slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:
CStrings:
+ "@\"<SKDDefaultsProviding>\""
+ "@\"<SKDFeatureFlagsProviding>\""
+ "@\"<SKDTrackingEvent>\""
+ "@\"NSNumber\"24@0:8@\"NSString\"16"
+ "B48@0:8@16@24Q32@?40"
+ "CSKeyphraseUpdaterTimeout"
+ "SKDAnalyticsLogProvider"
+ "SKDAnalyticsLogger"
+ "SKDAnalyticsTrackingEvent"
+ "SKDDefaultsProvider"
+ "SKDDefaultsProviding"
+ "T@\"<SKDDefaultsProviding>\",R,N"
+ "T@\"<SKDFeatureFlagsProviding>\",R,N"
+ "T@\"<SKDTrackingEvent>\",R,N"
+ "_analyticsLogger"
+ "_analyticsProvider"
+ "_analyticsTracker"
+ "_batchCount"
+ "_completedCount"
+ "_currentTrackingEvent"
+ "_defaultsProvider"
+ "_errorCount"
+ "_featureFlagsProvider"
+ "_lastEventTime"
+ "_maxLogCount"
+ "addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:bundleID:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:"
+ "analyticsLogger"
+ "analyticsTracker"
+ "com.apple.spotlightknowledge.CoreAnalyticsProvider"
+ "com.apple.spotlightknowledge.PowerLogProvider"
+ "containsAnyInAttributes:"
+ "currentTrackingEvent"
+ "defaultsProvider"
+ "didCompleteJournal"
+ "enabledForPipeline:"
+ "endBatch"
+ "errorCode"
+ "errorDomain"
+ "erroredCount"
+ "featureFlagsProvider"
+ "flushKeyphraser"
+ "generateKeyphrasesForRecord:processedItem:processorFlags:cancelBlock:"
+ "ignoredCount"
+ "initWithDomain:analyticsProvider:"
+ "initWithName:event:domain:"
+ "logs"
+ "process-batch"
+ "setAnalyticsLogger:"
+ "setAnalyticsTracker:"
+ "setDefaultsProvider:"
+ "setFeatureFlagsProvider:"
+ "setMaxLogCount:"
+ "setTextContentLanguage:"
+ "setTextContentLength:"
+ "startBatch"
+ "supportedJournalItem:"
+ "supportedTrackingEvent:"
+ "textContentLength"
+ "und"
+ "v48@?0r*8Q16{?=*Q{?=IC}}24"
+ "versionForPipeline:"
- "@\"SKDPowerLogger\""
- "SKG"
- "T@\"NSArray\",R,N,V_excludeBundles"
- "T@\"SKDPowerLogger\",R,N"
- "TB,R,N,V_anyPipelineEnabled"
- "TB,R,N,V_debugPipelineEnabled"
- "TB,R,N,V_keyphrasePipelineEnabled"
- "TB,R,N,V_pipelineEnabled"
- "Tq,R,N,V_keyphrasePipelineVersion"
- "_anyPipelineEnabled"
- "_debugPipelineEnabled"
- "_keyphrasePipelineEnabled"
- "_keyphrasePipelineVersion"
- "_pipelineEnabled"
- "addOrUpdateSearchableItemsInJournalFd:atOffset:size:indexType:protectionClass:serialNumber:journalCookie:additionalAttributes:client:config:completionHandler:"
- "com.apple.spotlightknowledge.PowerLogger"
- "debugPipelineEnabled"
- "generateKeyphrasesForRecord:processedItem:cancelBlock:"
- "initWithIdentifier:event:domain:"
- "keyphrasePipelineEnabled"
- "keyphrasePipelineVersion"
- "slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:"

```
