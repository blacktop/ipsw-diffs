## NotesSupport

> `/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport`

```diff

-2952.80.3.0.0
-  __TEXT.__text: 0x4c8ec
-  __TEXT.__auth_stubs: 0x1bd0
+2952.100.21.0.0
+  __TEXT.__text: 0x55fb4
+  __TEXT.__auth_stubs: 0x1ec0
   __TEXT.__delay_helper: 0x2cc
-  __TEXT.__objc_methlist: 0x3d0c
-  __TEXT.__const: 0x8a6
-  __TEXT.__cstring: 0x3fe2
-  __TEXT.__oslogstring: 0x3895
-  __TEXT.__gcc_except_tab: 0xfc0
+  __TEXT.__objc_methlist: 0x40bc
+  __TEXT.__const: 0xb6c
+  __TEXT.__cstring: 0x4119
+  __TEXT.__oslogstring: 0x3a36
+  __TEXT.__gcc_except_tab: 0xfb0
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__ustring: 0x18
-  __TEXT.__constg_swiftt: 0x1bc
-  __TEXT.__swift5_typeref: 0x188
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0xbb
-  __TEXT.__swift5_fieldmd: 0x158
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_capture: 0xd4
+  __TEXT.__constg_swiftt: 0x228
+  __TEXT.__swift5_typeref: 0x2a7
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_reflstr: 0xde
+  __TEXT.__swift5_fieldmd: 0x1c0
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_capture: 0x1c0
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x1a40
-  __TEXT.__eh_frame: 0x6c8
-  __TEXT.__objc_classname: 0x533
-  __TEXT.__objc_methname: 0xaed8
-  __TEXT.__objc_methtype: 0x10c1
-  __TEXT.__objc_stubs: 0x7f80
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0x1280
-  __DATA_CONST.__objc_classlist: 0x1d0
+  __TEXT.__unwind_info: 0x1d90
+  __TEXT.__eh_frame: 0x790
+  __TEXT.__objc_classname: 0x685
+  __TEXT.__objc_methname: 0xb964
+  __TEXT.__objc_methtype: 0x141c
+  __TEXT.__objc_stubs: 0x8840
+  __DATA_CONST.__got: 0x868
+  __DATA_CONST.__const: 0x12f0
+  __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x128
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e68
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x3020
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0xe00
-  __AUTH_CONST.__const: 0xf78
-  __AUTH_CONST.__cfstring: 0x41c0
-  __AUTH_CONST.__objc_const: 0x5730
+  __AUTH_CONST.__auth_got: 0xf78
+  __AUTH_CONST.__const: 0x14d0
+  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__objc_const: 0x5c10
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x98
+  __AUTH.__objc_data: 0x170
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0x55c
-  __DATA.__bss: 0x560
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__data: 0x6f4
+  __DATA.__bss: 0x880
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1158
-  __DATA_DIRTY.__data: 0x11c
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__objc_data: 0x11d0
+  __DATA_DIRTY.__data: 0x214
+  __DATA_DIRTY.__bss: 0x3f9
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 819FEBDF-30F0-34C1-90B2-591910D21212
-  Functions: 2236
-  Symbols:   6767
-  CStrings:  3542
+  UUID: 1BC151A4-C46B-380D-A122-DAC4E97F103B
+  Functions: 2450
+  Symbols:   7100
+  CStrings:  3663
 
Symbols:
+ -[ICBaseSearchIndexerDataSource fallbackProgressDataSource]
+ -[ICBaseSearchIndexerDataSource progressCoordinator]
+ -[ICBaseSearchIndexerDataSource progressDataSource]
+ -[ICBaseSearchIndexerDataSource searchIndexerDidFinishIndexingObjectIDs:searchableItems:error:]
+ -[ICBaseSearchIndexerDataSource setFallbackProgressDataSource:]
+ -[ICBaseSearchIndexerDataSource setProgressCoordinator:]
+ -[ICIndexItemsOperation currentCombinedProgress]
+ -[ICReindexAllItemsOperation delegate]
+ -[ICReindexAllItemsOperation initWithSearchableIndex:dataSources:delegate:]
+ -[ICReindexAllItemsOperation setDelegate:]
+ -[ICSearchIndexImplementation csProgressForSearchIndexProgress:]
+ -[ICSearchIndexImplementation indexSearchableItems:progress:completionHandler:]
+ -[ICSearchIndexImplementation reportProgress:completionHandler:]
+ -[ICSearchIndexer allDataSourcesSuccessfullyStagedSinceLastReindex]
+ -[ICSearchIndexer clearObjectIDsToProcessAndResetProgress]
+ -[ICSearchIndexer fullyStagedSinceLastReindex]
+ -[ICSearchIndexer reindexOperationSuccessfullyStagedAllDataSources:]
+ -[ICSearchIndexer setAllDataSourcesSuccessfullyStagedSinceLastReindex:]
+ GCC_except_table101
+ GCC_except_table102
+ GCC_except_table112
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table68
+ _MDItemDisplayName
+ _OBJC_CLASS_$_CSDonationProgress
+ _OBJC_CLASS_$_ICFileBasedIndexProgessDataSource
+ _OBJC_CLASS_$_ICSearchIndexProgress
+ _OBJC_CLASS_$_ICSearchIndexProgressCoordinator
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_ICBaseSearchIndexerDataSource._fallbackProgressDataSource
+ _OBJC_IVAR_$_ICBaseSearchIndexerDataSource._progressCoordinator
+ _OBJC_IVAR_$_ICReindexAllItemsOperation._delegate
+ _OBJC_IVAR_$_ICSearchIndexer._allDataSourcesSuccessfullyStagedSinceLastReindex
+ _OBJC_METACLASS_$_ICFileBasedIndexProgessDataSource
+ _OBJC_METACLASS_$_ICSearchIndexProgress
+ _OBJC_METACLASS_$_ICSearchIndexProgressCoordinator
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ __CLASS_METHODS_ICSearchIndexProgress
+ __CLASS_METHODS_ICSearchIndexProgressCoordinator
+ __CLASS_PROPERTIES_ICSearchIndexProgressCoordinator
+ __DATA_ICFileBasedIndexProgessDataSource
+ __DATA_ICSearchIndexProgress
+ __DATA_ICSearchIndexProgressCoordinator
+ __INSTANCE_METHODS_ICFileBasedIndexProgessDataSource
+ __INSTANCE_METHODS_ICSearchIndexProgress
+ __INSTANCE_METHODS_ICSearchIndexProgressCoordinator
+ __IVARS_ICFileBasedIndexProgessDataSource
+ __IVARS_ICSearchIndexProgress
+ __IVARS_ICSearchIndexProgressCoordinator
+ __METACLASS_DATA_ICFileBasedIndexProgessDataSource
+ __METACLASS_DATA_ICSearchIndexProgress
+ __METACLASS_DATA_ICSearchIndexProgressCoordinator
+ __OBJC_$_PROP_LIST_ICReindexing
+ __OBJC_$_PROP_LIST_ICSearchIndexProgressCoordinatorDataSource
+ __OBJC_$_PROP_LIST_ICSearchIndexerDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICReindexAllItemsOperationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICSearchIndexProgressCoordinatorDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICReindexAllItemsOperationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICSearchIndexProgressCoordinatorDataSource
+ __OBJC_$_PROTOCOL_REFS_ICReindexAllItemsOperationDelegate
+ __OBJC_$_PROTOCOL_REFS_ICSearchIndexProgressCoordinatorDataSource
+ __OBJC_LABEL_PROTOCOL_$_ICReindexAllItemsOperationDelegate
+ __OBJC_LABEL_PROTOCOL_$_ICSearchIndexProgressCoordinatorDataSource
+ __OBJC_PROTOCOL_$_ICReindexAllItemsOperationDelegate
+ __OBJC_PROTOCOL_$_ICSearchIndexProgressCoordinatorDataSource
+ __PROPERTIES_ICFileBasedIndexProgessDataSource
+ __PROPERTIES_ICSearchIndexProgress
+ __PROPERTIES_ICSearchIndexProgressCoordinator
+ __PROTOCOLS_ICFileBasedIndexProgessDataSource
+ __PROTOCOLS_ICFileBasedIndexProgessDataSource.7
+ ___161-[ICBaseSearchIndexerDataSource decisionOnObjectID:searchableItemToIndex:additionalItemsToIndex:objectIDURIToDelete:additionalUniqueIdentifiersToDelete:context:]_block_invoke.159
+ ___161-[ICBaseSearchIndexerDataSource decisionOnObjectID:searchableItemToIndex:additionalItemsToIndex:objectIDURIToDelete:additionalUniqueIdentifiersToDelete:context:]_block_invoke.159.cold.1
+ ___37-[ICIndexItemsOperation processItems]_block_invoke.5
+ ___37-[ICIndexItemsOperation processItems]_block_invoke.7
+ ___37-[ICIndexItemsOperation processItems]_block_invoke.7.cold.1
+ ___60-[ICBaseSearchIndexerDataSource addNewObjectsForProcessing:]_block_invoke
+ ___60-[ICBaseSearchIndexerDataSource loadOrClearStateIfNecessary]_block_invoke_2
+ ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke.30
+ ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke_2
+ ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke_2.cold.1
+ ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke_2.cold.2
+ ___65-[ICSearchIndexer deleteAllSearchableItemsWithCompletionHandler:]_block_invoke_2
+ ___65-[ICSearchIndexer deleteAllSearchableItemsWithCompletionHandler:]_block_invoke_2.cold.1
+ ___65-[ICSearchIndexer deleteAllSearchableItemsWithCompletionHandler:]_block_invoke_2.cold.2
+ ___76-[ICBaseSearchIndexerDataSource clearObjectIDsToIgnoreAndStageForReindexing]_block_invoke
+ ___95-[ICBaseSearchIndexerDataSource searchIndexerDidFinishIndexingObjectIDs:searchableItems:error:]_block_invoke
+ ___95-[ICBaseSearchIndexerDataSource searchIndexerDidFinishIndexingObjectIDs:searchableItems:error:]_block_invoke_2
+ ___95-[ICIndexItemsOperation commitIfNecessaryForDataSource:hasItemsToDeleteThenUpdate:forceCommit:]_block_invoke
+ ___95-[ICIndexItemsOperation commitIfNecessaryForDataSource:hasItemsToDeleteThenUpdate:forceCommit:]_block_invoke.cold.1
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e36_"NSString"16?0"CSSearchableItem"8l
+ ___block_descriptor_32_e37_"NSString"16?0"NSManagedObjectID"8l
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56w_e17_v16?0"NSError"8lw56l8s32l8s40l8s48l8
+ ___block_literal_global.11
+ ___block_literal_global.163
+ ___block_literal_global.176
+ ___block_literal_global.212
+ ___block_literal_global.24
+ ___block_literal_global.33
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy24_8
+ ___swift_project_boxed_opaque_existential_1
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV10CodingKeysOSHACSQ
+ _associated conformance So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV10CodingKeysOs0T3KeyACs23CustomStringConvertible
+ _associated conformance So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV10CodingKeysOs0T3KeyACs28CustomDebugStringConvertible
+ _block_copy_helper.15
+ _block_copy_helper.28
+ _block_copy_helper.38
+ _block_copy_helper.48
+ _block_copy_helper.58
+ _block_copy_helper.68
+ _block_descriptor.17
+ _block_descriptor.30
+ _block_descriptor.40
+ _block_descriptor.50
+ _block_descriptor.60
+ _block_descriptor.70
+ _block_destroy_helper.16
+ _block_destroy_helper.29
+ _block_destroy_helper.39
+ _block_destroy_helper.49
+ _block_destroy_helper.59
+ _block_destroy_helper.69
+ _bzero
+ _keypath_get_selector_completedItemCount
+ _keypath_get_selector_pendingItemCount
+ _keypath_get_selector_progress
+ _objc_msgSend$addBarrierBlock:
+ _objc_msgSend$adoptIndexState:forItemWithIdentifier:updatingProgress:
+ _objc_msgSend$allDataSourcesSuccessfullyStagedSinceLastReindex
+ _objc_msgSend$clearObjectIDsToProcessAndResetProgress
+ _objc_msgSend$completed
+ _objc_msgSend$completedItemCount
+ _objc_msgSend$csProgressForSearchIndexProgress:
+ _objc_msgSend$currentCombinedProgress
+ _objc_msgSend$dataSource
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$didIndexItems:willIndexState:
+ _objc_msgSend$finishBatch
+ _objc_msgSend$flush
+ _objc_msgSend$fullProgressUpdateWithCompletionHandler:
+ _objc_msgSend$generalASRLanguageForLocale:
+ _objc_msgSend$ic_briefFormattedDate
+ _objc_msgSend$ic_briefFormattedDateForSiriLocale:forAccessibility:
+ _objc_msgSend$ic_componentRangesSeparatedByPredicate:inRange:
+ _objc_msgSend$ic_endOfDay
+ _objc_msgSend$ic_isSameDayAsDate:
+ _objc_msgSend$ic_localDateWithSeconds
+ _objc_msgSend$ic_map:
+ _objc_msgSend$ic_numberOfDaysFromDate:
+ _objc_msgSend$ic_objectsOfClass:
+ _objc_msgSend$ic_rangeByTrimmingCharactersInSet:inRange:
+ _objc_msgSend$ic_shortFormattedDate
+ _objc_msgSend$ic_shortFormattedDateForAccessibility
+ _objc_msgSend$ic_startOfDay
+ _objc_msgSend$ic_truncated
+ _objc_msgSend$ic_uriString
+ _objc_msgSend$indexSearchableItems:progress:completionHandler:
+ _objc_msgSend$indexSearchableItems:updatingDonationProgress:completionHandler:
+ _objc_msgSend$initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:
+ _objc_msgSend$initWithDataSource:
+ _objc_msgSend$initWithPending:completed:
+ _objc_msgSend$initWithSearchableIndex:dataSources:delegate:
+ _objc_msgSend$isNotesTranscriptionAllowed
+ _objc_msgSend$isNotesTranscriptionSummaryAllowed
+ _objc_msgSend$minusSet:
+ _objc_msgSend$pendingItemCount
+ _objc_msgSend$pendingNew
+ _objc_msgSend$pendingUpdate
+ _objc_msgSend$persistenceURL
+ _objc_msgSend$progress
+ _objc_msgSend$progressCoordinator
+ _objc_msgSend$progressDataSource
+ _objc_msgSend$reindexOperationSuccessfullyStagedAllDataSources:
+ _objc_msgSend$reportDonationProgress:completionHandler:
+ _objc_msgSend$reportProgress:completionHandler:
+ _objc_msgSend$reset
+ _objc_msgSend$revertStaging:
+ _objc_msgSend$revertStagingWithItemIdentifier:
+ _objc_msgSend$searchIndexerDidFinishIndexingObjectIDs:searchableItems:error:
+ _objc_msgSend$setAllDataSourcesSuccessfullyStagedSinceLastReindex:
+ _objc_msgSend$setCompleted:
+ _objc_msgSend$setCompletedItemCount:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setPendingItemCount:
+ _objc_msgSend$setPendingNew:
+ _objc_msgSend$setPendingUpdate:
+ _objc_msgSend$setProgress:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$stageForProcessing:
+ _objc_msgSend$stageForProcessingWithItemIdentifier:updatingProgress:
+ _objc_msgSend$stageForReindex:
+ _objc_msgSend$stateOfItemWithIdentifier:
+ _objc_msgSend$supportedLanguagesForTaskHint:completion:
+ _objc_msgSend$totalItemCount
+ _objc_msgSend$update:
+ _objc_msgSend$willDeleteItems:
+ _objc_msgSend$willIndexItems:
+ _objectdestroy.23Tm
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getKeyPath
+ _swift_willThrow
+ _symbolic Ig_
+ _symbolic SS
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic ShySSG
+ _symbolic So21ICSearchIndexProgressC
+ _symbolic So21ICSearchIndexProgressCIeghg_
+ _symbolic So21ICSearchIndexProgressCIeyBhy_
+ _symbolic So32ICSearchIndexProgressCoordinatorC
+ _symbolic So33ICFileBasedIndexProgessDataSourceC
+ _symbolic _____ So12ICIndexStateV
+ _symbolic _____ So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV
+ _symbolic _____ So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV10CodingKeysO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497R9B3DFD33CFLLV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497R9B3DFD33CFLLV10CodingKeysO
+ _type_layout_string So33ICFileBasedIndexProgessDataSourceC12NotesSupportE13FileFormat_v1022_AFA060D7EC4A2CE087497O9B3DFD33CFLLV
- -[ICBaseSearchIndexerDataSource searchIndexerDidFinishIndexingObjectIDs:error:]
- -[ICSearchIndexImplementation indexSearchableItems:completionHandler:]
- -[ICSearchIndexer clearObjectIDsToProcess]
- GCC_except_table107
- GCC_except_table32
- GCC_except_table42
- GCC_except_table43
- GCC_except_table52
- GCC_except_table54
- GCC_except_table63
- GCC_except_table96
- GCC_except_table97
- ___161-[ICBaseSearchIndexerDataSource decisionOnObjectID:searchableItemToIndex:additionalItemsToIndex:objectIDURIToDelete:additionalUniqueIdentifiersToDelete:context:]_block_invoke.153
- ___161-[ICBaseSearchIndexerDataSource decisionOnObjectID:searchableItemToIndex:additionalItemsToIndex:objectIDURIToDelete:additionalUniqueIdentifiersToDelete:context:]_block_invoke.153.cold.1
- ___37-[ICIndexItemsOperation processItems]_block_invoke.4
- ___37-[ICIndexItemsOperation processItems]_block_invoke.6
- ___37-[ICIndexItemsOperation processItems]_block_invoke.6.cold.1
- ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke.23
- ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke.cold.1
- ___62-[ICIndexItemsOperation _commitObjectIDsToIndexForDataSource:]_block_invoke.cold.2
- ___65-[ICSearchIndexer deleteAllSearchableItemsWithCompletionHandler:]_block_invoke.cold.1
- ___65-[ICSearchIndexer deleteAllSearchableItemsWithCompletionHandler:]_block_invoke.cold.2
- ___79-[ICBaseSearchIndexerDataSource searchIndexerDidFinishIndexingObjectIDs:error:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$searchIndexerDidFinishIndexingObjectIDs:error:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "-[ICPersistentContainer backupPersistentStoreWithError:]"
+ "<SearchIndexProgress total="
+ "?"
+ "@\"<ICReindexAllItemsOperationDelegate>\""
+ "@\"<ICSearchIndexProgressCoordinatorDataSource>\""
+ "@\"ICSearchIndexProgress\""
+ "@\"ICSearchIndexProgressCoordinator\""
+ "@\"ICSearchIndexProgressCoordinator\"16@0:8"
+ "@\"NSSet\"24@0:8Q16"
+ "@\"NSString\"16@?0@\"CSSearchableItem\"8"
+ "@\"NSString\"16@?0@\"NSManagedObjectID\"8"
+ "@\"NSURL\"16@0:8"
+ "@\"OS_dispatch_queue\""
+ "Error while reporting progress: %@"
+ "Failed to open modern database. Backing up and creating a new database, error %@ (%@)"
+ "Fatal error"
+ "ICFileBasedIndexProgessDataSource"
+ "ICReindexAllItemsOperationDelegate"
+ "ICSearchIndexProgress"
+ "ICSearchIndexProgressCoordinator"
+ "ICSearchIndexProgressCoordinatorDataSource"
+ "ICSearchIndexState"
+ "Index progress coordinator missing data source in %s"
+ "NotesSupport.FileBasedIndexProgessDataSource"
+ "NotesSupport.SearchIndexProgress"
+ "NotesSupport.SearchIndexProgressCoordinator"
+ "NotesSupport/ICSearchIndexProgress.swift"
+ "Q24@0:8@\"NSString\"16"
+ "Reindexing previously indexed item %s"
+ "Removing previously indexed item %s"
+ "Reporting progress to Spotlight: %@"
+ "Revert staging of unstaged item %s (completed: %{bool}d"
+ "Should never happen"
+ "T@\"<ICReindexAllItemsOperationDelegate>\",W,N,V_delegate"
+ "T@\"<ICSearchIndexProgressCoordinatorDataSource>\",&,N,V_fallbackProgressDataSource"
+ "T@\"<ICSearchIndexProgressCoordinatorDataSource>\",N,W,VdataSource"
+ "T@\"ICSearchIndexProgress\",N,&,Vprogress"
+ "T@\"ICSearchIndexProgressCoordinator\",&,N,V_progressCoordinator"
+ "T@\"ICSearchIndexProgressCoordinator\",R,N"
+ "T@\"NSSet\",N,C"
+ "T@\"NSString\",N,R"
+ "T@\"NSURL\",N,R"
+ "T@\"OS_dispatch_queue\",N,R,Vqueue"
+ "TB,N,V_allDataSourcesSuccessfullyStagedSinceLastReindex"
+ "Tq,N,R"
+ "Tq,N,Vcompleted"
+ "Tq,N,Vpending"
+ "Unable to flush index progress state: %s"
+ "Unable to read index progress from disk, maybe new. Error: %s"
+ "Unexpected state "
+ "_allDataSourcesSuccessfullyStagedSinceLastReindex"
+ "_fallbackProgressDataSource"
+ "_progressCoordinator"
+ "addBarrierBlock:"
+ "adoptIndexState:forItemWithIdentifier:updatingProgress:"
+ "allDataSourcesSuccessfullyStagedSinceLastReindex"
+ "allItemIdentifiersForState:"
+ "clearObjectIDsToProcessAndResetProgress"
+ "com.apple.notes.file-based-index-progress-queue"
+ "com.apple.notes.search-index-progress-coordinator"
+ "completed"
+ "completedItemCount"
+ "csProgressForSearchIndexProgress:"
+ "currentCombinedProgress"
+ "dataSource"
+ "didIndexItems(_:willIndexState:)"
+ "didIndexItems:willIndexState:"
+ "fallbackProgressDataSource"
+ "finishBatch"
+ "flush"
+ "fullProgressUpdateWithCompletionHandler:"
+ "fullyStagedSinceLastReindex"
+ "indexSearchableItems:progress:completionHandler:"
+ "indexSearchableItems:updatingDonationProgress:completionHandler:"
+ "init()"
+ "initWithAllKnownItems:itemsNeedingDonation:donatedItems:partiallyDonatedItems:itemsNeedingDonationForRedonationRequests:"
+ "initWithDataSource:"
+ "initWithPending:completed:"
+ "initWithSearchableIndex:dataSources:delegate:"
+ "keyPathsForValuesAffectingValueForKey:"
+ "minusSet:"
+ "pending"
+ "pendingItemCount"
+ "pendingNew"
+ "pendingUpdate"
+ "persistenceURL"
+ "progress"
+ "progressCoordinator"
+ "progressDataSource"
+ "q24@0:8@16"
+ "reindexOperationSuccessfullyStagedAllDataSources:"
+ "reportDonationProgress:completionHandler:"
+ "reportProgress:completionHandler:"
+ "reset"
+ "revertStaging(_:)"
+ "revertStaging:"
+ "revertStagingWithItemIdentifier:"
+ "searchIndexerDidFinishIndexingObjectIDs:searchableItems:error:"
+ "setAllDataSourcesSuccessfullyStagedSinceLastReindex:"
+ "setCompleted:"
+ "setCompletedItemCount:"
+ "setDataSource:"
+ "setFallbackProgressDataSource:"
+ "setPendingItemCount:"
+ "setPendingNew:"
+ "setPendingUpdate:"
+ "setProgress:"
+ "setProgressCoordinator:"
+ "stageForProcessing(_:)"
+ "stageForProcessing:"
+ "stageForProcessingWithItemIdentifier:updatingProgress:"
+ "stageForReindex(_:)"
+ "stageForReindex:"
+ "stateOfItemWithIdentifier:"
+ "totalItemCount"
+ "update:"
+ "v16@?0@\"ICSearchIndexProgress\"8"
+ "v24@0:8@\"ICReindexAllItemsOperation\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?<v@?@\"ICSearchIndexProgress\">16"
+ "v32@0:8@\"ICSearchIndexProgress\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@\"ICSearchIndexProgress\"24"
+ "v40@0:8@\"NSArray\"16@\"ICSearchIndexProgress\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@\"NSError\"32"
+ "v40@0:8Q16@\"NSString\"24@\"ICSearchIndexProgress\"32"
+ "willDeleteItems(_:)"
+ "willDeleteItems:"
+ "willIndexItems(_:)"
+ "willIndexItems:"
- "searchIndexerDidFinishIndexingObjectIDs:error:"

```
