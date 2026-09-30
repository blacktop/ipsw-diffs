## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/Versions/A/SpotlightKnowledgeDaemon`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x490ba4
-  __TEXT.__objc_methlist: 0x9978
-  __TEXT.__const: 0x17448
-  __TEXT.__oslogstring: 0x1199e
-  __TEXT.__gcc_except_tab: 0x5bc8
-  __TEXT.__cstring: 0x15b33
+2465.1.2.0.0
+  __TEXT.__text: 0x4b182c
+  __TEXT.__objc_methlist: 0x9610
+  __TEXT.__const: 0x17938
+  __TEXT.__oslogstring: 0x12a2e
+  __TEXT.__cstring: 0x1637e
+  __TEXT.__gcc_except_tab: 0x5b74
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0xe9b2
-  __TEXT.__constg_swiftt: 0x8dc8
+  __TEXT.__swift5_typeref: 0xedea
+  __TEXT.__constg_swiftt: 0x90b8
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x880d
-  __TEXT.__swift5_fieldmd: 0x8d4c
-  __TEXT.__swift5_assocty: 0x1398
-  __TEXT.__swift5_capture: 0x37e8
-  __TEXT.__swift5_proto: 0x107c
-  __TEXT.__swift5_types: 0x8bc
+  __TEXT.__swift5_reflstr: 0x8d1a
+  __TEXT.__swift5_fieldmd: 0x9130
+  __TEXT.__swift5_assocty: 0x13b0
+  __TEXT.__swift5_capture: 0x38c4
+  __TEXT.__swift5_proto: 0x10ac
+  __TEXT.__swift5_types: 0x8e8
   __TEXT.__swift_as_entry: 0x488
-  __TEXT.__swift_as_ret: 0x4d4
-  __TEXT.__swift_as_cont: 0x57c
-  __TEXT.__swift5_protos: 0x274
+  __TEXT.__swift_as_ret: 0x4d8
+  __TEXT.__swift_as_cont: 0x580
+  __TEXT.__swift5_protos: 0x280
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__unwind_info: 0xf100
-  __TEXT.__eh_frame: 0x143f8
+  __TEXT.__swift5_types2: 0x4
+  __TEXT.__unwind_info: 0xf998
+  __TEXT.__eh_frame: 0x15000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd40
-  __DATA_CONST.__objc_classlist: 0x970
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__const: 0xd48
+  __DATA_CONST.__objc_classlist: 0x968
+  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f68
-  __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x4e8
-  __DATA_CONST.__objc_arraydata: 0x8c0
-  __DATA_CONST.__got: 0x2250
-  __AUTH_CONST.__const: 0x1bc08
-  __AUTH_CONST.__cfstring: 0x9520
-  __AUTH_CONST.__objc_const: 0x186b8
+  __DATA_CONST.__objc_selrefs: 0x5e48
+  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x4d8
+  __DATA_CONST.__objc_arraydata: 0x8b0
+  __DATA_CONST.__got: 0x2328
+  __AUTH_CONST.__const: 0x1c5f0
+  __AUTH_CONST.__cfstring: 0x9360
+  __AUTH_CONST.__objc_const: 0x18388
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x9c0
-  __AUTH_CONST.__objc_arrayobj: 0x5e8
+  __AUTH_CONST.__objc_intobj: 0x990
+  __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x34f8
-  __AUTH.__objc_data: 0x1738
-  __AUTH.__data: 0x2a28
-  __DATA.__objc_ivar: 0xbd4
-  __DATA.__data: 0x3a50
-  __DATA.__common: 0xb0
-  __DATA_DIRTY.__objc_data: 0x3f40
-  __DATA_DIRTY.__data: 0xc080
+  __AUTH_CONST.__auth_got: 0x35e8
+  __AUTH.__objc_data: 0x1698
+  __AUTH.__data: 0x2bb8
+  __DATA.__objc_ivar: 0xb68
+  __DATA.__data: 0x3ed0
+  __DATA.__common: 0xe0
+  __DATA_DIRTY.__objc_data: 0x3f50
+  __DATA_DIRTY.__data: 0xbf60
   __DATA_DIRTY.__bss: 0x8900
-  __DATA_DIRTY.__common: 0x3b0
+  __DATA_DIRTY.__common: 0x380
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16725
-  Symbols:   14467
-  CStrings:  3699
+  Functions: 16901
+  Symbols:   14380
+  CStrings:  3770
 
Symbols:
+ -[SKDDefaultsProvider onlineLocationsMaxAge]
+ -[SKDLocationProcessor referenceDateForRecord:]
+ -[SKDLocationProcessor shouldLookupOnlineLocationsForRecord:]
+ GCC_except_table22
+ GCC_except_table71
+ GCC_except_table77
+ GCC_except_table98
+ _MADUnifiedEmbeddingVersionToString
+ _OBJC_CLASS_$_CCAmbientSensingActivityContent
+ _OBJC_CLASS_$_CCGenerativeInsightContent
+ _OBJC_CLASS_$_CCHealthMeasurementContent
+ _SKDCascadeSourceItemIdentityPack
+ __DATA__TtC24SpotlightKnowledgeDaemon22RedonationDiscoveryJob
+ __IVARS__TtC24SpotlightKnowledgeDaemon22RedonationDiscoveryJob
+ __METACLASS_DATA__TtC24SpotlightKnowledgeDaemon22RedonationDiscoveryJob
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCJSONDescribing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCJSONDescribing
+ __OBJC_LABEL_PROTOCOL_$_CCJSONDescribing
+ __OBJC_PROTOCOL_$_CCJSONDescribing
+ ___42-[SKDLocationProcessor optionalAttributes]_block_invoke
+ ___swift_cannot_copy_noncopyable_type
+ ___swift_memcpy1328_8
+ ___swift_memcpy180_8
+ ___swift_memcpy424_8
+ ___swift_memcpy656_8
+ __si_exported_XXH3_64bits
+ __swift__destructor.18Tm
+ __swift_closure_destructor.122Tm
+ __swift_closure_destructor.254Tm
+ __swift_closure_destructor.297Tm
+ __swift_closure_destructor.364Tm
+ __swift_closure_destructor.467Tm
+ __swift_closure_destructor.604Tm
+ __swift_closure_destructor.66Tm
+ __swift_closure_destructor.695Tm
+ __swift_closure_destructor.704Tm
+ __swift_closure_destructor.72Tm
+ __swift_exist.box.addr_destructor.60Tm
+ __swift_exist.box.addr_destructor.715Tm
+ __swift_exist.box.addr_destructor.720Tm
+ __swift_exist.box.addr_destructor.786Tm
+ _associated conformance 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC12StoredStatusOSHAASQ
+ _objc_msgSend$categorySample
+ _objc_msgSend$classification
+ _objc_msgSend$entityType
+ _objc_msgSend$generationDate
+ _objc_msgSend$hasDay
+ _objc_msgSend$hasEndDate
+ _objc_msgSend$hasStartDate
+ _objc_msgSend$isGLPAmbientSensingActivityEnabled
+ _objc_msgSend$isGLPMessageIndexingEnabled
+ _objc_msgSend$isGLPNoteIndexingEnabled
+ _objc_msgSend$null
+ _objc_msgSend$onlineLocationsMaxAge
+ _objc_msgSend$overnightVitalsSummary
+ _objc_msgSend$resourceGenerationWithUseCase:error:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setReason:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$shouldLookupOnlineLocationsForRecord:
+ _objc_msgSend$sleepDaySummary
+ _objc_msgSend$stateOfMindSample
+ _objc_msgSend$statistics
+ _objc_msgSend$timeIntervalSinceNow
+ _symbolic $s24SpotlightKnowledgeDaemon13JobRunOutcomeP
+ _symbolic $s24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic $s24SpotlightKnowledgeDaemon32LegacyEmbeddingSelectionReceiverP
+ _symbolic SDySS______pG 24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic SDy_____Say_____GG 24SpotlightKnowledgeDaemon8BundleIDV s5Int64V
+ _symbolic SDy__________G s5Int64V 24SpotlightKnowledgeDaemon8BundleIDV
+ _symbolic SS6reason_t
+ _symbolic SSSg______pYbc s5ErrorP
+ _symbolic SS_______pt 24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic Say______pG 24SpotlightKnowledgeDaemon32LegacyEmbeddingSelectionReceiverP
+ _symbolic Say_____ySay_____G______pGG s6ResultOsRi_zRi0_zrlE 24SpotlightKnowledgeDaemon11TrackedItemV s5ErrorP
+ _symbolic _____ 18SpotlightKnowledge14UpdaterCommandO23ManageTransitionLoggingV
+ _symbolic _____ 18SpotlightKnowledge9StateDumpV019RedonationDiscoveryC0V3RunV7OutcomeO
+ _symbolic _____ 24SpotlightKnowledgeDaemon0A32LegacyEmbeddingSelectionReceiverV
+ _symbolic _____ 24SpotlightKnowledgeDaemon13JobRunHistoryV
+ _symbolic _____ 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV
+ _symbolic _____ 24SpotlightKnowledgeDaemon15FeatureMigratorV19OSVersionBreadcrumbV
+ _symbolic _____ 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC0fG0V
+ _symbolic _____ 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC12StoredStatusO
+ _symbolic _____ 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC
+ _symbolic _____ 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC10StepResult33_23E808ACECE2E4E2FFCE6D89C1DEDE3ELLO
+ _symbolic _____ 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC16EnumerationErrorV
+ _symbolic _____ 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC4Plan33_23E808ACECE2E4E2FFCE6D89C1DEDE3ELLV
+ _symbolic _____ 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC8CountersV
+ _symbolic _____ 24SpotlightKnowledgeDaemon35HDBLegacyEmbeddingSelectionReceiverV
+ _symbolic _____ 24SpotlightKnowledgeDaemon44ModelCatalogLegacyEmbeddingSelectionReceiverV
+ _symbolic _____3key_______p5valuet s5Int64V 24SpotlightKnowledgeDaemon14CascadeSetLikeP
+ _symbolic _____9indexType_______p7managert 18SpotlightKnowledge9IndexTypeO 0aB6Daemon22JournalManagerProtocolP
+ _symbolic _____9selection_SS6reasont 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC0fG0V
+ _symbolic _____Sg 18SpotlightKnowledge9StateDumpV019RedonationDiscoveryC0V
+ _symbolic _____Sg 24SpotlightKnowledgeDaemon29PipelineStateTransitionLoggerC
+ _symbolic ___________SSt 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC0fG0V AE12StoredStatusO
+ _symbolic ___________SStSg 24SpotlightKnowledgeDaemon15FeatureMigratorV22ModelSelectionProviderC0fG0V AE12StoredStatusO
+ _symbolic ___________pIeghrzo_ 18SpotlightKnowledge14UpdaterCommandO23ManageTransitionLoggingV8ResponseV s5ErrorP
+ _symbolic ___________pIeghrzo_ 18SpotlightKnowledge14UpdaterCommandO27GetRedonationDiscoveryStateV8ResponseV s5ErrorP
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______p 24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic ______p 24SpotlightKnowledgeDaemon32LegacyEmbeddingSelectionReceiverP
+ _symbolic _____ySG_pG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySS_______ptG s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic _____ySS______pG s18_DictionaryStorageC 24SpotlightKnowledgeDaemon30RedonationDiscoveryJobProtocolP
+ _symbolic _____y_Shy_____G14allowedSetKeys_SDyABSiG013outstandingByB3KeytG 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC10StepResult33_23E808ACECE2E4E2FFCE6D89C1DEDE3ELLO s5Int64V
+ _symbolic _____y_____9indexType_______p7managertG s23_ContiguousArrayStorageC 18SpotlightKnowledge9IndexTypeO 0dE6Daemon22JournalManagerProtocolP
+ _symbolic _____y_____G s11_SetStorageC 24SpotlightKnowledgeDaemon9SchedulerC21DynamicBackgroundTaskC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18SpotlightKnowledge9StateDumpV019RedonationDiscoveryF0V3RunV
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 24SpotlightKnowledgeDaemon8BundleIDV s5Int64V
+ _symbolic _____y______G 24SpotlightKnowledgeDaemon22RedonationDiscoveryJobC10StepResult33_23E808ACECE2E4E2FFCE6D89C1DEDE3ELLO AC4PlanAELLV
+ _symbolic _____y______G Sh5IndexV 24SpotlightKnowledgeDaemon9SchedulerC21DynamicBackgroundTaskC
+ _symbolic _____y__________G 24SpotlightKnowledgeDaemon13JobRunHistoryV AA019RedonationDiscoveryD0C8CountersV 0aB09StateDumpV0ghJ0V0E0V7OutcomeO
+ _symbolic _____y__________G s18_DictionaryStorageC s5Int64V 24SpotlightKnowledgeDaemon8BundleIDV
+ _symbolic _____y___________G 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC07RestartC0V8ResponseV AC0D5ErrorO
+ _symbolic _____y___________G 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC23ManageTransitionLoggingV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________G 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC27GetRedonationDiscoveryStateV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________G 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV AA019RedonationDiscoveryD0C8CountersV 0aB09StateDumpV0hiK0V0E0V7OutcomeO
+ _symbolic _____y___________GIeghn_ 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC07RestartC0V8ResponseV AC0D5ErrorO
+ _symbolic _____y___________GIeghn_ 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC23ManageTransitionLoggingV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________GIeghn_ 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC27GetRedonationDiscoveryStateV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________GSg 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV AA019RedonationDiscoveryD0C8CountersV 0aB09StateDumpV0hiK0V0E0V7OutcomeO
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 18SpotlightKnowledge14UpdaterCommandO07RestartD0V8ResponseV s5ErrorP
+ _symbolic _____y___________pGIeghn_AC_pIeghgzo_ s6ResultOsRi_zRi0_zrlE 18SpotlightKnowledge14UpdaterCommandO07RestartD0V8ResponseV s5ErrorP
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon32LegacyEmbeddingSelectionReceiverP
+ _symbolic _____y_____y___________GG 19CollectionsInternal12_DequeBufferC 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV AD019RedonationDiscoveryH0C8CountersV 0eF09StateDumpV0lmO0V0I0V7OutcomeO
+ _symbolic _____y_____y___________GG 19CollectionsInternal5DequeV 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV AD019RedonationDiscoveryG0C8CountersV 0dE09StateDumpV0klN0V0H0V7OutcomeO
+ _symbolic _____y_____y_____yxq__GGG 15Synchronization5MutexVAARi_zrlE 19CollectionsInternal5DequeV 24SpotlightKnowledgeDaemon13JobRunHistoryV6RecordV
+ optionalAttributes.onceLocOptionalToken
+ optionalAttributes.sLocOptionalAttributes
- +[SKGProcessorTaskManager breadcrumbsTask]
- +[SKGProcessorTaskManager keyphraseTask]
- +[SKGProcessorTaskManager sharedManager]
- +[SKGTextQueryManager queryForTask:event:]
- -[SKGJob(Updates) _runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]
- -[SKGJob(Updates) requestCSProcessingWithProtectionClasses:task:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]
- -[SKGJobContext shouldProcessAttributes]
- -[SKGProcessorTask .cxx_destruct]
- -[SKGProcessorTask _additionalQuery]
- -[SKGProcessorTask _backgroundQuery]
- -[SKGProcessorTask _cleanupQuery]
- -[SKGProcessorTask _excludedQuery]
- -[SKGProcessorTask _includedQuery]
- -[SKGProcessorTask _invalidVersionQuery]
- -[SKGProcessorTask _journalQuery]
- -[SKGProcessorTask _notExcludedQuery]
- -[SKGProcessorTask _notIncludedQuery]
- -[SKGProcessorTask _updatesQuery]
- -[SKGProcessorTask _versionQuery]
- -[SKGProcessorTask additionalQueries]
- -[SKGProcessorTask allowed]
- -[SKGProcessorTask canRun]
- -[SKGProcessorTask commonInitWithName:]
- -[SKGProcessorTask donationAttributes]
- -[SKGProcessorTask enabledForTesting]
- -[SKGProcessorTask enabledOverride]
- -[SKGProcessorTask enabled]
- -[SKGProcessorTask errorAttributeKey]
- -[SKGProcessorTask events]
- -[SKGProcessorTask excludeBundles]
- -[SKGProcessorTask excludeContentTypes]
- -[SKGProcessorTask fetchAttributes]
- -[SKGProcessorTask flags]
- -[SKGProcessorTask ignoreExternalBundles]
- -[SKGProcessorTask ignoreInternalBundles]
- -[SKGProcessorTask includeBundles]
- -[SKGProcessorTask includeContentTypes]
- -[SKGProcessorTask initWithName:]
- -[SKGProcessorTask journalAttributeKey]
- -[SKGProcessorTask name]
- -[SKGProcessorTask optionalAttributes]
- -[SKGProcessorTask processorAttributesForEvent:failed:]
- -[SKGProcessorTask processorFlags]
- -[SKGProcessorTask queryForEvent:]
- -[SKGProcessorTask requiredAttributes]
- -[SKGProcessorTask setAdditionalQueries:]
- -[SKGProcessorTask setCanRun:]
- -[SKGProcessorTask setEnabled:]
- -[SKGProcessorTask setEnabledForTesting:]
- -[SKGProcessorTask setEnabledOverride:]
- -[SKGProcessorTask setExcludeBundles:]
- -[SKGProcessorTask setExcludeContentTypes:]
- -[SKGProcessorTask setIgnoreExternalBundles:]
- -[SKGProcessorTask setIgnoreInternalBundles:]
- -[SKGProcessorTask setIncludeBundles:]
- -[SKGProcessorTask setIncludeContentTypes:]
- -[SKGProcessorTask setOptionalAttributes:]
- -[SKGProcessorTask setProcessorFlags:]
- -[SKGProcessorTask setRequiredAttributes:]
- -[SKGProcessorTask setSupportedEvent:]
- -[SKGProcessorTask setTaskOptions:]
- -[SKGProcessorTask setTrackingAttributes:]
- -[SKGProcessorTask setVersionValue:]
- -[SKGProcessorTask supportsBundleID:]
- -[SKGProcessorTask supportsEvent:]
- -[SKGProcessorTask supportsEvent:bundleID:]
- -[SKGProcessorTask supportsEvent:record:bundleID:]
- -[SKGProcessorTask taskOptions]
- -[SKGProcessorTask testWithEnabledFlag:]
- -[SKGProcessorTask trackingAttributes]
- -[SKGProcessorTask versionAttributeKey]
- -[SKGProcessorTask versionValue]
- -[SKGProcessorTaskManager .cxx_destruct]
- -[SKGProcessorTaskManager init]
- -[SKGProcessorTaskManager taskForName:]
- -[SKGProcessorTaskManager tasks]
- -[SKGTaskAgent beginProcessingTaskWithName:deviceUnlocked:knowledgedQueue:completeBlock:cancelBlock:deferBlock:]
- -[SpotlightKnowledge processAttributesWithJobContext:group:cancelBlock:]
- GCC_except_table102
- GCC_except_table105
- GCC_except_table78
- OBJC_IVAR_$_SKGProcessorTask._additionalQueries
- OBJC_IVAR_$_SKGProcessorTask._bgstOptions
- OBJC_IVAR_$_SKGProcessorTask._canRun
- OBJC_IVAR_$_SKGProcessorTask._donationAttributes
- OBJC_IVAR_$_SKGProcessorTask._enabled
- OBJC_IVAR_$_SKGProcessorTask._enabledForTesting
- OBJC_IVAR_$_SKGProcessorTask._enabledOverride
- OBJC_IVAR_$_SKGProcessorTask._errorAttributeKey
- OBJC_IVAR_$_SKGProcessorTask._events
- OBJC_IVAR_$_SKGProcessorTask._excludeBundles
- OBJC_IVAR_$_SKGProcessorTask._excludeContentTypes
- OBJC_IVAR_$_SKGProcessorTask._fetchAttributes
- OBJC_IVAR_$_SKGProcessorTask._flags
- OBJC_IVAR_$_SKGProcessorTask._ignoreExternalBundles
- OBJC_IVAR_$_SKGProcessorTask._ignoreInternalBundles
- OBJC_IVAR_$_SKGProcessorTask._includeBundles
- OBJC_IVAR_$_SKGProcessorTask._includeContentTypes
- OBJC_IVAR_$_SKGProcessorTask._journalAttributeKey
- OBJC_IVAR_$_SKGProcessorTask._name
- OBJC_IVAR_$_SKGProcessorTask._optionalAttributes
- OBJC_IVAR_$_SKGProcessorTask._override
- OBJC_IVAR_$_SKGProcessorTask._overrideEnabled
- OBJC_IVAR_$_SKGProcessorTask._requiredAttributes
- OBJC_IVAR_$_SKGProcessorTask._trackingAttributes
- OBJC_IVAR_$_SKGProcessorTask._versionAttributeKey
- OBJC_IVAR_$_SKGProcessorTask._versionValue
- OBJC_IVAR_$_SKGProcessorTaskManager._tasks
- _BGSystemTaskSchedulerErrorDomain
- _OBJC_CLASS_$_SKGProcessorTask
- _OBJC_CLASS_$_SKGProcessorTaskManager
- _OBJC_METACLASS_$_SKGProcessorTask
- _OBJC_METACLASS_$_SKGProcessorTaskManager
- __118-[SKGJob(Updates) _runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]_block_invoke
- __118-[SKGJob(Updates) _runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]_block_invoke_2
- __72-[SpotlightKnowledge processAttributesWithJobContext:group:cancelBlock:]_block_invoke
- __CATEGORY_BGNonRepeatingSystemTaskRequest_$_SpotlightKnowledgeDaemon
- __CATEGORY_INSTANCE_METHODS_BGNonRepeatingSystemTaskRequest_$_SpotlightKnowledgeDaemon
- __CATEGORY_PROPERTIES_BGNonRepeatingSystemTaskRequest_$_SpotlightKnowledgeDaemon
- __OBJC_$_CLASS_METHODS_SKGProcessorTaskManager
- __OBJC_$_INSTANCE_METHODS_SKGProcessorTask
- __OBJC_$_INSTANCE_METHODS_SKGProcessorTaskManager
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessorTask
- __OBJC_$_INSTANCE_VARIABLES_SKGProcessorTaskManager
- __OBJC_$_PROP_LIST_SKGProcessorTask
- __OBJC_CLASS_RO_$_SKGProcessorTask
- __OBJC_CLASS_RO_$_SKGProcessorTaskManager
- __OBJC_METACLASS_RO_$_SKGProcessorTask
- __OBJC_METACLASS_RO_$_SKGProcessorTaskManager
- ___118-[SKGJob(Updates) _runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]_block_invoke
- ___118-[SKGJob(Updates) _runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:]_block_invoke_2
- ___40+[SKGProcessorTaskManager sharedManager]_block_invoke
- ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke_3
- ___66-[SpotlightKnowledge processTextWithJobContext:group:cancelBlock:]_block_invoke_4
- ___72-[SpotlightKnowledge processAttributesWithJobContext:group:cancelBlock:]_block_invoke
- ___72-[SpotlightKnowledge processAttributesWithJobContext:group:cancelBlock:]_block_invoke_2
- ___block_descriptor_136_e8_32s40s48s56bs64bs72r80r88r96r104r112r120w_e17_v16?0"NSArray"8l
- ___block_descriptor_56_e8_32s40r48r_e26_B16?0"SKGProcessedItem"8l
- ___copy_helper_block_e8_32s40s48s56b64b72r80r88r96r104r112r120w
- ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r112r120w
- ___swift_memcpy1320_8
- ___swift_memcpy156_8
- ___swift_memcpy392_8
- ___swift_memcpy648_8
- __swift__destructor.19Tm
- __swift_closure_destructor.119Tm
- __swift_closure_destructor.266Tm
- __swift_closure_destructor.282Tm
- __swift_closure_destructor.346Tm
- __swift_closure_destructor.435Tm
- __swift_closure_destructor.460Tm
- __swift_closure_destructor.562Tm
- __swift_closure_destructor.653Tm
- __swift_closure_destructor.69Tm
- __swift_exist.box.addr_destructor.57Tm
- __swift_exist.box.addr_destructor.666Tm
- __swift_exist.box.addr_destructor.671Tm
- __swift_exist.box.addr_destructor.737Tm
- _objc_msgSend$_additionalQuery
- _objc_msgSend$_backgroundQuery
- _objc_msgSend$_cleanupQuery
- _objc_msgSend$_excludedQuery
- _objc_msgSend$_includedQuery
- _objc_msgSend$_invalidVersionQuery
- _objc_msgSend$_notExcludedQuery
- _objc_msgSend$_notIncludedQuery
- _objc_msgSend$_runCSProcessingForTask:queryString:queryContext:batchProcessedBlock:batchUpdatedBlock:cancelBlock:
- _objc_msgSend$_updatesQuery
- _objc_msgSend$_versionQuery
- _objc_msgSend$additionalQueries
- _objc_msgSend$breadcrumbsTask
- _objc_msgSend$canRun
- _objc_msgSend$commonInitWithName:
- _objc_msgSend$errorAttributeKey
- _objc_msgSend$events
- _objc_msgSend$finishedTextQueries
- _objc_msgSend$flags
- _objc_msgSend$ignoreExternalBundles
- _objc_msgSend$ignoreInternalBundles
- _objc_msgSend$isPipelineStateTransitionContentLoggingEnabled
- _objc_msgSend$isPipelineStateTransitionLoggingEnabled
- _objc_msgSend$isPostInstall
- _objc_msgSend$journalAttributeKey
- _objc_msgSend$keyphraseTask
- _objc_msgSend$postInstall
- _objc_msgSend$processAttributesWithJobContext:group:cancelBlock:
- _objc_msgSend$queryForEvent:
- _objc_msgSend$queryForTask:event:
- _objc_msgSend$queryRecordIncludesAttributes:
- _objc_msgSend$queryRecordNumberValueForKey:
- _objc_msgSend$requestCSProcessingWithProtectionClasses:task:batchProcessedBlock:batchUpdatedBlock:cancelBlock:
- _objc_msgSend$setAdditionalQueries:
- _objc_msgSend$setOptionalAttributes:
- _objc_msgSend$setPostInstall:
- _objc_msgSend$setProcessorFlags:
- _objc_msgSend$setRequiresBuddyComplete:
- _objc_msgSend$setScheduleAfter:
- _objc_msgSend$setSupportedEvent:
- _objc_msgSend$setTrySchedulingBefore:
- _objc_msgSend$setVersionValue:
- _objc_msgSend$shouldProcessAttributes
- _objc_msgSend$startTextQueries
- _objc_msgSend$supportsEvent:
- _objc_msgSend$supportsEvent:record:bundleID:
- _objc_msgSend$tasks
- _objc_msgSend$trackingAttributes
- _objc_msgSend$versionAttributeKey
- _objc_msgSend$withQueries
- _symbolic Si3key_Si5valuet
- _symbolic _____ 24SpotlightKnowledgeDaemon15FeatureMigratorV14ModelSelectionV
- _symbolic _____9selection_SS6reasont 24SpotlightKnowledgeDaemon15FeatureMigratorV14ModelSelectionV
- _symbolic _____Sg 24SpotlightKnowledgeDaemon15FeatureMigratorV14ModelSelectionV
- _symbolic ______SSt 24SpotlightKnowledgeDaemon15FeatureMigratorV14ModelSelectionV
- _symbolic ______SStSg 24SpotlightKnowledgeDaemon15FeatureMigratorV14ModelSelectionV
- _symbolic _____ySi3key_Si5valuetG s23_ContiguousArrayStorageC
- _symbolic y___________yyt______pGtYbcSg 24SpotlightKnowledgeDaemon9SchedulerC3JobC4KindO s6ResultOsRi_zRi0_zrlE s5ErrorP
- sharedManager.sSharedManager
CStrings:
+ "\nORDER BY pi.identityID"
+ "  donation[%{public}s] allKnown=%{public}ld needing=%{public}ld isPartial=%{public}s newestUndonated=%{public}s"
+ " Spotlight items not on the current version "
+ " is not downloadable"
+ " items are not on the current version <= "
+ " recommended for "
+ "%s for %{public}s: scanned %ld donations, inserted %ld journal keys, %ld candidates, %ld already pending in a journal, %ld flagged."
+ "%s: %{public}s does not participate in reindex. Completing early."
+ "%s: %{public}s excludes no bundles from Cascade processing. Completing early."
+ "%s: %{public}s has no journal managers, so journal pendency is unknowable. Completing early."
+ "%s: %{public}s is not enabled. Completing early."
+ "%s: %{public}s matched none of %ld candidates against %ld journal keys, and flagged all %ld of them. A zero hit rate at this size is the signature of the journal side and the state-store side deriving Cascade identities from different strings, which would make this job request redonations for items that do not need them. Check that the donation externalID is still the sourceItemIdentifier Cascade hashes for every set of these bundles."
+ "%s: all relevant sets of %{public}s are at the outstanding-redonation cap. Completing early."
+ "%s: inserted %ld journal keys for %{public}s, above the design capacity %ld. The false-positive rate for this run is worse than the configured %f, so more items than intended are skipped until the next run. Consider raising expectedJournalItemCapacity."
+ "%s: no candidates for %{public}s. Completing early."
+ "%s: no live Cascade sets for the redonation discovery bundles of %{public}s. Completing early."
+ "%s: redonation discovery reset version for %{public}s changed to %ld; cleared every recorded redonation attempt across every pipeline."
+ ")\nAND    pi.deleteStatus IS NULL\nAND    pi.processedVersion IS NULL\nAND    pi.errorCount < :cap\nAND    NOT EXISTS (SELECT 1 FROM redonation rd WHERE rd.identityID = i.identityID)\nAND    NOT (i.textContentHash IS NOT NULL\n            AND NOT EXISTS (SELECT 1 FROM document_store_cache dsc\n                            WHERE dsc.lookupID = i.lookupID)\n            AND     EXISTS (SELECT 1 FROM rehydration r\n                            WHERE r.identityID = i.identityID))"
+ ".RedonationDiscovery"
+ ".RedonationDiscovery."
+ ".redonation-discovery"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/SpotlightUI/corespotlight/SpotlightKnowledge/SpotlightKnowledgeDaemon/Utils/CascadeIdentity/SKDCascadeIdentity.h"
+ "AND    pi.source NOT IN ("
+ "AmbientSensingActivity"
+ "BacklogIndexProcessing"
+ "CascadeScanningJob: Could not confirm set %lld still exists: %@"
+ "CascadeScanningJob: Set %lld missing from batch enumeration but still opens via its bookmark; skipping this run."
+ "CascadeSetKeyResolution"
+ "Duplicate Cascade set key %{public}lld returned by setEnumerator(); keeping the last set seen."
+ "Exiting on request so launchd relaunches and configuration is re-read."
+ "Failed to list journal pages for %{public}s: %{public}@"
+ "Failed to open journal page %{public}llu of family %{public}s for %{public}s: %{public}@"
+ "Failed to read entries of journal page %{public}llu of family %{public}s for %{public}s: %{public}@"
+ "Failed to reset redonation attempts for %{public}s: %@"
+ "INSERT INTO metadata (key, value) VALUES (:key, :value)\nON CONFLICT(key) DO UPDATE SET value = excluded.value"
+ "Ignoring journal event for non-standard family: %s"
+ "MessageIndexing"
+ "No journal manager for required index type %{public}s; aborting scan."
+ "No legacy model recommended: No legacy version present (current version "
+ "No legacy model recommended: Only "
+ "No legacy model recommended: highest non-current version "
+ "NoteIndexing"
+ "Pipeline %{public}s declares %ld redonation discovery tasks, expected one"
+ "PipelineCompleteness"
+ "PipelineStateTransitionContentLoggingEnabled"
+ "PipelineStateTransitionLoggingEnabled"
+ "Post-install: baseline predates this build; recomputing before returning"
+ "Post-install: new build was detected; install date recorded"
+ "Post-install: same build; retry detected, no reseed"
+ "PriorityDiscovery"
+ "PriorityIndexProcessing"
+ "Redonation Discovery"
+ "Redonation Discovery Job"
+ "Redonation discovery reset version for %{public}s changed from %ld to %ld. Cleared %ld redonation attempts across every pipeline."
+ "RedonationDiscoveryJob"
+ "SELECT i.identityID, i.lookupID, i.source, i.textContentHash, i.priorityDate\nFROM   pipeline p\nJOIN   pipeline_item pi ON p.id = pi.pipeline\nJOIN   item i ON pi.identityID = i.identityID\nWHERE  p.name = :name\nAND    pi.source IN ("
+ "SELECT value FROM metadata WHERE key = ?"
+ "Transition content logging set to %{bool,public}d; restart required to apply."
+ "Transition log erased (existed: %{bool,public}d)."
+ "Transition log reached its %{public}ld byte cap; dropping further events. Delete %{public}s to resume."
+ "Transition logging set to %{bool,public}d; restart required to apply."
+ "UPDATE redonation SET attempts = 0 WHERE attempts > 0"
+ "[LegacyModel] Already concluded no legacy model is needed for this build: %s"
+ "[LegacyModel] Applying: legacy model already released for this build"
+ "[LegacyModel] Applying: legacy model version %ld required for build %s"
+ "[LegacyModel] Applying: no legacy model needed for this build"
+ "[LegacyModel] Applying: nothing concluded for this build, clearing any stored selection"
+ "[LegacyModel] Applying: releasing expired legacy model version %ld"
+ "[LegacyModel] Expiry check: no legacy model needed for this build"
+ "[LegacyModel] Expiry check: no stored selection"
+ "[LegacyModel] Expiry check: releasing version %ld left by OS version %s, now on %s"
+ "[LegacyModel] Expiry check: version %ld still active for build %s"
+ "[LegacyModel] HybridDatabase received selection %s"
+ "[LegacyModel] Legacy version %ld is the highest non-current version present"
+ "[LegacyModel] ModelCatalog received selection %s"
+ "[LegacyModel] Needed selection carried no embedding version"
+ "[LegacyModel] No ModelCatalog model for embedding version %ld"
+ "[LegacyModel] Pushed selection %s to %s"
+ "[LegacyModel] Receiver %s rejected selection: %@"
+ "[LegacyModel] Spotlight received selection %s"
+ "[LegacyModel] Statistics (downloadable): total=%ld, nonCurrent=%ld"
+ "[ModelSelection] Build %s settled as %s. Reason: %s"
+ "[OSVersion] Clearing OS versions"
+ "[OSVersion] OS version changed %s -> %s"
+ "[OSVersion] Recording first OS version %s"
+ "bounds check failure in SKDCascadeSourceItemIdentityPack: expected "
+ "determined needed, retaining "
+ "determined not needed"
+ "disableOfflineLocations"
+ "disableOnlineLocations"
+ "distinctAttributeValues(_:indexType:attribute:reason:cancellationToken:)"
+ "enableOfflineLocations"
+ "enableOnlineLocations"
+ "entries() failed for "
+ "expired"
+ "fetchPipelineCompleteness: display=%{public}s days=%{public}s percent=%{public}f calculatedAt=%{public}s donationsNotPartial=%{bool,public}d baselineIsCurrent=%{bool,public}d"
+ "itemContentScanned"
+ "legacyModel.status"
+ "missing manager for "
+ "noneNeeded"
+ "onlineLocationsMaxAgeDays"
+ "osVersion.current"
+ "osVersion.previous"
+ "page(_:from:) failed for "
+ "pageDescriptors() failed for "
+ "redonationDiscoveryCandidates"
+ "redonationDiscoveryResetVersion."
+ "redonationFlagged"
+ "required"
+ "sourceItemIdentifier"
+ "textContentHash="
- "  donation[%{public}s] allKnown=%{public}ld needing=%{public}ld newestUndonated=%{public}s"
- "% on current version >= "
- "%) while current version "
- "(false)"
- "(true)"
- "/tmp/StateTransitions"
- ":INC:%@"
- "=== Item (%@) has no bundleID."
- "=== Processed %llu items [of %llu items seen] for query %@"
- "=== Requesting scheduled processing of %@"
- "Breadcumbs"
- "DisableOfflineLocations"
- "DisableOnlineLocations"
- "EnableOfflineLocations"
- "EnableOnlineLocations"
- "No legacy model needed: "
- "No legacy model recommended: Best legacy version "
- "No legacy model recommended: No legacy versions found"
- "PipelineStateTransitionContentLogging"
- "PipelineStateTransitionLogging"
- "Post-install: new build was detected; computed state wiped"
- "Post-install: same build; retry detected, no-op"
- "[DAS] Could not submit post-install dynamic background task %{public}s; it has probably already run once this build."
- "[LegacyModel] Previous recommendation was for OS version %s, now on version %s. Re-evaluating."
- "[LegacyModel] Statistics (downloadable): total=%ld, onCurrent=%ld (%s%%)"
- "[ModelSelection] No recommendation. Reason: %s"
- "_kMDItem%@Error"
- "_kMDItem%@Version"
- "_kMDItemNeeds%@Processing"
- "distinctAttributeValues(_:indexType:attribute:cancellationToken:)"
- "end batch processing"
- "fetchPipelineCompleteness: display=%{public}s days=%{public}s percent=%{public}f calculatedAt=%{public}s"
- "kMDItemFullEmbeddingsError"
- "kMDItemNamedLocation"
- "kMDItemTitle"
- "processing all done"
- "processing attrs"
- "processor max items"
- "starting batch processing"
- "transitions-1.jsonl"
```
