## NotesSupport

> `/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport`

```diff

-  __TEXT.__text: 0x54b94
+  __TEXT.__text: 0x55ce0
   __TEXT.__delay_helper: 0x2cc
-  __TEXT.__objc_methlist: 0x4288
+  __TEXT.__objc_methlist: 0x4378
   __TEXT.__const: 0xb6c
-  __TEXT.__cstring: 0x4549
-  __TEXT.__gcc_except_tab: 0xea4
-  __TEXT.__oslogstring: 0x3c26
+  __TEXT.__cstring: 0x4589
+  __TEXT.__gcc_except_tab: 0xed8
+  __TEXT.__oslogstring: 0x3e86
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x2bb

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x1cf0
+  __TEXT.__unwind_info: 0x1d38
   __TEXT.__eh_frame: 0x7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1328
+  __DATA_CONST.__const: 0x1380
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3110
+  __DATA_CONST.__objc_selrefs: 0x3178
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x880
-  __AUTH_CONST.__const: 0x1660
-  __AUTH_CONST.__cfstring: 0x4420
-  __AUTH_CONST.__objc_const: 0x5e38
+  __DATA_CONST.__got: 0x888
+  __AUTH_CONST.__const: 0x16a0
+  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__objc_const: 0x5ed0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x1050
-  __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x218
-  __DATA.__data: 0x784
-  __DATA.__bss: 0x800
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1220
-  __DATA_DIRTY.__data: 0x24c
-  __DATA_DIRTY.__bss: 0x4b1
+  __AUTH.__objc_data: 0x120
+  __AUTH.__data: 0xa0
+  __DATA.__objc_ivar: 0x220
+  __DATA.__data: 0x6f4
+  __DATA.__bss: 0x570
+  __DATA_DIRTY.__objc_data: 0x1270
+  __DATA_DIRTY.__data: 0x418
+  __DATA_DIRTY.__bss: 0x741
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2512
-  Symbols:   7278
-  CStrings:  1557
+  Functions: 2539
+  Symbols:   7349
+  CStrings:  1572
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[ICBaseSearchIndexerDataSource indexingScope]
+ -[ICBaseSearchIndexerDataSource setIndexingScope:]
+ -[ICBaseSearchIndexerDataSource waitForPendingChangeProcessing]
+ -[ICCDCSIReindexer reindexAllSearchableItemsWithScope:completionHandler:]
+ -[ICIndexItemsOperation _indexBatchItemCount]
+ -[ICIndexItemsOperation _indexBatchMaxTotalSize]
+ -[ICIndexItemsOperation _resetContextForDataSourceIfNeededInExtension:]
+ -[ICReindexAllItemsOperation indexingScope]
+ -[ICReindexAllItemsOperation setIndexingScope:]
+ -[ICSearchIndexer _startObservingChangesOnIndexingQueue]
+ -[ICSearchIndexer determineIfReindexIsNeededFromClientStateWithCompletionHandler:]
+ -[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]
+ -[ICSearchIndexer indexPendingItemsWithCompletionHandler:]
+ -[ICSearchIndexer reindexAllSearchableItemsInIndex:scope:completionHandler:]
+ -[ICSearchIndexer reindexAllSearchableItemsWithScope:completionHandler:]
+ -[ICSearchIndexer startObservingChangesAndWait]
+ GCC_except_table28
+ GCC_except_table34
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table53
+ GCC_except_table63
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table71
+ _OBJC_IVAR_$_ICBaseSearchIndexerDataSource._indexingScope
+ _OBJC_IVAR_$_ICReindexAllItemsOperation._indexingScope
+ ___47-[ICSearchIndexer startObservingChangesAndWait]_block_invoke
+ ___58-[ICSearchIndexer indexPendingItemsWithCompletionHandler:]_block_invoke
+ ___63-[ICBaseSearchIndexerDataSource waitForPendingChangeProcessing]_block_invoke
+ ___71-[ICIndexItemsOperation _resetContextForDataSourceIfNeededInExtension:]_block_invoke
+ ___76-[ICSearchIndexer reindexAllSearchableItemsInIndex:scope:completionHandler:]_block_invoke
+ ___82-[ICSearchIndexer determineIfReindexIsNeededFromClientStateWithCompletionHandler:]_block_invoke
+ ___84-[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]_block_invoke
+ ___84-[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]_block_invoke_2
+ ___block_descriptor_42_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ _kICReindexAttachmentsOnLaunchKey
+ _objc_msgSend$_indexBatchItemCount
+ _objc_msgSend$_indexBatchMaxTotalSize
+ _objc_msgSend$_resetContextForDataSourceIfNeededInExtension:
+ _objc_msgSend$_startObservingChangesOnIndexingQueue
+ _objc_msgSend$indexingScope
+ _objc_msgSend$processChanges
+ _objc_msgSend$reindexAllSearchableItemsInIndex:scope:completionHandler:
+ _objc_msgSend$setIndexingScope:
+ _objc_msgSend$shouldDeferIndexingInMemoryConstrainedExtension
+ _objc_msgSend$waitForPendingChangeProcessing
- -[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]
- GCC_except_table13
- GCC_except_table36
- GCC_except_table51
- GCC_except_table56
- GCC_except_table59
- GCC_except_table69
- ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- _objc_msgSend$reindexAllSearchableItemsInIndex:completionHandler:
CStrings:
+ "Client state from CoreSpotlight does not match defaults; reindex needed"
+ "Deferring large object %@ from in-extension indexing to avoid jetsam; the app will index it on next launch."
+ "Error fetching client state from CoreSpotlight: %@; assuming reindex needed"
+ "Finished indexing pending items, error: %@"
+ "Finished observed changes and remaining indexing operations"
+ "ICAttachment"
+ "Indexing %lu pending item(s) with a regular indexing operation"
+ "No client state in CoreSpotlight; reindex needed"
+ "No client state in defaults; reindex needed"
+ "No pending items to index"
+ "ReindexAttachmentsOnLaunch"
+ "Search indexing disabled. Not indexing pending items."
+ "Staging data source %@ for reindexing in operation %@ (scope %lu)"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "Staging data source %@ for reindexing in operation %@"

```
